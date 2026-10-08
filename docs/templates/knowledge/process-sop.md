# Process SOP Template

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** a standard operating procedure (SOP) for one recurring process, written so that a trained BSA can run it the same way every time, with its controls, exceptions and records. It complements the process map (`docs/templates/bsa/03-process-map-as-is-to-be.md`): the map shows the flow and pain points; the SOP says exactly how to do each step.
- **Who uses it:** the hire who is learning the process writes it (learn-by-documenting). The person who runs the process today validates it. The checker (Senior or Manager) reviews it. Anyone running or covering the process follows it.
- **When:** draft SOP lines within 24 hours of any shadowing session. 1 SOP draft by day 30, 2 by day 60 (including your track's method SOP: Research method SOP v0.1 in W5), 3 by day 90 with your primary process SOP published as v1.0 in W13 (A90-4, B90-4). Exports and Reporting SOPs as those items transition (M7 from W6, M8 from W10).

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. **Shadow first, write fast.** Take notes during a real instance; write the steps within 24 hours, while you still remember the clicks.
2. **One SOP per process.** If a step is a whole process of its own (for example "load pending costs"), give it its own SOP and link it.
3. **Write steps as instructions.** Start with a verb, one action per step, name the system and screen, and say what the result should be. "Check the data" is not a step; "Compare the row count in the load log with the approved file; they must match" is.
4. **Mark every control.** Each maker-checker point appears in the procedure as [CONTROL Cn] and in the controls table.
5. **Test it.** The other hire, or the process owner, follows the SOP on a real or practice instance. Fix every place they hesitate.
6. **Status.** Draft, then Reviewed (checker has reviewed it), then Published (v1.0 or later, on the shared OneNote section "05 Process SOPs"). Drafts stay in your own OneNote section so nobody relies on unreviewed steps.
7. **Keep it alive.** Update it when the process, a system, a regulation or a template changes, and at least every [COMPANY: review interval]. Every change gets a revision line.

### Screenshot rules

- Put a placeholder in the step while drafting: `[Screenshot S3: Oracle cost type window, Cost Type field highlighted]`.
- Capture in OneNote with Insert > Screen Clipping (or Windows+Shift+S), and place the image directly under its step.
- Highlight the field or button; crop the rest.
- Remove or blur personal data, supplier prices, margins and anything confidential before the SOP is published.
- Re-capture screenshots after any system change, and during e2open cutover.

## Template

### 1. Document control

| Field | Entry |
|---|---|
| SOP ID and title | [SOP-RES-01 Respond to a new tariff action; SOP-STC-01 Standard cost update] |
| Version and status | [v0.1 Draft, v1.0 Published] |
| Author | [Hire A or B] |
| Process owner | [Role who runs the process today] |
| Checker | [Senior or Manager] |
| Effective date / next review | [Date] / [Date] |
| Related documents | [Process map, templates, tool docs, other SOPs] |

### 2. Purpose

[Two or three sentences: what the process achieves and why it matters (compliance, cost accuracy, broker data, Finance).]

### 3. Scope

| In scope | Out of scope |
|---|---|
| [Countries, product groups, systems, types of requests] | [What this SOP does not cover, and where that is covered] |

### 4. Roles and RACI

| Activity | [Role 1: maker] | [Role 2: checker] | [Role 3] | [Role 4] |
|---|---|---|---|---|
| [Activity] | [R] | [A] | [C] | [I] |

R = does it, A = accountable (one per row), C = consulted, I = informed. The maker and the checker are never the same person.

### 5. Frequency and trigger

| Field | Entry |
|---|---|
| Trigger | [Event that starts the process: new Federal Register notice, cost calendar date, Jira request] |
| Frequency and volume | [How often; typical volume] |
| Deadline | [Service level: for example, checked brief within n working days of publication] |
| Start and end points | [First step] / [Last step and its output] |

### 6. Inputs

| Input | Source | Format | Ready by |
|---|---|---|---|
| [Input] | [System, person, external source] | [File, report, notice] | [Time or day] |

### 7. Procedure

| Step | Role | Action | System | Expected result or output | Screenshot |
|---|---|---|---|---|---|
| 1 | [Role] | [Verb + object + detail] | [System and screen] | [What you should see or produce] | [S1] |
| 2 | [Role] | [ ] | [ ] | [ ] | [S2] |
| 3 | [Checker] | [CONTROL C1] [What the checker compares] | [ ] | [Sign-off recorded on Jira] | [n/a] |

### 8. Controls (maker-checker)

| Control ID | Step | What is checked, and how | Maker | Checker | Evidence |
|---|---|---|---|---|---|
| [C1] | [Step n] | [Compare X with Y; tolerance] | [Role] | [Senior or Manager] | [Jira comment with name, date, version, findings] |

Rule: every release of a tariff brief or model, and every standard cost update, has a documented second-person review before release. This does not stop after day 90.

### 9. Exceptions and escalation

| Situation | What to do | Escalate to | Within |
|---|---|---|---|
| [Source unclear or conflicting] | [Log the question; rate confidence Low; ask the broker] | [Senior] | [Same day] |
| [Deadline at risk] | [Tell the requester the new date and why] | [Manager] | [As soon as known] |
| [Error found after release] | [Stop further use; correct; re-check; tell recipients] | [Manager] | [Same day] |

### 10. KPIs

| KPI | Definition | Target | Source | Reviewed |
|---|---|---|---|---|
| [Cycle time] | [Trigger to checked output, working days] | [COMPANY: target] | [Jira dates] | [Monthly in the 1:1] |
| [Quality] | [Material errors found after release] | 0 | [Jira, closeouts] | [Monthly] |
| [Control] | [Releases with a documented checker sign-off] | 100% | [Jira] | [Monthly] |

Examples. Research: share of new actions logged within 1 working day of publication; checker findings per brief. Standard Cost: post-load tie-out differences (target 0); items above the variance threshold without an explanation (target 0); share of PPV explained by driver.

### 11. Records and retention

| Record | Where stored | Retention | Owner |
|---|---|---|---|
| [Brief, model, checker sign-off, cost file, approvals, load logs] | [COMPANY: folder or system] | [COMPANY: records retention schedule] | [Role] |

Customs-related records have legal minimum retention periods that the company schedule must meet. In general: US, 5 years from the date of entry (19 CFR 163.4), and drawback records until the third anniversary of payment of the claim; Canada, 6 years (CBSA Memorandum D17-1-21); Mexico, 5 years under the Código Fiscal de la Federación (article 30), longer where tax effects continue. Confirm with the Senior and [COMPANY: records retention policy owner] which records your process creates fall under these rules.

### 12. Revision history

| Version | Date | Change | Author | Reviewed by |
|---|---|---|---|---|
| [v0.1] | [ ] | [First draft from shadowing on [date]] | [ ] | [n/a] |

## Example: weak steps rewritten

| Weak step | Problem | Rewritten step |
|---|---|---|
| "Check the notice." | No action, no output | "Open the Federal Register notice. Copy the effective-date sentence word for word into Part 5 of the brief, with its page reference." |
| "Pull the items." | No system, no filter, no result | "Run the saved candidate query [COMPANY: query name] with the annex prefixes loaded. Expected: a list of items with HTS and origin; record the row count in Part 9." |
| "Get it reviewed." | Control not defined | "[CONTROL C2] Send the brief and model link to the Senior on the Jira story. The Senior compares each HTS prefix, rate and date with the source and records name, date, version and findings." |
| "Load the costs." | Hides a whole sub-process and its risk | "Follow SOP-STC-02 (load and simulate). Do not run the update until Finance has approved the simulation report." |

## Quality checklist before you send for review

- [ ] Trigger, start point, end point and deadline are clear.
- [ ] Every step starts with a verb, names its system, and states its expected result.
- [ ] Every maker-checker point is in the procedure and in the controls table, with evidence.
- [ ] Exceptions say what to do and whom to tell, by when.
- [ ] KPIs have a definition, a target and a data source.
- [ ] Records and retention are filled in.
- [ ] Screenshots are placeholders or captured, with confidential data removed.
- [ ] Someone other than me followed the SOP and I fixed the gaps.
- [ ] Status, version and revision history are updated.
