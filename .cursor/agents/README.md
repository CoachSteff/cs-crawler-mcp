# SuperPrompt Framework AI Agent System

## Overview

This directory contains the AI agent system for managing the SuperPrompt Framework GitHub repository. The system consists of multiple specialized agents coordinated by a central Orchestrator, designed to augment (not replace) human maintainers.

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   GitHub Webhook Events                  │
│         (issues, PRs, comments, periodic triggers)       │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │   Orchestrator Agent       │◄────── All agents report back
        │   (The Dispatcher)         │
        └────────────┬───────────────┘
                     │
         ┌───────────┴───────────┐
         │   Delegates tasks to: │
         └───────────┬───────────┘
                     │
     ┌───────────────┴────────┬──────────────┬──────────────┬────────────┬────────────┐
     ▼                        ▼              ▼              ▼            ▼            ▼
┌──────────┐        ┌──────────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│Concierge │        │   Triage     │  │Lifecycle │  │  Scribe  │  │Community │  │ Repo Mgr │
│  Agent   │        │    Agent     │  │  Agent   │  │  Agent   │  │  Agent   │  │  Agent   │
└──────────┘        └──────────────┘  └──────────┘  └──────────┘  └──────────┘  └──────────┘
    │                      │                │             │             │             │
    └──────────────────────┴────────────────┴─────────────┴─────────────┴─────────────┘
                                             │
                               Coordinated actions on issues,
                            PRs, community, and repository config
```

## Agent Roster

### 1. Orchestrator Agent (The Dispatcher)
**Location**: `orchestrator/`
**Role**: Central coordinator for all agent activities

**Responsibilities**:
- Consume GitHub webhook events
- Route tasks to specialized agents
- Maintain workflow state
- Facilitate inter-agent communication
- Coordinate Human-in-the-Loop approvals

### 2. Contributor Concierge Agent
**Location**: `concierge/`
**Role**: Welcoming and onboarding support

**Responsibilities**:
- Welcome first-time contributors
- Suggest good first issues
- Answer common questions
- Provide development guidance
- Support contributor success

**Key Metrics**:
- New contributor retention rate
- Time to first contribution
- Help request resolution rate

### 3. Triage & Prioritization Agent
**Location**: `triage/`
**Role**: Issue intake and categorization

**Responsibilities**:
- Classify and label new issues
- Detect duplicate issues
- Validate bug report completeness
- Monitor feature request engagement
- Assign preliminary priorities

**Key Metrics**:
- Time to triage (<15 minutes target)
- Triage accuracy (>90% target)
- Duplicate detection rate

### 4. Contribution Lifecycle Agent
**Location**: `lifecycle/`
**Role**: PR validation and code quality

**Responsibilities**:
- Trigger and monitor CI/CD
- Perform automated code reviews
- Generate PR summaries
- Create autonomous bug fixes
- **NEVER merge PRs** (humans only)

**Key Metrics**:
- PR cycle time (40% reduction target)
- Rework rate (30% reduction target)
- Automated review effectiveness (98% target)

### 5. Scribe & Archivist Agent
**Location**: `scribe/`
**Role**: Documentation maintenance

**Responsibilities**:
- Enforce "docs-as-code" principle
- Detect documentation gaps
- Generate documentation drafts
- Maintain foundational docs
- Track documentation quality

**Key Metrics**:
- Documentation staleness rate (<10% target)
- API documentation coverage (>95% target)
- PR documentation compliance (>90% target)

### 6. Community Health & Engagement Agent
**Location**: `community/`
**Role**: Community dynamics monitoring

**Responsibilities**:
- Monitor Code of Conduct (private flagging only)
- Track contributor recognition opportunities
- Manage stale issues/PRs
- Generate community health reports
- Support positive community culture

**Key Metrics**:
- Community sentiment (>85% positive target)
- Contributor diversity (25% YoY increase target)
- Response time to new contributors (<24h target)

### 7. Repository Management Agent
**Location**: `repository-manager/`
**Role**: Repository administration and infrastructure management

**Responsibilities**:
- Configure repository settings and features
- Manage branch protection and merge rules
- Create and publish releases (with approval)
- Generate changelogs and release notes
- Manage labels, milestones, and project boards
- Monitor repository health and generate reports
- Manage collaborator access (with approval)
- Audit repository configuration and compliance

**Key Metrics**:
- Repository Health Score (>85/100 target)
- Release cadence (predictable, on-schedule)
- Configuration accuracy (zero critical errors)

## Directory Structure

```
.cursor/
├── agents/
│   ├── README.md (this file)
│   ├── orchestrator/
│   │   ├── instructions.md        # Agent's operational instructions
│   │   ├── rules.md               # Strict operational rules
│   │   └── context/
│   │       ├── agent-ecosystem.md # How agents work together
│   │       └── repository-context.md # Project-specific context
│   ├── concierge/
│   │   ├── instructions.md
│   │   ├── rules.md
│   │   └── context/
│   │       └── agent-awareness.md # Collaboration with other agents
│   ├── triage/
│   │   ├── instructions.md
│   │   ├── rules.md
│   │   └── context/
│   │       └── agent-awareness.md
│   ├── lifecycle/
│   │   ├── instructions.md
│   │   ├── rules.md
│   │   └── context/
│   │       └── agent-awareness.md
│   ├── scribe/
│   │   ├── instructions.md
│   │   ├── rules.md
│   │   └── context/
│   │       └── agent-awareness.md
│   ├── community/
│   │   ├── instructions.md
│   │   ├── rules.md
│   │   └── context/
│   │       └── agent-awareness.md
│   └── repository-manager/
│       ├── instructions.md
│       ├── rules.md
│       └── context/
│           └── agent-awareness.md
└── shared-context/
    ├── guiding-principles.md      # Core principles for all agents
    └── communication-protocols.md # Inter-agent communication standards
