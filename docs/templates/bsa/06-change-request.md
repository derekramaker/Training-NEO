# Change Request Template: Custom Tools and Configuration

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** control every change to a custom tool (Python, Excel VBA, Access, Power Apps, Power Automate), a report, or a system configuration. Each change is described, assessed, tested, reviewed by a second person, reversible and communicated.
- **Who uses it:** the maker (the BSA making the change; from day 60, the hire who owns the tool); the checker (the Manager for tool changes; the Senior for data and report items in their area); the approver (the Manager, plus the system owner for configuration of a system the team does not own); the users, who are told before and after.
- **When:** before any change to a tool, a configuration or production data, whatever its size. First real use in W8 (first tool change, M6). Before day 60 the hires prepare and test changes in a test copy but do not deploy to production (`docs/04-access-request-checklist.md`, rule 2). From the day-60 review, if the Manager grants production change rights, write access covers only the tool the hire owns, and only through this template (rule 3).

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. Open the change request (CR) when the Jira story or bug is ready. Use [COMPANY: CR numbering], or the Jira key plus "-CR".
2. Describe the change as before and after, precisely enough that the checker could spot a difference you didn't intend.
3. Work through every row of the impact assessment. A "No" needs a reason too.
4. Rate the risk (section 5). The rating sets the controls you must complete.
5. Make the change on a copy (development or test), never on the production file. Follow the checklist for the technology (section 7).
6. Test, and attach the evidence. Always include a regression test: run the old and new versions on the same input and confirm the only differences are the ones you intended.
7. Write the rollback plan and confirm the backup exists before you implement.
8. The checker reviews the change, the tests and the rollback plan; the approver approves. Then implement in the agreed window.
9. Tell users before and after (section 10).
10. Do the post-implementation check after the first production run, update the documentation, and close the CR.

### Change types

| Type | When to use | Approval |
|---|---|---|
| Standard | A repeatable, low-risk change on the Manager's pre-approved list ([COMPANY: standard change list]) | Maker-checker on every change; no new approval each time |
| Normal | Everything else | Maker-checker plus approver, before implementation |
| Emergency | Production is producing wrong data now (for example, wrong data going to a broker or Finance) | Manager's verbal go-ahead; checker review the same day; this template completed within 1 working day |

## Template

### 1. Header

| Field | Entry |
|---|---|
| CR ID and Jira key | [ID; key] |
| Title | [Tool: what changes] |
| Tool or system | [COMPANY: tool name] (Tool Inventory row [n]) |
| Technology | [Python, Excel VBA, Access, Power Apps, Power Automate, configuration] |
| Change type | [Standard, Normal, Emergency] |
| Requested by | [Name, team] |
| Maker / Checker / Approver | [Name] / [Name] / [Name] |
| Date raised | [Date] |
| Target date and window | [Date, time; why this window] |

### 2. Description

