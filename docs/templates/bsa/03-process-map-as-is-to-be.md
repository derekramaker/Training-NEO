# Process Map Template: As-Is and To-Be

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** document how a process really works today (as-is), how it should work (to-be), and the gaps between them, including every control (maker-checker) and pain point. The step table is the source of truth; the swimlane drawing is made from it.
- **Who uses it:** both hires to map processes they learn, to draft SOPs (`docs/templates/knowledge/process-sop.md`) and to produce the e2open as-is document for their own process (day-90 criteria A90-2 and B90-2). The Manager reviews it; process owners validate it.
- **When:** first use W2 (redraw the trade data flow, Tue 10/27). Process mapping is taught in M4 in W4. The e2open as-is document is drafted in W10 and W11 and finished by W13 (M10).

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. Fill the header and the SIPOC first (about 20 minutes). They fix where the process starts and ends, so the interview stays on track.
2. Interview the person who does the work, and separately the person who checks it (45 to 60 minutes each). Use Part 3. Walk through the last real instance, not the theory.
3. Write the as-is step table within 24 hours of the interview, while your notes still make sense.
4. Play it back to the interviewee (15 minutes) and correct it. Only then write their name under "Validated by".
5. Give each control an ID (C1, C2) and each pain point an ID (P1, P2) as you go. Detail them in the registers in Parts 5 and 6.
6. Draw the swimlane from the validated table (Part 8). Table first, picture second.
7. Write the to-be only after the as-is is validated. Every to-be change must link to a pain point, a requirement or a control gap.
8. Record what really happens, not what an SOP says should happen. A difference between the two is a finding: note it in the pain point log.

## Part 1: Process header

| Field | Entry |
|---|---|
| Process name | [Verb + object, for example "Respond to a new tariff action"] |
| Version and state | [As-is v0.1, as-is v1.0 validated, to-be v0.1] |
| Process owner | [COMPANY: role] |
| Trigger (start) | [The event that starts it] |
| End point | [The last output and who receives it] |
| Frequency and volume | [How often; how many; how long each] |
| Countries | [US, CA, MX] |
| Systems | [AS400 trade system, Oracle, SQL Server, warehouse, Power BI, custom tools, broker portals, email] |
| Related documents | [SOP, tool docs, requirements, data mapping spec] |
| Mapped by and date | [Name, date] |
| Validated by and date | [Name of the person who does the work, date of playback] |

## Part 2: SIPOC

Fill the Process column first (5 to 7 high-level steps), then Outputs, Customers, Inputs, and Suppliers. One item per row; the rows do not need to line up across columns.

| Suppliers | Inputs | Process (high-level steps) | Outputs | Customers |
|---|---|---|---|---|
| [Who provides the input] | [What comes in] | 1. [Step] | [What goes out] | [Who receives it] |
| [ ] | [ ] | 2. [Step] | [ ] | [ ] |
| [ ] | [ ] | 3. [Step] | [ ] | [ ] |
| [ ] | [ ] | 4. [Step] | [ ] | [ ] |
| [ ] | [ ] | 5. [Step] | [ ] | [ ] |

## Part 3: Interviewing someone to map their process

### Before the interview

- Book 45 to 60 minutes. Ask them to bring the last real example: the email, the file, the screen, the output.
- Read any SOP, tool doc or Jira history first. Bring your SIPOC draft.
- Plan two interviews per process: the doer and the checker. You see the control from both sides.

### Opening (2 minutes)

"I'm mapping how this works today so we can document it and prepare for e2open. This is not an audit. I'll write it up and play it back to you for corrections."

### Questions to ask

