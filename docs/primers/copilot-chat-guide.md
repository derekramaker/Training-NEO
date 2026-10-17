# Copilot Chat Guide for BSA Work

Last updated: 2026-10-17 · Owner: BSA Manager

- **Purpose:** how to get real value from Microsoft 365 Copilot Chat in Research, Standard Cost, data, custom-tool and BSA work while staying inside the rules. It covers what the free tier is and what it cannot see, what you may paste, how to write prompts, what to verify for each use case, what Copilot gets wrong in trade work, and how the use log and the team prompt library work. Module M11.
- **Who uses it:** Hire A and Hire B, every week. The Manager runs the W1 setup and rules session, reviews the use logs in W4 and reviews prompt library entries. The Senior and the Manager, as checkers, use Section 2.3 to know what Copilot-assisted work must show. The library itself is `docs/templates/knowledge/copilot-prompt-library.md`.
- **When:** Parts 1 and 2 before the W1 setup and rules session; Parts 3, 5 and 6 in W2, when you start your use log; Part 4 one subsection at a time, the first time you use Copilot for that task. Re-read Section 2.2 whenever you are about to paste something new.

## How to use this guide

| Week | What | Time | Output |
|---|-----------------|----------|------------|
| W1 | Read Parts 1 and 2. M11 setup and rules session with the Manager (30 minutes, both hires; day and time in `docs/02-weeks-1-2-schedule.md`). Setup checklist (1.6). | About 1 h of the W1 new self-study line, plus the session | Checklist ticked; your tenant answers noted at the top of your use log page |
| W2 | Read Parts 3, 5 and 6. Start your use log. | About 0.75 h of the W2 new self-study line | Use log page with first entries |
| W3–W5 | Use Copilot in real tasks. Read the Part 4 subsection for a task the first time you use Copilot for it (5–10 minutes). | Inside the task | Log entries |
| W4 | Use-log review with the Manager (15 minutes for both hires) | Manager 0.25 h | Entries marked reviewed; two self-check questions (Part 7) answered aloud |
| Day 30 (evidence due Mon 11/16) | Should criterion: 5 reviewed uses in your log | None extra | Log link in your day-30 scorecard |
| W6–W13 | Keep logging. Propose your first prompt library entry by day 60, then add entries until 3 are reviewed (6.4). | Inside the task | Library entries with status Proposed, then Reviewed |
| Day 90 (evidence due Wed 1/13) | Should criterion: 3 library entries reviewed by the Manager | None extra | Library entries with status Reviewed |

Tailoring:
- **Hire A (Research):** the riskiest uses are yours: notices, HTS codes, rates and dates. Read 4.1, 4.2 and 5.1 to 5.3 first. If you script, Copilot can help you write a list-comparison script; it runs only on extracts, and its output is reviewed like any other (2.4).
- **Hire B (Standard Cost):** read 4.3 to 4.5, 5.4 and 5.5 first. You pick up data work quickly, and Copilot makes SQL and DAX drafts even faster, so the sandbox rule (2.4) matters more for you, not less.

Conventions: `[COMPANY: ...]` marks a company fact or tenant setting the Manager must confirm. Product facts change fast, so each one carries "as of Oct 2026" and a link to check: open the link when it matters, and trust what you actually see in our tenant over this page. Example items (KIT-100, PART-A, Country X) and all example numbers are fictional.

## 1. What Copilot Chat is here

### 1.1 Which Copilot we mean

This guide is about **Microsoft 365 Copilot Chat**, the Copilot that comes with your work (Microsoft Entra ID) account at no extra cost. Microsoft's pages also call it Microsoft Copilot Chat. This guide takes "Copilot basic" to mean this product. [COMPANY: confirm our Microsoft 365 plan includes Copilot Chat, and that the hires do not have paid Microsoft 365 Copilot licenses]

| Product | What it is | For our work |
|---|---------------|-------------|
| Microsoft 365 Copilot Chat | AI chat grounded in the web, included with an eligible Microsoft 365 work account | Yes: this guide |
| Microsoft 365 Copilot (paid add-on license) | Adds chat grounded in company data (mail, files, chats, meetings), plus extra agents and in-app features | Do not assume we have it |
| Microsoft Copilot (consumer, copilot.microsoft.com, personal account) | A free consumer service | Never for work data or work files |
| Copilot inside Power BI, Power Automate and Power Apps | Separate features with their own licensing, capacity and admin switches | See 1.5 |

