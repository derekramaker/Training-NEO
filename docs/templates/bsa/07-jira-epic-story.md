# Jira Epic, Story and Bug Templates

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** write Jira issues that anyone can pick up, test and close without a meeting. Covers epic, story and bug templates, acceptance criteria in Given/When/Then, the definitions of ready and done, naming conventions, and worked examples.
- **Who uses it:** both hires for every issue they create, starting with their onboarding epic; the Manager, who checks the definition of ready in the Monday confirm and the definition of done before closing; the Senior as checker on their items.
- **When:** from Wed 10/21 (onboarding epic and stories), taught in the Wed 10/28 session on intake and stories (M4), then for every issue.

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. Route the request first (`docs/templates/bsa/01-intake-request.md`). The route tells you the issue type.
2. Name the issue using the title convention below.
3. Copy the matching text block (epic, story or bug) into the Jira description and fill every line. Write "n/a" rather than deleting a line.
4. Write acceptance criteria in Given/When/Then, with real data.
5. Check the definition of ready before the issue moves to In progress. Check the definition of done before it moves to Done.

### Issue types

| Type | Use when | Size | Example |
|---|---|---|---|
| Epic | An outcome that needs more than one deliverable or track, or more than 5 working days | Weeks | Respond to a new tariff action (WHAT and $) |
| Story | One deliverable, one maker, one checker | 5 working days or less | Tariff-Impact Brief for one action |
| Bug | A tool, report, feed or data set does not do what its documentation or requirement says | Usually small; severity drives urgency | Broker export drops leading zeros |
| Sub-task | A step inside a story that someone else does | Hours | Senior advises on borderline items |

[COMPANY: confirm which issue types and statuses the Jira project uses.]

### Conventions

| Field | Convention |
|---|---|
| Title (story) | [Track]: [verb] [object] [scope]. Example: "Research: scope US duty on heading 7318 from Country X" |
| Title (bug) | [Tool or report]: [what is wrong] when [condition] |
| Project | [COMPANY: Jira project key] |
| Component | Exactly one, from [COMPANY: component list]. Suggested: Research, Standard Cost, Exports, Reporting, Drawback, Custom Tools, e2open, Onboarding |
| Labels | [COMPANY: label convention]. Suggested: country-us, country-ca, country-mx; tariff-action-[short id]; tool-[short tool name]; e2open-[object]; onboarding-hire-a, onboarding-hire-b. Lowercase with hyphens (Jira labels cannot contain spaces) |
| Priority | P1, P2, P3 as defined in `docs/05-time-management.md`, mapped to [COMPANY: Jira priority values] |
| Assignee and checker | Assignee is the maker. The checker goes in [COMPANY: checker field] or on the "Maker / Checker" line |
| Due date | The hard date. The reason goes in the description |
| Links | "Blocks" from the Research story to the Standard Cost story; "relates to" for the change request; parent epic set |
| Status | [COMPANY: workflow]. Suggested: Backlog, Ready, In progress, In review (checker), Done. Flag blocked issues with a comment saying who or what is blocking |

## Templates (paste into the Jira description)

### Epic

```text
EPIC: [Outcome in plain words]
Goal: [What will be true when this is done]
Why now: [Driver and date: effective date, cost cycle, e2open milestone]
Value: [Decision supported; $ or risk addressed]
Scope in: [Countries, items or HTS, systems, period]
Scope out: [ ]
Success measures: [How we will know]
Stakeholders: [Requester, business owner, Finance, broker contact]
Child issues: [Created as linked issues]
Documents: [Intake, requirements, process map, data map, UAT plan, change requests]
Risks and dependencies: [ ]
Done when: [All child issues done and the closeout written (08-project-closeout)]
```

### Story

```text
STORY: [Track]: [verb] [object] [scope]
As a [role], I want [deliverable or capability], so that [decision or benefit].
Context: [2-3 sentences; links to intake, brief, earlier work]
Scope in: [ ]
Scope out: [ ]
Inputs and sources: [Systems, files, notices]
Acceptance criteria:
AC1 Given [context], when [action], then [observable result].
AC2 Given [ ], when [ ], then [ ].
Maker / Checker: [Name] / [Name]
Due: [Date, time] because [reason]
Deliverable location: [Link]
Ready checked by: [Name, date]
```

### Bug

```text
BUG: [Tool or report]: [what is wrong] when [condition]
Version and environment: [Tool version, file, run date]
Steps to reproduce: 1. [ ] 2. [ ] 3. [ ]
Expected: [Per tool doc section or requirement ID]
Actual: [What happens, with values]
Impact: [Records affected; who received the bad output: broker, Finance, Oracle, report users]
Severity: [Critical, High, Medium, Low, as defined in 05-uat-test-plan]
Workaround: [ ]
Evidence: [Files, screenshots]
Acceptance criteria: AC1 Given [ ], when [ ], then [ ].
Root cause (at fix): [ ]
Fix: [Change request ID]
```

## Writing acceptance criteria in Given/When/Then