```

## Guiding Principles

All agents follow these five core principles:

### 1. Augmentation over Automation
Agents augment human maintainers, never replace them. Final authority rests with humans on all matters requiring judgment.

### 2. Radical Transparency
Every action is logged publicly with clear rationale and confidence scores. All decision-making is auditable.

### 3. Community Over Code
Community health and psychological safety take precedence over efficiency. Lower barriers to entry, be welcoming and supportive.

### 4. Secure by Design
Security is integrated at every layer. Scan all generated code, protect secrets, validate inputs, prevent abuse.

### 5. Meritocratic and Fair
Operate as a neutral facilitator. Ensure transparent attribution for all AI-assisted contributions. Treat all community members fairly.

## Human-in-the-Loop (HITL) Protocol

### Autonomous Actions (No Approval Required)
- Apply standard labels (confidence ≥95%)
- Post informational comments
- Trigger CI/CD pipelines
- Welcome new contributors
- Generate documentation drafts (as suggestions)

### Require Approval (HITL)
- Close issues as duplicates
- Apply `critical-bug` label (requires 2 maintainers)
- Create autonomous bug fix PRs
- Modify foundational documents

### Prohibited Actions (Never Allowed)
- **Merge pull requests** (always human decision)
- Close contentious issues without approval
- Make architectural decisions
- Override human maintainer decisions
- Take public enforcement action on CoC violations

## Communication Protocol

### Inter-Agent Communication
- All communication flows through the Orchestrator
- Structured JSON message format
- Includes confidence scores and rationale
- Logged to public audit trail (except CoC flags)
- Agents do NOT communicate directly with each other

### Message Types
1. **Task Delegation** - Orchestrator → Specialized Agent
2. **Task Completion** - Specialized Agent → Orchestrator
3. **HITL Approval Request** - Agent → Orchestrator → Human
4. **CoC Violation Flag** - Community Agent → Orchestrator → Moderators (PRIVATE)
5. **Agent Health Check** - Agent → Orchestrator

See `../shared-context/communication-protocols.md` for detailed specifications.

## Getting Started

### For Maintainers

1. **Review the Guiding Principles**: `../shared-context/guiding-principles.md`
2. **Understand Each Agent**: Read each agent's `instructions.md` and `rules.md`
3. **Configure Thresholds**: Adjust confidence thresholds and timeouts as needed
4. **Set Up Webhooks**: Configure GitHub webhooks to trigger agent workflows
5. **Monitor Activity**: Review audit logs and agent health reports

### For Contributors

1. **Interact with Agents**: @mention agents in comments for help
2. **Use Commands**:
   - `/agent find-gfi` - Suggest issue as good first issue (maintainer only)
   - `/agent summarize` - Generate PR summary
   - `/agent draft-docs` - Generate documentation draft
   - `/agent fix this` - Attempt autonomous bug fix (maintainer approval required)
   - `/agent configure [setting]` - Configure repository settings (maintainer only)
   - `/agent prepare-release [version]` - Prepare release (maintainer only)
   - `/agent repo-stats` - Generate repository statistics report
3. **Understand Agent Actions**: All agent comments are clearly marked
4. **Provide Feedback**: Help improve agents by reporting issues or suggestions

## Configuration

### Confidence Thresholds
- **Triage Agent**: 95% for auto-labeling, 85% for needs-triage
- **Lifecycle Agent**: 80% for auto-fix attempt, 70% for code review suggestions
- **Scribe Agent**: 85% for docs-needed flag, 75% for draft generation
- **Community Agent**: 80% for CoC violation flag

### Timeouts
- **Interactive tasks**: 60 seconds
- **Triage/labeling**: 5 minutes
- **Code review**: 10 minutes
- **Auto-fix generation**: 15 minutes

### Stale Item Thresholds
- **Issues**: 90 days of inactivity
- **PRs**: 60 days of inactivity
- **Grace period**: 14 days after first reminder

## Monitoring and Observability

### Audit Trail
All agent actions logged to: `.cursor/agents/audit-trail.log`
- Timestamp
- Agent name and version
- Event ID and type
- Action taken
- Rationale and confidence score
- Outcome

### Key Performance Indicators (KPIs)

**Project Velocity**:
- Pull Request Cycle Time (target: <43 hours)
- Time to First Triage (target: <15 minutes)
- Automated Review Effectiveness (target: 98%)

**Community Health**:
- New Contributor Retention Rate (target: 15%)
- Time to First Contribution (target: <48 hours)
- Community Sentiment Score (target: >85%)

**Agent Performance**:
- Automation Accuracy (target: >90%)
- Task Completion Rate (target: >60% for auto-fixes)
- Maintainer Adoption Rate (target: >80%)

### Health Checks
- Agents perform self-health checks every 5 minutes
- Orchestrator monitors agent responsiveness
- Alerts maintainers on repeated failures or degraded performance

## Troubleshooting

### Agent Not Responding
1. Check agent health status
2. Review recent error logs
3. Verify webhook configuration
4. Check rate limits and API quotas
5. Apply `AI-PAUSE` label if needed

### Incorrect Agent Actions
1. Human maintainers can always override
2. Provide feedback in agent-generated comments
3. Adjust confidence thresholds if needed
4. Report systematic issues to maintainer team

### Emergency Stop
Apply `AI-PAUSE` label to any issue, PR, or the repository to immediately halt agent activity in that scope.

## Security Considerations

### Secret Management
- All credentials stored in GitHub Secrets
- Agents scan for secrets in generated code
- Never expose API keys or tokens
- Use secure communication channels

### Vulnerability Scanning
- SAST (Static Application Security Testing) on all generated code
- Dependency scanning for known vulnerabilities
- Regular security audits of agent system

### Prompt Injection Defense
- All user input sanitized
- Context-fencing in agent prompts
- Input validation against malicious patterns
- Rate limiting to prevent abuse

## Attribution and Licensing

### AI-Generated Content
All AI-generated contributions include:
- Commit trailer: `Assisted-by: SuperPrompt-Agent-v1.x`
- Co-author: `Co-Authored-By: Claude <noreply@anthropic.com>`
- PR description section: "AI Assistance Disclosure"

### Licensing
All agent-generated code is subject to the project's open-source license. Agent activity tracked separately from human contributions.

## Version History

- **v1.0** (2025-10-20): Initial agent system deployment
  - 6 specialized agents (Orchestrator, Concierge, Triage, Lifecycle, Scribe, Community)
  - Hierarchical multi-agent architecture
  - HITL protocol implementation
  - Comprehensive documentation

## Contributing to the Agent System

### Suggesting Improvements
1. File an issue with `agent-improvement` label
2. Describe the problem or opportunity
3. Propose solution or enhancement
4. Include examples and use cases

### Modifying Agent Behavior
1. Update relevant `instructions.md` or `rules.md`
2. Test changes thoroughly
3. Document changes in version history
4. Get maintainer approval before deploying

### Adding New Agents
1. Propose new agent with clear mandate
2. Ensure no overlap with existing agents
3. Follow established directory structure
4. Include comprehensive documentation
5. Integrate with Orchestrator routing

## Support and Feedback

- **GitHub Issues**: Report bugs or request features
- **Discussions**: General questions and feedback
- **Maintainer Contact**: For security issues or urgent matters

## License

This agent system is part of the SuperPrompt Framework and is subject to the same license.

---

**Built with**: Claude AI by Anthropic
**Maintained by**: SuperPrompt Framework Core Team
**Last Updated**: 2025-10-20
