# Requirements Template (BRD-lite)

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** define what a change or new capability must do, why, and how everyone will know it works, in 2 to 6 pages. Use it for custom tool enhancements, new reports, process changes, and the hires' parts of the e2open requirements.
- **Who uses it:** the BSA (maker) writes it; the requester or business owner agrees to it and signs; the checker (Senior or Manager) reviews it; the developer or tool owner builds from it; UAT testers turn its acceptance criteria into test cases (`docs/templates/bsa/05-uat-test-plan.md`).
- **When:** after intake routes a request to an epic that adds or changes capability (`docs/templates/bsa/01-intake-request.md`), and before anyone builds. Taught in M4 in W3. A one-story change with clear acceptance criteria does not need this document; the Jira story is enough.

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. Start from the intake record. Copy the decision it supports and the date driver into section 1.
2. Talk to the requester and to one person who actually does the work (30 to 45 minutes each; use the interview questions in `docs/templates/bsa/03-process-map-as-is-to-be.md`). Ask to see real examples: last month's file, the screen, the report.
3. Write the problem statement and success measures first. Get the requester to agree to those two sections (a 15-minute check) before you write any requirement.
4. One requirement is one testable sentence: "The [tool, report or process] shall [behavior] [condition]." If it contains "and", it is probably two requirements.
5. Every Must needs acceptance criteria a tester can check with real data. Use Given/When/Then for behavior; use a measurable condition otherwise.
6. Keep business rules apart from requirements. A business rule is true whatever the system (for example, which date sets the duty rate). A requirement says what the system does about it.
7. Give every requirement a source: a person and date, a regulation, an SOP, a defect. Delete or confirm any requirement without one.
8. Keep open questions visible. Do not sign off while any open question blocks a Must.
9. Versions: 0.1, 0.2 for drafts; 1.0 at sign-off. After 1.0, every change goes in the change log and is re-approved.

### MoSCoW priorities

| Priority | Meaning | Test |
|---|---|---|
| Must | Without it the release fails its objective, a control, or a compliance need | Would we refuse to go live without it? |
| Should | Important; a workaround exists for a while | Can users live without it for one cycle? |
| Could | Nice to have; drop it first when time is short | Would anyone notice if it slipped? |
| Won't (this time) | Agreed out of scope for this release; recorded so it is not lost | Has the requester agreed in writing? |

If everything is a Must, nothing is. Aim for Musts to be no more than about 60% of the build effort.

A practical constraint for this team: anything built in the AS400-era tools now only lives until e2open replaces it ([COMPANY: expected e2open go-live]). Prefer the smallest fix that solves the problem, and say in section 3 whether the e2open project will replace it.

## Template

### 0. Document control

| Field | Entry |
|---|---|
| Title | [Short name of the change] |
| Jira epic | [Key] |
| Version and status | [0.1 Draft, In review, 1.0 Approved] |
| Maker (author) | [Name] |
| Checker | [Senior or Manager] |
| Approver | [Business owner and Manager] |
| Related documents | [Intake record, as-is map, data mapping spec, UAT plan, change request] |

### 1. Problem statement

[Who] cannot [do what] because [cause]. As a result, [impact, with numbers where you have them: hours, error counts, $, compliance exposure].

Evidence: [examples, counts, dates, links].

### 2. Objectives and success measures