- **Given** is the starting state and data. **When** is the action or event. **Then** is a result someone can check: a value, the content of a file, a message, a recorded review.
- One behavior per criterion. Use concrete data: an item, an HTS number, a date, a value.
- Add at least one edge or negative case whenever dates, thresholds or validations are involved.
- GWT works for analysis and research deliverables too: "Given the notice and our item list, when the brief is complete, then it lists every in-scope HTS number with a cited source."
- Never use: "works correctly", "as expected", "user-friendly", "fast", "all relevant items". Say what correct means.

## Definition of ready (before In progress)

- [ ] The issue type is right and the title follows the convention.
- [ ] The story says who benefits and which decision it supports.
- [ ] Scope in and out are written: countries, items or HTS, period.
- [ ] Inputs and sources are named and accessible, or access is requested.
- [ ] Acceptance criteria are in Given/When/Then, testable, with an edge case where dates or validation are involved.
- [ ] Maker and checker are named, are different people, and the checker has agreed a review slot.
- [ ] The due date has a reason; the priority is confirmed (by the Manager in days 1 to 60).
- [ ] Boundary rule: WHAT (Research) and $ (Standard Cost) are separate, linked stories.
- [ ] Dependencies are linked; a change request is open if a tool, configuration or data will change.
- [ ] Sized at 5 working days or less; otherwise split.

## Definition of done (before Done)

- [ ] Every acceptance criterion is met, with evidence linked.
- [ ] The checker's review is on the issue: name, date, version reviewed, findings, all findings closed.
- [ ] The deliverable is stored in [COMPANY: team location] and linked, with its final version number.
- [ ] The requester has been told, with the link.
- [ ] For tool changes: the change request is closed after its post-implementation check.
- [ ] Documentation is updated (tool doc, SOP, OneNote, company-specific Anki cards), or "none needed" is stated.
- [ ] Follow-ups are new linked issues, not notes in comments.

## Example 1: tariff research story

The action is hypothetical.

```text
STORY: Research: Tariff-Impact Brief for US additional duty on heading 7318 from Country X
Component: Research. Labels: country-us, tariff-action-cx7318. Priority: P1.
As the Standard Cost BSA and the pricing team, I want a checked brief stating which of
our items the action covers, at what rate and from when, so that cost and margin impact
can be modeled before Friday's pricing meeting.
Context: Federal Register notice [citation], published [date]; CBP CSMS message [number].
Intake [key]. Earlier action on the same heading: [key].
Scope in: US imports; HTS heading 7318; origin Country X; active items.
Scope out: Canada and Mexico; $ impact (see [key], Standard Cost).
Inputs and sources: the notice and annex; HTSUS Chapter 99; AS400 classification extract
dated [date]; CSMS guidance.
Acceptance criteria:
AC1 Given the notice annex, when the brief is complete, then it lists every in-scope HTS
    subheading exactly as the annex states it, each with a cited source line.
AC2 Given the item extract dated [date], when items are matched on HTS (as text) and origin
    Country X, then every match is on the item list and each borderline item has a
    one-line reasoning note.
AC3 Given the notice's timing language, when the brief states timing, then it quotes the
    effective date and time, the basis (entered for consumption or withdrawn from
    warehouse for consumption) and any in-transit terms.
AC4 Given other duties already apply to these items, when the brief states stacking, then
    for each in-scope item it says whether the new duty adds to them, replaces them or
    does not apply, with the source.
AC5 Given the boundary rule, when the brief is reviewed, then it contains no cost or
    margin figures.
AC6 Given the checker review, when the story moves to Done, then the Senior's comment
    records name, date, brief version and findings, all closed.
Maker / Checker: Hire A / Senior
Due: Thu [date] 12:00 because the duty applies from 12:01 a.m. ET [date] and pricing meets Fri.
Deliverable location: [COMPANY: briefs folder] and the WHAT tab of the Tariff-Impact Model.
Links: blocks [key] (Standard Cost).
```

## Example 2: standard cost story

```text
STORY: Standard Cost: landed-cost and margin impact of the Country X fastener duty
Component: Standard Cost. Labels: country-us, tariff-action-cx7318. Priority: P1.
As the pricing team, I want the per-unit landed-cost and margin change for each in-scope
item, so that we can decide price changes at Friday's meeting.
Context: brief v1.0 [link]; Tariff-Impact Model [link]; volume forecast from
[COMPANY: Purchasing] due Wed 12:00.
Scope in: items on the brief v1.0 item list; forecast volume for the next two quarters;
current standard cost from [COMPANY: Oracle cost type].
Scope out: changing Oracle standard costs (separate story in the next cost cycle);
customer price recommendations.
Acceptance criteria:
AC1 Given the brief v1.0 item list, when the model's $ tab is run, then every listed item
    appears exactly once and no other item appears.
AC2 Given entered value per unit from [COMPANY: source], when duty is calculated, then the
    additional duty for 3 sample items matches a hand calculation to $0.01.
AC3 Given the forecast, when the summary is produced, then it shows per item the current
    and new landed cost, change per unit, change in margin %, and $ impact per quarter,
    with a total.
AC4 Given an item has no forecast volume, when the summary is produced, then it is listed
    under "no volume" and left out of the totals, not silently dropped.
AC5 Given the boundary rule, when the model is reviewed, then scope, rates and dates come
    only from brief v1.0; any question goes to Research as a comment on [key].
AC6 Given the checker review, when the story moves to Done, then the Manager's comment
    records name, date, model version and findings, all closed, before the summary is sent.
Maker / Checker: Hire B / Manager
Due: Fri [date] 08:00 because pricing meets at 10:00.
Links: is blocked by [key] (Research).
```

