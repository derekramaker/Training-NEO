# Project Closeout Template

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** close an epic or project properly: compare results with objectives, hand over deliverables and support, update the documentation, give every open item an owner, capture lessons learned, and get sign-off. Keep it to 1 to 3 pages.
- **Who uses it:** the BSA who led the epic writes it; the Manager reviews it; the business owner and checkers sign; whoever takes over a deliverable confirms the handover.
- **When:** within 5 working days after the last child issue is Done. For a tool or system change, after go-live and the first clean production cycle. Use it for every epic: tariff action responses, tool enhancements, transition work (exports and reporting backlog items), e2open workstreams. Module M4.

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. Copy the objectives and measures from the requirements (`docs/templates/bsa/02-requirements.md`) or the epic description. Measure the actual results with data, not impressions.
2. List every deliverable with its location and who supports it from now on.
3. Work through the documentation checklist and link each updated page.
4. Turn anything unfinished into a Jira issue with an owner and a date. No "TBD" owners.
5. Run a 30-minute lessons-learned session with the people involved (agenda below). Record Keep, Stop and Start, each with evidence and an action.
6. Send it for sign-off. Close the epic only after sign-off.

## Template

### 1. Header

| Field | Entry |
|---|---|
| Project or epic | [Name] |
| Jira key | [Key] |
| Dates | Start [date]; planned end [date]; actual end [date] |
| Lead (maker) | [Name] |
| Checkers | [Names] |
| Business owner | [COMPANY: role] |
| Related documents | [Intake, requirements, process map, data map, UAT plan, change requests] |

### 2. Summary

[3 to 5 sentences: what was delivered, against which objective, the key result, and what is still open.]

### 3. Objectives vs results

| Objective | Measure | Target | Actual | Met? | Notes |
|---|---|---|---|---|---|
| [O1] | [Metric] | [Target] | [Actual, with source] | [Yes, Partly, No] | [Why, if not met] |

### 4. Scope delivered

- **Delivered as planned:** [items]
- **Delivered with changes:** [item, what changed, who agreed]
- **Not delivered:** [item, why, and where it went: Jira key or "dropped, agreed by [name] on [date]"]

### 5. Delivery measures

| Measure | Planned | Actual | Comment |
|---|---|---|---|
| End date | [ ] | [ ] | [ ] |
| Effort (hours) | [Estimate] | [Actual, if tracked] | [ ] |
| Defects found in UAT | n/a | [n] | [ ] |
| Defects found after go-live or release | 0 | [n] | [ ] |
| Checker findings before release | n/a | [n] | [Types of finding] |

### 6. Deliverables and handover

| Deliverable | Location | New owner | Support arrangement | Accepted (name, date) |
|---|---|---|---|---|
| [Brief, model, tool version, report, SOP, data map] | [Link] | [Name or role] | [Who to call; how issues are logged] | [ ] |

### 7. Controls evidence

| Release | Maker | Checker | Evidence link | Date |
|---|---|---|---|---|
| [Brief v1.0, model v1.1, CR, cost input file] | [ ] | [ ] | [Jira comment or sign-off block] | [ ] |

### 8. Documentation updated

- [ ] Tool docs (`docs/templates/knowledge/tool-doc.md`): new version number and change-history line.
- [ ] Process SOPs (`docs/templates/knowledge/process-sop.md`): steps, controls and exceptions that changed.
- [ ] OneNote: pages updated, links checked, superseded pages marked "superseded by [page]".
- [ ] Anki: company-specific cards added or corrected (`docs/templates/knowledge/anki-card-writing-guide.md`); list them.
- [ ] Trackers workbook: Tool Inventory row and glossary terms updated.
- [ ] Process maps: the to-be is now the as-is; the old version is archived.
- [ ] Data mapping specs and value maps reflect what was built.
- [ ] Jira: every child issue is closed or moved, with components and labels correct.
- [ ] e2open: anything the project team needs (data map changes, tool disposition notes) has been sent to [COMPANY: e2open project lead].
- [ ] Evidence is retained per [COMPANY: records retention policy].

### 9. Open items and owners

| ID | Item | Owner | Due | Jira key | Risk if not done |
|---|---|---|---|---|---|
| OI-1 | [What is left] | [Name] | [Date] | [Key] | [Consequence] |

### 10. Lessons learned (Keep, Stop, Start)

| Type | Lesson | Evidence | Action | Owner |
|---|---|---|---|---|
| Keep | [What worked and should be repeated] | [Fact or number] | [How to make it standard] | [Name] |
| Stop | [What caused rework, delay or risk] | [ ] | [ ] | [ ] |
| Start | [What to try next time] | [ ] | [ ] | [ ] |

Session agenda (30 minutes):

1. Timeline of facts (5 minutes): what happened, when, from the Jira history.
2. Keep (10 minutes): what worked, and why.
3. Stop and Start (10 minutes): what didn't work, and what to try instead.
4. Actions (5 minutes): pick no more than 3, each with an owner and a date.

