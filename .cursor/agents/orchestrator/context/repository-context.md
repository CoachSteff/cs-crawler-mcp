# Repository Context

## Project Overview

**Repository**: SuperPrompt Framework
**Purpose**: An open-source framework for building advanced prompt engineering solutions
**Governance Model**: Meritocratic, inspired by The Apache Way
**Community Values**: Open communication, community over code, security by design, radical transparency

## Strategic Goals

1. **Increase Maintainer Velocity**: Liberate >50% of maintainer time from automatable tasks
2. **Improve Contributor Experience**: Reduce time-to-first-merged-PR by >75%
3. **Enhance Quality**: 100% of PRs meet baseline quality standards before human review
4. **Foster Community Health**: Maintain >85% positive community sentiment

## Repository Structure

```
superprompt-framework/
├── .github/
│   ├── workflows/          # CI/CD pipeline definitions
│   ├── ISSUE_TEMPLATE/     # Issue templates (bug, feature, etc.)
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── copilot-instructions.md  # Agent constitution
│   └── CODEOWNERS          # Code ownership rules
├── .cursor/
│   └── agents/             # AI agent system (this directory)
├── docs/                   # Project documentation
├── src/                    # Source code
├── tests/                  # Test suites
├── CONTRIBUTING.md         # Contribution guidelines
├── CODE_OF_CONDUCT.md      # Community standards
├── LICENSE                 # Open-source license
├── README.md               # Project introduction
└── package.json            # Dependencies and scripts
```

## Key Documents

### .github/copilot-instructions.md
**Purpose**: Agent constitution - primary source of truth for project conventions, architectural principles, and coding standards

**What it contains**:
- Coding style guidelines
- Architectural patterns and principles
- Build and deployment instructions
- Testing requirements
- Documentation standards

**Agent Usage**: High-priority context for all agent tasks. Consult this file to understand project-specific expectations.

### CONTRIBUTING.md
**Purpose**: Guide for new and existing contributors

**What it contains**:
- How to set up development environment
- How to submit issues and PRs
- Code review process
- Testing requirements
- Branch naming conventions
- Commit message format

**Agent Usage**: Reference for Concierge Agent when onboarding new contributors and for Lifecycle Agent when validating PRs.

### CODE_OF_CONDUCT.md
**Purpose**: Define community standards and expected behavior

**What it contains**:
- Expected behavior standards
- Unacceptable behavior examples
- Reporting procedures
- Enforcement guidelines

**Agent Usage**: Community Health Agent uses this to monitor for violations and maintain community standards.

## CI/CD Pipeline

### Workflow Files
Located in `.github/workflows/`, these define:
- Automated testing on PR creation
- Code linting and style checks
- Security scanning
- Documentation builds
- Release automation

### Required Checks
Before a PR can be merged:
- [ ] All tests pass
- [ ] Code linting passes (no style violations)
- [ ] Security scan clean (no vulnerabilities)
- [ ] Documentation is up-to-date
- [ ] Required approvals obtained (per CODEOWNERS)

### Agent Integration
- Lifecycle Agent triggers CI on PR open/update
- Lifecycle Agent posts CI status in PR comments
- Lifecycle Agent flags PRs that fail checks

## Issue and PR Templates

### Bug Report Template
**Required Fields**:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- System environment (OS, version, etc.)
- Relevant logs or screenshots

**Agent Usage**: Triage Agent validates template completion and requests missing information.

### Feature Request Template
**Required Fields**:
- Feature description
- Use case / motivation
- Proposed solution
- Alternatives considered

**Agent Usage**: Triage Agent labels feature requests and monitors community engagement (upvotes) for prioritization.

### Pull Request Template
**Required Sections**:
- What changed and why
- Testing performed
- Documentation updated (Y/N)
- Breaking changes (Y/N)
- Related issues

**Agent Usage**: Lifecycle Agent validates PR template completion and checks if documentation updates are needed.

## Label Taxonomy

### Type Labels
- `bug` - Something isn't working correctly
- `feature-request` - Request for new functionality
- `documentation` - Improvements or additions to documentation
- `question` - Further information is requested
- `enhancement` - Improvement to existing functionality

### Priority Labels
- `critical-bug` - Requires immediate attention (2 maintainer approvals required)
- `high-priority` - Should be addressed soon
- `low-priority` - Can wait for future milestone

### Process Labels
- `good first issue` - Good for newcomers
- `needs-triage` - Awaiting initial categorization
- `needs-human-review` - Agent confidence below threshold
- `possible-duplicate` - May be duplicate of existing issue
- `docs-needed` - Requires documentation updates
- `agent-fix-approved` - Approved for autonomous bug fix by agent
- `agent-error` - Agent failed to complete task
- `AI-PAUSE` - Emergency stop for agent activity
- `stale` - No activity for extended period

### Status Labels
- `in-progress` - Actively being worked on
- `blocked` - Waiting on external dependency
- `wontfix` - Will not be addressed

### Agent Labels
- `ai-assisted` - Contribution includes AI assistance
- `agent-generated` - Fully generated by AI agent

## Contributor Lifecycle

### First-Time Contributors
**Identification**: GitHub API `author_association` = `FIRST_TIME_CONTRIBUTOR`

