# Tool Documentation Template

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** one page per custom tool (Python, Excel VBA, Access, Power Apps, Power Automate) so that someone other than its builder can run it, fix the common failures, change it safely and plan its future under e2open. Most of the team's 10+ tools have little or no documentation; these pages become the team's first tool library.
- **Who uses it:** the assigned learner writes it (Hire A or Hire B, per the Tool Inventory tab of BSA-Onboarding-Trackers.xlsx in the onboarding folder). The current knowledge holder checks it for accuracy. The Manager reviews and approves it (the Senior does not know these tools well, so the Manager is the checker). Anyone who runs or supports the tool reads it.
- **When:** Tool Inventory row in W2; candidate tool walkthrough in W4; doc for your owned tool started in W6 and complete by day 60 (A60-7, B60-7); second tool doc by day 90 (A90-7, B90-7). Update it with every change request (`docs/templates/bsa/06-change-request.md`) and re-verify it at least every [COMPANY: review interval]. Module M6.

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. **Start from the Tool Inventory row.** Use the same Tool ID (T-01, T-02, ...) and copy what is already known.
2. **Interview the current owner** for 45 to 60 minutes using the questions at the end of this page. Ask for a recent real run, not a demo.
3. **Run it yourself:** in production only with the current knowledge holder supervising, otherwise on a test copy (test inputs, output to a test folder). Before the day-60 review you have no production write access (`docs/04-access-request-checklist.md`, rule 2), so in a production run the knowledge holder executes every step that writes data or sends output to a broker, Finance, Oracle or another system, while you drive and explain the other steps. For day 60, one end-to-end run is enough: either supervised in production or alone on a test copy (`docs/01-30-60-90-plan.md`, "owns one tool"). Write the steps while you do them and take the screenshots then. A step you did not perform yourself is marked "not yet verified".
4. **Read the code or the file.** List every input, output, hard-coded path, date, rate, email address and credential it uses (stack-specific tips below).
5. **Write "how it breaks" from evidence:** emails, Jira issues, the owner's memory of real failures. Do not invent failure modes.
6. **Review:** the owner checks facts, then the Manager reviews. Status moves Draft, then Reviewed, then Published. Only Reviewed and Published pages go to the shared OneNote section "04 Tool Docs".
7. **Peer test:** the other hire follows your page on a test copy (test inputs, output to a test folder), or reads only your page while you and the knowledge holder run the real job. Before day 60 the peer never runs a step that writes data or sends output to a broker, Finance, Oracle or another system (`docs/04-access-request-checklist.md`, rule 2). Every place they get stuck is a gap to fix.
8. **Never paste secrets.** No passwords, keys, connection strings with credentials, or personal data. Say where credentials are managed ([COMPANY: credential store or service account owner]).

## Template

### 1. Summary

| Field | Entry | Example of a good entry |
|---|---|---|
| Tool ID and name | [T-nn], [COMPANY: tool name] | T-07, [COMPANY: tool name] |
| Doc status and version | [Draft, Reviewed, Published]; [v0.1] | Reviewed v1.0, 2026-12-11 |
| Purpose (one sentence) | [What business problem it solves] | Builds the weekly classification file sent to the US broker from the AS400 classification master |
| Process and module | [Research, Standard Cost, Exports, Reporting, Drawback, other; M-code] | Research (M5R); also used by Exports (M7) |
| Business users | [Roles and teams, how many people] | Research BSA (runs it); [COMPANY: US broker] (receives the file) |
| Criticality | [High, Medium, Low] and what happens if it does not run for a day, and for a week | High: the broker files with stale classifications after 1 week |
| Stack | [Python, Excel VBA, Access, Power Apps, Power Automate, other] and version | Python 3.11 script; pandas; pyodbc |
| Location of code or file | [COMPANY: repository, shared drive path, SharePoint library or Power Platform environment] | [COMPANY: repository]/broker-file, branch main |
| Owner and backup | [Name or role] / [Name or role] | Hire A (first point of contact; production change rights from the day-60 review) / Manager |
| e2open impact | [Replaced, Integrates, Unaffected, TBD] and why | TBD: depends on whether e2open sends classification data to brokers ([COMPANY: confirm]) |
| Last verified | [Date, by whom, how] | 2026-12-09, Hire A, full production run supervised by the knowledge holder |

### 2. Trigger and schedule

| Field | Entry |
|---|---|
| Trigger | [Manual, scheduled (Windows Task Scheduler, Power Automate recurrence), event (file arrives, email received), on request] |
| Schedule | [Day and time; time zone; what happens on holidays] |
| Run time | [Typical duration; longest seen] |
| Who starts it | [Role; service account if scheduled] |
| Business deadline | [When the output must be ready, and why] |

### 3. Inputs

| Input | Source system or file | Format | Provided by, and when | Checks before running |
|---|---|---|---|---|
| [Classification extract] | [AS400 file or warehouse table] | [CSV, table, Excel] | [Role, day and time] | [Row count vs last run; HTS as text] |

### 4. Outputs

| Output | Destination | Format | Used by | Checks after running |
|---|---|---|---|---|
| [Broker file] | [SFTP folder, email, SharePoint, Oracle interface] | [CSV with fixed columns] | [Broker, Finance, team] | [Row count, rejects, spot check of 5 rows] |

### 5. Data sources and connections

| Source | Type | Object (table, file, list) | Access needed | Credentials managed by |
|---|---|---|---|---|
| [Data warehouse] | [SQL Server, AS400 via ODBC, Oracle extract, SharePoint list, Excel, Access] | [Object name] | [Read, write] | [COMPANY: service account or personal account] |

