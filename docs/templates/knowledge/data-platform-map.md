# Data Platform Map Template

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** one reference page that shows how the team's data platform fits together, with our real names: the components, the connections between them and the account each one uses, the accounts themselves, the scheduled jobs, the data sources the gateway serves, who to call, and each owned tool's platform path. It is the filled-in version of Part 2 of `docs/primers/data-platform-primer.md` and the first thing to open when something breaks (primer Part 9).
- **Who uses it:** the **Manager or the Senior fills it in and keeps it current**, on company systems only, in [COMPANY: location of the filled data platform map, access limited to the team]. It is **never filled in inside this training repository**, which stays generic. The hires read it, and propose rows from their Power Platform and server labs (primer 10.2 and 10.3); the Manager or the Senior checks each proposed row before adding it. The hires copy their owned tool's row into its tool doc (`docs/templates/knowledge/tool-doc.md`, Sections 2, 5 and 8).
- **When:** a first draft (at least Sections 1, 3 and 6) before the Senior's W1 data landscape tour (Thu 10/22), filled out as prep for the Manager's W2 data platform walkthrough. Rows from the labs in W5 and W6. Reviewed at the day-30, day-60 and day-90 reviews, after every change request that touches a connection, an account or a schedule, and whenever someone joins or leaves the team (Section 8).

## How to fill this in

Text in [square brackets] is a prompt: replace it. [COMPANY: ...] is a company-specific value.

1. **No secrets, ever.** No passwords, keys, tokens, recovery keys or connection strings with credentials. "Who holds the secret" names a role and the vault, never the secret.
2. **Account labels.** If [COMPANY: security policy] treats service account names as sensitive, write a label (for example "Team service account 1") and keep the label-to-name key in [COMPANY: password vault].
3. **One row per thing.** One connection, one job, one account per row. When in doubt, split.
4. **Owners are roles plus a backup.** Write the role and [COMPANY: name], and always a backup.
5. **Date what you check.** Each row you verify gets the date and your initials in the "Last checked" column or the review log.
6. **Example rows are fictional** and marked "Example (fictional)". Object names in them are made up. Delete the example rows in the filled copy.
7. **Record the account-model decision.** **Manager decision:** [COMPANY: confirm the service-account model before access requests go out]. The decision (primer 3.3) goes in the header below; until it is made, write "Open: recommended model assumed". Under the recommended model the service account appears only in saved, unattended connections (tables 2, 4 and 5), never as the account a person signs in with.

| Field | Entry |
|---|---|
| Map version and status | [v0.1, Draft or Reviewed] |
| Filled by / checked by | [Manager or Senior] / [the other one] |
| Last full review | [Date] |
| Next review | [Day-30, day-60 or day-90 review date, or a change request] |
| Service-account model | [Open: recommended model assumed / Decided on (date): (model)] |
| Where this map lives | [COMPANY: location of the filled data platform map] |

## Template

### 1. Components

Include at least: the Oracle EBS production database, the team database, the sandbox or staging schema, the data warehouse (if separate), the on-premises data gateway, each Power BI workspace the team uses, each Power Platform environment, the remote server, the password vault, the code repository, and the file shares or landing folders that tools read or write.

| Component | What it is for | Owner (and backup) | How people connect | What hires may do before day 60 | Last checked |
|---|---|---|---|---|---|
| Example (fictional): team database `TEAMDB01` (example name) on SQL Server | The team's working copy of EBS, trade and broker data; reporting views in schema `rpt` (example name) | Objects: Senior. Server and backups: [COMPANY: DBA] | SSMS, Windows Authentication, personal login | Read; load only into schema `sbx` (example name) | 2026-10-16, Senior |
| [Component] | [Purpose] | [Role and backup] | [Tool, authentication] | [Read only, sandbox only, view only, nothing] | [Date, initials] |

### 2. Connections

Every link along the data path (primer 2.2): EBS to the team database, AS400 and broker files to the team database, team database to each semantic model, each flow and app connection, and each job that reads or writes data.

| From | To | Method | Account used | Schedule | Owner |
|---|---|---|---|---|---|
| Example (fictional): Oracle EBS production | Team database, table `stg.ebs_item_cost` (example name) | Nightly extract job on the remote server (job J-03, example) | Team service account 1 | Daily 02:00 [time zone] | Senior |
| [Source system or object] | [Target system or object] | [Extract job, gateway, flow connection, linked server, file drop] | [Account label] | [Frequency and time] | [Role] |

### 3. Accounts

List every non-person account, plus one row per group of personal accounts (not one row per person).

| Account (label or name) | Type | Access it has | Who holds the secret | Used by |
|---|---|---|---|---|
| Example (fictional): Team service account 1 | Service account (domain) | Same as the team on the team database: read, plus write on `stg` (example name) for the extract job [narrower if the Manager decides] | Manager; password in [COMPANY: password vault]; rotated [COMPANY: interval] | Gateway connection GW-SQL-TEAM; job J-03; flow "Daily load notice" (all example names) |
| [Account] | [Personal group, service account, group Managed Service Account, service principal, built-in service identity] | [Grants, least privilege] | [Role and vault; "Windows manages it" for a gMSA] | [Connections, jobs, flows, apps] |

### 4. Scheduled jobs