| Topic | Questions |
|---|---|
| Trigger and boundaries | What starts this? How do you hear about it? How often does it happen? What is the last thing you do, and who gets the result? |
| Walk-through | Take me through the last time you did this, step by step, and show me the screens and files. What did you do next? Where did that number come from? |
| Decisions and exceptions | Where do you make a judgement call, and what do you look at? When does it not go this way? What was the strangest case in the last 3 months? What do you do when data is missing? |
| Systems and data | Which system or file do you use at each step? What do you copy and paste between systems? What do you key by hand? Which source do you trust when two disagree? Where do you save the result? |
| Controls | Who checks your work before it goes out? What exactly do they compare? Where is the evidence that they checked? What would catch your mistake? What happens when the checker is away? |
| Handoffs and timing | Who do you wait for, and for how long? What do you hand over, in what format? Which dates drive this (tariff effective date, broker cut-off, Finance cost cycle)? |
| Pain points and numbers | What takes longest? What goes wrong most often? What do you redo? How many per month, and how long each? If you could change one thing, what would it be? |
| Knowledge risk | Is there anything only you know how to do? Is there a personal spreadsheet or macro this depends on? |

### Closing (5 minutes)

- "Who else should I talk to?"
- "Can I have a sanitized copy of the file or screenshots?"
- "Can we do a 15-minute playback on [date]?"

### Interview habits that work

- Ask "show me" rather than "tell me". People skip steps they do on autopilot.
- Use their words for step names; translate to standard terms in a note, not in the step.
- Do not suggest solutions during an as-is interview. Write ideas in your own notes for the to-be.
- Ask for numbers: volumes, minutes, error counts. "Often" is not evidence.
- Treat workarounds (personal spreadsheets, macros, email folders) as part of the real process. Map them.
- Take notes; do not record audio or video without the person's agreement and [COMPANY: recording policy].

## Part 4: As-is step table

Writing rules:

- Number the steps 1, 2, 3. Write a decision as "D1: [question]? Yes: go to step [n]. No: go to step [n]."
- Start each action with a verb and name the input when it isn't the previous step's output.
- One role per step. If two roles do something together, split it into two steps.
- System: name the system or file, or write "manual" or "email".
- Output: a noun (a file, a list, a decision, an email).
- Last column: "C1" for a control, "P1" for a pain point, with a few words. Full detail goes in Parts 5 and 6.

| Step | Lane/Role | Action | System | Output | Pain point / Control |
|---|---|---|---|---|---|
| 1 | [Role] | [Verb + object] | [System or file] | [Output] | [C or P ID and short note] |
| 2 | [ ] | [ ] | [ ] | [ ] | [ ] |
| D1 | [ ] | [Question]? Yes: step [n]. No: step [n]. | [ ] | [Decision] | [ ] |

## Part 5: Controls register (how to capture maker-checker)

| Control ID | Step | What is checked, and how | Maker / Checker | Evidence | Status |
|---|---|---|---|---|---|
| C1 | [Step] | [What is compared with what] | [Maker role] / [Checker role] | [Where the proof is] | [Designed, Performed, Gap] |

How to describe a control well:

