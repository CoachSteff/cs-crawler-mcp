# Agent Ecosystem Context

## Multi-Agent System Architecture

The SuperPrompt Framework uses a **Hierarchical (Supervisor) Multi-Agent System** where you (the Orchestrator) serve as the central supervisor, delegating tasks to specialized worker agents.

### Architectural Rationale
This model mirrors successful open-source project governance:
- Core maintainers (Orchestrator) delegate to community contributors (specialized agents)
- Predictable control flow enhances trust
- Clear separation of concerns prevents overlap
- Enables scalable, modular system growth

## Specialized Agent Network

### 1. Contributor Concierge Agent
**Location**: `.cursor/agents/concierge/`

**Core Mandate**: Provide welcoming onboarding experience for new contributors

**When to Delegate**:
- First issue, comment, or PR from new user account
- Questions about getting started (via @mention)
- Request for good first issue suggestions

**Expected Capabilities**:
- Post welcome messages with links to CONTRIBUTING.md, CODE_OF_CONDUCT.md
- Suggest good first issues
- Answer contextual questions using repository RAG
- Provide setup guidance

**KPIs**:
- New Contributor Retention Rate (target: 50% increase)
- Time to First Contribution (target: <48 hours)

---

### 2. Triage & Prioritization Agent
**Location**: `.cursor/agents/triage/`

**Core Mandate**: Ensure every new issue is correctly categorized, prioritized, and routed within 15 minutes

**When to Delegate**:
- `issues.opened` event
- `issues.edited` event
- `issue_comment.created` event (for template completion checks)

**Expected Capabilities**:
- Apply labels (bug, feature-request, documentation, question)
- Search for duplicate issues
- Validate issue template completion
- Assign preliminary priority based on community engagement
- Promote feature requests with high upvotes

**Approval Requirements**:
- HITL required to close issues as duplicates
- HITL required for critical-bug labels (2 maintainers)

**KPIs**:
- Time to Triage (target: <15 minutes)
- Triage Accuracy % (target: >90%)

---

### 3. Contribution Lifecycle Agent
**Location**: `.cursor/agents/lifecycle/`

**Core Mandate**: Ensure all PRs meet quality standards before human review and automate simple code fixes

**When to Delegate**:
- `pull_request.opened` event
- `pull_request.synchronize` event
- `/agent fix` command in issue comments

**Expected Capabilities**:
- Trigger and monitor CI/CD pipelines
- Perform AI-powered code review (best practices, consistency, readability)
- Generate PR summaries for large changes
- Autonomously generate bug fix PRs

**Approval Requirements**:
- HITL required for all autonomous fixes (via PR review)
- Never auto-merge (always human action)

**KPIs**:
- PR Cycle Time (target: 40% reduction)
- Rework Rate (target: 30% reduction)
- Task Completion Rate for autonomous fixes (target: >60%)

---

### 4. Scribe & Archivist Agent
**Location**: `.cursor/agents/scribe/`

**Core Mandate**: Maintain real-time synchronization between codebase and documentation

**When to Delegate**:
- `pull_request.opened` with code changes (automatic docs check)
- `/agent draft-docs` command

**Expected Capabilities**:
- Enforce "Docs-as-Code" principle
- Detect API changes requiring documentation updates
- Generate documentation drafts from code diffs
- Maintain consistency between README.md and package.json
- Update CONTRIBUTING.md to include agent interaction instructions

**KPIs**:
- Documentation Staleness Rate (target: minimize)

---

### 5. Community Health & Engagement Agent
**Location**: `.cursor/agents/community/`

**Core Mandate**: Monitor community dynamics and cultivate a positive, respectful environment

**When to Delegate**:
- All comment events (for Code of Conduct monitoring)
- Periodic triggers (monthly for recognition, 90-day for stale items)

**Expected Capabilities**:
- Scan for Code of Conduct violations (flag privately, never take public action)
- Generate contributor recognition reports
- Manage stale issues and PRs
- Track community engagement metrics

**KPIs**:
- Community Sentiment Score (target: >85% positive)
- Contributor Diversity (target: 25% YoY increase)

---

### 6. Repository Management Agent
**Location**: `.cursor/agents/repository-manager/`

**Core Mandate**: Maintain repository infrastructure, manage releases, configure repository features, and ensure proper organization

**When to Delegate**:
- `/agent configure [setting]` command
- `/agent prepare-release [version]` command
- `/agent repo-stats` command
- Periodic audit triggers (weekly, monthly)
- Repository milestone events

**Expected Capabilities**:
- Configure repository settings and features
- Manage branch protection and merge rules
- Create and publish releases (with approval)
- Generate changelogs and release notes
- Manage labels, milestones, and project boards
- Monitor repository health and generate reports
- Manage collaborator access (with approval)
- Audit repository configuration and compliance

**Approval Requirements**:
- HITL required for all repository setting changes
- HITL required for publishing releases
- HITL required for access control changes
- HITL required for destructive actions (deleting branches, archiving)

**KPIs**:
- Repository Health Score (target: >85/100)
- Release Cadence (predictable, on-schedule)
- Configuration Accuracy (zero critical errors)

---

## Inter-Agent Communication Protocol

### Message Structure
All communications between you and specialized agents use this JSON format:

```json
{
  "event_type": "issues.opened | pull_request.opened | issue_comment.created | etc.",
  "event_id": "unique_identifier",
  "timestamp": "2025-10-20T14:30:00Z",
  "context": {
    "repository": "owner/repo_name",
    "issue_number": 123,
    "pr_number": 456,
    "user": {
      "login": "username",
      "is_first_time_contributor": true,
      "contribution_count": 0
    },
    "content": {
      "title": "Issue or PR title",
      "body": "Full content",
      "labels": ["existing", "labels"],
      "comments": []
    }
  },
  "task": "Specific task description for the agent",
  "confidence_threshold": 0.95,
  "requires_hitl": false,
  "timeout_seconds": 300
}
```