## Example 3: custom tool fix (logged as a bug)

A tool fix is a bug when the tool fails its documented behavior. Use a story when the fix adds new behavior.

```text
BUG: [COMPANY: tool closest to Research]: HTS numbers in chapters 01-09 lose their
leading zero in the US broker export
Component: Custom Tools. Labels: tool-[short name], country-us. Priority: P1.
Version and environment: v1.4, production run of [date].
Steps to reproduce: 1. Run the export on the production input of [date]. 2. Open the
output in a text editor, not Excel. 3. Find any item classified in chapters 01-09.
Expected: 10-digit HTS, identical to the AS400 classification master (tool doc, section [n]).
Actual: 9 digits. 312 rows affected in the last run.
Impact: US broker file for [COMPANY: broker] since [first bad run date]; possible wrong or
rejected lines on entries for these items.
Severity: Critical (wrong compliance data reaching a broker).
Workaround: Manager sent the broker a corrected list on [date].
Acceptance criteria:
AC1 Given an input HTS of 10 digits starting with 0, when the export runs, then the output
    has the same 10 digits.
AC2 Given an input HTS of any other length, when the export runs, then the row goes to the
    error file, the log names the item, and the rest of the file is written.
AC3 Given the last production input, when old and new versions run, then only the 312
    affected rows differ, and only in the HTS column.
AC4 Given the fix is live, when the post-implementation check is done, then the broker
    confirms receipt with no rejects.
Fix: [key]-171-CR. Maker / Checker: Hire A / Manager.
Follow-up: Research story [key] to check entries for the affected items over the last 90 days.
```

## A bad example, rewritten

Bad:

```text
Title: Update tariff stuff
Description: New tariffs came out, need to update the tool and let everyone know ASAP.
See email.
```

What is wrong with it:

- The title says nothing: which action, which country, which tool?
- It mixes three jobs (the research, a tool change and a communication) owned by different people.
- "ASAP" is not a date, and the reason for urgency is missing.
- "See email" means the context is not in the record.
- No acceptance criteria, no maker, no checker, no change request for the tool change.

Rewritten as an epic with three linked issues: (1) the Research brief (Example 1), (2) the rate-table update below, with a change request, and (3) the business communication, sent by the Manager after both checks. Issue 2 in full:

```text
STORY: Custom Tools: load the Country X fastener duty from brief v1.0 into the
[COMPANY: name of std-cost tool] rate table
Component: Custom Tools. Labels: tool-[short name], tariff-action-cx7318. Priority: P2.
As the Standard Cost BSA, I want the new rate and its effective date in the rate table,
so that the next cost run uses the right duty for the right period.
Scope in: the HTS numbers and rates in brief v1.0, US only. Scope out: other actions.
Acceptance criteria:
AC1 Given brief v1.0, when the rates are loaded, then each in-scope HTS number has one new
    row with the brief's rate and effective-from date.
AC2 Given an existing open-ended row for the same HTS number and rate type, when the new
    row is loaded, then the old row is end-dated the day before the new effective date.
AC3 Given the load is complete, when the checker compares the rate table with the brief,
    then the row count and every rate and date match, and the review is recorded here.
Maker / Checker: Hire B / Manager. Change request: [key]-CR (a Standard change if rate
loads from a checked brief are on the Manager's standard change list).
Due: [date] because the cost run for [period] starts [date].
Links: is blocked by [key] (Research brief); relates to [key]-CR.
```

## Filled example: onboarding epic

```text
EPIC: Onboarding: Hire A, Research track (2026-10-19 to 2027-01-15)
Goal: Hire A meets the day-30, day-60 and day-90 criteria in docs/01-30-60-90-plan.md.
Why now: start date Mon 2026-10-19; day-90 review Fri 2027-01-15.
Child issues (one story per graded deliverable): Tool Inventory rows (W2, complete W4);
small real analysis (W4); SOP draft from a shadowed process (W5); Tariff-Impact Brief
for a real recent action (W7); tool doc for [COMPANY: tool closest to Research] (W9);
e2open as-is document (W13); e2open data map (W13).
Done when: the day-90 scorecard is complete and the days 91-180 plan is approved.
```

## Quality checklist before you save the issue

- [ ] The issue type matches the route, and the title follows the convention.
- [ ] One component and the agreed labels are set; the priority is confirmed.
- [ ] The description uses the right template with every line filled or marked n/a.
- [ ] Acceptance criteria are Given/When/Then with real data, including an edge case.
- [ ] Maker and checker are named and different; the checker's review is an acceptance criterion.
- [ ] The due date has a reason.
- [ ] WHAT and $ are split into linked stories; tool or data changes link to a change request.
- [ ] The context is in the issue, not "see email".
- [ ] The definition of ready is met before work starts.