The table is as of Oct 2026 (check https://learn.microsoft.com/en-us/copilot/microsoft-365/which-copilot-for-your-organization). Microsoft shows a label under your name that tells you which experience you have: "Copilot chat (Basic)" (no Copilot chat inside Word, Excel, PowerPoint and OneNote), "M365 Copilot (Basic)" (standard access in those apps) or "M365 Copilot (Premium)" (the paid license) (as of Oct 2026; check https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-overview). Note which one you see (1.6).

### 1.2 Where to open it

- **Web or app:** m365copilot.com, or the Microsoft 365 Copilot app on Windows or Mac. Use this for real work: the exact web queries Copilot sent are shown here for 24 hours, not in the in-app panes (1.4).
- **Teams, Outlook and Microsoft Edge:** usually pinned in the left bar of Teams and Outlook, and in the Edge sidebar when you are signed in with your work account (as of Oct 2026; check the link in 1.1).
- **Word, Excel and PowerPoint:** some users without the paid license see a Copilot pane beside the open file (and, in Excel, an Agent Mode), and some do not. It depends on our tenant and on Microsoft's rollout. [COMPANY: confirm whether we see the Copilot pane in Word/Excel/PowerPoint and which label shows under our name]
- **Not on a personal phone.** No company data on personal devices (`docs/04-access-request-checklist.md`, rule 7; [COMPANY: mobile device policy]).

### 1.3 What it can see and what it cannot

Copilot Chat cannot see our internal data except what you put into the chat, with the Outlook exception below (as of Oct 2026; check https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-chat-considerations).

| It can work with | It cannot see |
|---------------|---------------|
| Text you paste | Your OneDrive, SharePoint, Teams chats and channels, meetings, Jira or OneNote, unless you paste or upload the content |
| Files you upload, such as Word, PowerPoint and PDF files and saved emails (types, number and size are limited, and the limits change; see https://www.microsoft.com/en-us/copilot/solutions/business; test Excel and CSV in setup, 1.6) | The team database, Oracle EBS, the AS400 trade system, the data warehouse, Power BI datasets, flows and apps |
| In Edge, the page or open tabs you ask about. That can include a page you are signed in to, such as a broker portal, an Oracle EBS page or a Power BI report, so asking about it counts as pasting it (2.2) | Other people's files and mail |
| Public web results from Bing, if web search is on for us [COMPANY: confirm whether web search is on for us] | Web pages behind a login, through its web search |
| In Outlook, your own inbox and calendar (rolling out to users without the paid license) [COMPANY: confirm what we see] | Anything you did not give it in this chat (memory aside, 1.4) |

Two consequences follow. First, if an answer sounds company-specific (our items, tools, rules or history), it is a guess. Second, Copilot sees exactly what you paste, so the paste rules in 2.2 are the main control.

### 1.4 Enterprise data protection (EDP), in plain words

When you are signed in with your work account, Copilot Chat runs under enterprise data protection (as of Oct 2026; check https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection):

- Your prompts and Copilot's responses are covered by Microsoft's Data Protection Addendum and Product Terms, with Microsoft as data processor: the same kind of terms that cover our Exchange email and SharePoint files.
- They are not used to train Microsoft's foundation models.
- Our own permissions, sensitivity labels, retention policies and audit still apply.

What EDP does **not** mean:
- **It is not permission to paste anything.** EDP is a contract about how Microsoft handles the data. Our own policy decides what may go in (2.1, 2.2).
- **Web searches are handled differently.** When Copilot searches the web, it sends Bing a few words built from your prompt, with your user and tenant IDs removed. Those queries fall outside the Data Protection Addendum. So keep confidential names, prices and supplier terms out of any prompt that may need a web search, and look at the web-query citations to see what was sent. You cannot switch web search off yourself: Copilot Chat has no user web toggle, only the admin setting. Writing "do not use the web" steers the answer; it is not a control (as of Oct 2026; check https://learn.microsoft.com/en-us/copilot/microsoft-365/manage-public-web-access).
- **It is not private from the company.** Prompts and responses are stored as your Copilot activity history. Admins can search them with Microsoft Purview (Microsoft's compliance and eDiscovery tool), and a "temporary" chat can be found the same way. Write every prompt as if an auditor will read it. [COMPANY: confirm our retention period for Copilot interactions] (as of Oct 2026; check https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy)
- **Memory lasts.** Copilot can remember custom instructions and details from your chats. Saved memories stay until you delete them, and retention policies do not apply to them. Never ask it to remember company data (as of Oct 2026; check https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-personalization-memory).

**Check the shield.** Copilot Chat shows an enterprise data protection shield near the chat box when you are signed in with your work account. If you do not see it, you may be signed in with a personal account: stop and switch. Microsoft restyles this indicator from time to time. [COMPANY: confirm what the indicator looks like for us]

### 1.5 What the free tier does not include

Do not plan work around these. Each needs the paid license, extra capacity or an admin decision (as of Oct 2026; check https://www.microsoft.com/en-us/microsoft-365-copilot/pricing). How Power BI and the Power Platform reach our data is in `docs/primers/data-platform-primer.md`.

| Feature | In free Copilot Chat? | What to do instead |
|------------|------------|---------------|
| Searching your mail, files, chats and meetings (work data, which Microsoft calls Work IQ) | No: paid license (Outlook inbox and calendar exception in 1.3) | Paste or upload the item you need, within the paste rules |
| Researcher and Analyst agents | No: paid license | Break the task into steps yourself (Part 3) |
| Copilot that answers from a Teams meeting's transcript; intelligent meeting recap | No: paid license (recap also comes with Teams Premium) [COMPANY: confirm whether we have Teams Premium] | Take your own notes; 4.8 turns them into a summary |
| Scheduled prompts | No: paid license | A recurring Planner task |
| Answers from Power BI data inside Copilot Chat | No: paid license | Paste a small fictional table or the measure (4.6) |
| Copilot in Power BI | Depends on Fabric or Premium capacity and an admin switch, not on Copilot Chat [COMPANY: confirm the workspace license mode and whether the Copilot tenant setting is on] | Copilot Chat with the DAX pasted in (as of Oct 2026; check https://learn.microsoft.com/en-us/fabric/fundamentals/copilot-enable-fabric) |
| Copilot in the Power Automate designer and in Power Apps | Separate features with their own licensing, region and admin rules [COMPANY: confirm whether our Power Platform environment has Copilot enabled] | Any flow or app change still goes through change control (2.4) (as of Oct 2026; check https://learn.microsoft.com/en-us/power-automate/copilot-overview) |
| Agents that read SharePoint or other company data | Metered (pay-as-you-go), only if an admin connects billing | Do not build or use agents unless the Manager confirms [COMPANY: confirm whether hires may build or use agents] |

What the free tier does include, subject to admin settings and capacity: chat with web grounding, file upload, Copilot Pages (save, edit and share an output), the Prompt Gallery (save your prompts), chat history and memory. Copilot Notebooks is rolling out to Copilot Chat users. At busy times, users without the paid license may see slower answers or limits on some features (as of Oct 2026; check https://support.microsoft.com/en-us/microsoft-365-copilot/standard-versus-priority-access-to-features-in-microsoft-365-copilot-chat).

### 1.6 Setup checklist (W1)

- [ ] Read `[COMPANY: AI acceptable-use policy]` and complete any acknowledgement it asks for.
- [ ] Open Copilot Chat at m365copilot.com, signed in with your work account. Find the enterprise data protection shield (1.4).
- [ ] Note which label shows under your name (1.1) and whether you see a Copilot pane in Excel and Word (1.2). Bring both answers to the session.
- [ ] Upload one practice-pack file (items.csv from the practice-data folder, or Practice-Data.xlsx, both in the onboarding folder; fictional data) and ask how many rows the items table has. Note whether the upload worked and whether Copilot showed code it ran (5.4). Compare its answer with the Tables section of `docs/analytics/practice-exercises.md` (150).
- [ ] In the session, get the tenant answers you cannot see yourself: web search on or off; Pages, Notebooks and memory on or off; whether agents are allowed; the retention period [COMPANY: confirm tenant settings].
- [ ] If personalization is on (Settings > Personalization), add the custom instructions below. Put no company data in them.
- [ ] Create your "Copilot use log" page in your own OneNote section (6.1). Bookmark the team's Copilot prompt library page in OneNote ([COMPANY: team OneNote section for the prompt library]).
- [ ] Use no other AI tool for work data, never the consumer Copilot, and never a personal Copilot subscription on work files. [COMPANY: AI acceptable-use policy: which other AI tools, if any, are allowed]

Suggested custom instructions:
> I work as a business systems analyst on a trade compliance and trade data team (imports into the US, Canada and Mexico). Use plain English. Always list your assumptions and say what you are unsure of. Never present an HTS code, duty rate, date, legal citation or regulation as confirmed: tell me which official source to check. When I paste a source, use only that source unless I ask otherwise. When I ask for SQL, assume Microsoft SQL Server unless I say Oracle.

### 1.7 How this applies to our work

For **Research**, Copilot is fast at laying out a pasted notice as a table, but it is not a source of tariff facts (2.3, 5.1 to 5.3). For **Standard Cost**, it helps with formulas, variance hypotheses and first drafts of emails, and every number is recomputed (5.4). For your **owned tool**, it explains old VBA, Python or flows for the tool doc, and never changes production (2.4, 4.7). For **e2open**, it turns your interview notes into as-is step tables and drafts test cases, but knows nothing about our e2open scope (4.11).

## 2. Rules first

### 2.1 The policy comes first

`[COMPANY: AI acceptable-use policy]` overrides this guide. Microsoft's Enterprise AI Services Code of Conduct also applies (https://learn.microsoft.com/en-us/legal/ai-code-of-conduct). Until the Manager confirms what our policy says, follow the defaults in this part. When in doubt, ask the Manager **before** you paste. If you pasted something you should not have, tell the Manager straight away: it passes the "ask now" test for a possible security or compliance problem (`docs/05-time-management.md`).

### 2.2 What you may paste

| Category | Examples | Rule |
|---------|-----------------|-----------------|
| Public official text | Federal Register notices, CBP CSMS (Cargo Systems Messaging Service) messages, HTSUS notes, CBSA notices, decrees in Mexico's Diario Oficial (DOF), Microsoft documentation | Yes |
| Fictional or synthetic data | The analytics practice pack; KIT-100 examples; five made-up rows with the same columns as a real table | Yes. Describing the shape of real data, or inventing rows that look like it, is the safest way to get help with it |
| Your own notes and drafts about how we work, with no personal data (write people as roles or initials) | Meeting notes, process steps, requirement notes, a draft SOP | Yes, if `[COMPANY: AI acceptable-use policy]` allows internal data under EDP |
| Code from our custom tools | VBA, Python, Power Query M, SQL, flow definitions | Only if the policy allows it [COMPANY: may internal tool code be pasted]. Always remove credentials, connection strings, server names and file paths first |
| Company business data | Item lists with costs, supplier prices, margins, broker entry data, Finance figures, anything with a Confidential sensitivity label | Ask the Manager first. Paste the smallest piece that does the job, or a fictional copy |
| Third-party confidential material | e2open project documents under the vendor's terms, advice from trade counsel, broker correspondence | Ask the Manager first |
| Credentials | Passwords, keys, tokens, connection strings with passwords, MFA codes, any service account password (under the recommended model you never see one: `docs/primers/data-platform-primer.md` Part 1; [COMPANY: confirm the service-account model before access requests go out]) | Never |
| Personal data | Names with contact details, employee or HR data, personal IDs, anything about a person's performance | Never |
| Restricted classes | [COMPANY: data classes the policy restricts] | Never |

If a file or a piece of code you want help with contains a credential, do not paste it. Tell the Manager: a credential inside a file or code is itself a finding (`docs/templates/knowledge/tool-doc.md`, "Never paste secrets").

### 2.3 AI output is a draft

- **Maker-checker still applies.** Copilot is never the maker or the checker. You are the maker of anything you submit, and you must be able to explain every line of it. Tell your checker when Copilot drafted part of the work and what you verified; the use log entry is the evidence. [COMPANY: AI acceptable-use policy: whether AI-assisted content must be labelled]
- **Primary sources still apply.** Never cite Copilot as the source of a regulatory fact, an HTS code, a rate, a date or a legal citation. Every claim in a Tariff-Impact Brief, a model or a cost update cites the official source you opened yourself. Copilot's citations are leads to open, not evidence (5.1).
- **Microsoft says the same.** Its own prompting advice includes "always review and verify AI-generated responses", and it warns that outputs "may be inaccurate, incomplete, biased, misaligned, or irrelevant to your intended goals" (as of Oct 2026; check https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-application-card).
- **Copilot does not change the rules of the work.** The urgency rule still decides who is maker for a live tariff action, and Copilot does not shorten any review (`docs/01-30-60-90-plan.md` Section 7). The boundary rule holds: Standard Cost never asks Copilot which items are in scope (that is Research's WHAT), and Research never asks it for the $ impact.
- **Nothing Copilot drafted leaves the team unreviewed:** no email to Finance or the business, no data to a broker, no update to a system. Before the day-60 review you do not contact brokers or counsel at all; questions go through the Senior (or the Manager).

### 2.4 Code and data: the sandbox rule

Code that Copilot writes or changes (SQL, DAX, Power Query M, Python, VBA, a flow) is untested text until you have read it, run it in a safe place and checked the result.

1. **Never run Copilot's code straight from the chat on anything production:** Oracle EBS, production objects in the team database, production Power BI workspaces, production flows and apps, production tool files. Never paste Copilot-written SQL into a DBeaver session connected to EBS.
2. **Read it line by line first,** and write down in your own words what each line does. If you cannot explain a line, do not run it.
3. **Test in the sandbox.** Run SQL in `[COMPANY: sandbox or staging schema in the team database]` or on the practice data. Run Python or VBA on an extract or a test copy of the tool.
4. **Check row counts** before and after every join and filter, and compare the total with a known control total (the habit from `docs/analytics/practice-exercises.md`). Only when steps 2 to 4 are done, and you can explain every line, is it your query. A read-only query (SELECT only) may then run, under your personal login, wherever the data platform rules allow (`docs/primers/data-platform-primer.md`, Part 1); if its result feeds work that others rely on, your checker reviews it like any other query. Anything that loads or changes data runs only in `[COMPANY: sandbox or staging schema in the team database]`. EBS has a stricter rule (step 5).
5. **Oracle EBS is different.** The team sandbox is SQL Server, so you have no place to test Copilot-written Oracle SQL. Copilot may explain Oracle syntax or an existing reviewed query; you write any EBS query yourself and follow the EBS rules in Part 1 of `docs/primers/data-platform-primer.md` (read-only account; never DML or DDL, the statements that change data or structure).
6. **No schema changes.** Copilot will happily write CREATE, ALTER and DROP statements. Schema changes in the team database (tables, views, procedures, jobs) go through the Senior. If your owned tool depends on team-database objects, a change to those objects goes through a change request (`docs/templates/bsa/06-change-request.md`) with the Senior as checker. Any other change to your owned tool also goes through a change request, and there is no production write access before the day-60 review (`docs/04-access-request-checklist.md`, rule 2).
7. **Power Platform:** a flow or app that Copilot helped build or change is still a change: test copy first, change request, the Manager as checker.

### 2.5 Before you press Enter, and before you use the output

Before you press Enter:
- [ ] Signed in with the work account; the shield is visible.
- [ ] Nothing in the prompt, the file or (in Edge) the open tabs breaks 2.2: no credentials, no personal data, company data only with the Manager's agreement.
- [ ] If the answer may need a web search, no confidential names, prices or supplier terms in the prompt.
- [ ] The source is pasted or uploaded, and the prompt says to use only that source.

Before you use the output:
- [ ] Every fact checked against a primary source you opened; every number that matters recomputed.
- [ ] Any code read line by line and run only in the sandbox or a test copy, with row counts checked.
- [ ] The use log entry is written (Part 6): every use whose output went into your work, and every use you rejected. Your checker will know Copilot helped.

## 3. Prompting that works

### 3.1 Goal, context, source, expectations

Microsoft's prompting training describes four parts of a good prompt: the **goal** (what you want), the **context** (why, for whom, what you already know), the **source** (what Copilot should draw on) and the **expectations** (format, length, tone, level of detail) (as of Oct 2026; check https://learn.microsoft.com/en-us/training/modules/write-effective-prompts-do-more-prompting/2-write-effective-prompt). In Copilot Chat the source must be something you paste or upload, because it cannot reach our files (1.3). For our work, add a fifth part, **the checks**: ask for its assumptions, its uncertainties and what you should verify (3.4).

### 3.2 Worked example: Research

Weak:
> What HTS codes are covered by the new tariff on steel products from Country X, and when does it start?

Why it fails: there is no source, so Copilot answers from its training data or a web search that may find a news article; it may invent or mix up codes and dates; and nothing tells you what to check.

Strong:
> **Goal:** list every HTS provision in the notice below, with rate and timing, so I can check each one against the official text.\
> **Context:** I am a trade compliance analyst drafting a Tariff-Impact Brief. I will verify every row myself.\
> **Source:** use only the notice text I paste below. Do not use the web or your own knowledge. If something is not in the text, write NOT IN TEXT.\
> **Expectations:** a table with one row per HTS heading or subheading: the number exactly as written, the product description, countries covered, rate, effective date and time, exclusions, and the sentence or annex line it comes from, quoted. After the table: the total number of HTS entries in the annex, anything ambiguous, and anything you could not read.\
> [PASTE: notice text]

### 3.3 Worked example: Standard Cost

Weak:
> Why is PPV up on PART-A?

Strong:
> **Goal:** a list of possible drivers of the purchase price variance below, so I can test each one against the data.\
> **Context:** fictional numbers. PART-A has a standard landed cost of 10.00 per unit, set on 2026-01-01. Actual landed cost on receipts since June is 11.20 per unit, and 5,000 units were received since June. The PO price has not changed. A reviewed Tariff-Impact Brief says an additional duty on this origin started in May.\
> **Source:** only the facts above.\
> **Expectations:** show the PPV arithmetic step by step. Then rank the possible drivers (duty, freight, exchange rate, unit of measure, data error, other) and, for each, say what data would confirm or rule it out. List your assumptions.

Then check it yourself: (11.20 − 10.00) × 5,000 = 6,000, unfavorable (positive = unfavorable, as in the practice pack; [COMPANY: confirm Finance's sign convention]). Copilot's ranked list is a test plan, not an explanation. The explanation in your PPV workbook comes from the receipts, the entry lines and the brief.

### 3.4 Ask for assumptions, uncertainties and a check list

End most prompts with the lines below. Copilot's check list is only a starting point; your own verification (Part 4) decides.

> List the assumptions you made. Mark anything you are not sure of. Then give me a short list of what I should check, and where, before I rely on this.

### 3.5 Iterate

- **Don't settle for the first answer.** Follow up: "Quote the sentence that supports row 3." "You have 12 rows; the annex has 15. Find the missing ones." "Redo the table using only Annex I."
- **Ask neutrally.** "Is the rate 25%?" invites a yes. "What rate does the text give for this heading?" does not.
- **One chat per task.** Start a new chat for each task and restate the key facts. Long chats drift, and details from an earlier task leak into the next answer. (This is a working habit, not a Microsoft rule.)

### 3.6 Show the output you want

One example row beats a paragraph of description:
> Use exactly these columns, in this order, like this fictional example row: HTS 9903.xx.xx; Products of Country X of heading 7318; Country X; 25%; 2026-11-02 12:01 a.m. ET; none; Annex I, line 4.

### 3.7 Ask it to quiz you

Copilot is a patient quiz partner when you give it the text:
> Quiz me on the text below. Ask one question at a time and wait for my answer. Grade each answer only against the text and quote the sentence that answers it. After 5 questions, list what I got wrong.\
> [PASTE: primer section]

If its grading disagrees with the primer, the primer wins. Log the difference in your question log if you are unsure. More in 4.9.

## 4. Use cases for this job

Each use case has an example prompt and what you must verify. Starter prompts for most of them are in the prompt library (`docs/templates/knowledge/copilot-prompt-library.md`). The paste rules (2.2) and the sandbox rule (2.4) apply every time.

### 4.1 Research: summarize a notice and extract the HTS headings and dates

Good for: a first pass through a long notice or annex, so you know where to look, and a list of provisions to check. Use the strong prompt in 3.2. Upload the PDF from federalregister.gov or paste the CSMS message text.

You must verify:
- Open the official text (the Federal Register document, the HTSUS Chapter 99 provision at hts.usitc.gov, the CSMS message on cbp.gov) and tick every row against it: the number digit by digit, the rate, the date and time, the countries.
- Count the annex entries yourself. Copilot can drop rows from a long list without saying so. Your count must equal the table's.
- Search the document for each quoted sentence. If it is not there word for word, treat the row as invented.
- Stacking, in-transit rules, exclusions and scope are interpretation: yours and the Senior's, from the legal text. Mark each point "confirmed in source", "interpretation" or "open" (`docs/05-time-management.md`, Scenario 1).
- The brief cites the notice, never Copilot (Part 4 of `docs/templates/domain/tariff-impact-brief.md`).

### 4.2 Research: a working translation of a Mexican notice

Good for: a first English reading of a DOF decree or a SAT rule, to find the parts that matter. (Canadian notices are published in English and French, so you rarely need this for Canada.)

> Translate the DOF extract below into English for my working notes. Keep every tariff fraction number, rate and date exactly as in the Spanish text. After each legal term, put the Spanish term in brackets, for example "temporary import [importación temporal]". Then list any sentence where a different translation could change the legal meaning.\
> [PASTE: DOF extract]

You must verify: every number and date against the Spanish original, character by character. The legal meaning comes from the Spanish text, with the Senior. Never cite the translation; the brief cites the DOF decree.

### 4.3 Standard Cost: Excel formulas

> **Goal:** an Excel formula for duty per unit. **Context:** table Items has item_id (text), hts10 (text), country_of_origin and customs_value_per_unit. Table Rates has hts10, country_of_origin, effective_from, effective_to and rate (a decimal: 0.034 means 3.4%). The as-of date is in cell B1. **Expectations:** one formula using SUMIFS or XLOOKUP, an explanation of each argument, what it returns when no rate or two rates match, and three test rows I can check by hand, including one with no rate.

You must verify:
- Hand-check three rows with a calculator before you fill the column down.
- Add a COUNTIFS with the same criteria. It must return 1 on every row: 0 means no rate, 2 means overlapping periods (Exercise 3 in the practice pack).
- HTS codes stay text and rates stay decimals. The duty base follows the brief and the country: the US and Canada use a different duty base from Mexico (customs primer 3.3).
- The total ties to your control total, and the checker reviews the model as usual.

### 4.4 Standard Cost: explaining a variance

Use the strong prompt in 3.3, with fictional or rounded numbers unless the Manager agrees to real ones (2.2). You must verify: recompute the PPV yourself; test every hypothesis against receipts, entry lines and the brief; only tested explanations go into the PPV workbook, which the Manager and [COMPANY: Finance cost accounting contact] review (B60-3).

### 4.5 Standard Cost: drafting an email to Finance

> Draft a short email to a Finance cost accountant saying the reviewed duty impact for the next cost update is ready. Use only these facts and add no numbers: [FILL: number of items; reviewed impact; brief ID; checker and review date; data as of; what is not included]. Under 120 words, plain tone, assumptions as bullets.

You must verify: every number matches the reviewed model; delete anything Copilot added (a softening "approximately", an extra caveat, a deadline nobody agreed); send only after the maker-checker review; in days 1–60, any P1 or P2 date is the Manager's call (`docs/05-time-management.md`, Scenario 2).

### 4.6 Data: SQL, DAX and Power Query M

Good for: explaining a query or measure you inherited; a first draft that you then test; spotting the join or NULL trap.

> Explain this SQL Server query line by line for a new analyst. Then list: every join and whether it can add or drop rows; how NULLs are handled in each filter; any integer division or rounding; and three row-count checks I should run. Do not rewrite the query unless I ask.\
> [PASTE: query, with practice-pack or placeholder table names]

For DAX, ask for the measure and for a SQL query that should return the same number for one filter, so you can tie the two out. For Power Query, paste the M from the Advanced Editor and ask Copilot to flag every step that changes a column type (hts10 turned into a number is the classic).

You must verify:
- Run it only in the sandbox or on the practice data (2.4). Row counts before and after every join; the total ties to the control total.
- Your own line-by-line explanation matches Copilot's. Where they differ, test it.
- DAX: the Power BI value equals the SQL value for the same filter (the tie-out table in Exercise 7).
- Work that is evidence (the practice exercises, the small real analysis, the SSMS lab) is still reviewed by the Senior. Say where Copilot helped.

### 4.7 Custom tools: explaining code for a tool doc

> Explain what this VBA macro does, step by step, for a tool documentation page. List every input it reads, every output it writes, every hard-coded value (paths, dates, rates, sheet names, email addresses) and every place it could fail without an error message. I replaced credentials and server names with [REMOVED].\
> [PASTE: code, only if the policy allows it]

You must verify:
- Before pasting: the policy allows this code, and credentials, connection strings, server names and paths are removed (2.2).
- Run the tool on a test copy (or watch the knowledge holder's run) and compare what it actually does with Copilot's explanation (`docs/templates/knowledge/tool-doc.md`, step 3).
- Search the code yourself for hard-coded values (quoted text, paths, dates, email addresses). Copilot misses some.
- The knowledge holder confirms the facts. Any change Copilot suggests becomes a change request, made in a test copy (2.4).

### 4.8 BSA craft

| Task | Example prompt | You must verify |
|---------|-------------------|-------------------|
| Interview questions | "Draft 12 open questions for a 45-minute interview with a purchasing lead about how they hear about new tariffs today: current process, pain points, data used, what they need from us. No yes/no questions. Mark the 3 most important." | Check them against `docs/primers/business-systems-analysis-primer.md` Section 4 and Part 3 of `docs/templates/bsa/03-process-map-as-is-to-be.md`. Remove leading questions. Add what your stakeholder list says this person cares about |
| User stories | "Turn my requirement notes below into user stories with Given/When/Then acceptance criteria. Use only my notes; where a detail is missing, write OPEN QUESTION." | Every story traces to a line in your notes (BSA primer 5.6). Open questions go back to the stakeholder. Format per `docs/templates/bsa/07-jira-epic-story.md` |
| UAT test cases | "From this acceptance criterion, write one happy-path, two negative and one boundary test case (for example an effective date on the first and the last day). Columns: ID, precondition, steps, test data, expected result." | You compute every expected result yourself from the rule. Test data is fictional or from a test copy. Format per Section 8 of `docs/templates/bsa/05-uat-test-plan.md` |
| Meeting summary | "Summarize my notes below into Decisions, Actions (owner, due date) and Open questions. Use only my notes; write MISSING where an owner or date is missing." | Your own notes are the source (Copilot cannot recap the meeting for you, 1.5); people appear as roles or initials (2.2). If you organized the meeting, send the five-line recap (purpose, decisions, actions, open questions, next meeting) the same day so attendees can correct it (`docs/05-time-management.md`, meeting hygiene) |

### 4.9 Learning

- **Explain a concept:** "Explain the difference between customs value and landed cost to a new analyst, with one worked example using fictional numbers. Then tell me which statements I should check in an official source." Check every statement against the primer (customs primer Section 9; trade systems primer 1.4). Anything you cannot find there goes to your question log, not into your notes.
- **Anki cards:** write the card yourself first, then ask Copilot to critique it: "Check my card below against these rules [PASTE: the quality checklist from the Anki guide] and against the pasted primer text only. Say what is wrong and suggest a better front. Do not add facts that are not in the text." Only cards you write count toward your targets ("Which cards count" in `docs/templates/knowledge/anki-card-writing-guide.md`), and writing the card is half the learning, so Copilot critiques your card; it does not write it. Check every fact against the source in the card's Source field. Company cards follow the paste rules in 2.2.
- **Quiz me:** the prompt in 3.7. Useful before a teach-back and before the day-30 knowledge check (Mon 11/16).

### 4.10 Time management

Friday self-report draft:
> Draft my Friday self-report from my notes below, using these five headings exactly: [PASTE: the five prompts from Section 5 of the check-ins and scorecards page]. Use only my notes. Do not invent hours, ratings, links or outcomes; where a heading has nothing in my notes, write NOTHING IN NOTES. Under 250 words.

You still own it (`docs/03-check-ins-and-scorecards.md` Section 5): every line is true, the hours and the 0–4 ratings are yours (Copilot never rates your skills), the links work, and it is honest about what slipped. Do not let a smooth draft hide a blocker.

- **Question batch for office hours:** "Rank my open questions below as B (blocks a dated deliverable this week), N (needed this week) or L (later). Rewrite each as one clear sentence. Do not answer them." Check the labels yourself (Scenario 3 in `docs/05-time-management.md`), keep "tried so far" true, and send at most 5.
- **Saying "not by then":** paste the request and ask for a reply that follows the five steps in `docs/05-time-management.md` (acknowledge, say what is possible, say what the full ask needs, offer options, confirm). In days 1–60, the Manager agrees the options and dates before you send it.

### 4.11 How this applies to our work

| Area | Good uses | Never |
|---|-----------------|---------------|
| Research (M5R) | Provision tables from pasted notices; working translations; formulas or a script to compare old and new HTS lists, run on extracts; a first draft of the brief's Part 2 summary from your verified table | Decide scope, rates or dates; cite Copilot; work from a news summary |
| Standard Cost (M5C) | Formulas; variance hypotheses; first drafts of Finance emails; explaining a checklist step | Decide which items are in scope; send unreviewed numbers; anything that loads to Oracle |
| Owned tool (M6) | Explaining code for the tool doc; drafting test cases and rollback steps for a change request, for the Manager to review | Run changed code on production; paste credentials |
| e2open (M10) | Turning your interview notes into as-is step tables; drafting data-map transformation rules and UAT cases from your own notes | Paste vendor project documents without the Manager's approval; guess e2open target fields (trade systems primer 6.1) |

## 5. What it gets wrong

Microsoft warns that even when it is given sources, Copilot "may produce ungrounded results" (as of Oct 2026; check the transparency note linked in 2.3). In trade work, expect these patterns.

### 5.1 Invented citations

Copilot can cite a Federal Register document, a CSMS message number, a CFR section or a CROSS ruling that does not exist, or a real one that says something else. A citation shows where Copilot looked, or says it looked; it does not prove the claim. Open every cited source yourself (federalregister.gov, cbp.gov, ecfr.gov, rulings.cbp.gov) and find the sentence.

### 5.2 Invented or wrong HTS codes

Typical errors: a 10-digit number in the right format that is not in the HTSUS; a real number for a different product; a Canadian or Mexican tariff line given as a US one; a code that was valid before a schedule change; the right 6 digits with the wrong national line. Classification uses the GRIs, the schedule and its notes, and rulings, with maker-checker (customs primer Section 8). Never take a code from Copilot, and never let it "confirm" one.

### 5.3 Stale tariff status

A model's training data stops at some date, and a web search can bring back a news article or an outdated page instead of the notice. Tariff actions in all three countries changed many times in 2025 and 2026. Copilot may, for example, describe the 2025 IEEPA tariffs without knowing what happened to them in 2026 (US-1 in `docs/primers/current-tariff-landscape.md`). Current status lives only in that document, and every brief cites the primary source with the date you checked it.

### 5.4 Arithmetic slips

Watch for: percent versus percentage points (a rate that goes from 5% to 30% is up 25 points, not 25%); annualizing nine months (× 12 / 9); rates as decimals (0.034 is 3.4%); a total over a column it silently cut short; rounding each line before summing. When a number matters, recompute it in Excel or SQL and reconcile it to a control total. If Copilot ran code on an uploaded file, it shows that code: read it, but still recompute the number you report. [COMPANY: test once with fictional data whether Copilot Chat runs code on an uploaded workbook for us]

### 5.5 SQL that runs but answers a different question

The dangerous query is the one that runs without an error. Copilot can produce every trap in the practice pack:

| Trap | What the query does | How you catch it |
|---------------|-----------------|-----------------|
| INNER JOIN where you needed LEFT | Drops entry lines whose item is not in the master, so the totals shrink | Row count before and after the join; orphans counted (Exercise 1) |
| Rate join without the date condition | Each line matches several rate periods, so the duty multiplies | The row count after the join must equal the scope (Exercise 3) |
| `program_claimed <> 'USMCA'` | Silently drops the NULL rows | Count `IS NULL` rows separately |
| Average of line rates | A different rate from total duty divided by total value | Use `SUM(duty) / SUM(value)` |
| `12 / 9` in T-SQL | Integer division returns 1 | Write `12.0 / 9` |
| A similar-sounding column | Uses the supplier's country instead of the item's country of origin | Check every column name against the data dictionary or the tool doc |

### 5.6 Other patterns

- **It agrees with you.** A leading question gets a yes. Ask neutrally, and ask "what would make this wrong?".
- **It drops rows from long lists** without saying so (4.1). Count.
- **It mixes countries,** applying a US rule to Canada or Mexico (for example the FOB-like US duty base to a Mexican import, whose base is CIF-like; customs primer 3.3). Put the country first in the prompt and check each country separately.
- **It sounds sure.** Its tone tells you nothing about accuracy.
- **It fills gaps.** Ask for MISSING or OPEN QUESTION markers instead of invented details (4.8).

### 5.7 How this applies to our work

The cost of each failure depends on where it lands. An invented HTS code in a brief can reach a broker and a filing. An arithmetic slip in a cost input reaches Oracle standard cost and the margin reports. A fan-out in a query (a join that multiplies rows, 5.5) overstates a tariff exposure that the business will act on. That is why maker-checker review covers Copilot-assisted work exactly like any other work.

## 6. The use log and the team prompt library

### 6.1 The use log

Keep one page, "Copilot use log", in your own OneNote section. Put your tenant answers from 1.6 at the top. Add one row per use on a work task, whether you used the output or rejected it.

| Date and task (Jira key) | Prompt (text, without the pasted data) | Output used for | Verified: what and how | Outcome and time saved | Reviewed (initials, date) |
|---|---|---|---|---|---|
| | | | | | |

Rules:
- Copy the prompt text, not the data you pasted with it. If you used a library prompt, give its ID.
- "Verified" names the source and the check, for example "14 rows ticked against Annex I of the notice; annex count 14 = 14", not "checked".
- "Outcome" says used, partly used or rejected, and a rough time saved (or lost). Honest numbers are worth more than big ones.
- The reviewer is the Manager (W4 review) or the checker of the work the use fed.

### 6.2 Example entries (fictional)

| Date and task (Jira key) | Prompt (text, without the pasted data) | Output used for | Verified: what and how | Outcome and time saved | Reviewed (initials, date) |
|---|---|---|---|---|---|
| 11/03, [KEY] practice brief on a fictional action | Library CP-01 (provisions table from a pasted notice) | List of provisions to check for brief Parts 5 to 7 | Every row ticked against the notice PDF. The annex had 16 entries and the table 14: 2 added by hand, 1 date corrected | Partly used; about 30 minutes saved | |
| 11/06, Friday self-report | Library CP-14 (self-report draft from my notes) | First draft of the self-report | Each line checked against my notes and Jira; hours and ratings rewritten by me | Used after edits; about 10 minutes saved | |

### 6.3 Sessions, reviews and milestone evidence

| When | What | Who | Evidence |
|---|-------------------|---------|-------------|
| W1 | Setup and rules session (30 minutes): the policy, Parts 1 and 2, the tenant answers, one prompt checked live against its source | Manager, both hires | Setup checklist (1.6) ticked |
| W2 onward | Use Copilot where it helps; log every use | Each hire | Use log entries |
| W4 | Use-log review (15 minutes for both hires). Each hire flags the 5 entries they want reviewed. The Manager reads them with the hire, marks those with a real check as reviewed, and asks two self-check questions | Manager | Entries with initials and date |
| Day 30 | Should criterion: 5 reviewed uses (prompt, output, what was verified, outcome) | Each hire | Log link in the day-30 scorecard (`docs/03-check-ins-and-scorecards.md`) |
| By day 60 | Propose at least one prompt library entry (a target, not a criterion) | Each hire | Library entry with status Proposed |
| Day 90 | Should criterion: 3 entries in the team prompt library, each reviewed by the Manager (entries you added; the starter set does not count) | Each hire; the Manager reviews in work review time | Library entries with status Reviewed |

Only Must criteria decide the milestone outcome (`docs/01-30-60-90-plan.md` Section 4); the Should criteria above are tracked in the scorecard. The criterion IDs are in Section 4 of the plan.

### 6.4 The team prompt library

The library holds prompts that have worked here, each with the check that must follow it. The template is `docs/templates/knowledge/copilot-prompt-library.md`; the live copy is a page in the team OneNote section ([COMPANY: team OneNote section for the prompt library]).

To propose an entry: use the prompt at least twice with a good, verified result (both in your log); make it generic (placeholders, no company names or data); write a Verify step that names the source and the check; add it with status Proposed and tell the Manager. The Manager reviews it in work review time and marks it Reviewed or sends it back. The library page has the full steps and a quality checklist. If allowed, also save reviewed prompts in the Copilot Prompt Gallery ("Your Prompts", or shared with the team in Teams) so they are one click away (as of Oct 2026; check https://learn.microsoft.com/en-us/copilot/microsoft-365/copilot-prompt-gallery) [COMPANY: confirm sharing prompts to a team is allowed]. The OneNote library stays the master, because the Verify step lives there.

## 7. Self-check questions

| No. | Question | Where to check |
|---|-------------------------|---|
| 1 | Which Copilot does this guide cover, and how do you check which experience you have? | 1.1 |
| 2 | Name four things Copilot Chat cannot see here, and the exception that is rolling out. | 1.3 |
| 3 | What does enterprise data protection promise, and name three things it does not mean. | 1.4 |
| 4 | Why should a prompt that may trigger a web search not contain a supplier's name and price? | 1.4 |
| 5 | Name three features you should not plan on with the free tier, and what you do instead of each. | 1.5 |
| 6 | Give two examples each of data you may paste, data you ask the Manager about first, and data you never paste. | 2.2 |
| 7 | You find a password in a VBA module you want Copilot to explain. What do you do? | 2.2, 4.7 |
| 8 | Why can you never cite Copilot in a Tariff-Impact Brief, and what do you cite instead? | 2.3, 5.1 |
| 9 | You need a new query on Oracle EBS, and Copilot offers to write it. What are the rules? | 2.4 |
| 10 | Rewrite a weak prompt of your own using goal, context, source and expectations, plus the checks. | 3.1 to 3.4 |
| 11 | Copilot gives you 12 HTS rows from an annex. Which three checks do you run before you use any of them? | 4.1, 5.2 |
| 12 | Hire B wants to ask Copilot which of our items a new action covers. What is wrong with that? | 2.3, 4.11 |
| 13 | Name four ways a Copilot-written SQL query can run without an error and still give the wrong answer. | 5.5 |
| 14 | Copilot drafted your Friday self-report. What must you check before you post it? | 4.10 |
| 15 | What are the six fields of a use log entry, and what makes a "Verified" entry good enough to be reviewed? | 6.1 |
| 16 | What are the day-30 and day-90 Copilot criteria, and are they Must or Should? | 6.3 |

## 8. Sources and related documents

Every Microsoft fact in this guide carries its own link, dated as of Oct 2026. Open the link before you rely on a fact, and tell the Manager when something has changed so this page can be updated.

Repo documents:

- `docs/templates/knowledge/copilot-prompt-library.md`: the team prompt library template.
- `docs/primers/data-platform-primer.md`: the safe-use rules for the team database, EBS and Power Platform (Part 1).
- `docs/primers/business-systems-analysis-primer.md`: elicitation and requirements, for the BSA craft uses in 4.8.
- `docs/primers/current-tariff-landscape.md`: the only place current tariff status is stated.
- `docs/analytics/practice-exercises.md`: the SQL habits and traps behind 2.4 and 5.5.
- `docs/05-time-management.md` and `docs/03-check-ins-and-scorecards.md`: the self-report, question log and "not by then" methods in 4.10.
