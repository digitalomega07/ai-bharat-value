# India Quality Screen

Screen `$ARGUMENTS` to remove clearly weak candidates while minimizing false rejection of high-quality companies.

## Rules

- Fix an as-of date and use the constituent universe known on that date.
- Include delisted, merged, and failed companies in historical tests.
- Never infer missing values as passing.
- Compare primarily within sectors and flag sector-inappropriate metrics.
- Screening selects candidates for diligence; it does not create buy recommendations.

## Industrial-company checks

Use a full-cycle or five-year median where practicable:

1. ROCE and incremental ROIC
2. CFO/PAT cash conversion
3. Cumulative FCF after maintenance and growth capex
4. Net debt/EBITDA and interest coverage
5. Gross and operating-margin stability versus peers
6. Receivable and inventory days trend
7. Share-count dilution, warrants, and preferential allotments
8. Promoter pledge and ownership trend
9. Related-party transactions relative to revenue/assets
10. Auditor qualifications, resignations, and restatements

Do not use universal cut-offs blindly. State the sector distribution and explain each threshold.

## Sector routing

- Banks/NBFCs: asset quality, provision coverage, capital adequacy, liability franchise, NIM, credit cost, and underwriting-cycle performance.
- Insurers: VNB, persistency, solvency, product mix, claim experience, and embedded-value quality.
- REITs: occupancy, WALE, distribution coverage, leverage, sponsor quality, and asset concentration.
- Commodity/cyclical: mid-cycle margins, cost-curve position, balance-sheet survival, and capital discipline.
- Utilities/PSUs: regulated returns, receivables, government exposure, capital allocation, and minority-shareholder treatment.

## Output

Provide the full screened universe with values, sources, missing-data flags, keep/drop reason, and sector. Separate `Pass`, `Borderline`, `Data insufficient`, and `Reject for further work`. Finish with a reproducibility note covering universe date, publication cutoff, corporate actions, and survivorship treatment.

