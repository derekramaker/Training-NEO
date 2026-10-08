# Customs and Trade Compliance Primer: US, Canada and Mexico

Last updated: 2026-10-08 · Owner: BSA Manager

- **Purpose:** the self-study backbone for M1 (customs and trade compliance fundamentals). It explains how imports into the United States, Canada and Mexico are declared, classified, valued, qualified for USMCA, corrected and audited, and where our team's data drives each step. It is training material, not legal advice.
- **Who uses it:** Hire A and Hire B for self-study in W1 to W5 (about 8 hours of focused reading and exercises). The Senior uses it as the source for the M1 sessions and the day-30 knowledge check. The Manager uses Section 16 for the oral part of the day-30 review.
- **When:** follow the study plan below. Re-read Section 12 before taking exports backlog items (W6), Section 11 before the drawback shadow (W12), and Section 14 before drafting your e2open data map (W10 to W13).

## How to use this primer

| Session | When (see `docs/02-weeks-1-2-schedule.md`) | Sections | Focused time | Output |
|---|---|---|---|---|
| 1 | W1 Tue 10/20, 08:30 | 1 to 4: why it matters, roles, the three countries side by side, US imports | 1.5 h | 10+ new terms and 3+ questions in your question log |
| 2 | W1 Thu 10/22 (pre-read for the Senior's Friday session) | Skim 8, 9 and 10: classification, valuation, origin and marking | 0.75 h | Questions for the session |
| 3 | W2 Mon 10/26, 08:30 | 5: Canada imports | 0.75 h | Canada questions in the question log |
| 4 | W2 Mon 10/26, 13:00 | 6 and 11.1: Mexico imports and IMMEX | 0.75 h | Mexico questions; start your own US/CA/MX comparison |
| 5 | W2 Wed 10/28, 08:30 | 8 in full, then Exercise 1 | 1.25 h | 5-item classification worksheet |
| 6 | W3 | 9 and 10 in full, then Exercise 2 (BOM) | 1.5 h | Valuation rebuild and BOM qualification worksheet |
| 7 | W4 | 7, 11.2 and 13: auditing broker filings, drawback, penalties and corrections | 0.75 h | Broker-audit notes for the Senior's W5 hands-on session |
| 8 | W4, by Fri 11/13 (before the knowledge check on Mon 11/16) | 12 (exports), 14 to 16 (what a BSA touches, self-check) | 0.75 h | Self-check answers; 10 Anki cards; questions for the Senior's exports overview |

The schedule slots are longer than the focused time above because they include notes, Anki cards and the question log.

Tailoring:

- **Hire A (Research):** parts of Section 10 (USMCA) may be review. If you pass the 15-minute oral USMCA test-out with the Senior (Wed 10/28: self-check questions 14 to 18 in Section 16, without notes; 4 of 5 is a pass), skim 10.2 to 10.5 and spend the saved time on 10.6 (sets and kits), 10.9 (supplier solicitation) and the sources in `docs/primers/current-tariff-landscape.md`.
- **Hire B (Standard Cost):** Sections 4.3, 5.3, 6.3 (duties and taxes) and 9 (valuation) are the inputs to landed cost. Rebuild the worked examples in Excel and keep the file for M5C.

Rules for using this primer:

1. **Verify before you rely.** Every regulatory statement here points to a primary source in Section 17. Where the text says "(verify)", the point could not be confirmed against the official text when this primer was written; check it before using it in real work.
2. **Never quote a rate, threshold or the status of a tariff action from memory or from this primer.** Those change. Use `docs/primers/current-tariff-landscape.md` and record the date you checked.
3. **[COMPANY: ...] marks a company fact** that the Manager or Senior must confirm. Do not guess one.
4. **Log every question** in your question log (`docs/05-time-management.md`) after 15 minutes of looking. Definitions are in `data/trackers/glossary.csv`.
5. **Broker and counsel questions go through the Senior.** Before the day-60 review you never contact a customs broker, agente aduanal or trade counsel directly; send the question to the Senior (or the Manager). After day 60, with the Senior's agreement, you may email the broker with the Senior copied. Wherever this primer says "confirm with [COMPANY: broker or counsel]", that is how.

## 1. Why trade compliance matters to a BSA

Every customs declaration is built from data: the tariff classification, the value, the country of origin, any preference claim (such as USMCA), the quantity and unit of measure, the manufacturer, and data for other agencies. Our team maintains much of that data and the tools around it [COMPANY: confirm which elements the team owns], and we audit what the brokers file. If our data is wrong, the filing is wrong, even though a licensed broker transmitted it.

### The broker files; the importer is responsible

| Country | Who files | Who is responsible | What it means for us |
|---|---|---|---|
| United States | A CBP-licensed customs broker, using our data | The importer of record (IOR). It must use **reasonable care** to enter, classify and value goods (19 U.S.C. 1484). Duties are the importer's personal debt to the US (19 CFR 141.1) | Relying blindly on the broker is not reasonable care. We must be able to show how each classification, value and origin was decided |
| Canada | A CBSA-licensed customs broker, using our data | The importer. If it has "reason to believe" an origin, classification or value-for-duty declaration is wrong, it must correct it and pay any duties owed within 90 days (Customs Act s. 32.2) | Errors we find start a legal clock. Escalate the same day |
| Mexico | An agente aduanal (or agencia aduanal), using our data | The importer remains responsible for classification and taxes even when it uses a broker. The 2026 Ley Aduanera reform (DOF 19 Nov 2025, in force 1 Jan 2026) also tightened the brokers' own obligations | The broker's tighter checks are not a substitute for our controls. The Senior confirms with [COMPANY: Mexico broker or counsel] how the reform changed our process |

### What reasonable care looks like in our team

These are the habits CBP, CBSA and ANAM/SAT expect an importer to be able to show. Each one is also a data or process control a BSA can build or check.

- A written classification rationale for each item and country: the heading, the rule applied, notes and rulings cited, who decided and who checked, and when.
- Tariff research with primary sources (Federal Register, CBP CSMS, DOF, CBSA customs notices), not news articles.
- Origin support on file **before** a USMCA claim is made: a valid certification and the BOM or supplier evidence behind it.
- Regular reconciliation of what the broker filed against our master data (Section 7).
- Controlled changes to trade master data: who may change an HTS code or origin, with maker-checker review (`docs/templates/bsa/06-change-request.md`).
- Records kept for the required period (Section 3.4) and retrievable within days, not weeks.
- Fast escalation of errors, so the right correction route is still open (Section 13).

### What wrong data costs

| Wrong data | Immediate effect | Later effect |
|---|---|---|
| Classification | Wrong duty rate; other-agency data not filed; additional duties missed or wrongly applied | Duty bills, penalties, held shipments, wrong standard cost |
| Value | Duty and fees under- or overpaid | Penalty exposure (US 19 U.S.C. 1592, Canada AMPS, Mexico fines) |
| Origin or preference claim | Preference claimed without support, or savings missed | Claims denied in a verification; duties plus interest; penalties |
| Duty rate in cost data | Wrong standard cost and margin | Inventory revaluation and PPV noise that Finance cannot explain |

Both tracks depend on this. Research (Hire A) decides the WHAT of a tariff action: scope, HTS codes, origins, rates, dates and stacking. Standard Cost (Hire B) turns it into the $: landed cost, margin and the Oracle cost update. Both are only as good as the classification, value and origin data underneath.

## 2. Who does what

| Role | United States | Canada | Mexico | Responsible for |
|---|---|---|---|---|
| Customs authority | U.S. Customs and Border Protection (CBP), part of DHS | Canada Border Services Agency (CBSA) | Agencia Nacional de Aduanas de México (ANAM) since 2022 for customs; SAT stays the tax authority (RFC, the Registro Federal de Contribuyentes tax ID; e.firma; padrón de importadores) | Release goods, assess and collect duties and taxes, verify and audit, penalize |
| Importer | Importer of record (IOR) | Importer, identified by its Business Number and import-export (RM) account | Importer registered in the padrón de importadores with an active RFC | Accurate declarations, payment, records, corrections |
| Customs broker | Licensed customs broker (19 CFR Part 111) | Licensed customs broker | Agente aduanal holding a patente, or an agencia aduanal | Prepares and transmits declarations on our behalf, using our data |
| Other agencies | Partner Government Agencies (PGAs), for example FDA, USDA, EPA, CPSC | Other government departments, for example CFIA, Health Canada, Global Affairs Canada (permits) | Secretaría de Economía (permits, quotas), COFEPRIS, SENASICA; product labeling under NOMs (Normas Oficiales Mexicanas) | Product admissibility, permits, labeling |
| Carrier or forwarder | Manifest data; ocean carriers file part of the ISF | eManifest advance data | Transport documents and manifest data | Getting the goods and the advance data to the border |
| Supplier or producer | Commercial invoice, packing list | Commercial invoice | Commercial invoice, data for the value declaration | Price, description, origin information, USMCA certifications |
| Our team | Data owner and auditor [COMPANY: confirm scope] | Same | Same | Classification, origin and qualification data; tariff research; landed cost; audits of broker filings |

## 3. The three countries side by side

Use these tables as a quick reference. Sections 4 to 6 explain each country.

### 3.1 Agencies, parties and registration

| Topic | United States | Canada | Mexico |
|---|---|---|---|
| Customs agency | CBP | CBSA | ANAM (customs operations) with SAT (tax administration) |
| Who files | Licensed broker through ABI, the Automated Broker Interface (or an importer that self-files) | Licensed broker (or the importer itself) through CBSA's electronic channels and CARM (CBSA Assessment and Revenue Management) | Generally an agente aduanal or agencia aduanal |
| Importer registration | IOR number (IRS EIN or CBP-assigned number, set up on CBP Form 5106) | 9-digit Business Number plus an import-export (RM) program account (BN15), both issued by the Canada Revenue Agency (CRA); the importer then registers in the CARM Client Portal | RFC, active registration in the padrón de importadores (plus a padrón sectorial for listed goods), e.firma, and an electronic authorization naming the agente aduanal (encargo conferido) |
| Financial guarantee | Customs bond: single transaction or continuous | Financial security the importer posts in CARM to use release prior to payment (RPP) | No general bond; guarantees apply in specific situations (the Senior confirms which apply to us with [COMPANY: Mexico broker]) |
| Importer's portal | ACE (Automated Commercial Environment) Portal: account management, reports on our own entries | CARM Client Portal (account, broker delegation, statements, declarations) | The foreign-trade single window for permits and digitized documents: the Ventanilla Única de Trámites de Comercio Exterior (VUTCE), run by the ATDT under a decree of 4 May 2026. It replaced the SAT-run VUCEM (Ventanilla Única de Comercio Exterior Mexicana), a name the trade still uses. SAT portal for padrón matters |
| Where the rules live | 19 CFR, CBP Informed Compliance Publications, CSMS messages | Customs Act, regulations, D-Memoranda, Customs Notices | Ley Aduanera and its Reglamento, the annual Reglas Generales de Comercio Exterior (RGCE) and their annexes, published in the DOF |

### 3.2 Declarations and tariff schedules

| Topic | United States | Canada | Mexico |
|---|---|---|---|
| Release filing | Entry (CBP Form 3461 data) | Release request on minimum documentation (for RPP importers), or a CAD paid at release | The pedimento, paid before release, then the automated selection ("semáforo") |
| Accounting declaration | Entry summary (CBP Form 7501 data), due within 10 working days of release | Commercial Accounting Declaration (CAD). For RPP releases, due within 5 business days of release | The pedimento itself: one declaration with classification, value, origin, regime and taxes |
| Tariff schedule | Harmonized Tariff Schedule of the United States (HTSUS), published by the USITC | Customs Tariff schedule; CBSA publishes a departmental consolidation, updated each 1 January and on amendments | TIGIE, the tariff inside the LIGIE (Ley de los Impuestos Generales de Importación y de Exportación); changes are published in the DOF (Diario Oficial de la Federación) |
| Code length | 10 digits: 8-digit tariff line (sets the rate) + 2-digit statistical suffix | 10 digits: 8-digit tariff item (sets the rate) + 2-digit statistical suffix | 10 digits: 8-digit fracción arancelaria (sets the rate) + 2-digit NICO |
| Rates and preferences | Column 1 General (normal trade relations), Column 1 Special (program codes such as USMCA), Column 2 | Tariff treatments, for example MFN (most-favoured-nation) and the CUSMA treatments | IGI (Impuesto General de Importación) rate per fracción; T-MEC preference where claimed |
| Additional duties | HTSUS Chapter 99 measures, antidumping and countervailing duties (AD/CVD) | Surtax orders; AD/CVD under the Special Import Measures Act (SIMA) | Cuotas compensatorias (Mexico's AD/CVD) and other measures by decree |

Additional duties are the most time-sensitive part of any tariff. Their current status is in `docs/primers/current-tariff-landscape.md`.

### 3.3 Money: duty base, taxes, fees, currency and payment

| Topic | United States | Canada | Mexico |
|---|---|---|---|
| Duty base | Transaction value; international freight and insurance are excluded when identified separately (FOB-like) | Value for duty; transport and insurance after the place of direct shipment to Canada are excluded (FOB-like) | Valor en aduana; includes freight, insurance and related charges until the goods arrive in Mexico (CIF-like) (Ley Aduanera arts. 64, 65 and 56) |
| Import taxes | No federal VAT or GST on imports | GST (5% federal rate at the time of writing) on value for duty plus duties, collected by CBSA; registrants may have to self-assess the provincial part of HST; registrants generally recover GST as an input tax credit | IVA (16% general rate at the time of writing) on valor en aduana plus IGI and other import charges (Ley del IVA art. 27); generally creditable. IEPS (Impuesto Especial sobre Producción y Servicios, an excise tax) on specific goods |
| Customs fees | Merchandise Processing Fee (MPF): ad valorem on formal entries, with a per-entry minimum and maximum; a small flat fee on informal entries. Harbor Maintenance Fee (HMF) on imported vessel cargo only. USMCA-originating goods properly claimed are exempt from MPF | No US-style merchandise processing fee (verify); excise duties, excise taxes or surtaxes are added only for goods subject to them | Derecho de Trámite Aduanero (DTA) and other charges on the pedimento |
| Currency conversion | Rate certified by the Federal Reserve Bank of New York (or CBP's quarterly rate) for the date of exportation (19 CFR 159.32 and 152.1(c)) | Bank of Canada rate on the date of direct shipment to Canada (Memorandum D13-2-3) | Peso-dollar rate in force on the date of entry (art. 56) or the payment date in the cases of art. 83, declared on the pedimento (RGCE Anexo 22) |
| When duties are paid | With the entry summary, or monthly through the Periodic Monthly Statement (PMS) | Monthly statement of account in CARM for RPP importers; at release otherwise | When the pedimento is paid, before the goods are presented |

Fee amounts and tax rates change. Take them from `docs/primers/current-tariff-landscape.md` and the official sources, with the date checked.

### 3.4 Records, rulings, corrections and penalties

| Topic | United States | Canada | Mexico |
|---|---|---|---|
| Record retention | 5 years from the date of entry (19 CFR 163.4); drawback records longer | 6 years (Imported Goods Records Regulations; Memorandum D17-1-21) | 5 years (Código Fiscal de la Federación art. 30) for the electronic file of each pedimento (Ley Aduanera art. 59); longer when tax effects continue |
| USMCA origin records | At least 5 years after importation (USMCA Art. 5.8); national law can require longer | Same, but Canada's 6-year rule is longer | Same |
| Binding advice | CBP rulings under 19 CFR Part 177, searchable in CROSS | Advance rulings on classification (D11-11-3); origin advance rulings under FTAs (D11-4-16); National Customs Rulings for non-preferential origin, value and marking (D11-11-1) | Classification consultation before the operation (Ley Aduanera art. 47); Consejo de Clasificación Arancelaria opinions published as criteria (RGCE Anexo 6); T-MEC origin rulings |
| Correcting before final | Post Summary Correction (PSC): within 300 days of entry and at least 15 days before scheduled liquidation | Correct within 90 days of "reason to believe" (s. 32.2); corrections and adjustments are new versions of the CAD | Rectificación of the pedimento (Ley Aduanera art. 89); some cases need prior authorization |
| Challenging a decision | Protest within 180 days of liquidation (19 U.S.C. 1514) | Request a re-determination with CBSA, then appeal to the Canadian International Trade Tribunal (verify current time limits) | Administrative appeal (recurso de revocación) or a lawsuit before the federal administrative court, the Tribunal Federal de Justicia Administrativa (TFJA) |
| Penalty regime | 19 U.S.C. 1592 (negligence, gross negligence, fraud); prior disclosure reduces penalties | Administrative Monetary Penalty System (AMPS); seizures in serious cases | Infractions and fines in the Ley Aduanera, plus omitted taxes with inflation updates (actualización) and surcharges (recargos) |

## 4. United States imports

### 4.1 Players and registrations

- **Importer of record (IOR):** the owner or purchaser of the goods, or a licensed broker designated by them (19 U.S.C. 1484). For us: [COMPANY: legal entity that acts as IOR, and its IOR number owner].
- **Customs broker:** acts under a customs power of attorney from the IOR. [COMPANY: US broker(s)].
- **Bond:** guarantees duties, taxes, fees and penalties. A continuous bond covers all entries for a year. [COMPANY: bond type].
- **ACE Portal:** where the importer manages its account and runs reports on its own entries. Ask the Senior which ACE reports the team uses for audits [COMPANY: ACE report names and who holds portal access].

### 4.2 The life of a US entry

| Stage | What happens | Who | Our data or action | Timing |
|---|---|---|---|---|
| 1. Pre-arrival | Purchase order, commercial invoice and packing list are produced. For ocean cargo the Importer Security Filing (ISF, "10+2") is filed. Some PGAs need advance data | Supplier, forwarder, broker or ISF filer | Item data, HTS (6 digits on the ISF), manufacturer, country of origin | ISF at least 24 hours before loading at the foreign port |
| 2. Entry (release) | Broker files entry data (CBP Form 3461) and PGA data in ACE. CBP may hold or examine, then releases | Broker, CBP, PGAs | Classification, value, origin, PGA data | Generally within 15 calendar days of arrival (19 CFR 142.2) |
| 3. Entry summary | Broker files CBP Form 7501 data: HTS per line, value, origin, special program indicator (SPI), manufacturer ID (MID), duties and fees. Often filed together with the entry | Broker | Everything in Section 7.1 | Within 10 working days of release (19 CFR 142.12) |
| 4. Payment | Estimated duties and fees are deposited, per entry or monthly through the PMS | Broker or importer | [COMPANY: who pays, and how broker invoices reach AP] | With the summary, or by the PMS due date |
| 5. Before liquidation | Errors are fixed by Post Summary Correction. CBP may send a Request for Information (CBP Form 28) or a Notice of Action (CBP Form 29) | Broker, CBP, us | Pull the data and documents CBP asks for; the Senior leads the response | PSC: within 300 days of entry and 15+ days before scheduled liquidation |
| 6. Liquidation | CBP's final computation of duties. It results in a bill, a refund or no change | CBP | Monitor liquidations; actual duty feeds PPV and drawback | ACE schedules it about 314 days after entry; statutory limit 1 year, extendable to 4 (19 U.S.C. 1504) |
| 7. After liquidation | Protest to challenge a decision. Prior disclosure for a possible 1592 violation | Importer (Senior, counsel) | Evidence for the protest or disclosure | Protest: 180 days from liquidation |
| 8. Audit and records | CBP can audit (for example a Focused Assessment) and must be able to get records on request | CBP, us | Records for 5 years from entry | Ongoing |

### 4.3 US duties, taxes and fees

- **Duty types:** ad valorem (percent of value), specific (amount per unit, such as per kg) and compound (both). Specific duties need the right quantity and unit of measure.
- **Rate columns:** Column 1 General is the normal-trade-relations rate. Column 1 Special lists preference rates with program codes; "S" marks USMCA. Column 2 applies to the few countries without normal trade relations.
- **Preference claim:** the entry summary line carries an SPI, for example "S" for USMCA ("S+" is used only for certain agricultural goods and textile goods under tariff preference levels; see the CBP USMCA FAQs). A wrong or missing SPI changes the duty paid.
- **HTSUS Chapter 98:** special provisions, such as US goods returned or assembled abroad, that can reduce duty when their conditions are met.
- **HTSUS Chapter 99:** temporary and additional duties (for example Section 232 and Section 301 measures). A Chapter 99 number is reported **in addition to** the Chapter 1 to 97 classification, never instead of it. Which actions are in force, and how they stack, is a Research question: see `docs/primers/current-tariff-landscape.md`.
- **AD/CVD:** antidumping and countervailing duties on specific products from specific countries, often by manufacturer. Scope is decided by the written scope of the order, not by the HTS number, which is listed for convenience.
- **MPF and HMF:** MPF is charged ad valorem on formal entries with a per-entry minimum and maximum that change each fiscal year; informal entries pay a small flat MPF instead (19 CFR 24.23). Originating goods properly claimed under USMCA are exempt. HMF applies to imported cargo unloaded from vessels at covered seaports, not to air, truck or rail, and not to exports (the Supreme Court struck it down for exports in United States v. United States Shoe Corp., 1998). Current amounts: `docs/primers/current-tariff-landscape.md`.
- **No federal VAT:** the US has no federal VAT or GST at import. State sales and use taxes are not collected at the border.
- **Informal and low-value entries:** informal entry is generally available for shipments of US$2,500 or less (19 CFR 143.21), with exceptions. One exception matters for tariff modeling: articles valued over US$250 that are classified in HTSUS Chapter 99, Subchapters III and IV, where additional duties such as Sections 232 and 301 are reported, cannot use informal entry (19 CFR 143.21(a)). CBP confirmed in March 2025 that this covers goods reported under heading 9903, so most tariffed shipments over US$250 need a formal entry. The low-value "de minimis" treatment (Section 321) changed repeatedly in 2025; its status is time-sensitive (see the landscape doc).

Worked example (hypothetical rates, for the method only). One entry line, entered value US$10,000.

| Item | Rate (hypothetical) | Amount (US$) | Note |
|---|---|---|---|
| Base duty (Column 1 General) | 3.5% | 350.00 | 10,000 x 3.5% |
| Additional duty (Chapter 99) | 25% | 2,500.00 | Applies only if the Research brief says the action covers this item and stacks |
| Total duty |  | 2,850.00 | Effective duty rate 28.5% |
| MPF | Current rate, minimum and maximum | from the landscape doc | Not due if the line is a valid USMCA claim |
| HMF | Current rate | from the landscape doc | Ocean shipments only |

### 4.4 When CBP asks questions

A CBP Form 28 (Request for Information) asks for documents or explanations about an entry. A CBP Form 29 (Notice of Action) tells the importer that CBP proposes to change, or has changed, the entry, for example its classification or value. Both have response dates. If one reaches you: tell the Senior the same day, pull the data asked for, and do not answer CBP or the broker yourself unless the Senior asks you to.

## 5. Canada imports

### 5.1 Players and registrations

- **CBSA** releases goods, assesses and collects duties and taxes, and verifies compliance.
- **Importer:** identified by its BN15 (the 9-digit Business Number plus the import-export (RM) program account, both issued by the Canada Revenue Agency), and registered in the CARM Client Portal. [COMPANY: Canadian importer entity and BN15 owner].
- **Customs broker:** acts for the importer once the importer delegates access in the CARM Client Portal. [COMPANY: Canada broker(s)].
- **CARM** (CBSA Assessment and Revenue Management) has been the system of record for assessing and collecting duties and taxes on commercial imports since 21 October 2024. The Commercial Accounting Declaration (CAD) replaced the B3.
- **Release prior to payment (RPP):** importers that enrol and post their own financial security get goods released before paying, and pay through a monthly statement. Since the end of the CARM transition period in May 2025, importers cannot rely on their broker's security.

### 5.2 The life of a Canadian import

| Stage | What happens | Who | Our data or action | Timing |
|---|---|---|---|---|
| 1. Pre-arrival | Carriers and forwarders send advance commercial information (eManifest). Permits from other departments are obtained if needed | Carrier, forwarder, broker | Item data for the broker | Before arrival |
| 2. Release | For RPP importers, the broker transmits a release request on minimum documentation. CBSA may examine, then releases | Broker, CBSA | Classification, value, origin | At the border |
| 3. Accounting | The broker submits the CAD: classification, value for duty, origin, tariff treatment (for example a CUSMA treatment), duties and GST | Broker | Everything in Section 7.1 | RPP releases: CAD accepted within 5 business days of release (release day is day 0). Non-RPP: CAD and payment at release |
| 4. Payment | Amounts post to the importer's monthly statement of account in CARM | Importer | [COMPANY: who pays and reconciles the statement] | By the payment due date on the CBSA calendar |
| 5. Corrections | Changes before the payment due date are corrections; changes after it are adjustments, made as new versions of the CAD. An importer with reason to believe an origin, classification or value declaration is wrong must correct it within 90 days (s. 32.2) | Broker, importer | Find errors early; escalate the same day | 90 days from reason to believe |
| 6. Verification and audit | CBSA trade compliance verifications (classification, valuation, origin) and CUSMA origin verifications | CBSA, us | Records for 6 years | Ongoing |
| 7. Review and appeal | The importer can request a re-determination of a CBSA decision, then appeal to the Canadian International Trade Tribunal (verify time limits in the Customs Act) | Importer (Senior, counsel) | Evidence | Statutory time limits |

### 5.3 Canadian duties and taxes

- **Customs duty** = value for duty x the rate for the tariff item and tariff treatment (MFN, a CUSMA treatment, or others). Surtaxes and SIMA duties are added where they apply (time-sensitive: see the landscape doc).
- **GST** is charged on the value for duty plus duties and other taxes (except GST). CBSA collects the federal GST at the border; for commercial goods brought into a participating province, a registrant may have to self-assess the provincial part of the HST on its GST/HST return. Registrants generally recover GST as an input tax credit, so it is usually not part of item cost [COMPANY: confirm the treatment with Finance].
- **Value for duty** includes transport and insurance up to the place of direct shipment to Canada and excludes them after that point.

Worked example (hypothetical rate), continuing Section 9.7. Value for duty US$11,000 equivalent; duty rate 6.5%. Amounts are kept in US$ to match Section 9.7; in real life everything is in CAD.

| Item | Amount (US$ equivalent) | Note |
|---|---|---|
| Value for duty | 11,000.00 | From Section 9.7; the broker converts to CAD at the Bank of Canada rate for the date of direct shipment (D13-2-3) |
| Duty at 6.5% | 715.00 | 11,000 x 6.5% |
| Value for GST | 11,715.00 | Value for duty + duty |
| GST at 5% | 585.75 | Usually recoverable; check with Finance |

### 5.4 What is different from the US

- One accounting declaration (the CAD) replaces the entry summary, with a 5-business-day deadline for RPP releases.
- GST is collected at import; there is no MPF or HMF.
- Records are kept 6 years, not 5.
- The 90-day "reason to believe" correction duty means a discovered error is urgent.
- Penalties under AMPS are issued against the importer's BN15, some automatically (for example for late accounting). See Section 13.

## 6. Mexico imports

### 6.1 Players and registrations

- **ANAM** runs customs operations; **SAT** remains the tax authority and manages the RFC, the e.firma and the padrón de importadores.
- **Importer:** must have an active RFC and an active registration in the padrón de importadores, plus a padrón sectorial for certain goods. It authorizes its agente aduanal electronically (encargo conferido). [COMPANY: Mexican importer entity, RFC owner, IMMEX status].
- **Agente aduanal / agencia aduanal:** prepares, validates and transmits the pedimento. [COMPANY: Mexico broker(s)].
- **Non-tariff regulations:** permits (for example from the Secretaría de Economía) and Normas Oficiales Mexicanas (NOMs, for example product labeling) apply by fracción arancelaria. A wrong fracción can trigger or miss them.

### 6.2 The life of a Mexican import

| Stage | What happens | Who | Our data or action | Timing |
|---|---|---|---|---|
| 1. Pre-arrival | Documents are gathered: commercial invoice, transport documents, the value declaration (manifestación de valor), permits and NOM evidence, the T-MEC certification if preference will be claimed. Supporting documents are digitized in the single window | Supplier, broker, importer | Item data, fracción and NICO, value elements, origin | Before the goods reach customs |
| 2. Pedimento and payment | The broker classifies (fracción + NICO), computes the valor en aduana, IGI, DTA, IVA and any IEPS or cuotas compensatorias, validates the pedimento and pays the contributions. Each pedimento has a key: A1 is a definitive import; IMMEX temporary imports use other keys (RGCE Anexo 22) | Broker | Everything in Section 7.1; IMMEX status | Before presenting the goods |
| 3. Automated selection | The goods and pedimento are presented and the automated selection mechanism decides: release, or a physical inspection (reconocimiento aduanero) | ANAM | Make sure documents match the goods | At the customs office |
| 4. Release | Goods are released. Irregularities found at inspection can start an administrative proceeding (PAMA, Procedimiento Administrativo en Materia Aduanera) | ANAM | [COMPANY: who is told when a shipment is held] | At the customs office |
| 5. Corrections | The pedimento can be corrected (rectificación, Ley Aduanera art. 89) as often as needed before the selection mechanism is activated; after that it is still possible except in cases that need SAT authorization (for example a correction that creates an undue payment or changes the customs regime). Complementary pedimentos settle differences | Broker, importer | Find errors early | Before the authority starts an audit, where possible |
| 6. Post-clearance review and audit | Pedimentos are reviewed after clearance (glosa) and the authorities can audit the importer. IMMEX companies are also checked against their inventory control (Anexo 24) | ANAM, SAT | Electronic file per pedimento; IMMEX records | Ongoing |
| 7. Records | The importer keeps an electronic file for each pedimento with its annexes and acknowledgments (art. 59) | Importer | [COMPANY: where pedimento files are stored] | 5 years (CFF art. 30) |

### 6.3 Mexican taxes and charges

- **IGI** (Impuesto General de Importación) = valor en aduana x the TIGIE rate for the fracción, unless a preference such as T-MEC applies.
- **DTA** (Derecho de Trámite Aduanero): the customs processing fee on the pedimento.
- **IVA** on imports = (valor en aduana + IGI + other import contributions) x the IVA rate (Ley del IVA art. 27). It is generally creditable, so it usually does not belong in item cost [COMPANY: confirm with Finance]. IMMEX companies with IVA/IEPS certification do not pay it in cash on temporary imports; a tax credit covers it (Section 11.1).
- **IEPS** applies to specific goods; **cuotas compensatorias** are Mexico's AD/CVD.
- **Valor en aduana** includes freight, insurance and handling until the goods arrive (port of unloading, first airport, or the border crossing), so the same purchase has a higher duty base in Mexico than in the US or Canada.

Worked example (hypothetical rates; DTA left out for clarity). Valor en aduana US$11,850, converted to pesos at the pedimento rate.

| Item | Amount (US$ equivalent) | Note |
|---|---|---|
| Valor en aduana | 11,850.00 | Includes freight and insurance to arrival (Section 9.7) |
| IGI at 5% | 592.50 | 11,850 x 5%; zero if a valid T-MEC claim applies and the rate is free |
| IVA base | 12,442.50 | Valor en aduana + IGI (+ DTA and other contributions in real life) |
| IVA at 16% | 1,990.80 | Generally creditable |

### 6.4 Changes to watch in 2026

- **Ley Aduanera reform:** published in the DOF on 19 Nov 2025 and generally in force from 1 Jan 2026, with a reform of its Reglamento in force from 24 Feb 2026. Commentators report stricter obligations for agentes aduanales, a fuller electronic file for importers (including evidence of the resources used to pay for the operation), and higher fines. Ask the Senior to confirm with [COMPANY: Mexico broker or counsel] what changed in our document flow.
- **Single window:** a decree published in the DOF on 4 May 2026 enabled the Ventanilla Única de Trámites de Comercio Exterior (VUTCE), run by the Agencia de Transformación Digital y Telecomunicaciones (ATDT) instead of SAT, as the single channel for foreign-trade procedures with the Secretaría de Economía, SAT, ANAM and other agencies. It replaced the SAT-run VUCEM; the trade still often says "VUCEM". The e.firma is still used to sign. Check the transition rules for pending procedures before mapping this data.
- **Tariff changes** to the TIGIE: time-sensitive; see `docs/primers/current-tariff-landscape.md`.

## 7. What we send brokers and how we audit what they file

### 7.1 Data we supply

| Data element | Why the broker needs it | Country notes |
|---|---|---|
| Item number and a plain-language description (what it is, what it is made of, what it does) | To classify, and to describe the goods on the declaration | Vague descriptions trigger questions (CBP Form 28) and inspections |
| Classification per country | Sets the duty rate, other-agency requirements and statistics | US HTSUS 10 digits; Canada 10 digits; Mexico fracción + NICO. The first 6 digits should normally match across countries |
| Country of origin (non-preferential) | Rate column, additional duties by country, marking | Not the same as "shipped from" |
| Preference claim and support | To claim USMCA / CUSMA / T-MEC | Certification reference, origin criterion, blanket period |
| Manufacturer or producer | US entry summary needs the manufacturer ID (MID); AD/CVD rates can be manufacturer-specific; USMCA certifications name the producer | Supplier is not always the manufacturer |
| Price, currency and Incoterm | Transaction value | [COMPANY: from Oracle POs or invoices] |
| Additions to value (assists, royalties, selling commissions, buyer-paid packing) | They must be added to the declared value | Rarely on the invoice; see Section 9 |
| Related-party indicator | Related-party transactions must be flagged and the price defended | [COMPANY: supplier master field] |
| Quantity, customs unit of measure, net weight | Specific duties and statistics are per customs unit | Stocking unit is often different from the customs unit |
| Other-agency data | PGA (US), OGD permits (Canada), permits and NOMs (Mexico) | Triggered by the classification |
| Additional duty flags | Chapter 99 numbers, AD/CVD case numbers, surtax indicators | Research decides scope; see `docs/templates/domain/tariff-impact-brief.md` |
| IMMEX status (Mexico) | Temporary versus definitive import; pedimento key | [COMPANY: confirm] |
| Importer identifiers | IOR number and bond (US), BN15 (Canada), RFC (Mexico) | Set up once; changes are rare and risky |

How this data reaches each broker today, and in what format, is covered in M2 and in `docs/primers/trade-systems-gtm-e2open-primer.md` [COMPANY: broker interface specifications].

### 7.2 What comes back

From each broker: the declaration (US entry summary, Canadian CAD, Mexican pedimento) at line level, with entry or transaction number, line number, classification, value, origin, preference claimed, rates, duties, taxes and fees, and release (and in the US, liquidation) dates; plus the broker's invoice. The importer can also see its own data in the ACE Portal (US) and the CARM Client Portal (Canada) [COMPANY: which reports we pull; whether we obtain the authority's pedimento data extract for Mexico]. This data is the "actual duty" for PPV analysis, the import side of drawback claims, and the basis for audits.

### 7.3 Auditing a filed line

Compare these four fields first. They drive the money and most of the risk.

| Field | Compare the filed value to | Typical mismatch | Who owns the fix |
|---|---|---|---|
| Classification | Our classification for that item, country and date | Broker used an old code, its own code, or a code for a similar item | If our master is wrong: the team (maker-checker). If the broker deviated: the broker, through the Senior |
| Value | Invoice and PO price, plus additions | Missing assist; wrong currency or conversion; freight treated wrongly | Depends on the cause; the Senior decides the correction route |
| Origin and preference claim | Our origin and USMCA qualification data, and the certification on file | Preference claimed with no certification; preference missed on a qualifying item; wrong origin | Team for master data; Senior for claims and corrections |
| Duty rate and amount | The rate for that code, origin and date, including Chapter 99 or surtaxes | Additional duty missed or wrongly applied; wrong rate column | Research for the rule; broker for the filing |

Also check: quantity and customs unit of measure, manufacturer ID (US), and the importer identifiers.

Audit routine (the Senior's W4 and W5 sessions go through this with real data):

- [ ] Pull the broker's line-level data for the period [COMPANY: source table or report].
- [ ] Join it to our master data by item, country and date. Count rows before and after the join to catch join fan-out (see the glossary and the M3 practice pack).
- [ ] Flag mismatches in the four fields above. Focus on new items, high-duty lines, preference claims and items under new tariff actions.
- [ ] Log each finding with evidence: entry and line, filed value, expected value, source, possible duty impact.
- [ ] Escalate to the Senior. You do not contact the broker or customs about a correction unless asked.
- [ ] If our master data caused it, raise a change request and fix the master data with maker-checker review.

## 8. Classification

### 8.1 How the Harmonized System is built

The Harmonized System (HS) is the World Customs Organization's product nomenclature. It has 21 sections and 97 chapters (chapter 77 is reserved for future use). The first 6 digits are the same in every country that uses it; each country adds its own digits.

| Level | Digits | Example | Who controls it |
|---|---|---|---|
| Section | Roman numeral | Section XI: textiles and textile articles | WCO |
| Chapter | 2 | 61: apparel, knitted or crocheted | WCO |
| Heading | 4 | 6109: T-shirts, singlets and other vests, knitted or crocheted | WCO |
| Subheading | 6 | 6109.10: of cotton | WCO |
| National tariff line | 8 | Sets the duty rate in the US, Canada and Mexico | Each country |
| Statistical suffix or NICO | 10 | Statistics (US, Canada) or commercial identification (Mexico NICO) | Each country |

Points that matter for data:

- **The legal text** is the headings plus the section and chapter notes. Section and chapter titles are for reference only. The WCO Explanatory Notes are not legally binding in the US but CBP and courts treat them as persuasive.
- **Digits 7 to 10 differ by country.** A US HTS number does not carry over to Canada or Mexico. Each country's code must be classified and maintained separately, and the first 6 digits should normally agree. A mismatch at 6 digits is a data-quality flag that needs a documented reason.
- **National special chapters:** HTSUS Chapter 98 (special provisions) and Chapter 99 (temporary and additional duties); Canada's Chapter 99 holds special classification provisions; Mexico's Chapter 98 covers special operations.
- **Editions:** the HS is amended about every five years. HS 2022 is current; **HS 2028 takes effect on 1 January 2028**. Every item's classification in every country must be checked against the HS 2022 to HS 2028 correlation tables, and items in amended subheadings must be remapped; most headings do not change. That falls inside the life of the e2open system, so the data model must keep classification history with effective dates.

### 8.2 The General Rules of Interpretation (GRIs)

The six GRIs are legal rules, applied in order. Stop at the first rule that settles the classification.

| Rule | What it says | Mini-example |
|---|---|---|
| GRI 1 | Classify by the terms of the headings and any relevant section or chapter notes. Titles are for reference only | A knitted cotton T-shirt is named by heading 6109. Done at GRI 1, as most goods are |
| GRI 2(a) | An incomplete or unfinished article that has the essential character of the complete article is classified as the complete article. So is a complete article shipped unassembled or disassembled | A bicycle shipped in a box, unassembled, is classified as a bicycle. A bicycle frame alone is not; it is a part |
| GRI 2(b) | A reference to a material includes mixtures and combinations of it with other materials. Goods of more than one material go to GRI 3 | A rubber glove with a textile lining is still "of rubber" for a rubber heading, but it could also fall in a textile heading; with two candidates, GRI 3 decides |
| GRI 3(a) | When two or more headings apply, the most specific description wins | Tufted textile carpets made for cars: the carpet heading (5703) is more specific than "parts of motor vehicles" (8708) |
| GRI 3(b) | Mixtures, composite goods and retail sets that 3(a) cannot settle are classified by the material or component that gives them their essential character | A hairdressing set (electric hair clipper, comb, scissors, brush and towel in a case) is classified as the hair clipper |
| GRI 3(c) | If 3(a) and 3(b) cannot decide, use the heading that occurs last in numerical order among those that equally merit consideration | Rare; a last resort, and a sign you should look for a ruling |
| GRI 4 | Goods that cannot be classified by GRIs 1 to 3 go in the heading for the goods they are most akin to | Very rare |
| GRI 5 | (a) Cases specially shaped for an article and suitable for long-term use, presented with it, are classified with it. (b) Normal packing is classified with the goods unless it is clearly suitable for repeated use | A fitted camera case shipped with the camera goes with the camera; a cardboard carton goes with its contents |
| GRI 6 | Subheadings are chosen by their terms and subheading notes, applying GRIs 1 to 5 at that level, comparing only subheadings at the same level (one-dash with one-dash) | Inside heading 6109, compare "of cotton" with "of other textile materials", not with deeper indented lines |

The US also has Additional U.S. Rules of Interpretation in the HTSUS (for example on "principal use" and on parts). Read them before classifying in the US.

### 8.3 Kits and sets

Kits matter in a distribution business. Under the Explanatory Notes to GRI 3(b), goods are a "set put up for retail sale" only if all three conditions hold:

1. At least two different articles that, on their face, are classifiable in different headings.
2. Put together to meet a particular need or carry out a specific activity.
3. Put up in a way suitable for sale directly to users without repacking.

If the kit qualifies, it is classified as one article by the component that gives it its essential character, and it goes on the declaration as one line. If it does not qualify (for example a "kit" that is really a box of unrelated items), each item is classified separately and goes on its own line. This affects broker data (one code or several), duty, and USMCA qualification (Section 10.6). Record the decision and the reason in the item's classification rationale.

### 8.4 A classification method

1. **Understand the product.** What it is, what it is made of (with percentages), what it does, how it is used, how it is presented for import (alone, in a set, unassembled). Get the spec sheet or a photo. Most classification errors are description errors.
2. **List candidate headings** from the HTSUS index and search, not just the first hit.
3. **Read the section and chapter notes** for each candidate. Exclusion notes often end the analysis.
4. **Apply GRI 1;** move to GRIs 2 to 5 only if GRI 1 does not settle it.
5. **Pick the subheading with GRI 6,** then the national digits for each country.
6. **Check rulings** (Section 8.5) for the same or similar goods.
7. **Check the consequences:** the USMCA product-specific rule for the new code, other-agency flags, AD/CVD scope and additional duties (Research checks scope against the legal text).
8. **Document** the item, description, materials, candidate headings, rule applied, notes and rulings cited, decision per country, preparer, checker and effective date [COMPANY: where classification rationale is stored].
9. **Maker-checker:** a second person reviews before the code reaches the brokers.

### 8.5 Rulings

| Country | Instrument | How much it binds | How we use it |
|---|---|---|---|
| United States | CBP rulings (19 CFR Part 177), searchable in CROSS at rulings.cbp.gov | A ruling binds CBP for the transaction it describes, while the facts stay the same. A ruling issued to another importer is guidance only (19 CFR 177.9) | Search CROSS for the same or similar goods and cite rulings in the rationale. For high-value or uncertain items, ask the Senior about requesting our own ruling |
| Canada | Advance rulings on tariff classification (Memorandum D11-11-3); origin advance rulings under free trade agreements (D11-4-16); National Customs Rulings for non-preferential origin, valuation and marking (D11-11-1) | An advance ruling applies to the same goods while the facts and law stay the same | Apply well before importing. A ruling does not replace a CUSMA certification of origin |
| Mexico | Classification consultation before the operation (Ley Aduanera art. 47), with opinions from the Consejo de Clasificación Arancelaria published as classification criteria (RGCE Anexo 6) | The resolution applies to operations after it is notified | Ask the Senior to check with the agente aduanal whether a published criterion covers the item |
| USMCA origin | Each USMCA country issues advance rulings on origin (USMCA Chapter 5) | A ruling by one country does not bind the others | For high-volume items where qualification is uncertain |

### 8.6 How classification errors show up

| Error | What breaks | Who usually notices |
|---|---|---|
| Wrong heading or subheading | Duty over- or underpaid; wrong landed cost | A CBP Form 29, a CBSA verification, a Mexican glosa, or our own audit |
| Wrong code for the USMCA analysis | The product-specific rule is looked up by the good's HS code, and the tariff shift compares the codes of the materials, so a wrong code can turn a valid claim invalid (or hide a valid one) | Origin verification; our BOM review |
| Missed other-agency requirement | US PGA data is triggered by the HTS number; Mexican permits and NOMs by the fracción. Shipments are held or refused | Broker, at the border |
| Additional duties | Chapter 99 measures and surtaxes are scoped by HTS lists (with exceptions). A wrong code applies or misses them | Research; duty audits |
| AD/CVD | Scope is by product description, not the code; a wrong code can hide an in-scope item | CBP, sometimes years later |
| Inconsistent codes across countries | The same item has different 6-digit codes in the US, Canada and Mexico | Data profiling (M3, M10) |
| Exports | Schedule B or HTS reported in export data is wrong | Census edits; export audits |

### 8.7 Exercise 1: classify five items

Use the five sanitized practice items from the Senior [COMPANY: practice item list].

- [ ] For each item, follow Section 8.4 and record the US 10-digit HTSUS number (hts.usitc.gov) and the GRI you relied on.
- [ ] Find at least one CROSS ruling for each item, or record that none was close.
- [ ] Find the Canadian tariff item (CBSA Customs Tariff) and the Mexican fracción and NICO (the Secretaría de Economía tariff lookup, SIAVI; ask the Senior for the current link) and confirm the first 6 digits agree.
- [ ] Compare your answers with our master data. Do not change the master data; log differences for the Senior's review on Thursday.

## 9. Valuation basics

### 9.1 The valuation methods

All three countries follow the WTO Customs Valuation Agreement. The methods are applied in order; the first one that works is used. In practice almost every one of our imports should use transaction value.

| Order | Method | Basis |
|---|---|---|
| 1 | Transaction value | The price actually paid or payable for the goods when sold for export to the importing country, plus defined additions |
| 2 | Transaction value of identical goods | Price of identical goods sold for export to the same country at about the same time |
| 3 | Transaction value of similar goods | Same, for similar goods |
| 4 | Deductive value | Resale price in the importing country, minus profit, costs and duties |
| 5 | Computed value | Cost of production, plus profit and general expenses, plus additions |
| 6 | Fallback | A reasonable adaptation of the methods above |

The importer may generally ask to use computed value before deductive value.

### 9.2 Transaction value

Transaction value is the price actually paid or payable, including indirect payments to the seller. It can be used only if there is a sale for export, there are no restrictions or conditions that make the value impossible to determine, no undisclosed proceeds of resale go back to the seller, and, for related parties, the relationship did not influence the price.

### 9.3 Additions and exclusions

| Element | United States | Canada | Mexico |
|---|---|---|---|
| Packing costs paid by the buyer | Added | Added | Added |
| Selling commissions paid by the buyer | Added | Added | Added |
| Buying commissions (paid to our own buying agent) | Not added | Not added | Not added |
| Assists (molds, tooling, materials or engineering we supplied free or at reduced cost) | Added | Added | Added |
| Royalties and license fees paid as a condition of sale | Added | Added | Added |
| Proceeds of resale that go to the seller | Added | Added | Added |
| International freight and insurance | Excluded if separately identified | Included up to the place of direct shipment to Canada, excluded after | Included until the goods arrive in Mexico |
| Transport and costs after importation | Excluded | Excluded | Excluded |
| Import duties and taxes | Excluded | Excluded | Excluded |

Assists are the classic BSA data problem: the value must be added to the declared value, but it is not on the supplier's invoice or the PO. If we pay for a mold the supplier uses, someone must know, record the value, and apportion it across the shipments [COMPANY: where assists are tracked; often nowhere]. The apportionment method must be reasonable and applied consistently; agree it with the Senior and the broker.

### 9.4 Related parties

If buyer and seller are related (for example, affiliates), transaction value can still be used if the importer can show the relationship did not influence the price, either from the circumstances of the sale or because the price closely approximates a test value. The declaration must flag the relationship. Transfer pricing adjustments made after import can change the customs value; escalate any you hear about [COMPANY: are any of our suppliers related parties?].

### 9.5 Currency conversion

Each country fixes which day's exchange rate applies, and the broker applies it. Our landed-cost models use a planning rate instead [COMPANY: Finance's rate policy], so model duty and filed duty will differ slightly. That difference is expected and should be explainable in PPV.

| Country | Rate | Date |
|---|---|---|
| United States | Federal Reserve Bank of New York certified rate, or CBP's certified quarterly rate where it applies | Date of exportation: the day the goods finally leave the exporting country for the US (19 CFR 159.32, 152.1(c)) |
| Canada | Bank of Canada rate as used by CBSA | Date of direct shipment to Canada (D13-2-3) |
| Mexico | Peso-dollar rate for tax purposes | Date of entry (Ley Aduanera art. 56) or the payment date where art. 83 applies, as declared on the pedimento |

### 9.6 Incoterms are not valuation rules

Incoterms 2020 say where risk passes and who pays transport and clearance. They do not set the customs value. They tell you what the invoice price includes, so you know what to add or deduct. Example: on an FCA price at the supplier's factory, we pay the main freight. In the US that freight is not part of the customs value. In Canada, transport from the factory to the place of direct shipment is added, but the international leg after it is not. In Mexico all of it is added, up to arrival.

### 9.7 Worked example: one purchase, three duty bases

A purchase of goods from a supplier in Taiwan, shown in US dollars to keep the arithmetic simple. Each country's broker would convert to its own currency at its own rule (Section 9.5).

- Invoice price: US$10,000, FOB Kaohsiung (the supplier's price already includes packing and delivery onto the vessel).
- Ocean freight to the port of import: US$800. Marine insurance: US$50. Both paid by us.
- We supplied a mold free of charge, cost US$3,000, apportioned evenly over three shipments: US$1,000 to this one.
- We paid our own buying agent a commission of US$200.

| Element | US value (US$) | Canada value for duty (US$ equivalent) | Mexico valor en aduana (US$ equivalent) |
|---|---|---|---|
| Invoice price, FOB Kaohsiung | 10,000 | 10,000 | 10,000 |
| Assist (mold, apportioned) | 1,000 | 1,000 | 1,000 |
| Buying commission | 0 (not added) | 0 (not added) | 0 (not added) |
| Ocean freight | 0 (excluded) | 0 (after the place of direct shipment) | 800 |
| Insurance | 0 (excluded) | 0 (after the place of direct shipment) | 50 |
| Customs value | 11,000 | 11,000 | 11,850 |

The Canada and Mexico examples in Sections 5.3 and 6.3 continue from these numbers.

### 9.8 Where valuation data breaks

- Assists, royalties and buyer-paid packing are not captured anywhere in the systems.
- Price changes after import (retroactive price increases, rebates, transfer pricing adjustments) are not passed to the broker.
- The invoice currency or Incoterm on the PO differs from the actual invoice.
- Freight is netted into a delivered (DAP or DDP) price and not separated for the US and Canada.

## 10. Origin and USMCA

### 10.1 Preferential and non-preferential origin

"Origin" means different things for different purposes, and the answers can differ for the same item.

| Purpose | Rule used | Example |
|---|---|---|
| Preferential duty under USMCA | USMCA Chapter 4 and the product-specific rules in Annex 4-B (in the US, also General Note 11 of the HTSUS and 19 CFR Part 182) | Does the pump qualify for the USMCA rate? |
| US country-of-origin marking | 19 U.S.C. 1304 and 19 CFR Part 134. For goods imported from Canada or Mexico, origin for marking is decided by the tariff-shift rules in 19 CFR Part 102 | Must the box say "Made in Mexico"? |
| Additional duties tied to a country | Non-preferential origin, usually "substantial transformation" (a new article with a new name, character or use), unless the action's legal text says otherwise | Is this item "of China" for an additional duty? |
| Statistics and AD/CVD scope | Non-preferential origin and the order's scope | Which country goes in the trade statistics? |

The classic trap: an item assembled in Mexico from Chinese parts may be a product of Mexico for marking (if it meets the Part 102 tariff shift) and, separately, for a China-specific additional duty (if the assembly is a substantial transformation, or meets whatever origin rule the action's text sets), yet still fail the USMCA product-specific rule. Each answer comes from a different test. Never use one answer for another purpose.

Marking basics (US): every article of foreign origin, or its container, must be marked legibly, conspicuously and permanently with the English name of the country of origin, unless an exception applies (19 CFR Part 134). Canada has its own marking rules for specified goods (Memorandum D11-3-1); Mexico regulates labeling through NOMs.

### 10.2 USMCA basics

- In force since 1 July 2020, replacing NAFTA. Called USMCA in the US, CUSMA in Canada and T-MEC in Mexico.
- A good is originating if it is (A) wholly obtained or produced in the region; (B) produced in the region using non-originating materials and meets the Annex 4-B product-specific rule; (C) produced in the region exclusively from originating materials; or (D) one of a narrow set of cases decided by a regional value content test (USMCA Art. 4.2).
- Preference is claimed by the importer, based on a certification of origin it holds when it makes the claim.
- The agreement's joint review, extension and any changes to its rules are time-sensitive: see `docs/primers/current-tariff-landscape.md`.

### 10.3 Product-specific rules: the rule types

You look up the rule by the finished good's HS classification. Most rules use one or both of these tests.

| Rule type | How the rule reads | The test | Data you need |
|---|---|---|---|
| Change of chapter (CC) | "A change to heading X from any other chapter" | Every non-originating material is classified in a different 2-digit chapter than the good | HS code of the good and of each non-originating material |
| Change of heading (CTH) | "A change to heading X from any other heading" | Every non-originating material is in a different 4-digit heading | Same |
| Change of subheading (CTSH) | "A change to subheading X from any other subheading" | Every non-originating material is in a different 6-digit subheading | Same |
| Exceptions | "...from any other heading, except from heading Y" | Non-originating materials from the excepted codes are not allowed | Same, read carefully |
| Regional value content (RVC) | "...provided there is a regional value content of not less than N percent under the transaction value method, or not less than M percent under the net cost method" | The share of regional value meets the threshold | Value of the good, value of non-originating materials, and for net cost, the producer's cost data |
| Alternatives | Two rules joined by "or" | Meeting either one is enough | Both data sets, if the first fails |

Some sectors have special regimes (automotive goods, textiles and apparel). If an item falls in one, stop and ask the Senior.

### 10.4 Regional value content

Two formulas (USMCA Art. 4.5):

- **Transaction value method:** RVC = (TV - VNM) / TV x 100
- **Net cost method:** RVC = (NC - VNM) / NC x 100

Where TV is the transaction value of the good, adjusted to exclude the costs of international shipping; VNM is the value of non-originating materials used by the producer; and NC is the net cost: total cost minus sales promotion, marketing and after-sales service, royalties, shipping and packing costs, and non-allowable interest.

Things to know:

- The rule states which methods are allowed and the threshold for each. Many rules allow both, with a higher threshold for transaction value than for net cost, but read the actual rule; never assume a threshold.
- Net cost needs the producer's own cost accounting. When we are the importer and not the producer, we depend on the producer's analysis and certification.
- The value of non-originating materials depends on the origin of each component, which comes from supplier information. Unknown origin should be treated as non-originating.

### 10.5 De minimis, accumulation and other provisions

- **De minimis (Art. 4.12):** a good still qualifies under a tariff-shift rule even if some non-originating materials fail the required shift, provided the value of all those failing materials is no more than 10 percent of the good's transaction value or total cost. Exceptions exist, and textiles use weight. Our reading of the text is that materials allowed in under de minimis still count as non-originating in any RVC calculation; confirm with the Senior.
- **Accumulation (Art. 4.11):** originating materials and production in any USMCA country count toward the good's origin. A component made in Canada that originates counts as originating for a good assembled in Mexico.
- **Other Chapter 4 provisions to know exist:** intermediate (self-produced) materials, indirect materials, fungible goods and materials, accessories and spare parts delivered with a good, packaging for retail sale, packing materials for shipment (disregarded), sets of goods (10.6), transshipment (Art. 4.18: the good must not be processed outside the region after qualifying), and non-qualifying operations (Art. 4.19: mere dilution with water or another substance, or a production or pricing practice designed to circumvent the chapter). Do not confuse the Art. 4.19 list with the 19 CFR 102.17 list (simple packing, repacking, retail packaging), which applies to US marking origin, not to USMCA preference.

Do not confuse USMCA de minimis with the US low-value "de minimis" import treatment (Section 321). They are unrelated. The second is a time-sensitive topic in `docs/primers/current-tariff-landscape.md`.

### 10.6 Kits and sets under USMCA

USMCA has a specific article on sets of goods (Art. 4.17). Except where Annex 4-B provides otherwise, a set classified under GRI 3 is originating only if every good in the set is originating; alternatively, the set is originating if the value of all the non-originating goods in it does not exceed 10 percent of the value of the set. Both the set and its goods must meet the other Chapter 4 requirements. Practical points:

- The sets article applies only when the kit is classified as a set (Section 8.3). If each item is classified separately, each item is qualified separately under its own product-specific rule.
- A GRI 3 set is not run through a product-specific rule as if it were one manufactured good. The goods in the set are tested.
- For our kits, the data needed is like a BOM: each good's classification, origin and value [COMPANY: where kit structures live: Oracle BOM, AS400, spreadsheet?].

Mini-example (fictional). Retail tool kit KT-200, classified as a set under GRI 3(b), value US$50.00: a drill (originating, US$35.00), a case (originating, US$8.00), a manual (originating, US$3.00) and a bit set (made in China, non-originating, US$4.00).

- Not every good is originating, so test the alternative: 4.00 / 50.00 = 8 percent, no more than 10 percent. The set would be originating.
- If the bit set cost US$7.00 (set value US$53.00): 7 / 53 = 13.2 percent. The set would not be originating unless the bit set itself originates.

### 10.7 Certification of origin

- **Who certifies:** the importer, the exporter or the producer (Art. 5.2). Mexico has accepted importer certifications since 1 January 2024.
- **Form:** no mandatory form. Any format, including on the invoice, if it contains the nine minimum data elements of Annex 5-A. NAFTA's CBP Form 434 is no longer used.
- **Blanket certification:** can cover multiple shipments of identical goods for a period of up to 12 months.
- **Validity:** customs must accept a certification for four years after the date it was completed. That is separate from the five-year recordkeeping duty.

| No. | Minimum data element (Annex 5-A) | Where it comes from |
|---|---|---|
| 1 | Certifier role: importer, exporter or producer | Who signs |
| 2 | Certifier: name, title, address, phone, email | Certifier |
| 3 | Exporter: name, address, contact | Supplier master [COMPANY] |
| 4 | Producer: name, address, contact (or "various" or "available upon request" in some cases) | Supplier or producer |
| 5 | Importer: name, address, contact | Us |
| 6 | Description of the good and its 6-digit HS classification | Item master and classification |
| 7 | Origin criterion (A, B, C or D) | Qualification result |
| 8 | Blanket period, if any | Certification record |
| 9 | Authorized signature and date, with a statement that the information is true and accurate | Certifier |

Claiming and keeping a claim valid:

- **At entry:** the US claim is made with SPI "S" on the entry summary line ("S+" only for certain agricultural and textile goods, Section 4.3); Canada and Mexico claim the preference on the CAD or pedimento. The importer must hold the certification when it makes the claim.
- **After entry:** in the US, a post-importation claim can be made within one year of importation (19 U.S.C. 1520(d); 19 CFR 182.31 to 182.33). An approved claim refunds the excess duty and the MPF paid on the originating goods: the Consolidated Appropriations Act, 2021 (Pub. L. 116-260) authorized MPF refunds on these claims, back-dated to 1 July 2020. CBP's earlier (July 2020) no-refund position is superseded, so ignore older guidance that says otherwise. Canada and Mexico have their own procedures (verify time limits with the Senior).
- **When a claim turns out wrong:** the importer must correct the declaration and pay the duties owed. In Canada, the 90-day "reason to believe" clock applies (Section 5.2). Escalate the same day.

### 10.8 Exercise 2: BOM-based qualification (fictional)

All names, codes, values and the rule below are **fictional**, built only to practise the method. Do not use them for real items.

The good: pump PK-100, assembled in Mexico by our supplier from the components below and imported into the US. Assume it is classified at GRI 1 in fictional heading 84.AA (it is one assembled article, not a set), and that its fictional product-specific rule is:

"A change to heading 84.AA from any other heading; or no required change in tariff classification to heading 84.AA, provided there is a regional value content of not less than 60 percent under the transaction value method or not less than 50 percent under the net cost method."

Transaction value of the pump, adjusted to exclude international shipping: US$200.00.

| Component | Classification (fictional) | Origin | Value (US$) | Originating? |
|---|---|---|---|---|
| Motor | Heading 85.BB | China | 60.00 | No |
| Pump housing | Heading 84.AA | Germany | 14.00 | No |
| Impeller | Heading 84.AA | Mexico, supplier certification on file | 20.00 | Yes |
| Fasteners | Heading 73.CC | China | 4.00 | No |
| Seals | Heading 40.DD | United States, supplier certification on file | 6.00 | Yes |
| Assembly labor, overhead and profit | Not a material | Mexico | 96.00 | Not a material |

Step 1: list non-originating materials. Motor (60), pump housing (14), fasteners (4). VNM = 78.00.

Step 2: test the tariff shift for each non-originating material against heading 84.AA.

| Non-originating material | Its heading | Change of heading to 84.AA? |
|---|---|---|
| Motor | 85.BB | Yes |
| Pump housing | 84.AA | No: same heading |
| Fasteners | 73.CC | Yes |

Step 3: one material fails, so apply de minimis. Value of failing materials / TV = 14 / 200 = 7.0 percent. That is no more than 10 percent, so the pump meets the tariff-shift rule under de minimis. Origin criterion B.

Step 4 (what if): the pump housing actually costs US$25.00, so TV becomes US$211.00 and VNM US$89.00. De minimis: 25 / 211 = 11.8 percent, more than 10 percent, so the tariff shift fails. Try the alternative rule:

- Transaction value method: (211 - 89) / 211 x 100 = 57.8 percent. Below 60, fails.
- Net cost method, using the producer's net cost of US$185.00: (185 - 89) / 185 x 100 = 51.9 percent. At least 50, qualifies.

Under net cost the pump qualifies, but only the producer can calculate and support net cost, so the producer (or exporter) would normally certify.

Step 5: document. Keep the BOM with each component's classification, origin, value and source; the supplier certifications for the originating components; the calculation; the rule text and its source; who prepared and who checked; and the date. Then the certification can be issued or accepted, and the item's qualification flag set in [COMPANY: system that holds USMCA qualification].

Your turn:

- [ ] Rebuild Steps 1 to 4 in Excel with formulas, so changing a component's value or origin changes the result.
- [ ] Change the motor's origin to Canada (with a valid supplier certification). What happens to VNM and to the de minimis test?
- [ ] List the data you would need from our systems to run this for a real item, and where each field lives [COMPANY].
- [ ] Hire A: redo the KT-200 mini-example in Section 10.6 in the same workbook, and write down how you would decide whether one of our real kits is a set.

### 10.9 Supplier solicitation

When we are not the producer, our USMCA claims rest on supplier information. Supplier solicitation is the recurring process of collecting it.

1. Select the items and suppliers in scope: items imported into a USMCA country from a USMCA country, plus components used in goods we certify [COMPANY: scope].
2. Send each supplier a request for a USMCA certification (or origin information for components), with item numbers, descriptions and the blanket period.
3. Track responses, follow up, and escalate non-responders.
4. Review each response: all nine data elements, item match, period, signature. Reject incomplete ones.
5. Validate on a risk basis: high-value items, items with sudden changes, suppliers with weak answers. Ask for the supporting analysis.
6. Load the result into the system that drives the broker's preference claim, with the certification reference and expiry date.
7. Before a blanket period ends, start the next cycle. An expired certification means the claim is unsupported.

Useful measures: percent of in-scope import value covered by a valid certification; number of certifications expiring in the next 60 days; number of claims filed without a certification on file (should be zero). GTM systems such as e2open automate this cycle (`docs/primers/trade-systems-gtm-e2open-primer.md`).

### 10.10 Recordkeeping and verifications

- **Keep:** the certification, the BOM and qualification calculation, supplier certifications and origin information, cost data for net cost, invoices and proof of the transaction, for at least 5 years after importation (USMCA Art. 5.8), 6 in Canada.
- **Verifications:** the importing country's customs can verify a claim by written requests or questionnaires to the importer, exporter or producer, and by visits to the producer (USMCA Chapter 5). In the US, a CBP Form 28 is often the first sign.
- **What a BSA must be able to do:** produce the qualification file for any claimed item within days. If the supporting data cannot be found, the claim can be denied, with duties, interest and possibly penalties.

## 11. Special programs: IMMEX and US duty drawback

### 11.1 Mexico IMMEX

- **What it is:** IMMEX (Industria Manufacturera, Maquiladora y de Servicios de Exportación), set up by the IMMEX Decree of 1 November 2006. Authorized companies import inputs, components, packaging and machinery temporarily to manufacture, transform or repair goods for export, without paying the general import duty (IGI) at import. Companies that also hold SAT's IVA/IEPS certification cover the IVA and IEPS on those temporary imports with a tax credit instead of paying them in cash.
- **Time limits:** temporary imports must be exported, transferred or changed to a definitive import within set periods: generally up to 18 months for raw materials, parts and components (Ley Aduanera art. 108); machinery and equipment can stay for the life of the program. Inputs not returned or changed to another regime in time are deemed to be in Mexico illegally, because the temporary regime has ended (art. 108), so IGI, IVA/IEPS with surcharges, and fines can be assessed (verify current periods in the Ley Aduanera).
- **Anexo 24 (automated inventory control):** IMMEX companies must keep an automated inventory control system that meets RGCE Anexo 24. It tracks each temporarily imported input from its pedimento to its consumption, export, transfer or change of regime, generally on a first-in, first-out basis, and the authorities must have online access to it.
- **Anexo 30, formerly Anexo 31 (credit and guarantee accounts):** SAT's Sistema de Control de Cuentas de Créditos y Garantías (SCCCyG) is set out in **Anexo 30** of the current RGCE. It was Anexo 31 before the RGCE for 2022, and the trade still often calls it "Anexo 31". It tracks the IVA and IEPS credits that certified companies take on temporary imports, and their discharge as goods are exported. Cite it as "Anexo 30 (formerly Anexo 31)" and check the numbering in the current year's RGCE. Its balances must reconcile with the Anexo 24 inventory.
- **USMCA interaction:** USMCA Article 2.5 limits duty deferral and drawback programs for non-originating inputs in goods exported to another USMCA country, so IMMEX goods sent to the US or Canada can owe Mexican duty on those inputs. Ask the Senior how this applies to us.
- **Where it sits:** [COMPANY: who owns IMMEX and Anexo 24 compliance: the Mexican entity, the broker, or this team; which system holds the Anexo 24 inventory]. The hires get an overview in W4; deeper work only if the Manager assigns it.

### 11.2 US duty drawback

- **What it is:** a refund of up to 99 percent of the duties, taxes and fees paid on imported merchandise when the merchandise, or permitted substitute merchandise, is exported or destroyed (19 CFR Part 190, as modernized by the Trade Facilitation and Trade Enforcement Act of 2015, TFTEA).
- **Main types:**

| Type | Statute | In plain words |
|---|---|---|
| Manufacturing, direct identification | 19 U.S.C. 1313(a) | Imported merchandise used to make an article that is exported or destroyed |
| Manufacturing, substitution | 19 U.S.C. 1313(b) | Other merchandise (imported or domestic) classifiable under the same 8-digit HTSUS subheading as the imported input is used instead of it. There is no 10-digit "Other" rule for this type |
| Unused merchandise, direct identification | 19 U.S.C. 1313(j)(1) | Imported goods exported or destroyed without being used in the US |
| Unused merchandise, substitution | 19 U.S.C. 1313(j)(2) | Substitute goods classifiable under the same 8-digit HTSUS subheading are exported or destroyed unused instead of the imported goods. If the 8-digit description begins with "Other", they must match at the 10-digit level; if the 10-digit description also begins with "Other", substitution is not available (direct identification still is) |
| Rejected merchandise | 19 U.S.C. 1313(c) | Goods that did not conform to sample or specifications, were shipped without the consignee's consent, or were defective at import, and are exported or destroyed under CBP supervision |

"Same kind and quality" and "commercially interchangeable" are the pre-TFTEA substitution standards (19 CFR Part 191, legacy claims only). Current claims use the 8-digit tests above.

- **Time limit:** generally 5 years from the date of importation (check the rule for each type in 19 CFR Part 190).
- **Records:** drawback needs import data (entries, lines, duty paid), export data (proof of export), and the link between them (inventory or manufacturing records). Drawback records are kept until 3 years after the drawback claim is liquidated (19 U.S.C. 1508(c); 19 CFR 190.15). Liquidation of the claim comes after any accelerated payment, so this is longer than it sounds.
- **USMCA limits:** USMCA Article 2.5 restricts drawback on non-originating goods exported to Canada or Mexico.
- **Where it sits:** US duty drawback **stays with the Senior**. The hires get exposure from W10 (M9): a shadow session and a one-page note on what data drawback needs from our import and export records, which feeds the e2open data maps.

## 12. Exports overview

The hires take exports backlog items from W6 (M7). License determinations stay with the Senior.

### 12.1 US export controls

- **Who controls what:** most commercial and dual-use items are "subject to the EAR", the Export Administration Regulations (15 CFR Parts 730 to 774), administered by the Commerce Department's Bureau of Industry and Security (BIS). Defense articles fall under the ITAR (State Department), which is unlikely for a distributor but must be ruled out, not assumed.
- **Classification:** an item on the Commerce Control List (CCL, Supplement No. 1 to Part 774) has an Export Control Classification Number (ECCN), a five-character code such as 3A001 that shows its reasons for control. An item subject to the EAR but not on the CCL is **EAR99**.
- **License determination:** combine the ECCN's reasons for control with the Commerce Country Chart (Supplement No. 1 to Part 738) for the destination, then check the general prohibitions (Part 736): restricted end users and end uses, embargoed destinations, and parties on restricted lists. An EAR99 item can still need a license for an embargoed destination, a prohibited end use or a restricted party.
- **Red flags and screening:** BIS's "Know Your Customer" guidance lists red flags (for example a customer unwilling to say where the item will be used). Restricted party screening checks parties against government lists such as the Consolidated Screening List; awareness only for the hires. A possible match is put on hold and escalated, never cleared by a hire.
- **Records:** EAR records are generally kept 5 years (15 CFR Part 762).

### 12.2 Electronic Export Information (EEI)

- **What:** export data filed in the Automated Export System (AES) under the Foreign Trade Regulations (15 CFR Part 30, Census Bureau). The filer receives an Internal Transaction Number (ITN) as proof of filing.
- **When required:** generally when the value of goods under one Schedule B or HTS number is over US$2,500, or a license is required, plus other mandatory cases (15 CFR 30.2 and 30.37(a)).
- **Canada:** shipments from the US to Canada are generally exempt from EEI (15 CFR 30.36), except for goods that need a license or fall under other mandatory filing cases, goods stored in Canada for a third country, and goods moving through Canada to a third country.
- **Who:** the US Principal Party in Interest (USPPI), usually the US seller, is responsible for accurate data; in a routed export transaction the foreign buyer's agent may file. EEI records are kept 5 years (15 CFR 30.10).
- **Schedule B:** the Census Bureau's 10-digit export classification. The first 6 digits are the HS; for most goods the HTSUS number may be reported instead.

### 12.3 Canadian and Mexican exports (awareness)

- Canada: export declarations are filed through CBSA, for example with the Canadian Export Reporting System (CERS), and need the exporter's BN15. Most exports to the US do not need a declaration unless the goods are controlled; verify in Memorandum D20-1-1.
- Mexico: exports are declared on an export pedimento by an agente aduanal. IMMEX returns are exports.

### 12.4 What the hires will do from W6

Exports backlog items as maker, for example export data-quality fixes, Schedule B or ECCN data gaps, and report fixes, with the Senior as checker. Not: license determinations, screening match decisions, or voluntary disclosures. [COMPANY: Jira label for the exports transition; which export flows we have: from the US, Canada, Mexico].

## 13. Penalties and corrections

### 13.1 The concepts by country

| Topic | United States | Canada | Mexico |
|---|---|---|---|
| Main regime | 19 U.S.C. 1592: false statements or omissions by fraud, gross negligence or negligence | AMPS: graduated monetary penalties for contraventions listed in the Master Penalty Document, issued against the BN15 | Ley Aduanera infractions and fines; omitted taxes with actualización and recargos; PAMA after a border inspection |
| How big | The statutory maximum depends on culpability: domestic value for fraud; the lesser of domestic value or 4 times the lost duties for gross negligence; the lesser of domestic value or 2 times the lost duties for negligence (19 U.S.C. 1592(c)) | Penalty levels rise for repeat contraventions; serious cases can lead to seizure or ascertained forfeiture | Fines are often a percentage of the omitted taxes; the 2026 reform raised some. Ask counsel for amounts |
| Voluntary disclosure | Prior disclosure before, or without knowledge of, a formal investigation: for negligence or gross negligence, the penalty is limited to interest on the lost duties if they are tendered; for fraud, it is reduced (19 CFR 162.74) | Correcting within the 90-day s. 32.2 window; CBSA's voluntary disclosure process (verify current guidance) | Spontaneous compliance before the authority acts generally avoids fines (CFF art. 73; verify) |
| Correction tools | PSC before liquidation; protest after | CAD corrections and adjustments | Rectificación; complementary pedimento |

The US multiples come from the statute named; Canadian and Mexican penalty amounts are deliberately not given here. Never estimate a penalty yourself; that is for the Senior and counsel.

### 13.2 What to do when you find an error

1. **Contain:** stop the error spreading. Tell the owner of the data, and do not send more filings with the known-bad value.
2. **Record** what you found, with evidence: item, country, entries affected, filed value, correct value, source, date found.
3. **Escalate the same day** to the Senior (and the Manager if the Senior is out). In Canada the 90-day clock may have started; in the US the PSC window may be closing.
4. **Do not** contact customs, and do not ask the broker to correct a filed declaration, unless the Senior asks you to.
5. **Scope it:** find every affected entry, line and period with a query; the Senior uses this to choose the route.
6. **Fix the root cause** in master data through a change request with maker-checker review (`docs/templates/bsa/06-change-request.md`).
7. **The correction route** (PSC, protest, prior disclosure, CAD adjustment, rectificación) is decided by the Senior or Manager, with counsel where needed. You prepare the data.

## 14. What a BSA touches

The data elements below drive filings, costs and reports. "Lives in" is the system of record; confirm each one in M2 [COMPANY: confirm every row].

| Data element | Lives in | Used by | What breaks if wrong |
|---|---|---|---|
| Item number and trade description | [COMPANY: Oracle item master and/or AS400 trade system] | Brokers, classification, reports | Broker cannot classify or match lines; vague descriptions trigger CBP Form 28s and inspections; audits cannot join data |
| US HTSUS number (10 digits) | [COMPANY: AS400 trade system] | US broker, landed cost, Research, reports | Wrong duty; PGA data missed; Chapter 99 measures missed or wrongly applied; penalty exposure |
| Canada classification (10 digits) | [COMPANY: AS400 trade system] | Canada broker, landed cost | Wrong duty and GST base; surtaxes missed; s. 32.2 corrections |
| Mexico fracción and NICO | [COMPANY: AS400 trade system or Mexico broker] | Mexico broker, IMMEX inventory | Wrong IGI; permits or NOMs missed; Anexo 24 records do not match pedimentos |
| Country of origin (non-preferential) | [COMPANY] | Brokers, marking, Research | Country-specific additional duties missed or wrongly applied; marking violations; AD/CVD exposure |
| USMCA qualification (yes/no, criterion, producer, certification reference, blanket period) | [COMPANY] | Brokers (preference claim), Standard Cost (duty rate) | Claims without support are denied in a verification; or savings are missed |
| Supplier and manufacturer identity and address (US MID) | [COMPANY: Oracle supplier master, AS400] | US broker, certifications, AD/CVD | Entry summary errors; wrong producer on certifications; wrong AD/CVD rate |
| Unit price, currency and Incoterm | [COMPANY: Oracle purchase orders, supplier invoices] | Brokers (value), landed cost | Under- or overvaluation; wrong duty base; model and filed duty disagree |
| Assists, royalties, buyer-paid packing | [COMPANY: often not recorded anywhere] | Brokers (additions to value), the Senior | Undervaluation; 1592 or AMPS exposure |
| Related-party indicator | [COMPANY: Oracle supplier master] | Brokers, valuation reviews | Relationship not declared; price cannot be defended |
| Quantity, customs unit of measure, net weight | [COMPANY: AS400 or Oracle] | Brokers (specific duties, statistics) | Wrong specific duty; rejected lines; statistics errors |
| Other-agency attributes (PGA, OGD, NOM data) | [COMPANY] | Brokers | Holds, refused entries, delays |
| Additional-duty indicators (Chapter 99, AD/CVD case, surtax) | Tariff-Impact Briefs; [COMPANY: where flags are stored] | Brokers, Standard Cost | Underpaid duties; wrong cost and margin |
| Duty rate used in standard cost | [COMPANY: name of std-cost tool] | Standard Cost, Finance | Wrong inventory value; PPV that nobody can explain |
| Broker entry data returned (entry, CAD or pedimento numbers, lines, duty paid) | [COMPANY: broker files, SQL Server, data warehouse] | Audits, PPV, drawback, reports | Audits impossible; PPV unexplained; drawback claims lack import support |
| IMMEX status and temporary import pedimento references | [COMPANY] | Mexico broker, Anexo 24 system | Inputs exceed time limits and are deemed to be in Mexico illegally, with duties, taxes and fines |
| ECCN, Schedule B and export flags | [COMPANY] | Exports, EEI filers | Wrong license determination; EEI errors |
| Supplier certifications and expiry dates | [COMPANY: certificate repository] | USMCA claims, verifications | Expired support; claims denied in a verification |

## 15. Time-sensitive topics: where to look instead

This primer deliberately does not state the current status of anything that changes often. For each of these, use `docs/primers/current-tariff-landscape.md` and the primary sources it lists, and record the date you checked:

- Which additional duties are in force (Section 232, Section 301, IEEPA-based actions and their replacements, other Chapter 99 measures), their HTS scope, rates, exclusions and stacking.
- US low-value (Section 321 "de minimis") treatment, and the informal-entry limit for goods with Chapter 99 duties (Section 4.3).
- MPF minimum and maximum, MPF and HMF rates.
- Canadian surtax orders and countermeasures; Mexican TIGIE changes and decrees.
- The USMCA joint review and any changes to the agreement's rules or term.
- Current duty rates for any specific HTS, tariff item or fracción.

## 16. Self-check questions

Answer without notes first, then check against the section shown. The Manager builds the day-30 knowledge check (Mon 11/16) from questions like these and the Anki decks.

| No. | Question | Where to check |
|---|---|---|
| 1 | Our US broker files a wrong HTS number using data we supplied. Who is liable to CBP, and what legal duty did we fail? | 1 |
| 2 | What is the difference between the US entry (CBP Form 3461) and the entry summary (CBP Form 7501), and when is the summary due? | 4.2 |
| 3 | An entry liquidated last month and you find a classification error. Which correction routes are still open, and who decides? | 4.2, 13 |
| 4 | Why does an ocean entry usually carry HMF while a truck entry from Mexico does not? | 4.3 |
| 5 | What replaced the B3 in Canada, and what must an importer post to use release prior to payment? | 5.1 |
| 6 | A Canadian CAD was filed with the wrong origin, and you noticed it today. What clock has started, and how long is it? | 5.2 |
| 7 | Which registrations must a Mexican importer hold before an agente aduanal can file a pedimento for it? | 6.1 |
| 8 | Is international freight part of the customs value in the US, in Canada and in Mexico? | 3.3, 9.3 |
| 9 | Name the three parts of a Mexican 10-digit code and the US 10-digit code, and which digits set the duty rate. | 3.2, 8.1 |
| 10 | Why must you read the section and chapter notes before choosing a heading, and when do you move past GRI 1? | 8.2 |
| 11 | A "kit" holds a flashlight, batteries and a strap, packed for retail sale. What three conditions decide whether it is classified as one set? | 8.3 |
| 12 | Is a CROSS ruling issued to another importer binding for our item? How should you use it? | 8.5 |
| 13 | We paid US$6,000 for tooling that our supplier uses to make our parts. What is it called, and what must happen to its value? | 9.3 |
| 14 | Why can an item assembled in Mexico from Chinese parts be "of Mexico" for a China-specific additional duty yet fail USMCA? | 10.1 |
| 15 | Write the USMCA transaction value and net cost RVC formulas, and say why net cost usually needs the producer's data. | 10.4 |
| 16 | One non-originating component fails the required tariff shift. Which two provisions might still let the good qualify? | 10.5, 10.8 |
| 17 | List the nine minimum data elements of a USMCA certification. How long can a blanket period be? | 10.7 |
| 18 | We learn after entry that a USMCA certification we relied on is wrong. What must we do? | 10.7, 13.2 |
| 19 | What does an IMMEX temporary import defer, and what do Anexo 24 and the SCCCyG (Anexo 30, formerly Anexo 31) each track? | 11.1 |
| 20 | What is the maximum share of duties refunded under US drawback, what is the general time limit, and who owns drawback in our team? | 11.2 |
| 21 | What does EAR99 mean, and in which three situations might an EAR99 item still need a license? | 12.1 |
| 22 | A US$12,000 shipment of EAR99 goods, all under one Schedule B number, needs no license. Is EEI required if it goes to Canada? To Mexico? | 12.2 |
| 23 | Which four fields do you compare first when auditing a filed entry line, and who owns the fix for each? | 7.3 |
| 24 | You find an error affecting 40 entries. List the first four things you do, in order. | 13.2 |
| 25 | Why must our item data keep classification history with effective dates, and what happens on 1 January 2028? | 8.1 |

## 17. Glossary, Anki and further reading

- **Glossary:** `data/trackers/glossary.csv` (also the Glossary tab in the trackers workbook). Add a term when you meet one that is missing, with a source.
- **Anki:** deck 01 (customs, classification and USMCA) and deck 02 (programs, exports and cost) cover this primer. Write company-specific cards with `docs/templates/knowledge/anki-card-writing-guide.md`.
- **Current status of tariff actions:** `docs/primers/current-tariff-landscape.md`.
- **Systems view of the same data:** `docs/primers/trade-systems-gtm-e2open-primer.md`.

Official sources (primary sources win over this primer):

| Topic | Source | Link |
|---|---|---|
| US importing overview | CBP, Importing into the United States | https://www.cbp.gov/document/publications/importing-united-states |
| US informed compliance publications (reasonable care, valuation, classification and more) | CBP | https://www.cbp.gov/trade/rulings/informed-compliance-publications |
| HTSUS | USITC | https://hts.usitc.gov/ |
| US rulings | CBP CROSS | https://rulings.cbp.gov/ |
| US regulations (19 CFR) | eCFR | https://www.ecfr.gov/current/title-19 |
| US recordkeeping | 19 CFR Part 163 | https://www.ecfr.gov/current/title-19/chapter-I/part-163 |
| US penalties | 19 U.S.C. 1592 | https://www.law.cornell.edu/uscode/text/19/1592 |
| US prior disclosure | CBP informed compliance publication | https://www.cbp.gov/sites/default/files/assets/documents/2020-Feb/Prior%20Disclosure%20FINAL.pdf |
| US rules of origin for marking (goods of Canada and Mexico) | 19 CFR Part 102 | https://www.ecfr.gov/current/title-19/chapter-I/part-102 |
| US marking | 19 CFR Part 134 | https://www.ecfr.gov/current/title-19/chapter-I/part-134 |
| US drawback | CBP drawback overview; 19 CFR Part 190 | https://www.cbp.gov/trade/programs-administration/entry-summary/drawback-overview |
| US drawback recordkeeping | 19 CFR 190.15 | https://www.ecfr.gov/current/title-19/chapter-I/part-190/subpart-A/section-190.15 |
| USMCA text (all chapters) | USTR | https://ustr.gov/trade-agreements/free-trade-agreements/united-states-mexico-canada-agreement/agreement-between |
| USMCA rules of origin (Chapter 4) | USTR | https://ustr.gov/sites/default/files/files/agreements/FTA/USMCA/Text/04-Rules-of-Origin.pdf |
| USMCA origin procedures (Chapter 5) | USTR | https://ustr.gov/sites/default/files/files/agreements/FTA/USMCA/Text/05_Origin_Procedures.pdf |
| USMCA in the US | CBP USMCA pages and FAQs | https://www.cbp.gov/trade/priority-issues/trade-agreements/free-trade-agreements/USMCA |
| USMCA post-importation claims and MPF refunds | CBP USMCA Implementation Instructions Addendum (January 2021) | https://www.cbp.gov/document/guidance/usmca-implementation-instructions-addendum |
| CARM | CBSA | https://www.cbsa-asfc.gc.ca/services/carm-gcra/menu-eng.html |
| Canada Customs Tariff | CBSA | https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/menu-eng.html |
| Canada valuation | CBSA customs valuation handbook | https://www.cbsa-asfc.gc.ca/import/valuation-valeur/customs-val-douane-eng.html |
| Canada exchange rate for value for duty | Memorandum D13-2-3 | https://www.cbsa-asfc.gc.ca/publications/dm-md/d13/d13-2-3-eng.html |
| Canada classification advance rulings | Memorandum D11-11-3 | https://www.cbsa-asfc.gc.ca/publications/dm-md/d11/d11-11-3-eng.html |
| Canada origin advance rulings | Memorandum D11-4-16 | https://www.cbsa-asfc.gc.ca/publications/dm-md/d11/d11-4-16-eng.html |
| Canada corrections (s. 32.2) | Memorandum D11-6-6 | https://www.cbsa-asfc.gc.ca/publications/dm-md/d11/d11-6-6-eng.html |
| Canada AMPS | Memorandum D22-1-1 | https://www.cbsa-asfc.gc.ca/publications/dm-md/d22/d22-1-1-eng.html |
| Mexico customs | ANAM | https://www.anam.gob.mx/ |
| Mexico RGCE 2026 and annexes (Anexo 22 pedimento, Anexo 24, Anexo 30) | SAT | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/normatividad_rmf_rgce2026.html |
| Mexico padrón de importadores | SAT | https://www.sat.gob.mx/minisitio/PadronImportadoresExportadores/pi_inscripcion.html |
| Mexico official gazette | DOF | https://www.dof.gob.mx/ |
| Mexico single window decree (4 May 2026) | DOF | https://www.dof.gob.mx/nota_detalle.php?codigo=5786598&fecha=04/05/2026 |
| IMMEX | SNICE (Secretaría de Economía) | https://www.snice.gob.mx/cs/avi/snice/progfom.immex.acercade.html |
| EAR | BIS | https://www.bis.gov/regulations/ear |
| EEI and AES | Census Bureau | https://www.census.gov/foreign-trade/aes/index.html |
| Foreign Trade Regulations | 15 CFR Part 30 | https://www.ecfr.gov/current/title-15/subtitle-B/chapter-I/part-30 |
| Schedule B | Census Bureau | https://www.census.gov/scheduleb |
| Restricted party screening | Consolidated Screening List (trade.gov) | https://www.trade.gov/consolidated-screening-list |