| ID | Objective | Measure | Baseline | Target | How and when measured |
|---|---|---|---|---|---|
| O1 | [What must be true after the change] | [Metric] | [Today's value] | [Target value] | [Method, date] |
| O2 | [ ] | [ ] | [ ] | [ ] | [ ] |

### 3. Scope

- **In scope:** [processes, tools, countries, item sets, reports]
- **Out of scope:** [what is explicitly not included]
- **Constraints:** [dates, systems, budget, e2open timing, access]
- **Replaced by e2open?** [Yes, no, unknown; why]

### 4. Stakeholders and RACI

R = does the work, A = accountable (one per row), C = consulted, I = informed.

| Activity | Requester | BSA maker | Checker | Data owner | Manager |
|---|---|---|---|---|---|
| Agree problem and objectives | A | R | C | C | I |
| Write requirements | C | R | C | C | A |
| Approve requirements | A | R | C | C | C |
| Build or configure | I | C | I | I | A |
| UAT and sign-off | A | R | C | C | I |

Adjust the columns to the real stakeholders and keep exactly one A per row. The business owner is accountable for what the requirements say; the Manager still signs in section 14 to confirm the BSA work is complete and checked.

| Stakeholder | Role in this change | What they need | How engaged |
|---|---|---|---|
| [Name or COMPANY role] | [Requester, user, data owner, Finance, broker contact, IT] | [Their interest] | [Interview, review, sign-off, informed by email] |

Broker, agente aduanal or trade counsel as a stakeholder: before your day-60 review you do not contact them yourself; the Senior (or the Manager) puts your questions to them. After day 60, with the Senior's agreement, you may email the broker with the Senior copied.

### 5. Current state

[3 to 6 sentences: how it works today, volumes, workarounds, known defects. Link the as-is map (`docs/templates/bsa/03-process-map-as-is-to-be.md`).]

### 6. Business rules

| ID | Rule | Source | Owner |
|---|---|---|---|
| BR-01 | [A rule that holds whatever the system] | [Regulation, policy, SOP, person and date] | [Research, Standard Cost, Finance, other] |

### 7. Functional requirements

| ID | Requirement | Priority (MoSCoW) | Source | Acceptance criteria |
|---|---|---|---|---|
| FR-01 | The [tool, report or process] shall [behavior] [condition]. | [Must, Should, Could, Won't] | [Person and date, regulation, defect] | Given [context], when [action], then [observable result]. |
| FR-02 | [ ] | [ ] | [ ] | [ ] |

### 8. Non-functional requirements

| ID | Category | Requirement | Measure |
|---|---|---|---|
| NF-01 | Access and security | [Who can view, edit, approve; least privilege; no shared logins] | [Role list checked by the system owner] |
| NF-02 | Audit trail | [Who changed what, when, old value, new value, reason or Jira key] | [Log fields present for every change] |
| NF-03 | Control | [Maker-checker step and its evidence] | [Checker name and date recorded before release] |
| NF-04 | Performance | [Run time, volume] | [Seconds or minutes for N records] |
| NF-05 | Supportability | [Tool doc updated; no hard-coded rates, dates or paths; settings in a table] | [Tool doc reviewed; code review finds no hard-coded values] |
| NF-06 | Retention | [How long outputs and evidence are kept] | [COMPANY: records retention policy] |

### 9. Data and reports

| Data element or report | Source system | Owner | Frequency | Used for |
|---|---|---|---|---|
| [Element] | [AS400, Oracle, SQL Server, warehouse, Excel, external source] | [Data owner] | [Daily, per cycle, ad hoc] | [Decision or output] |

Field-level detail goes in a data mapping spec (`docs/templates/bsa/04-data-mapping-spec.md`).

### 10. Assumptions and dependencies

| ID | Assumption or dependency | Impact if wrong | Confirm by (who, when) |
|---|---|---|---|
| A-01 | [Something you believe but have not confirmed] | [What changes] | [Name, date] |

### 11. Risks

| ID | Risk | Likelihood (H, M, L) | Impact (H, M, L) | Mitigation | Owner |
|---|---|---|---|---|---|
| R-01 | [What could go wrong] | [ ] | [ ] | [Action] | [Name] |

### 12. Open questions

| ID | Question | Asked to | Asked on | Answer | Status |
|---|---|---|---|---|---|
| Q-01 | [Question] | [Name] | [Date] | [Answer and date] | [Open, Answered, Blocks a Must] |

### 13. Change log

| Version | Date | Change | By | Approved by |
|---|---|---|---|---|
| 0.1 | [Date] | First draft | [Maker] | n/a |

### 14. Sign-off

| Role | Name | Decision | Date | Conditions or comments |
|---|---|---|---|---|
| Business owner or requester | [ ] | [Approved, Approved with conditions, Rejected] | [ ] | [ ] |
| Data owner | [ ] | [ ] | [ ] | [ ] |
| Checker | [ ] | [Review complete; findings closed] | [ ] | [ ] |
| Manager | [ ] | [ ] | [ ] | [ ] |
| Tool or system owner | [ ] | [ ] | [ ] | [ ] |

## Filled example (short)

Effective-dated duty rates in [COMPANY: name of std-cost tool]. Maker: Hire B. Checker: Manager. Hire A consulted on BR-01 and BR-03. Figures are illustrative.

**Problem statement.** Standard Cost analysts cannot reproduce the duty rate behind a past cost run because [COMPANY: name of std-cost tool] holds one duty rate per HTS number and country, with no effective or end date. When a tariff action starts mid-period, the rate is overwritten by hand and the prior rate is lost. As a result, duty-driven PPV cannot be separated from vendor price changes, and an audit question on one closed period took about 6 hours to rebuild from emails.

| ID | Objective | Measure | Baseline | Target | How and when measured |
|---|---|---|---|---|---|
| O1 | Every duty rate carries its date range | Rates with an effective-from date | 0% | 100% | Query the rate table at go-live |
| O2 | Past cost runs can be reproduced | Closed periods re-run with identical duty | 0 of 3 | 3 of 3 | UAT: re-run three closed periods |
| O3 | Every rate change is checked | Changes with a checker recorded | Not tracked | 100% | Monthly audit-log review |

| ID | Rule | Source | Owner |
|---|---|---|---|
| BR-01 | A US import is dutiable at the rate in effect at the time of entry (or withdrawal from warehouse for consumption), not the PO, ship or receipt date, unless the action itself says otherwise (for example an in-transit provision) | 19 CFR 141.69; the Tariff-Impact Brief for each action | Research |
| BR-02 | A period's standard cost uses the duty rate expected for that period, measured on [COMPANY: costing reference date, for example the first day of the cost period] | [COMPANY: Finance costing policy] | Standard Cost and Finance |
| BR-03 | Rates and effective dates are entered only from a checked Tariff-Impact Brief; the tool does not decide legal scope | Boundary rule | Research |

| ID | Requirement | Priority (MoSCoW) | Source | Acceptance criteria |
|---|---|---|---|---|
| FR-01 | The tool shall store an effective-from date and an optional effective-to date for each HTS number, country and rate type (base or additional). | Must | Hire B interview with [COMPANY: Finance cost accountant], date | Given a new rate row, when I save it without an effective-from date, then the save is blocked with a message naming the missing field. |
| FR-02 | The tool shall apply, in a cost run, the rate whose date range contains the costing reference date. | Must | BR-02 | Given a base rate of 2.5% and an additional 25% from 2026-11-03 (hypothetical), when the reference date is 2026-11-02, then 2.5% is applied; when it is 2026-11-03, then 27.5% is applied (the brief says the additional duty stacks on the base rate). |
| FR-03 | The tool shall reject overlapping date ranges for the same HTS number, country and rate type. | Must | Defect history | Given an open-ended row from 2026-11-03, when I add a row from 2026-12-01 without closing the first, then the save is blocked and the conflicting row is named. |
| FR-04 | The tool shall keep a new or changed rate pending until a second user, not the maker, approves it, and shall record the approver and timestamp. | Must | Control rule; O3 | Given a rate saved by user A, when user A tries to approve it, then approval is refused; when user B approves it, then the rate becomes active and the NF-02 log shows A, B and both timestamps. |
| FR-05 | The tool shall show, on each rate row, the ID and version of the Tariff-Impact Brief the rate came from. | Should | BR-03 | Given a rate loaded from brief [brief ID] v1.0, when I open the rate row, then it shows "[brief ID] v1.0". Workaround until built: the Jira key in the NF-02 audit log links to the brief. |
| FR-06 | The tool shall feed automatic tariff content updates. | Won't (this time) | Manager decision | Deferred to the e2open project. |

Audit logging is a quality the tool must have, so it sits with the non-functional requirements (Section 8), not in the functional table:

| ID | Category | Requirement | Measure |
|---|---|---|---|
| NF-02 | Audit trail | The tool shall log every rate change with user, timestamp, old value, new value and Jira key (Must; source: control rule, O3). | Given any rate edit, when it is saved, then one log row holds all five values; the monthly audit-log review finds them on 100% of changes. |

**Open question.** Q-01: Does Finance measure the period's standard on the first day of the period or with a weighted rate when an action starts mid-period? Asked to [COMPANY: Finance cost accountant]. Status: Blocks FR-02.

## Quality checklist before you send

- [ ] The problem statement names who, what, why and the impact, and contains no solution.
- [ ] The requester agreed the problem and objectives before requirements were written.
- [ ] Every objective has a measure, a baseline and a target.
- [ ] Out of scope is written down, including what e2open will replace.
- [ ] Exactly one A per RACI row.
- [ ] Business rules are separate from requirements, and each has a source.
- [ ] Each requirement is one testable sentence with a MoSCoW priority and a source.
- [ ] Every Must has acceptance criteria with concrete data a tester can use.
- [ ] Non-functional needs cover access, audit trail, the maker-checker step and supportability.
- [ ] The boundary rule holds: Research rules (scope, rates, dates) come from a brief; cost rules come from Finance policy.
- [ ] No open question blocks a Must at sign-off.
- [ ] Version, change log and sign-off table are filled in; the checker's review is recorded on the Jira epic.