Rules: talk about the process, not the person. Back each lesson with a fact. Make each action specific. Actions land in an SOP change, a Jira issue, an Anki card, or a template change request to the Manager (the Manager owns these templates).

### 11. Sign-off

| Role | Name | Decision | Date | Comments |
|---|---|---|---|---|
| Business owner | [ ] | [Accepted, Accepted with open items, Not accepted] | [ ] | [ ] |
| New owner of the deliverables | [ ] | [Handover accepted] | [ ] | [ ] |
| Checker | [ ] | [Controls evidence complete] | [ ] | [ ] |
| Manager | [ ] | [Approved to close] | [ ] | [ ] |

## Filled example (short)

Closeout for the hypothetical "Tariff action: Country X steel fasteners" epic (see the example in `docs/templates/bsa/01-intake-request.md`). Lead: Hire A, with Hire B. Checkers: Senior (brief), Manager (model). Business owner: [COMPANY: Pricing lead].

**Summary.** The checked brief and the $ impact were both delivered before the pricing meeting. Of the 140 candidate items, 138 were confirmed in scope; the Senior's review moved 2 borderline items out of heading 7318, and their classification was corrected through change requests before the effective date. The $ summary arrived 40 minutes late because the volume forecast arrived 4 hours late (Wed 16:00 instead of 12:00). Three items remain open.

| Objective | Measure | Target | Actual | Met? | Notes |
|---|---|---|---|---|---|
| O1 Checked brief released early | Release time | Thu 12:00 | Thu 11:30 | Yes | 1 checker finding (stacking wording), closed |
| O2 $ impact checked and sent before pricing | Send time | Fri 08:00 | Fri 08:40 | Partly | Forecast arrived Wed 16:00 instead of 12:00 |
| O3 No material errors after release | Errors found in 30-day look-back | 0 | 0 | Yes | Look-back done by Hire A, checked by the Senior |
| O4 Classification right before the effective date | Borderline items resolved | 6 of 6 | 6 of 6 | Yes | 2 changed via change requests |

| Deliverable | Location | New owner | Support arrangement | Accepted (name, date) |
|---|---|---|---|---|
| Tariff-Impact Brief v1.0 | [COMPANY: briefs folder] | Hire A | Updated if CBP issues further guidance | [COMPANY: Pricing lead], [date] |
| Tariff-Impact Model v1.1 | [COMPANY: model folder] | Hire B | Feeds the next standard cost cycle | Manager, [date] |
| Rate-table rows with effective dates | [COMPANY: name of std-cost tool] | Hire B | Normal tool support | Manager, [date] |

| ID | Item | Owner | Due | Jira key | Risk if not done |
|---|---|---|---|---|---|
| OI-1 | Watch CBP CSMS for guidance on the in-transit terms | Hire A | Effective date + 10 working days | [key] | Wrong duty basis on in-transit goods |
| OI-2 | Include the new duty in the next standard cost update (maker-checker) | Hire B | [COMPANY: next cycle date] | [key] | Standard cost understated; PPV inflated |
| OI-3 | List every entry for the 2 reclassified items since their 7318 classification was set, with each entry's liquidation status; the Manager and [COMPANY: trade compliance lead] decide the correction route with the broker | Hire A, with the Senior | [date] | [key] | Unflagged errors on past entries; correction options narrow as entries liquidate |

| Type | Lesson | Evidence | Action | Owner |
|---|---|---|---|---|
| Keep | Split WHAT and $ into linked stories on day 1 | Handoff took 15 minutes; no clarification rounds | Already in the intake routing rule; keep it | Both hires |
| Stop | Matching items in Excel | Leading zeros lost; 3 items missed in the first pass | Saved SQL matching query in [COMPANY: code repository]; added to the Research SOP | Hire A |
| Start | Agree a fallback volume basis at intake (for example the last 12 months' import quantity) in case the forecast is late | Forecast arrived 4 hours late; $ summary 40 minutes late | Add the fallback to the Standard Cost SOP intake step, and name it in the covering note when used; ask the Manager whether to add it to the intake template | Hire B |

Documentation updated: Research SOP draft (in-transit step and SQL matching); 4 new Anki cards (Chapter 99 stacking basics, in-transit terms, reading an annex, HTS leading zeros); Tool Inventory unchanged.

## Quality checklist before you send

- [ ] Every objective has a measured actual result with its source, and an honest Met, Partly or No.
- [ ] Anything not delivered says why, and where it went.
- [ ] Every deliverable has a location, a new owner, a support arrangement and an acceptance.
- [ ] Every release has maker-checker evidence linked.
- [ ] The documentation checklist is complete, with links; Anki cards are listed.
- [ ] Every open item has one owner, a date, a Jira key and the risk if not done.
- [ ] Lessons have evidence and no more than 3 actions, each with an owner; no blame.
- [ ] Anything the e2open project needs has been sent.
- [ ] Sign-off is recorded before the epic is closed.