Include Task Scheduler tasks on the remote server, SQL Server Agent jobs, flows with a recurrence trigger, and Power BI scheduled refreshes.

| Job | Where it runs | Schedule | Runs as | What it does (inputs and outputs) | Who is told on failure |
|---|---|---|---|---|---|
| Example (fictional): J-03 EBS item cost extract | Remote server, Task Scheduler folder `\Team` (example name) | Daily 02:00 | Team service account 1 | Reads EBS item cost data; writes `stg.ebs_item_cost` (example name); log in `D:\Jobs\J03\logs` (example path) | Senior by email; the Manager if it fails twice in a row |
| [Job ID and name] | [Server and folder, SQL Agent, Power Automate environment, Power BI workspace] | [Frequency, time, holidays] | [Account label] | [Inputs, outputs, log location] | [Role; how they are told] |

### 5. Data sources the gateway serves

| Field | Entry |
|---|---|
| Gateway name and mode | [COMPANY: gateway name]; [standard mode; a personal-mode gateway is not for team solutions] |
| Machine it runs on | [COMPANY: server; if it is the remote server, a restart there stops every refresh and flow that uses it] |
| Gateway admins (at least two) | [Roles and names] |
| Recovery key held by | [Role; where it is kept, so another admin can find it. Never the key itself] |
| Who installs monthly updates | [Role] |

| Gateway connection | Source (server and database) | Credential (account label) | Used by (models, flows, apps) | Connection owner |
|---|---|---|---|---|
| Example (fictional): GW-SQL-TEAM (example name) | `TEAMDB01` on server `SQL-T1` (example names) | Team service account 1 | Semantic model "Duty by origin"; flow "Daily load notice" (example names) | Manager (backup: [COMPANY: IT gateway admin]) |
| [Connection name] | [Server, database] | [Account label] | [Every item that depends on it] | [Role and backup] |

### 6. Who to call

Include at least: team database objects, the database server and backups, EBS access and slow queries, ERP security (the read-only EBS accounts), the gateway, each Power BI workspace, the Power Platform environments, the remote server, the password vault and rotations, and the IT service desk.

| Area | Problem | Contact (role) | How to reach them | Hours and backup |
|---|---|---|---|---|
| Example (fictional): gateway | Every refresh and flow that uses the gateway fails at once | [COMPANY: IT gateway admin] | Ticket queue "BI Platform" (example name), then a Teams call | Business hours; backup: Manager |
| [System] | [Typical problem] | [Role, COMPANY: name] | [Ticket queue, Teams, phone] | [Hours; backup] |

### 7. Tool platform paths

One row per owned tool; the same facts go in the tool doc (Sections 2, 5 and 8). This row is part of the day-60 owned-tool evidence (`docs/01-30-60-90-plan.md` Section 4).

| Tool ID | Database objects it reads or writes | Connection | Runs as | Schedule | Server location |
|---|---|---|---|---|---|
| Example (fictional): T-07 | Reads `rpt.v_item_trade` (example name); writes nothing to the database | Python with pyodbc, Windows Authentication (example) | Team service account 1 (scheduled run); personal login for test runs | Weekdays 06:00 | Remote server, `D:\Jobs\T07` (example path) |
| [T-nn] | [schema.object, read or write] | [Driver or connector; gateway connection name] | [Account label] | [Trigger and time] | [Server, folder, environment] |

### 8. Leaver and joiner check

When anyone on the team leaves or changes role, the Manager works through this before their last day:

- [ ] Flows and apps they own or co-own, and connections they created: add a co-owner or change the owner (solution-aware flows only; others must be copied), and move each connection to the agreed account (primer 7.4).
- [ ] Gateway: are they an admin or a connection owner? Make sure at least two admins remain and every connection has an owner.
- [ ] Scheduled jobs that run as their personal account: move them to the agreed account and test the next run.
- [ ] Workspace roles, sandbox tables and personal grants (team database, EBS read-only account): removed through [COMPANY: access removal process], and their sandbox tables dropped.
- [ ] Did they know or hold the service account password? If so, rotate it and update every connection in tables 2 and 5 the same day.
- [ ] Update tables 1 to 7 and add a review-log line.

When someone joins: personal accounts only, requested through `docs/04-access-request-checklist.md`; they read Part 1 of the primer before their first SSMS or DBeaver session.

### 9. Review log

| Date | Reviewer | What changed | Trigger |
|---|---|---|---|
| Example (fictional): 2026-11-18 | Senior | Added the flow connection from the Power Platform lab; corrected job J-03's schedule | Day-30 review |
| [Date] | [Name] | [Rows added, changed, removed] | [Milestone review, CR ID, leaver, incident] |

## Quality checklist before you publish the filled map

- [ ] No passwords, keys, tokens, recovery keys or connection strings with credentials anywhere on the page.
- [ ] Every connection (table 2) and every gateway connection (table 5) names an account that appears in table 3.
- [ ] No connection, job or app runs as a person's account without a note saying why and when it will move.
- [ ] Every scheduled job names who is told when it fails.
- [ ] The gateway has at least two admins, and the recovery key's location is recorded.
- [ ] Every owned tool has a row in table 7 that matches its tool doc.
- [ ] The service-account decision is recorded in the header with its date, or marked open.
- [ ] Example rows are deleted from the filled copy; the filled copy is stored only in [COMPANY: location of the filled data platform map].