- Say exactly what is compared: "The checker compares each HTS number in the brief with the notice annex, line by line". Not "reviewed".
- Say when it happens. A maker-checker control happens before release, not after.
- Say what the evidence is: a Jira comment with the checker's name, date, version reviewed and findings, or the template's sign-off block.
- Say what happens if the check fails: returned to the maker, fixed, and checked again.
- Mark the status: **Designed** (written down), **Performed** (evidence exists for recent instances), or **Gap** (should exist but doesn't). Ask to see the evidence for the last two instances before you mark a control Performed.
- A person checking their own work is not a control. If the checker is away, the release waits or the Manager names another checker.
- Automated checks count too (for example, a tool that rejects a 9-digit US HTS number). Note them as automated.

## Part 6: Pain point log

| Pain ID | Step | Pain point | Evidence (frequency, time, errors) | Root cause | Idea or requirement |
|---|---|---|---|---|---|
| P1 | [Step] | [What goes wrong or is slow] | [Numbers] | [Why it happens] | [Idea, or FR ID in the requirements document] |

Common types to look for: rework, waiting, re-keying between systems, missing or untrusted data, unclear ownership, missing control, knowledge held by one person, a personal workaround tool.

## Part 7: To-be step table and gap summary

Use the same columns as the as-is. In the last column, show the control that remains or is added, and the pain point the change resolves.

| Step | Lane/Role | Action | System | Output | Pain point / Control |
|---|---|---|---|---|---|
| 1 | [ ] | [ ] | [ ] | [ ] | [Resolves P1; keeps C1] |

| Gap ID | As-is step | To-be step | Change type | Pain or requirement ID | e2open fit |
|---|---|---|---|---|---|
| G1 | [n] | [n] | [Process, system, data, role, control] | [P1, FR-03] | [Standard, configuration, gap, unknown] |

## Part 8: Drawing the swimlane

### Rules for any tool

- One lane per role, not per person. Order lanes by when they first appear. Put outside parties (broker, Finance, government source) in the top or bottom lane.
- Flow left to right. Number each shape to match the step table.
- Shapes: rounded rectangle for start and end; rectangle for a step; diamond for a decision, with "Yes" and "No" on the arrows; document shape for a file, report or email; cylinder for a system or database.
- Mark controls with a small labelled box ("C1") in one color and pain points ("P1") in another. Add a legend.
- Keep to 15 to 20 shapes per page. Split a long process into sub-processes joined by labelled off-page connectors.
- Write the system under each step, or add a "Systems" lane at the bottom.
- Put the title, "as-is" or "to-be", version and date on every page.

### Visio

1. File > New > Cross-Functional Flowchart. Choose horizontal lanes.
2. Name each lane with a role. Add a lane by dragging the Swimlane shape onto the diagram.
3. Optional: add Separators for phases (for example Detect, Scope, Check, Release).
4. Connect shapes with the Connector tool so the lines stay attached when you move shapes.
5. Export: File > Export (PNG) or Save As (PDF). Insert the image into the OneNote page. Keep the .vsdx file in [COMPANY: SharePoint folder for process maps].
6. If Visio is not licensed ([COMPANY: confirm Visio license]), use PowerPoint.

### PowerPoint

1. Use a widescreen slide. Insert a table with one row per lane and two columns; type the role names in the narrow first column. Remove the fill so it acts as a background grid.
2. Draw steps with Insert > Shapes on top of the table. Use Elbow Arrow connectors and attach them to the shapes' connection points.
3. Use Arrange > Align and Distribute to keep spacing even. Group everything when done.
4. Avoid SmartArt: it does not handle lanes or decisions well.
5. Save as PDF or export the slide as PNG for OneNote; keep the .pptx with the other process maps.

### Whiteboard (fastest for a live session)

1. Draw lanes with tape or a marker. Use one sticky-note color per element: steps, decisions, controls, pain points, systems.
2. Walk the flow with the person who does the work, moving notes until they agree.
3. Photograph it. Transcribe it into the step table within 24 hours, then redraw it in Visio or PowerPoint.

## Filled example (illustrative, not validated)

Research process: respond to a new US tariff action, as-is. This shows the method; the real as-is must come from interviews.

### Header (selected fields)

| Field | Entry |
|---|---|
| Process name | Respond to a new tariff action (Research) |
| Trigger (start) | A tariff action is announced or published |
| End point | Business communication sent; $ handoff to Standard Cost complete |
| Frequency and volume | [COMPANY: actions per month]; 2 to 4 working days per action |
| Systems | Federal Register, CBP CSMS, HTSUS; AS400 trade system (inquiry); SQL Server and warehouse; shared Tariff-Impact Model (Excel); Jira; email |

### SIPOC

| Suppliers | Inputs | Process (high-level steps) | Outputs | Customers |
|---|---|---|---|---|
| Federal Register (agency notices) | Notice text and annexes | 1. Detect the action | Tariff-Impact Brief | Standard Cost (Hire B) |
| CBP (CSMS messages) | CBP filing guidance | 2. Log and triage | In-scope item list | Purchasing and Pricing |
| USITC (HTSUS) | HTSUS Chapter 99 provisions | 3. Read and scope | WHAT inputs in the model | Finance |
| AS400 trade system | Item classification master | 4. Match our items | Jira trail with checker sign-off | Brokers (if data changes) |
| Data warehouse | 12 months of import history | 5. Write the brief | | Manager |
| | | 6. Check (maker-checker) | | |
| | | 7. Hand off and communicate | | |

### As-is steps

| Step | Lane/Role | Action | System | Output | Pain point / Control |
|---|---|---|---|---|---|
| 1 | Research BSA | Find the notice in the daily source check, or from a forwarded email | Federal Register, CSMS, email | Notice link | P1: no single watch list; some actions found days late |
| 2 | Research BSA | Log in Jira, score, and tell the Manager within 30 minutes | Jira | P1 issue | C1: Manager confirms priority |
| 3 | Research BSA | Read the notice and annexes; list HTS numbers, countries, rate, effective date, exclusions, in-transit terms | Federal Register, HTSUS | WHAT notes | P2: annex HTS lists are PDFs, re-typed by hand |
| 4 | Research BSA | Pull active items whose HTS number and origin match | AS400 extract, Excel | Candidate item list | P3: 8-digit annex vs 10-digit item HTS matched in Excel; leading zeros lost |
| D1 | Research BSA | Any item whose description doesn't clearly fit the annex? Yes: step 5. No: step 6. | Item specs | Borderline list | |
| 5 | Senior | Advise on borderline items | Teams | Classification notes | |
| 6 | Research BSA | Write the brief; fill the WHAT tab of the model | Word, Excel model | Brief v0.x | |
| 7 | Senior (checker) | Check the brief against the sources, line by line; record findings | Jira | Brief v1.0 | C2: maker-checker before release |
| 8 | Research BSA | Hand off to Standard Cost | Email attachment | Handoff | P4: model emailed; versions diverge |
| 9 | Manager | Approve and send the business communication | Email | Communication | C3: Manager approves release |

### Controls register

| Control ID | Step | What is checked, and how | Maker / Checker | Evidence | Status |
|---|---|---|---|---|---|
| C1 | 2 | Priority and due date against the effective date | Research BSA / Manager | Jira comment | Performed |
| C2 | 7 | Each HTS number, rate, date and exclusion in the brief traced to a cited source | Research BSA / Senior | Jira comment: name, date, version, findings | Performed |
| C3 | 9 | Brief and $ summary are both checked before the communication goes out | Research and Standard Cost BSAs / Manager | Sent email filed on the Jira epic | Designed (no evidence for last 2 actions) |

### Pain point log

| Pain ID | Step | Pain point | Evidence (frequency, time, errors) | Root cause | Idea or requirement |
|---|---|---|---|---|---|
| P3 | 4 | HTS matching loses leading zeros for chapters 01 to 09 | 2 of the last 5 actions had missed items | HTS stored or opened as a number | Match on text in SQL; keep HTS as text |
| P4 | 8 | Two versions of the model in circulation | 1 rework round per action | Email attachments | Link one model file on the Jira story |

### Gap summary (to-be for e2open)

| Gap ID | As-is step | To-be step | Change type | Pain or requirement ID | e2open fit |
|---|---|---|---|---|---|
| G1 | 3 | 3 | System | P2 | Unknown: depends on whether the e2open scope includes trade content ([COMPANY: confirm]) |
| G2 | 4 | 4 | Data | P3 | Configuration: classification held as text per country in e2open |

## Quality checklist before you send

- [ ] The header states a clear trigger and end point.
- [ ] The SIPOC has 5 to 7 process steps and names real customers of the output.
- [ ] I interviewed the doer and the checker, and walked through a real recent instance.
- [ ] Every step has one role, starts with a verb, and names its system and output.
- [ ] Decisions show both paths, and exceptions are captured.
- [ ] Every maker-checker point is in the controls register with what is compared, evidence and status.
- [ ] Control status "Performed" is backed by evidence I have seen.
- [ ] Pain points have numbers (frequency, time or errors), not adjectives.
- [ ] The as-is shows what really happens; differences from the SOP are logged.
- [ ] The interviewee validated the as-is in a playback (name and date in the header).
- [ ] Every to-be change links to a pain point, requirement or control gap, with an e2open fit.
- [ ] The swimlane matches the table step numbers and has a legend, version and date.