- **Before:** [what the tool does now]
- **After:** [what it will do]
- **Not changing:** [what stays the same, to limit the checker's review]

| Object changed | Location | Current version | New version |
|---|---|---|---|
| [Script, module, query, form, flow, setting] | [Path or environment] | [v n] | [v n+1] |

### 3. Reason

[The problem or benefit, in 2 to 3 sentences. Link the Jira bug or story, the requirement IDs and the pain point ID.]

### 4. Impact assessment

| Area | Affected? | Details, and who confirmed |
|---|---|---|
| Users | [Yes or No] | [Who uses the tool or its output; what they will notice] |
| Data | [ ] | [Fields, tables or files changed; is existing data converted?] |
| Downstream reports and tools | [ ] | [Every report, workbook, Power BI dataset or tool that reads the output] |
| Interfaces and schedules | [ ] | [Broker feeds, Oracle loads, Power Automate flows, scheduled jobs] |
| Compliance | [ ] | [Does it touch classification, value, origin or preference claim data that reaches a customs declaration?] |
| Financial | [ ] | [Standard cost, landed cost, PPV, margin, Finance reports] |
| Security and access | [ ] | [Credentials, connections, permissions, who can run it] |
| Documentation | [ ] | [Tool doc, SOP, OneNote, Anki cards to update] |
| e2open | [ ] | [Does it change a data map, an as-is document or the tool's e2open disposition?] |

### 5. Risk rating

- **Likelihood** that something goes wrong: 1 Unlikely, 2 Possible, 3 Likely.
- **Impact** if it does: 1 Minor (internal, easy to fix), 2 Moderate (wrong output for internal users, caught before use), 3 Major (wrong data reaches a broker, Finance, Oracle or a filing, or affects a cost update).

| Likelihood | Impact | Score (L x I) | Rating |
|---|---|---|---|
| [1-3] | [1-3] | [1-9] | [Low 1-2, Medium 3-4, High 6-9] |

| Rating | Required before implementation |
|---|---|
| Low | Maker's tests; checker reviews the change and the evidence; approver approves |
| Medium | All of Low, plus a regression run on a full real input set, users told in advance, and no implementation during a cost cycle or within [COMPANY: n] working days of a tariff effective date |
| High | All of Medium, plus data owner or Finance approval, a parallel run for one full cycle or a rollback rehearsal, a scheduled window, and the maker on standby for the first production run |

### 6. Test evidence

| Test ID | What is tested | Input data | Expected | Actual | Result |
|---|---|---|---|---|---|
| T1 | [The intended change] | [File or data set, date] | [Exact result] | [Exact result] | [Pass, Fail] |
| T2 | Regression: old vs new on the same input | [Same input] | Only the intended differences | [ ] | [ ] |
| T3 | [Error or boundary case] | [ ] | [ ] | [ ] | [ ] |

Attach output files, diffs and screenshots to the Jira issue.

### 7. Technology checklist: making the change safely

Python

- [ ] The code is in [COMPANY: code repository]; I work on a branch; commit messages include the Jira key.
- [ ] Dependencies are pinned (for example requirements.txt) and the same in test and production.
- [ ] No credentials, paths, rates or dates are hard-coded; settings live in a config file or table.
- [ ] I ran the old and new versions on a copy of real inputs and compared the outputs.
- [ ] The release is tagged; the previous tag is the rollback.

Excel VBA

- [ ] I saved a copy of the current production file, with its version in the file name, in [COMPANY: backup location] before starting.
- [ ] I work on a copy, not the production file.
- [ ] I exported the changed modules (.bas, .cls, .frm) before and after, so the checker can compare them as text.
- [ ] Every module has Option Explicit, and Debug > Compile VBAProject runs without errors.
- [ ] I checked the named ranges, sheet names, file paths and rate cells the code depends on.
- [ ] I tested with macros enabled the way users open the file ([COMPANY: trusted locations and macro policy]).

Access

- [ ] I backed up the front-end and back-end files before the change.
- [ ] If the database is split, I changed a copy of the front-end with its linked tables pointed at a test copy of the back-end; I re-link to production only at implementation.
- [ ] I recorded the SQL of every changed query, before and after.
- [ ] For a table design change, I checked every query, form and report that uses the table, and every Excel or Power BI file linked to it.

Power Apps

- [ ] I noted the current published version (canvas apps keep a version history you can restore from).
- [ ] I made the change in [COMPANY: development environment] or a copy of the app, not in the live app during working hours.
- [ ] I tested as a user with a normal role, not as the app owner, and checked data source connections and permissions.
- [ ] I published only after approval and noted the new version number.

Power Automate

- [ ] I exported the flow (or its solution), or saved a copy, before editing. That copy is the rollback.
- [ ] I checked the trigger, the connections (whose account the flow runs under) and any run-only users.
- [ ] I tested with test inputs and turned off any test copy afterwards so it cannot run twice.
- [ ] I check the run history after the first production run.

Configuration (AS400 trade system setting, Power BI refresh, e2open configuration, and similar)

- [ ] I saved screenshots or an export of the current values.
- [ ] I confirmed who is allowed to make the change; usually the BSA prepares and checks, and the system owner makes it.
- [ ] I tested in a test environment. If there is none, the CR says why and which extra checks replace the test.

### 8. Rollback plan

| Item | Entry |
|---|---|
| Rollback trigger | [The result that means "roll back", for example output row count differs from input, receiver rejects the file, errors in the log] |
| Who decides | [Name] |
| Steps | [1. ... 2. ... 3. ...] |
| Backup location, verified by and date | [Path; name; date] |
| Time to roll back | [Minutes] |
| Data clean-up | [Outputs already produced by the faulty version, who received them, and how they will be corrected or re-sent] |

### 9. Implementation steps

| Step | Action | Who | When | Done |
|---|---|---|---|---|
| 1 | [Confirm backup exists] | [ ] | [ ] | [ ] |
| 2 | [Deploy] | [ ] | [ ] | [ ] |
| 3 | [First run and checks] | [ ] | [ ] | [ ] |

### 10. Maker-checker approval

| Role | Name | What was reviewed | Decision | Date |
|---|---|---|---|---|
| Maker | [ ] | Built and tested; evidence attached | Submitted | [ ] |
| Checker | [ ] | [Diff of code or configuration, test evidence, impact rows, rollback plan] | [Approved, Returned with findings] | [ ] |
| Approver | [ ] | [Risk rating, timing, communication] | [Approved, Rejected] | [ ] |
| Data owner or Finance (High risk only) | [ ] | [ ] | [ ] | [ ] |

Rules: the maker is never the checker. The checker's findings and decision go on the Jira issue. No approval, no implementation.

### 11. Communication

| Audience | Message | When | Channel |
|---|---|---|---|
| [Tool users] | [What changes, when, what they need to do] | [Before and after] | [Email, Teams] |
| [Downstream receivers: broker, Finance] | [ ] | [ ] | [ ] |

> Before: "On [date, time], [tool] will change: [one-sentence change]. You need to [action, or "do nothing"]. Questions to [maker] by [date]."
>
> After: "[Tool] v[n] is live. First run on [date] checked OK: [the check]. Report anything unexpected to [maker] and quote [CR ID]."

### 12. Post-implementation check

- [ ] The first production run output matches the expected result; counts tie to the input.
- [ ] The log or run history shows no errors.
- [ ] Downstream receivers confirm (broker accepted the file; Finance load reconciled).
- [ ] Users confirm the change works for them.
- [ ] The tool doc (`docs/templates/knowledge/tool-doc.md`) shows the new version and a change-history line.
- [ ] The Tool Inventory row, SOP, OneNote pages and any affected Anki cards are updated.
- [ ] The CR is closed in Jira with evidence linked. If anything went wrong: rolled back or a bug logged.

## Filled example (illustrative)

This example is set after Hire A's day-60 review, when the Manager granted production change rights for this owned tool. Before that review, the same CR stops after testing on the test copy, and the Manager implements it.

| Field | Entry |
|---|---|
| CR ID and Jira key | [COMPANY: project key]-171-CR |
| Title | [COMPANY: tool closest to Research]: keep HTS numbers as 10-digit text in the broker export |
| Technology | Python |
| Change type | Normal, expedited (P1). Not Emergency: the Manager had already sent the broker a corrected list (the workaround), which stopped further wrong data, so there was time to test fully before the next scheduled run |
| Maker / Checker / Approver | Hire A (tool owner) / Manager / Manager; data owner approval: [COMPANY: trade compliance lead] |

- **Before:** the script reads the AS400 extract with default column types, so the HTS column becomes a number. HTS numbers starting with 0 (chapters 01 to 09) are written to the broker file with 9 digits.
- **After:** the HTS column is read as text (in pandas, dtype=str for that column). Each HTS number is checked for exactly 10 digits; any other value goes to an error file and a warning in the run log.
- **Not changing:** file layout, column order, file name, schedule.

| Area | Affected? | Details, and who confirmed |
|---|---|---|
| Interfaces and schedules | Yes | The US broker file for [COMPANY: broker]; layout unchanged; only the affected rows change |
| Compliance | Yes | The broker may have received 312 truncated numbers since [first bad run date]. Research lists every entry for those items from that date, with each entry's liquidation status. The Manager and [COMPANY: trade compliance lead] decide the correction route with the broker |
| Financial | No (unless entries used a wrong number) | Depends on the compliance check above |
| Documentation | Yes | Tool doc: input handling and error file; new Anki card on leading zeros |

Risk: Likelihood 2 x Impact 3 = 6, **High**. Required: regression on the full last production input; users and the broker told in advance (the broker email goes with the Senior's agreement and the Senior copied); approval from the classification data owner ([COMPANY: trade compliance lead]); a broker test file; rollback rehearsal; a scheduled window outside any cost cycle and not within [COMPANY: n] working days of a tariff effective date; maker on standby for the first run.

| Test ID | What is tested | Input data | Expected | Actual | Result |
|---|---|---|---|---|---|
| T1 | Leading zero kept | Last production input (13,750 US rows) | 312 rows now have 10 digits starting with 0 | 312 | Pass |
| T2 | Regression: old vs new | Same input | Only those 312 rows differ, and only in the HTS column | 312 rows, HTS only | Pass |
| T3 | Invalid lengths rejected | Test file with 9- and 11-digit values | Rows in the error file; warning in the log; rest of the file written | As expected | Pass |
| T4 | Broker accepts the file | Test file to [COMPANY: broker test mailbox], Senior copied | Accepted, no rejects | Accepted | Pass |

**Rollback:** trigger is a broker reject or an output row count that differs from the input minus the error rows. Restore the previous release tag (v1.4) and re-run; about 10 minutes. Rehearsed in test.

**Post-implementation check:** first production run had 13,750 rows in and out, 0 error rows; broker confirmed receipt; tool doc v1.5 published; CR closed.

## Quality checklist before you send

- [ ] Before, after and "not changing" are specific enough for the checker to spot an unintended change.
- [ ] Every impact row is answered, and each "No" has a reason.
- [ ] Compliance and financial impacts are assessed explicitly, including data already sent to brokers or Finance.
- [ ] The risk rating is calculated and every control the rating requires is done.
- [ ] The change was made and tested on a copy, never in production.
- [ ] Test evidence includes a regression comparison of old vs new output on the same input.
- [ ] No hard-coded credentials, paths, rates or dates were added.
- [ ] The backup exists and its location is written down; the rollback steps are specific and timed.
- [ ] The checker is not the maker, and the review and approval are recorded on Jira before implementation.
- [ ] Users and downstream receivers are told before and after.
- [ ] Post-implementation check done; tool doc, Tool Inventory and SOP updated; CR closed.