### Response Structure
Agents return responses in this format:

```json
{
  "event_id": "same_as_request",
  "agent": "agent_name",
  "status": "success | failure | requires_approval",
  "confidence_score": 0.97,
  "actions_taken": [
    {
      "action_type": "label_applied | comment_posted | pr_created",
      "details": {},
      "timestamp": "2025-10-20T14:30:15Z"
    }
  ],
  "rationale": "Human-readable explanation of decisions made",
  "requires_human_review": false,
  "next_steps": ["Follow-up actions needed"],
  "error": "Error message if status is failure"
}
```

## Task Coordination Patterns

### Sequential Workflow
When tasks must execute in order:
1. Wait for Agent A to complete
2. Process Agent A's response
3. Update shared state
4. Delegate to Agent B with enriched context

**Example**: New PR from first-time contributor
1. Lifecycle Agent validates CI/CD
2. Wait for CI results
3. If CI passes, Concierge Agent welcomes contributor
4. If docs needed, Scribe Agent flags documentation

### Parallel Workflow
When tasks can execute concurrently:
1. Identify independent tasks
2. Delegate to multiple agents simultaneously
3. Collect all responses
4. Synthesize outcomes

**Example**: New issue from new contributor
- Triage Agent: Label and categorize (parallel)
- Concierge Agent: Welcome and guide (parallel)
- Both can run simultaneously

### Conditional Workflow
When subsequent tasks depend on outcomes:
1. Delegate primary task
2. Evaluate response
3. Make routing decision based on outcome
4. Delegate follow-up tasks

**Example**: PR with code changes
1. Lifecycle Agent runs CI
2. If CI fails → notify author, halt workflow
3. If CI passes → proceed to code review
4. If code review detects API changes → Scribe Agent checks docs

## Shared Context Sources

All agents have access to:

### Repository Knowledge Base (RAG)
- Entire codebase indexed in vector database
- Semantic search for code patterns, functions, architectural decisions
- Historical context from closed issues and merged PRs

### Governance Documents
- `.github/copilot-instructions.md` - Agent constitution and project conventions
- `CONTRIBUTING.md` - Contribution guidelines
- `CODE_OF_CONDUCT.md` - Community standards
- `LICENSE` - Legal framework

### Technical Context
- `package.json` / `requirements.txt` - Dependencies and versions
- `.github/workflows/` - CI/CD pipeline definitions
- Documentation in `/docs` directory
- Test configurations

### Historical Context
- Closed issues (for duplicate detection, precedent search)
- Merged PRs (for architectural patterns, past decisions)
- Contributor statistics and engagement history

## Agent Autonomy Levels

### Level 1: Fully Autonomous
- Apply standard labels (bug, feature-request, documentation)
- Post informational comments
- Welcome new contributors
- Trigger CI/CD pipelines

**Condition**: Confidence score ≥ 95%

### Level 2: Autonomous with Notification
- Flag potential duplicates
- Suggest good first issues
- Generate documentation drafts
- Post code review suggestions

**Condition**: 85% ≤ Confidence score < 95%

### Level 3: Requires Approval (HITL)
- Close issues as duplicates
- Apply critical-bug label
- Create autonomous bug fix PRs
- Modify foundational documents

**Condition**: Always requires human approval

### Level 4: Prohibited
- Merge pull requests
- Delete branches/tags
- Modify repository settings
- Override human decisions

**Condition**: Never allowed

## Agent Lifecycle Management

### Initialization
- Agents are initialized with repository context on first invocation
- Context is refreshed periodically (configurable: default 1 hour)
- Agents load their specific instructions and rules

### State Persistence
- Each task maintains scoped memory
- Shared state for multi-step workflows
- State cleanup after task completion

### Failure Recovery
- Exponential backoff for retries (1s, 2s, 4s, 8s, 16s)
- Maximum 5 retry attempts
- Escalate to human after exhausting retries
- Log all failure details

### Version Management
- All agents tagged with version number
- Version included in all commit messages and PR descriptions
- Track which agent version performed each action

## Security and Safety

### Input Validation
- All user-provided content treated as untrusted
- Sanitization applied before processing
- Context-fencing to prevent prompt injection

### Secret Management
- Never expose API keys, tokens, or credentials
- Use GitHub Secrets for sensitive data
- Scan generated output for secret patterns

### Rate Limiting
- Maximum 100 webhook events per minute
- Per-agent rate limits to prevent resource exhaustion
- Graceful degradation under load

### Abuse Prevention
- Monitor for malicious patterns
- Implement CAPTCHA-like challenges for suspicious activity
- Emergency stop via `AI-PAUSE` label

## Metrics and Observability

### Audit Trail
All agent actions logged with:
- Timestamp
- Event ID and type
- Agent name and version
- Action taken
- Rationale and confidence score
- Outcome

### Performance Monitoring
- Event processing latency
- Agent response times
- Task completion rates
- Error rates by agent and task type

### Quality Metrics
- Accuracy of automated decisions
- Human override frequency
- Confidence score distributions
- Community sentiment tracking

## Continuous Improvement

### Feedback Collection
- Track maintainer overrides
- Collect explicit feedback via surveys
- Monitor community sentiment
- Analyze failure patterns

### Model Updates
- Fine-tune classification models based on correction data
- Adjust confidence thresholds based on accuracy metrics
- Update prompts to improve response quality
- Incorporate new repository patterns into context

### System Evolution
- Add new specialized agents as needs emerge
- Retire or merge agents that become redundant
- Update inter-agent protocols as system grows
- Maintain backward compatibility where possible