**Expected Treatment**:
1. Concierge Agent posts welcome message
2. Links to CONTRIBUTING.md and CODE_OF_CONDUCT.md
3. Offers assistance and suggests good first issues
4. Extra patience and guidance throughout first PR

**Success Metric**: New Contributor Retention Rate (target: 50% increase)

### Experienced Contributors
**Identification**: Multiple merged PRs in history

**Expected Treatment**:
1. Streamlined process with fewer checks
2. Higher trust level for autonomous actions
3. May receive invitations to become maintainers

### Core Maintainers
**Identification**: Listed in CODEOWNERS or with `OWNER`/`MEMBER` association

**Expected Treatment**:
1. Full authority over agent actions
2. Can approve/reject agent proposals
3. Can trigger emergency stops with `AI-PAUSE`
4. Receive escalations from agents

## Repository Knowledge Base (RAG)

### Indexed Content
- All source code files in `src/`
- All documentation in `docs/`
- README.md and other root-level .md files
- Historical issues (open and closed)
- Historical PRs (merged and closed)
- Commit messages and PR descriptions

### Search Capabilities
Agents can perform semantic searches for:
- Function definitions and usage
- Architectural patterns
- Error handling approaches
- Testing methodologies
- Documentation on specific topics
- Historical decisions on similar issues

### Context Refresh
- RAG index updates on every push to main branch
- Incremental updates for new issues and PRs
- Full re-index weekly (configurable)

## Permissions and Access Control

### What Agents CAN Do
- Read all repository content
- Create issues and comments
- Apply labels (with confidence thresholds)
- Create branches and PRs
- Request reviews
- Trigger CI/CD workflows
- Read workflow run results

### What Agents CANNOT Do
- Merge PRs
- Delete branches or tags
- Modify repository settings
- Change permissions
- Force-push
- Bypass required checks
- Modify .github/ governance files without approval
- Override maintainer decisions

## Security Considerations

### Secret Patterns to Detect
- API keys (common formats)
- Private keys (SSH, GPG)
- Tokens (OAuth, JWT)
- Passwords (plaintext)
- Database connection strings
- Cloud provider credentials

### Vulnerability Scanning
- SAST (Static Application Security Testing) on all generated code
- Dependency scanning for known vulnerabilities
- Supply chain security checks

### Prompt Injection Defense
- All user input sanitized before processing
- Context-fencing in agent prompts
- Input validation against malicious patterns

## Performance Expectations

### Response Times
- Interactive tasks (comments, welcome messages): <60 seconds
- Triage and labeling: <5 minutes
- CI/CD integration: <2 minutes from trigger
- Code review: <10 minutes for typical PR

### Throughput
- Handle up to 100 concurrent webhook events per minute
- Process backlog of stale issues/PRs efficiently
- Scale with repository growth

## Quality Standards

### Code Quality
- Pass all linting checks (defined in project config)
- Follow architectural patterns from copilot-instructions.md
- Maintain test coverage thresholds
- Include appropriate error handling
- Use clear, descriptive variable and function names

### Documentation Quality
- Keep README.md synchronized with code
- Update API documentation when signatures change
- Include code examples where helpful
- Maintain changelog for releases
- Write clear commit messages

### Community Interaction Quality
- Welcoming and respectful tone
- Clear, actionable feedback
- Appropriate use of markdown formatting
- Link to relevant documentation
- Acknowledge limitations and offer human escalation

## Attribution and Licensing

### AI-Generated Content Attribution
All agent-generated contributions must include:
- Commit trailer: `Assisted-by: SuperPrompt-Agent-v1.x`
- PR description section: "AI Assistance Disclosure"
- Details of which agent(s) contributed
- Clear distinction from human contributions

### License Compliance
- All code inherits project's open-source license
- Verify AI model terms don't conflict with project license
- Respect contributor license agreements
- Maintain proper copyright notices

## Success Metrics (KPIs)

### Project Velocity
- Pull Request Cycle Time: median time from open to merge (target: <43 hours)
- Time to First Triage: time from issue creation to first label (target: <15 minutes)
- Automated Review Effectiveness: % of CI failures caught by agents (target: 98%)

### Community Health
- New Contributor Retention Rate: % who submit 2nd PR within 90 days (target: 15%)
- Time to First Contribution: median time to first merged PR (target: <48 hours)
- Community Sentiment Score: from surveys and analysis (target: >85% positive)

### Agent Performance
- Automation Accuracy: % of agent actions not reverted by humans (target: >90%)
- Task Completion Rate: % of autonomous fixes that merge with minor edits (target: >60%)
- Maintainer Adoption: % of maintainers using agent features weekly (target: >80%)

## Contact and Escalation

### Human Maintainers
- Listed in CODEOWNERS file
- Tagged for approvals using @mentions
- Receive notifications for agent errors
- Can override any agent decision

### Emergency Procedures
1. Apply `AI-PAUSE` label to halt agent activity
2. Create issue with `agent-error` label
3. Tag maintainer team for urgent attention
4. Document incident for post-mortem

### Feedback Channels
- GitHub Discussions for general feedback
- Issue tracker for bugs and feature requests
- Monthly community calls for strategic input
- Anonymous surveys for sentiment tracking
