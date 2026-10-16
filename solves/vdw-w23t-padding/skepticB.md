# Skeptic B — Hunt 58: w(2;3,32) ≥ 1012, w(2;3,36) ≥ 1260
Independent; skepticA not read. Code: skB/sk.py (own regex parser of tex/main.tex App. A.2 + set-based checker).

## Re-derivation
- Parsed AKS paragraphs "vdw(2;3,32) > 1006" and "vdw(2;3,36) > 1257" myself: lengths 1006 / 1257, both valid.
- NEW_t32_n1011 = "11111" + AKS_t32 exactly; NEW_t36_n1259 = "11" + AKS_t36 exactly. Same strings as Hunt 58 (sha256 4b3b2305…, f26c9eb6…).
- Set-based checker: colour 0 has no 3-AP (all pairs a<b, test 2b−a), colour 1 has no t-AP (all start, all d). Both NEW certs PASS.
- Self-tests: planted 000 at start → caught (0-3AP); 1^32 rejected at t=32, 1^31 accepted; AKS t=36 cert rejected at t=35 (correct sensitivity).

## Break attempts
- Convention: AKS w(2;3,t) = least n s.t. every 2-colouring of {1..n} has 3-AP in colour 0 or t-AP in colour 1; "w > n" = valid length-n certificate. Certs use 0 = sparse 3-AP-free colour, 1 = t-AP-free. Matches.
- Off-by-one: length 1011 valid ⇒ w ≥ 1012 (AKS: w > 1006 i.e. ≥1007). Length 1259 ⇒ w ≥ 1260 (AKS ≥1258). Gains +5 and +2. Correct.
- Padding-spanning APs: the full padded string is checked, so any red/blue AP through the prefix is covered. Maximality confirmed: 1^6 prefix fails at t=32 (1-AP start 0, d=5); 1^3 prefix fails at t=36 (d=34). Appending 0/1 at the end or 0 at front fails for both.
- Table: OEIS A171081 (fetched today) only has Marcano a(31)≥954, a(33)≥1072 (Aug 2026). Marcano paper (local pdf, Zenodo 21943191) explicitly says t=32 not surpassed; lists AKS 1006/1257 as current. Luo 21718186 = restricted, t=39 only (≥1421). Luo 21855349: Zenodo API 410 "record has been deleted" — no competing claim there. Zenodo "van der Waerden" recent search: nothing on t=32/36.

## Verdict
- Validity: ACCEPT (both certificates valid; bounds w(2;3,32) ≥ 1012, w(2;3,36) ≥ 1260 correct).
- Novelty: MINOR (appear to be new records as far as checkable, but obtained by trivial prefix padding of 2014 published certs; Luo's t=39 +2 suggests others use the same trick).
- OEIS comment: yes, worth a short comment in A171081 style ("a(32) ≥ 1012, a(36) ≥ 1260; previous AKS 1007/1258"), with cert files linked. Honest framing: extension of AKS certificates by padding.
