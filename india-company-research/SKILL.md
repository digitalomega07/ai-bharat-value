---
name: india-company-research
description: Use for india company research of Indian listed equities with point-in-time, source-backed evidence. Trigger when the user asks to run india-company-research or requests the corresponding India public-equity workflow.
---

# India Company Research

Research `$ARGUMENTS` as an Indian listed company using point-in-time, source-backed evidence.

## Guardrails

- This is research and education, not personalized investment advice.
- Do not invent a price, filing, management statement, estimate, or source.
- Use an explicit as-of date. Exclude information published after it.
- Prefer consolidated financials unless the question requires standalone results; state the perimeter.
- Classify each conclusion as reported fact, adjusted figure, estimate, or inference.
- A clear verdict is required, but it is a research-priority verdict rather than a trade instruction.

## Workflow

### 1. Identity and evidence map

Confirm legal name, NSE/BSE symbols, ISIN when available, sector, fiscal year-end, reporting currency, as-of date, and whether the company changed name or structure. List the filings used.

Primary-source order: exchange/SEBI filing; annual report or audited result; investor presentation/transcript; credit-rating rationale; regulator/government/industry body; reputable secondary source.

### 2. Information-quality rating

Rate `A`, `B`, or `C` based on filing history, segment disclosure, accounting stability, and availability of independent evidence. State what remains unverifiable.

### 3. Business economics

Explain the business in plain language. Cover revenue segments, customer and supplier concentration, unit economics, pricing power, recurrence, capital intensity, working capital, reinvestment runway, and key regulation.

### 4. Industry structure and moat

Test brand, switching costs, distribution, cost advantage, network effect, licences, process capability, scale, and access to scarce inputs. For every claimed moat, provide observable evidence and a plausible erosion path.

### 5. Financial quality

Build at least five years of revenue, EBITDA/EBIT, PAT, CFO, capex, FCF, net debt, shares, ROCE, ROE, margins, and working-capital days. Reconcile PAT to CFO. Explain exceptional items and acquisitions.

Do not apply industrial-company metrics mechanically to banks, NBFCs, insurers, REITs, utilities, or commodity companies. Use a sector module or mark the analysis incomplete.

### 6. Promoter, management, and capital allocation

Review promoter ownership and pledging, dilution, warrants, remuneration, related parties, acquisitions, divestments, dividends, buybacks, capital expenditure, and succession. Separate economic ownership from control.

### 7. Forensic quick scan

Check auditor changes/qualifications, cash conversion, receivables, inventory, other income, capitalized expenses, CWIP, contingent liabilities, guarantees, tax rate, subsidiary transactions, and unexplained restatements. Escalate material concerns to `india-forensic-accounting`.

### 8. Valuation

Use at least two appropriate methods. Possible methods include reverse DCF, normalized P/E, EV/EBITDA, FCF yield, residual income, sum-of-parts, or sector-specific book-value methods. Show bull/base/bear assumptions, probability only when defensible, and sensitivity to the two most important variables.

### 9. Inversion and variant perception

State why a capable sceptic would reject the thesis, how the company could permanently impair capital, what expectations appear priced in, and what evidence would prove the current view wrong.

### 10. Decision memo

Output:

| Dimension | Conclusion | Evidence quality | Confidence |
|---|---|---|---|
| Business quality | | | |
| Moat direction | | | |
| Financial quality | | | |
| Governance | | | |
| Reinvestment | | | |
| Valuation | | | |
| Principal risk | | | |

Finish with one verdict: `Pass for deeper diligence`, `Watch`, `Needs primary verification`, or `Reject for further work`. Include prove/kill triggers, missing evidence, source list, and limitations.


