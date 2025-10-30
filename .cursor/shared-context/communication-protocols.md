# Communication Protocols for Multi-Agent System

This document defines the standardized communication protocols used by all agents in the SuperPrompt Framework multi-agent system.

## Message Passing Architecture

### Overview
The system uses a **Hierarchical (Supervisor) Multi-Agent System** where:
- **Orchestrator Agent** = Supervisor/Dispatcher
- **Specialized Agents** = Workers with specific domains
- All inter-agent communication flows through the Orchestrator
- Agents do NOT communicate directly with each other

### Message Format Standard
All messages use **structured JSON** for machine-readable, predictable communication.

---

## Task Delegation Messages

### From Orchestrator to Specialized Agent

```json
{
  "message_type": "task_delegation",
  "message_id": "unique_uuid",
  "timestamp": "2025-10-20T14:30:00Z",
  "from_agent": "orchestrator",
  "to_agent": "concierge|triage|lifecycle|scribe|community",

  "event_context": {
    "event_type": "issues.opened|pull_request.opened|issue_comment.created|periodic_trigger",
    "event_id": "github_event_id",
    "repository": "owner/repo_name",
    "trigger_timestamp": "2025-10-20T14:29:45Z"
  },

  "task": {
    "description": "Human-readable task description",
    "priority": "high|medium|low",
    "timeout_seconds": 300,
    "requires_hitl": false,
    "confidence_threshold": 0.95
  },

  "context": {
    "issue_number": 123,
    "pr_number": 456,
    "comment_id": 789,

    "user": {
      "login": "username",
      "author_association": "FIRST_TIME_CONTRIBUTOR|CONTRIBUTOR|MEMBER|OWNER",
      "is_first_time_contributor": true,
      "contribution_count": 0,
      "account_created": "2025-01-15T10:00:00Z"
    },

    "content": {
      "title": "Issue or PR title",
      "body": "Full text content",
      "labels": ["existing", "labels"],
      "state": "open|closed",
      "created_at": "2025-10-20T14:29:45Z",
      "updated_at": "2025-10-20T14:29:45Z",
      "comments_count": 0
    },

    "additional_context": {
      "related_issues": [123, 456],
      "related_prs": [789],
      "mentions": ["@username"],
      "commands": ["/agent summarize"]
    }
  },

  "repository_context": {
    "rag_available": true,
    "governance_docs": ["CONTRIBUTING.md", "CODE_OF_CONDUCT.md"],
    "ci_workflows": [".github/workflows/ci.yml"]
  }
}
```

---

## Task Completion Messages

### From Specialized Agent to Orchestrator

```json
{
  "message_type": "task_completion",
  "message_id": "unique_uuid",
  "in_reply_to": "original_message_id",
  "timestamp": "2025-10-20T14:30:15Z",
  "from_agent": "concierge|triage|lifecycle|scribe|community",
  "to_agent": "orchestrator",

  "task_id": "original_task_id",
  "status": "success|failure|requires_approval|partial_success",
  "confidence_score": 0.97,
  "execution_time_ms": 2543,

  "actions_taken": [
    {
      "action_type": "label_applied|comment_posted|pr_created|branch_created|review_posted",
      "timestamp": "2025-10-20T14:30:05Z",
      "details": {
        "label": "bug",
        "issue_number": 123,
        "comment_url": "https://github.com/owner/repo/issues/123#issuecomment-xyz",
        "pr_number": 456
      },
      "confidence": 0.98
    }
  ],

  "rationale": "Clear, human-readable explanation of why actions were taken",

  "requires_human_review": false,
  "human_review_reason": "Optional: Why human review is needed",

  "next_steps": [
    "Monitor for follow-up questions",
    "Check if documentation needs update"
  ],

  "flags": {
    "documentation_gap": "FAQ section lacks setup troubleshooting",
    "potential_issue": "API change not documented",
    "coc_concern": false
  },

  "metrics": {
    "tokens_used": 1250,
    "api_calls_made": 3,
    "rag_queries": 2
  },

  "error": null
}
```

### For Failed Tasks

```json
{
  "message_type": "task_completion",
  "message_id": "unique_uuid",
  "in_reply_to": "original_message_id",
  "timestamp": "2025-10-20T14:30:15Z",
  "from_agent": "lifecycle",
  "to_agent": "orchestrator",

  "task_id": "original_task_id",
  "status": "failure",
  "execution_time_ms": 5000,

  "actions_taken": [],

  "error": {
    "error_type": "ci_trigger_failed|insufficient_context|api_error|timeout",
    "error_message": "Detailed error description",
    "error_code": "ERR_001",
    "timestamp": "2025-10-20T14:30:10Z",
    "retry_count": 3,
    "is_recoverable": true,
    "suggested_action": "Retry with exponential backoff"
  },

  "rationale": "Explanation of what went wrong and why",

  "requires_human_review": true,
  "human_review_reason": "Repeated failures require maintainer investigation",

  "next_steps": [
    "Apply agent-error label",
    "Tag maintainer team",
    "Investigate CI/CD pipeline issues"
  ]
}
```

---

## Special Message Types

### Human-in-the-Loop Approval Request