### 6. How to run it

| Step | Action | Expected result | Screenshot |
|---|---|---|---|
| 1 | [Verb first: "Open ...", "Run ...", "Check ..."] | [What you should see] | [Screenshot 1: what it shows] |
| 2 | [ ] | [ ] | [ ] |

Write steps a new BSA can follow without help. One action per step. Include where files must be saved and what to name them.

### 7. How it breaks and known fixes

| Symptom | Likely cause | Fix | Who can fix it | Last seen |
|---|---|---|---|---|
| [Error message text, or "output has fewer rows"] | [Cause] | [Steps] | [Role] | [Date or Jira key] |

### 8. Dependencies

- Systems and data: [AS400 extract job, warehouse refresh time, Oracle interface]
- Other tools: [Tool IDs this one feeds or is fed by]
- Software and libraries: [Python packages and versions, Access runtime, Office version, VBA references, Power Platform connectors and licences]
- Infrastructure: [mapped drives, file paths, scheduled tasks, service accounts, the server or PC it runs on]
- People: [anyone whose manual step the tool relies on]

### 9. Controls

| Control | How it works | Evidence |
|---|---|---|
| [Output check before sending] | [Who checks what, against what] | [Log, email, Jira comment] |
| [Change control] | Every change through a change request with a checker (`docs/templates/bsa/06-change-request.md`); the owner does not approve their own change | [CR keys in the change history] |

### 10. e2open impact

| Question | Answer |
|---|---|
| Impact | [Replaced, Integrates, Unaffected, TBD] |
| Which e2open function or interface would take over or connect | [Function, or "unknown: ask the e2open project team"] |
| Data the e2open data map needs from this tool | [Fields, value lists, business rules hidden in the code] |
| Business rules in the code that must not be lost | [List them; they go into requirements (`docs/templates/bsa/02-requirements.md`)] |
| Retirement or change plan | [Date or milestone; owner] |

### 11. Change history

| Version | Date | Change | CR or Jira key | By | Checked by |
|---|---|---|---|---|---|
| [v1.0] | [ ] | [First documented version] | [n/a] | [ ] | [Manager] |

### 12. Open questions

| # | Question | Asked to | Date | Answer |
|---|---|---|---|---|
| [1] | [ ] | [ ] | [ ] | [ ] |

## Stack-specific things to capture

| Stack | Where to look | What to record |
|---|---|---|
| Python | The script folder, any `requirements.txt`, imports at the top of each file, config files, logs, Task Scheduler entries | Python version; packages and versions; virtual environment; how it is scheduled; config values; hard-coded paths and dates; where logs go |
| Excel VBA | Developer tab > Visual Basic: modules, forms, Tools > References; Formulas > Name Manager; Data > Edit Links | Module list and what each does; references; named ranges; links to other workbooks; hard-coded sheet names and paths; trusted location needed; any sheet protection and where its password is held ([COMPANY]) |
| Access | Navigation pane (tables, queries, forms, macros, modules); Linked Table Manager; any AutoExec macro (runs on open) | Front-end and back-end files; linked tables and their sources (ODBC data source names); action queries that change data; who has the file open when it locks; compact and repair routine |
| Power Apps and Power Automate | The environment and solution; the app or flow details page; connections and connection references; run history | Environment; owners and co-owners; each connection and the account it runs as; premium connectors and licences; triggers; how long run history is kept, so you export evidence you need; whether it is in a solution |

## Questions to ask the current owner

Purpose and users

- What problem did you build it to solve, and who asked for it?
- Who uses the output, and what decision or filing depends on it?
- Who would notice first if the output were wrong but looked normal?

Running it

- Walk me through the last real run, start to finish. What did you check by eye before you sent the output?
- What do you do differently at month-end, year-end, on holidays or when a new tariff action starts?
- Which manual steps happen before or after the tool runs?

Data

- Where does each input come from, and who produces it? What time must it be ready?
- Which values are hard-coded: paths, dates, rates, item lists, email addresses, sheet names?
- Which fields does the tool change or derive, and what are the rules?

Failure

- When did it last fail? What happened, and what did you do?
- What are the error messages you have seen, and what does each one mean?
- If you were out for two weeks, what would break first?

Code and change

- Where is the latest version? Are there other copies, and which one is real?
- Who else has changed it? Is there any change log, even an email trail?
- What would you change if you had a week? What do you not dare to touch, and why?

Access and security

- Does it run under your personal account or a service account? What happens if your password changes or you leave?
- Who has access to the code and the output folders? Should they?
- Does any output contain personal data, supplier prices or other sensitive data?

Future

- Which parts would e2open replace? Which business rules in the tool would e2open need to know?
- Is anything about to change that affects the tool (Oracle, AS400 extracts, broker formats)?

## Quality checklist before you send for review

- [ ] All 12 sections are filled or marked "not applicable" with a reason.
- [ ] I ran the tool myself, or I marked the steps I could not verify.
- [ ] The other hire ran the tool from this page alone on a test copy, and I fixed what they got stuck on.
- [ ] "How it breaks" is based on real failures, each with a date or Jira key.
- [ ] Every hard-coded value I found is listed.
- [ ] e2open impact is stated with a reason, and the business rules hidden in the code are listed.
- [ ] No passwords, keys or personal data on the page.
- [ ] The Tool Inventory row (documentation status, e2open impact, knowledge holder, backup, tool doc link) is updated.
- [ ] The current owner has checked the facts; the Manager has reviewed the page.