```json
{
  "message_type": "hitl_approval_request",
  "message_id": "unique_uuid",
  "timestamp": "2025-10-20T14:30:00Z",
  "from_agent": "triage",
  "to_agent": "orchestrator",

  "approval_needed_for": "close_duplicate_issue",
  "priority": "high|medium|low",
  "timeout_hours": 72,

  "proposed_action": {
    "action_type": "close_issue",
    "issue_number": 123,
    "reason": "Duplicate of #456",
    "details": {
      "duplicate_of": 456,
      "similarity_score": 0.96,
      "comparison": "Both issues describe same bug with identical reproduction steps"
    }
  },

  "rationale": "Why this action is recommended",
  "confidence": 0.96,

  "human_decision_options": [
    "approve",
    "reject",
    "modify"
  ],

  "github_comment_posted": true,
  "github_comment_url": "https://github.com/owner/repo/issues/123#issuecomment-xyz",
  "approvers_tagged": ["@maintainer1", "@maintainer2"]
}
```

### Code of Conduct Violation Flag

**CRITICAL**: This message type is ALWAYS private, NEVER posted publicly.

```json
{
  "message_type": "coc_violation_flag",
  "message_id": "unique_uuid",
  "timestamp": "2025-10-20T14:30:00Z",
  "from_agent": "community",
  "to_agent": "orchestrator",
  "privacy_level": "PRIVATE_TO_MODERATORS",

  "violation": {
    "severity": "high|medium|low",
    "confidence": 0.85,
    "violation_type": "harassment|discrimination|spam|rudeness|other",
    "location": "issue #123, comment by @username",
    "url": "https://github.com/owner/repo/issues/123#issuecomment-xyz",
    "timestamp": "2025-10-20T14:29:50Z"
  },

  "context": {
    "excerpt": "Relevant portion of concerning content (not full text)",
    "user_history": "First time concern flagged for this user",
    "thread_context": "Discussion about feature implementation became heated"
  },

  "analysis": {
    "sentiment_score": -0.7,
    "keywords_detected": ["keyword1", "keyword2"],
    "pattern_matched": "personal_attack"
  },

  "recommended_action": "Review for potential CoC violation",

  "important_notes": [
    "This is a private flag for human moderators only",
    "No public action has been taken",
    "Context and intent should be reviewed by humans",
    "User has not been notified"
  ],

  "human_review_required": true,
  "escalate_to": ["moderation_team"]
}
```

---

## Agent Status Updates

### Periodic Health Check

```json
{
  "message_type": "agent_health_check",
  "message_id": "unique_uuid",
  "timestamp": "2025-10-20T15:00:00Z",
  "from_agent": "lifecycle",
  "to_agent": "orchestrator",

  "status": "healthy|degraded|error",
  "uptime_seconds": 86400,
  "last_task_completed": "2025-10-20T14:55:23Z",

  "performance_metrics": {
    "tasks_completed_last_hour": 12,
    "average_response_time_ms": 2340,
    "error_rate_percentage": 0.5,
    "confidence_score_average": 0.92
  },

  "issues": [
    "CI/CD API experiencing intermittent timeouts"
  ],

  "warnings": [
    "Token usage approaching daily limit"
  ]
}
```

---

## Communication Best Practices

### For All Agents

#### DO:
- ✅ Use structured JSON for all inter-agent messages
- ✅ Include confidence scores for all decisions
- ✅ Provide clear, human-readable rationale
- ✅ Log all messages to audit trail
- ✅ Include timestamps in ISO 8601 format
- ✅ Use unique message IDs for tracking
- ✅ Reference previous messages with `in_reply_to`

#### DON'T:
- ❌ Send unstructured text messages
- ❌ Omit confidence scores
- ❌ Skip rationale explanations
- ❌ Communicate directly between specialized agents (always via Orchestrator)
- ❌ Include secrets or credentials in messages
- ❌ Make CoC flags public

### Message Size Limits
- **Maximum message size**: 100KB
- **Rationale field**: Max 1000 characters
- **Context content**: Use excerpts, not full documents
- **Action lists**: Max 50 actions per message

### Timeout Handling
- **Default timeout**: 5 minutes per task
- **Long-running tasks**: Request extended timeout
- **Timeout response**: Send failure message with timeout reason
- **Retry protocol**: Exponential backoff (1s, 2s, 4s, 8s, 16s)

### Error Reporting
- Always include specific error type
- Provide actionable error messages
- Indicate if error is recoverable
- Track retry attempts
- Escalate after max retries (default: 3)

---

## Audit Trail Format

All messages are logged to public audit trail (except CoC flags) in this format:

```
[2025-10-20T14:30:00Z] [orchestrator→triage] TASK: Triage new issue #123
[2025-10-20T14:30:15Z] [triage→orchestrator] SUCCESS: Applied 'bug' label (confidence: 0.97)
[2025-10-20T14:30:16Z] [orchestrator] LOGGED: Issue #123 triaged as bug
```

### Audit Trail Requirements
- Public by default (except CoC flags and credentials)
- Immutable once written
- Include timestamps, agents, actions, confidence
- Human-readable format
- Queryable for analysis

---

## Version History

- **v1.0** (2025-10-20): Initial protocol specification

## Compliance

All agents MUST comply with these protocols. Violations should be logged and reported to maintainers for system improvement.
