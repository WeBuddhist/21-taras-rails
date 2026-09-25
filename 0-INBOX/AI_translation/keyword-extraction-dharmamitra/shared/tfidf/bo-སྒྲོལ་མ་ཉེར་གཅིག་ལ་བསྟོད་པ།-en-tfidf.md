---
title: TF-IDF Vocabulary Analysis — bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en
source: /sessions/rcw-01hesxe9hczshzdudaktd6ke/mnt/21-taras-rails/3-TRANSFORMATIONS/Translations/machine-drafts/zero-shot/dharmamitra-en/bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en.md
corpus: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth_idf=True)
method: TF × IDF — term frequency in translation vs. inverse document frequency in Reuters corpus
generated: 2026-09-24
unique_terms: 318
total_content_tokens: 457
status: draft
---

# TF-IDF Vocabulary Analysis — bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en

Generated **2026-09-24** · source: `bo-སྒྲོལ་མ་ཉེར་གཅིག་ལ་བསྟོད་པ།-en.md` · **318 unique content terms** ranked.

This report answers two questions:

1. **Which words in this translation are most frequent here but rare in everyday English?**  
   → High TF-IDF score. These are the lexical signatures of the text.
2. **Which words appear in the text but are also very common in general English?**  
   → Low TF-IDF score. These look familiar but carry specialist meaning here.

---

## Methodology

**Term Frequency (TF)** — count of each word in the translation, normalised by total content-token count.
Frontmatter, verse markers (`^1-2`), numbers and markdown syntax are stripped before counting.

**Inverse Document Frequency (IDF)** — computed from the Reuters-21578 newswire corpus
(10,788 documents, ~1.3 M tokens) using sklearn's smooth IDF formula:
`idf(t) = log((1 + N) / (1 + df(t))) + 1`. Corpus maximum ≈ 9.59. Scale:

| IDF range | Meaning |
|-----------|---------|
| 1.0 – 1.5 | Function word — present in virtually every document |
| 1.5 – 3.0 | Common content word — high general-English frequency |
| 3.0 – 6.0 | Moderately rare — limited domain or register |
| 6.0 – 9.0 | Uncommon / archaic — rare in Reuters |
| 9.59 (max) | Absent from Reuters — domain-exclusive, coined, or Pāli |

**TF-IDF score** = TF × IDF × 10⁶ (scaled for readability).

**Colour bands** used in the table:

| Band | Score range | Interpretation |
|------|-------------|----------------|
| 🔴 | ≥ 50,000 | Text-exclusive — word essentially does not exist outside this translation |
| 🟠 | 10,000 – 49,999 | Domain-specific — Buddhist / Abhidhamma vocabulary |
| 🟡 | 3,000 – 9,999 | Specialist register — unusual in general English |
| 🟢 | 500 – 2,999 | Moderately distinctive — identifiable domain presence |
| 🔵 | 50 – 499 | Moderately common — has general English presence |
| ⚪ | 0 – 49 | Universal / function word |

---

## Distribution by Band

| Band | Terms | % of vocabulary |
|------|-------|----------------|
| 🔴 extremely high — text-exclusive | 22 | 6.9% |
| 🟠 very high — domain-specific | 290 | 91.2% |
| 🟡 high — specialist register | 6 | 1.9% |
| 🟢 medium — moderately distinctive | 0 | 0.0% |
| 🔵 low — common in general English | 0 | 0.0% |
| ⚪ very low — function / universal word | 0 | 0.0% |

---

## Most Distinctive Words (highest TF-IDF)

Words that appear **frequently in this text** yet are **rare or absent in general English**.

**1. homage** — count: 24, TF-IDF: 503,632, IDF: 9.59 🔴 extremely high — text-exclusive
**2. tārā** — count: 5, TF-IDF: 104,923, IDF: 9.59 🔴 extremely high — text-exclusive
**3. hūṃ** — count: 5, TF-IDF: 104,923, IDF: 9.59 🔴 extremely high — text-exclusive
**4. praise** — count: 4, TF-IDF: 83,966, IDF: 9.593135 🔴 extremely high — text-exclusive
**5. hosts** — count: 4, TF-IDF: 83,939, IDF: 9.59 🔴 extremely high — text-exclusive
**6. destroys** — count: 4, TF-IDF: 83,939, IDF: 9.59 🔴 extremely high — text-exclusive
**7. syllable** — count: 4, TF-IDF: 83,939, IDF: 9.59 🔴 extremely high — text-exclusive
**8. every** — count: 5, TF-IDF: 63,432, IDF: 5.797646 🔴 extremely high — text-exclusive
**9. blazing** — count: 3, TF-IDF: 62,975, IDF: 9.593135 🔴 extremely high — text-exclusive
**10. utterly** — count: 3, TF-IDF: 62,975, IDF: 9.593135 🔴 extremely high — text-exclusive
**11. joy** — count: 3, TF-IDF: 62,975, IDF: 9.593135 🔴 extremely high — text-exclusive
**12. twenty-one** — count: 3, TF-IDF: 62,954, IDF: 9.59 🔴 extremely high — text-exclusive
**13. syllables** — count: 3, TF-IDF: 62,954, IDF: 9.59 🔴 extremely high — text-exclusive
**14. ture** — count: 3, TF-IDF: 62,954, IDF: 9.59 🔴 extremely high — text-exclusive
**15. moon** — count: 3, TF-IDF: 62,954, IDF: 9.59 🔴 extremely high — text-exclusive
**16. endowed** — count: 3, TF-IDF: 62,954, IDF: 9.59 🔴 extremely high — text-exclusive
**17. lotus** — count: 3, TF-IDF: 60,313, IDF: 9.18767 🔴 extremely high — text-exclusive
**18. worlds** — count: 3, TF-IDF: 60,313, IDF: 9.18767 🔴 extremely high — text-exclusive
**19. light** — count: 5, TF-IDF: 59,715, IDF: 5.457969 🔴 extremely high — text-exclusive
**20. peace** — count: 3, TF-IDF: 56,960, IDF: 8.676844 🔴 extremely high — text-exclusive
**21. perfectly** — count: 3, TF-IDF: 53,874, IDF: 8.206841 🔴 extremely high — text-exclusive
**22. spirits** — count: 3, TF-IDF: 50,201, IDF: 7.647225 🔴 extremely high — text-exclusive
**23. complete** — count: 4, TF-IDF: 47,772, IDF: 5.457969 🟠 very high — domain-specific
**24. exception** — count: 3, TF-IDF: 47,234, IDF: 7.19524 🟠 very high — domain-specific
**25. completely** — count: 3, TF-IDF: 45,420, IDF: 6.918987 🟠 very high — domain-specific
**26. intensely** — count: 2, TF-IDF: 41,983, IDF: 9.593135 🟠 very high — domain-specific
**27. brilliant** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**28. adorned** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**29. sphere** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**30. realms** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**31. trampling** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**32. summon** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**33. zombies** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**34. yak** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**35. phaṭ** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**36. tuttāre** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**37. frown** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**38. enemies** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**39. shatters** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**40. mantra** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**41. reciting** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**42. gods** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**43. dispels** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**44. goddess** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**45. recollection** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**46. poisons** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**47. desiring** — count: 2, TF-IDF: 41,969, IDF: 9.59 🟠 very high — domain-specific
**48. eyes** — count: 2, TF-IDF: 40,209, IDF: 9.18767 🟠 very high — domain-specific
**49. leg** — count: 2, TF-IDF: 38,950, IDF: 8.899988 🟠 very high — domain-specific
**50. child** — count: 2, TF-IDF: 38,950, IDF: 8.899988 🟠 very high — domain-specific

---

## Least Distinctive Words (lowest TF-IDF)

Words that appear in this text but are also extremely common in general English.

**1. end** — count: 1, TF-IDF: 8,069.53, IDF: 3.687773 🟡 high — specialist register
**2. world** — count: 1, TF-IDF: 8,539.99, IDF: 3.902776 🟡 high — specialist register
**3. lower** — count: 1, TF-IDF: 8,551.11, IDF: 3.907856 🟡 high — specialist register
**4. state** — count: 1, TF-IDF: 9,359.89, IDF: 4.277469 🟡 high — specialist register
**5. off** — count: 1, TF-IDF: 9,562.54, IDF: 4.37008 🟡 high — specialist register
**6. levels** — count: 1, TF-IDF: 9,640.59, IDF: 4.405749 🟡 high — specialist register
**7. within** — count: 1, TF-IDF: 10,005.58, IDF: 4.57255 🟠 very high — domain-specific
**8. whether** — count: 1, TF-IDF: 10,162.75, IDF: 4.644375 🟠 very high — domain-specific
**9. gold** — count: 1, TF-IDF: 10,647.15, IDF: 4.865747 🟠 very high — domain-specific
**10. local** — count: 1, TF-IDF: 11,322.31, IDF: 5.174295 🟠 very high — domain-specific
**11. holds** — count: 1, TF-IDF: 11,573.46, IDF: 5.28907 🟠 very high — domain-specific
**12. able** — count: 1, TF-IDF: 11,573.46, IDF: 5.28907 🟠 very high — domain-specific
**13. greater** — count: 1, TF-IDF: 11,726.54, IDF: 5.359029 🟠 very high — domain-specific
**14. head** — count: 1, TF-IDF: 11,943.04, IDF: 5.457969 🟠 very high — domain-specific
**15. activity** — count: 1, TF-IDF: 12,163.88, IDF: 5.558895 🟠 very high — domain-specific
**16. times** — count: 1, TF-IDF: 12,262.91, IDF: 5.604151 🟠 very high — domain-specific
**17. various** — count: 1, TF-IDF: 12,303.81, IDF: 5.622843 🟠 very high — domain-specific
**18. having** — count: 1, TF-IDF: 12,324.56, IDF: 5.632322 🟠 very high — domain-specific
**19. others** — count: 1, TF-IDF: 12,366.64, IDF: 5.651553 🟠 very high — domain-specific
**20. together** — count: 1, TF-IDF: 12,387.99, IDF: 5.66131 🟠 very high — domain-specific
**21. opening** — count: 1, TF-IDF: 12,409.54, IDF: 5.671162 🟠 very high — domain-specific
**22. away** — count: 1, TF-IDF: 12,711.04, IDF: 5.808946 🟠 very high — domain-specific
**23. moving** — count: 1, TF-IDF: 12,786.94, IDF: 5.843631 🟠 very high — domain-specific
**24. granted** — count: 1, TF-IDF: 13,060.82, IDF: 5.968794 🟠 very high — domain-specific
**25. speech** — count: 1, TF-IDF: 13,090.19, IDF: 5.982217 🟠 very high — domain-specific
**26. brings** — count: 1, TF-IDF: 13,243.27, IDF: 6.052176 🟠 very high — domain-specific
**27. india** — count: 1, TF-IDF: 13,373.95, IDF: 6.111895 🟠 very high — domain-specific
**28. direction** — count: 1, TF-IDF: 13,407.88, IDF: 6.127399 🟠 very high — domain-specific
**29. actual** — count: 1, TF-IDF: 13,407.88, IDF: 6.127399 🟠 very high — domain-specific
**30. bad** — count: 1, TF-IDF: 13,512.93, IDF: 6.175409 🟠 very high — domain-specific
**31. clearly** — count: 1, TF-IDF: 13,820.55, IDF: 6.31599 🟠 very high — domain-specific
**32. concluded** — count: 1, TF-IDF: 13,904.72, IDF: 6.354457 🟠 very high — domain-specific
**33. proceed** — count: 1, TF-IDF: 13,904.72, IDF: 6.354457 🟠 very high — domain-specific
**34. sun** — count: 1, TF-IDF: 14,227.77, IDF: 6.502093 🟠 very high — domain-specific
**35. million** — count: 1, TF-IDF: 14,382.30, IDF: 6.57271 🟠 very high — domain-specific
**36. twice** — count: 1, TF-IDF: 14,436.33, IDF: 6.597403 🟠 very high — domain-specific
**37. lake** — count: 1, TF-IDF: 14,548.57, IDF: 6.648696 🟠 very high — domain-specific
**38. strikes** — count: 1, TF-IDF: 14,548.57, IDF: 6.648696 🟠 very high — domain-specific
**39. under** — count: 2, TF-IDF: 14,660.57, IDF: 3.34994 🟠 very high — domain-specific
**40. autumn** — count: 1, TF-IDF: 14,791.95, IDF: 6.759922 🟠 very high — domain-specific
**41. experience** — count: 1, TF-IDF: 14,857.28, IDF: 6.789775 🟠 very high — domain-specific
**42. desire** — count: 1, TF-IDF: 14,857.28, IDF: 6.789775 🟠 very high — domain-specific
**43. drawn** — count: 1, TF-IDF: 15,140.02, IDF: 6.918987 🟠 very high — domain-specific
**44. heart** — count: 1, TF-IDF: 15,296.38, IDF: 6.990446 🟠 very high — domain-specific
**45. gone** — count: 1, TF-IDF: 15,378.96, IDF: 7.028186 🟠 very high — domain-specific
**46. arranged** — count: 1, TF-IDF: 15,378.96, IDF: 7.028186 🟠 very high — domain-specific
**47. crown** — count: 1, TF-IDF: 15,464.79, IDF: 7.067407 🟠 very high — domain-specific
**48. space** — count: 1, TF-IDF: 15,464.79, IDF: 7.067407 🟠 very high — domain-specific
**49. person** — count: 1, TF-IDF: 15,647.24, IDF: 7.150788 🟠 very high — domain-specific
**50. thousand** — count: 1, TF-IDF: 15,647.24, IDF: 7.150788 🟠 very high — domain-specific

---

## Full Ranked Table

All 318 content terms, sorted by TF-IDF descending.

| Rank | Word | Count | TF-IDF | IDF | Band |
|------|------|-------|--------|-----|------|
| 1 | **homage** | 24 | 503,632.39 | 9.59 | 🔴 extremely high — text-exclusive |
| 2 | **tārā** | 5 | 104,923.41 | 9.59 | 🔴 extremely high — text-exclusive |
| 3 | **hūṃ** | 5 | 104,923.41 | 9.59 | 🔴 extremely high — text-exclusive |
| 4 | **praise** | 4 | 83,966.17 | 9.593135 | 🔴 extremely high — text-exclusive |
| 5 | **hosts** | 4 | 83,938.73 | 9.59 | 🔴 extremely high — text-exclusive |
| 6 | **destroys** | 4 | 83,938.73 | 9.59 | 🔴 extremely high — text-exclusive |
| 7 | **syllable** | 4 | 83,938.73 | 9.59 | 🔴 extremely high — text-exclusive |
| 8 | **every** | 5 | 63,431.58 | 5.797646 | 🔴 extremely high — text-exclusive |
| 9 | **blazing** | 3 | 62,974.63 | 9.593135 | 🔴 extremely high — text-exclusive |
| 10 | **utterly** | 3 | 62,974.63 | 9.593135 | 🔴 extremely high — text-exclusive |
| 11 | **joy** | 3 | 62,974.63 | 9.593135 | 🔴 extremely high — text-exclusive |
| 12 | **twenty-one** | 3 | 62,954.05 | 9.59 | 🔴 extremely high — text-exclusive |
| 13 | **syllables** | 3 | 62,954.05 | 9.59 | 🔴 extremely high — text-exclusive |
| 14 | **ture** | 3 | 62,954.05 | 9.59 | 🔴 extremely high — text-exclusive |
| 15 | **moon** | 3 | 62,954.05 | 9.59 | 🔴 extremely high — text-exclusive |
| 16 | **endowed** | 3 | 62,954.05 | 9.59 | 🔴 extremely high — text-exclusive |
| 17 | **lotus** | 3 | 60,312.93 | 9.18767 | 🔴 extremely high — text-exclusive |
| 18 | **worlds** | 3 | 60,312.93 | 9.18767 | 🔴 extremely high — text-exclusive |
| 19 | **light** | 5 | 59,715.20 | 5.457969 | 🔴 extremely high — text-exclusive |
| 20 | **peace** | 3 | 56,959.59 | 8.676844 | 🔴 extremely high — text-exclusive |
| 21 | **perfectly** | 3 | 53,874.23 | 8.206841 | 🔴 extremely high — text-exclusive |
| 22 | **spirits** | 3 | 50,200.60 | 7.647225 | 🔴 extremely high — text-exclusive |
| 23 | **complete** | 4 | 47,772.16 | 5.457969 | 🟠 very high — domain-specific |
| 24 | **exception** | 3 | 47,233.52 | 7.19524 | 🟠 very high — domain-specific |
| 25 | **completely** | 3 | 45,420.05 | 6.918987 | 🟠 very high — domain-specific |
| 26 | **intensely** | 2 | 41,983.09 | 9.593135 | 🟠 very high — domain-specific |
| 27 | **brilliant** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 28 | **adorned** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 29 | **sphere** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 30 | **realms** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 31 | **trampling** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 32 | **summon** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 33 | **zombies** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 34 | **yak** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 35 | **phaṭ** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 36 | **tuttāre** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 37 | **frown** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 38 | **enemies** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 39 | **shatters** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 40 | **mantra** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 41 | **reciting** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 42 | **gods** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 43 | **dispels** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 44 | **goddess** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 45 | **recollection** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 46 | **poisons** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 47 | **desiring** | 2 | 41,969.37 | 9.59 | 🟠 very high — domain-specific |
| 48 | **eyes** | 2 | 40,208.62 | 9.18767 | 🟠 very high — domain-specific |
| 49 | **leg** | 2 | 38,949.62 | 8.899988 | 🟠 very high — domain-specific |
| 50 | **child** | 2 | 38,949.62 | 8.899988 | 🟠 very high — domain-specific |
| 51 | **surrounded** | 2 | 37,973.06 | 8.676844 | 🟠 very high — domain-specific |
| 52 | **violent** | 2 | 37,973.06 | 8.676844 | 🟠 very high — domain-specific |
| 53 | **wealth** | 2 | 37,973.06 | 8.676844 | 🟠 very high — domain-specific |
| 54 | **feet** | 3 | 37,913.06 | 5.775423 | 🟠 very high — domain-specific |
| 55 | **face** | 3 | 36,728.23 | 5.594934 | 🟠 very high — domain-specific |
| 56 | **gathered** | 2 | 35,400.69 | 8.089058 | 🟠 very high — domain-specific |
| 57 | **power** | 3 | 34,632.26 | 5.275647 | 🟠 very high — domain-specific |
| 58 | **like** | 3 | 34,086.64 | 5.192532 | 🟠 very high — domain-specific |
| 59 | **mass** | 2 | 33,165.13 | 7.578232 | 🟠 very high — domain-specific |
| 60 | **language** | 2 | 32,617.37 | 7.453069 | 🟠 very high — domain-specific |
| 61 | **supreme** | 2 | 31,294.48 | 7.150788 | 🟠 very high — domain-specific |
| 62 | **without** | 3 | 30,996.25 | 4.721762 | 🟠 very high — domain-specific |
| 63 | **destroyed** | 2 | 29,849.22 | 6.820546 | 🟠 very high — domain-specific |
| 64 | **fire** | 2 | 28,261.01 | 6.457641 | 🟠 very high — domain-specific |
| 65 | **hand** | 2 | 27,984.52 | 6.394462 | 🟠 very high — domain-specific |
| 66 | **obtain** | 2 | 27,478.99 | 6.278949 | 🟠 very high — domain-specific |
| 67 | **single** | 2 | 26,300.29 | 6.009616 | 🟠 very high — domain-specific |
| 68 | **benefits** | 2 | 25,087.11 | 5.732405 | 🟠 very high — domain-specific |
| 69 | **left** | 2 | 23,992.39 | 5.482261 | 🟠 very high — domain-specific |
| 70 | **extended** | 2 | 23,714.43 | 5.418748 | 🟠 very high — domain-specific |
| 71 | **right** | 2 | 22,514.74 | 5.144619 | 🟠 very high — domain-specific |
| 72 | **form** | 2 | 22,514.74 | 5.144619 | 🟠 very high — domain-specific |
| 73 | **praises** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 74 | **ati** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 75 | **flash** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 76 | **born** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 77 | **stars** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 78 | **children** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 79 | **victors** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 80 | **wheel** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 81 | **garland** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 82 | **palms** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 83 | **stamps** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 84 | **essence** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 85 | **meru** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 86 | **infectious** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 87 | **dawn** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 88 | **confer** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 89 | **potent** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 90 | **afflicted** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 91 | **fevers** | 1 | 20,991.54 | 9.593135 | 🟠 very high — domain-specific |
| 92 | **tārās** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 93 | **translator** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 94 | **nama** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 95 | **ekaviṃ** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 96 | **stotra** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 97 | **guṇahita** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 98 | **sāka** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 99 | **tibet** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 100 | **verses** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 101 | **venerable** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 102 | **heroic** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 103 | **stamens** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 104 | **moons** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 105 | **water-born** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 106 | **generosity** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 107 | **meditative** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 108 | **tathāgatas** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 109 | **perfection** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 110 | **tuttāra** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 111 | **fills** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 112 | **indra** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 113 | **agni** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 114 | **brahmā** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 115 | **vāyu** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 116 | **varas** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 117 | **worship** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 118 | **gandharvas** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 119 | **traṭ** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 120 | **magical** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 121 | **swirling** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 122 | **fearful** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 123 | **subduer** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 124 | **champions** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 125 | **māra** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 126 | **frowning** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 127 | **slays** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 128 | **mudrā** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 129 | **symbolizing** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 130 | **jewels** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 131 | **beautifully** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 132 | **adorn** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 133 | **graced** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 134 | **radiating** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 135 | **turbulent** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 136 | **brilliance** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 137 | **emits** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 138 | **garlands** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 139 | **radiant** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 140 | **majestic** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 141 | **laughter** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 142 | **demons** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 143 | **guardians** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 144 | **vibrating** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 145 | **liberates** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 146 | **destitution** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 147 | **crescent** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 148 | **ornament** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 149 | **blazes** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 150 | **matted** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 151 | **amitābha** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 152 | **radiates** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 153 | **dwells** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 154 | **conflagration** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 155 | **eon** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 156 | **bent** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 157 | **armies** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 158 | **tramples** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 159 | **wrathful** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 160 | **underworld** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 161 | **blissful** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 162 | **virtuous** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 163 | **nirvāṇa** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 164 | **svāhā** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 165 | **negativity** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 166 | **ten-syllable** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 167 | **lamp** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 168 | **seed-syllable** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 169 | **mandara** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 170 | **vindhya** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 171 | **tremble** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 172 | **deer-marked** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 173 | **celestial** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 174 | **tāra** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 175 | **kinnaras** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 176 | **majesty** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 177 | **joyful** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 178 | **dreams** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 179 | **hara** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 180 | **suchnesses** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 181 | **homages** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 182 | **devotion** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 183 | **recites** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 184 | **dusk** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 185 | **fearlessness** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 186 | **misdeeds** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 187 | **pacified** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 188 | **seventy** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 189 | **victorious** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 190 | **empowerment** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 191 | **buddhahood** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 192 | **stationary** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 193 | **drunk** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 194 | **masses** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 195 | **sentient** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 196 | **beings** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 197 | **recited** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 198 | **colophon** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 199 | **blessed** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 200 | **buddha** | 1 | 20,984.68 | 9.59 | 🟠 very high — domain-specific |
| 201 | **noble** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 202 | **patience** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 203 | **infinite** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 204 | **attained** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 205 | **wheels** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 206 | **amidst** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 207 | **fingers** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 208 | **midst** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 209 | **constantly** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 210 | **armor** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 211 | **strife** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 212 | **eaten** | 1 | 20,104.31 | 9.18767 | 🟠 very high — domain-specific |
| 213 | **directions** | 1 | 19,474.81 | 8.899988 | 🟠 very high — domain-specific |
| 214 | **expression** | 1 | 19,474.81 | 8.899988 | 🟠 very high — domain-specific |
| 215 | **locks** | 1 | 19,474.81 | 8.899988 | 🟠 very high — domain-specific |
| 216 | **peaceful** | 1 | 19,474.81 | 8.899988 | 🟠 very high — domain-specific |
| 217 | **awareness** | 1 | 19,474.81 | 8.899988 | 🟠 very high — domain-specific |
| 218 | **desires** | 1 | 19,474.81 | 8.899988 | 🟠 very high — domain-specific |
| 219 | **enemy** | 1 | 18,986.53 | 8.676844 | 🟠 very high — domain-specific |
| 220 | **concentration** | 1 | 18,587.58 | 8.494523 | 🟠 very high — domain-specific |
| 221 | **earth** | 1 | 18,587.58 | 8.494523 | 🟠 very high — domain-specific |
| 222 | **clears** | 1 | 18,587.58 | 8.494523 | 🟠 very high — domain-specific |
| 223 | **trace** | 1 | 18,587.58 | 8.494523 | 🟠 very high — domain-specific |
| 224 | **thoroughly** | 1 | 18,587.58 | 8.494523 | 🟠 very high — domain-specific |
| 225 | **spoken** | 1 | 18,587.58 | 8.494523 | 🟠 very high — domain-specific |
| 226 | **lightning** | 1 | 18,250.27 | 8.340372 | 🟠 very high — domain-specific |
| 227 | **diseases** | 1 | 18,250.27 | 8.340372 | 🟠 very high — domain-specific |
| 228 | **full** | 2 | 18,184.05 | 4.155056 | 🟠 very high — domain-specific |
| 229 | **acts** | 1 | 17,958.08 | 8.206841 | 🟠 very high — domain-specific |
| 230 | **deeply** | 1 | 17,958.08 | 8.206841 | 🟠 very high — domain-specific |
| 231 | **intelligent** | 1 | 17,958.08 | 8.206841 | 🟠 very high — domain-specific |
| 232 | **genuine** | 1 | 17,958.08 | 8.206841 | 🟠 very high — domain-specific |
| 233 | **arisen** | 1 | 17,958.08 | 8.206841 | 🟠 very high — domain-specific |
| 234 | **swiftly** | 1 | 17,958.08 | 8.206841 | 🟠 very high — domain-specific |
| 235 | **most** | 2 | 17,854.29 | 4.079706 | 🟠 very high — domain-specific |
| 236 | **fulfilled** | 1 | 17,700.35 | 8.089058 | 🟠 very high — domain-specific |
| 237 | **title** | 1 | 17,469.80 | 7.983697 | 🟠 very high — domain-specific |
| 238 | **blue** | 1 | 17,469.80 | 7.983697 | 🟠 very high — domain-specific |
| 239 | **attain** | 1 | 17,469.80 | 7.983697 | 🟠 very high — domain-specific |
| 240 | **austerity** | 1 | 17,261.24 | 7.888387 | 🟠 very high — domain-specific |
| 241 | **praised** | 1 | 17,261.24 | 7.888387 | 🟠 very high — domain-specific |
| 242 | **causes** | 1 | 17,261.24 | 7.888387 | 🟠 very high — domain-specific |
| 243 | **root** | 1 | 17,261.24 | 7.888387 | 🟠 very high — domain-specific |
| 244 | **mount** | 1 | 17,070.84 | 7.801376 | 🟠 very high — domain-specific |
| 245 | **cast** | 1 | 17,070.84 | 7.801376 | 🟠 very high — domain-specific |
| 246 | **swift** | 1 | 16,895.70 | 7.721333 | 🟠 very high — domain-specific |
| 247 | **relied** | 1 | 16,895.70 | 7.721333 | 🟠 very high — domain-specific |
| 248 | **intense** | 1 | 16,895.70 | 7.721333 | 🟠 very high — domain-specific |
| 249 | **ultimate** | 1 | 16,895.70 | 7.721333 | 🟠 very high — domain-specific |
| 250 | **victory** | 1 | 16,733.53 | 7.647225 | 🟠 very high — domain-specific |
| 251 | **vast** | 1 | 16,733.53 | 7.647225 | 🟠 very high — domain-specific |
| 252 | **rely** | 1 | 16,733.53 | 7.647225 | 🟠 very high — domain-specific |
| 253 | **obstacles** | 1 | 16,733.53 | 7.647225 | 🟠 very high — domain-specific |
| 254 | **lord** | 1 | 16,582.56 | 7.578232 | 🟠 very high — domain-specific |
| 255 | **bodies** | 1 | 16,582.56 | 7.578232 | 🟠 very high — domain-specific |
| 256 | **poison** | 1 | 16,582.56 | 7.578232 | 🟠 very high — domain-specific |
| 257 | **ones** | 1 | 16,582.56 | 7.578232 | 🟠 very high — domain-specific |
| 258 | **meaning** | 1 | 16,441.34 | 7.513694 | 🟠 very high — domain-specific |
| 259 | **surface** | 1 | 16,441.34 | 7.513694 | 🟠 very high — domain-specific |
| 260 | **emerging** | 1 | 16,441.34 | 7.513694 | 🟠 very high — domain-specific |
| 261 | **hundred** | 1 | 16,308.68 | 7.453069 | 🟠 very high — domain-specific |
| 262 | **diligence** | 1 | 16,308.68 | 7.453069 | 🟠 very high — domain-specific |
| 263 | **applies** | 1 | 16,183.61 | 7.395911 | 🟠 very high — domain-specific |
| 264 | **significance** | 1 | 16,065.30 | 7.341843 | 🟠 very high — domain-specific |
| 265 | **eliminated** | 1 | 15,953.06 | 7.29055 | 🟠 very high — domain-specific |
| 266 | **suffering** | 1 | 15,846.30 | 7.24176 | 🟠 very high — domain-specific |
| 267 | **forms** | 1 | 15,744.51 | 7.19524 | 🟠 very high — domain-specific |
| 268 | **king** | 1 | 15,744.51 | 7.19524 | 🟠 very high — domain-specific |
| 269 | **thousand** | 1 | 15,647.24 | 7.150788 | 🟠 very high — domain-specific |
| 270 | **person** | 1 | 15,647.24 | 7.150788 | 🟠 very high — domain-specific |
| 271 | **space** | 1 | 15,464.79 | 7.067407 | 🟠 very high — domain-specific |
| 272 | **crown** | 1 | 15,464.79 | 7.067407 | 🟠 very high — domain-specific |
| 273 | **arranged** | 1 | 15,378.96 | 7.028186 | 🟠 very high — domain-specific |
| 274 | **gone** | 1 | 15,378.96 | 7.028186 | 🟠 very high — domain-specific |
| 275 | **heart** | 1 | 15,296.38 | 6.990446 | 🟠 very high — domain-specific |
| 276 | **drawn** | 1 | 15,140.02 | 6.918987 | 🟠 very high — domain-specific |
| 277 | **desire** | 1 | 14,857.28 | 6.789775 | 🟠 very high — domain-specific |
| 278 | **experience** | 1 | 14,857.28 | 6.789775 | 🟠 very high — domain-specific |
| 279 | **autumn** | 1 | 14,791.95 | 6.759922 | 🟠 very high — domain-specific |
| 280 | **under** | 2 | 14,660.57 | 3.34994 | 🟠 very high — domain-specific |
| 281 | **strikes** | 1 | 14,548.57 | 6.648696 | 🟠 very high — domain-specific |
| 282 | **lake** | 1 | 14,548.57 | 6.648696 | 🟠 very high — domain-specific |
| 283 | **twice** | 1 | 14,436.33 | 6.597403 | 🟠 very high — domain-specific |
| 284 | **million** | 1 | 14,382.30 | 6.57271 | 🟠 very high — domain-specific |
| 285 | **sun** | 1 | 14,227.77 | 6.502093 | 🟠 very high — domain-specific |
| 286 | **proceed** | 1 | 13,904.72 | 6.354457 | 🟠 very high — domain-specific |
| 287 | **concluded** | 1 | 13,904.72 | 6.354457 | 🟠 very high — domain-specific |
| 288 | **clearly** | 1 | 13,820.55 | 6.31599 | 🟠 very high — domain-specific |
| 289 | **bad** | 1 | 13,512.93 | 6.175409 | 🟠 very high — domain-specific |
| 290 | **actual** | 1 | 13,407.88 | 6.127399 | 🟠 very high — domain-specific |
| 291 | **direction** | 1 | 13,407.88 | 6.127399 | 🟠 very high — domain-specific |
| 292 | **india** | 1 | 13,373.95 | 6.111895 | 🟠 very high — domain-specific |
| 293 | **brings** | 1 | 13,243.27 | 6.052176 | 🟠 very high — domain-specific |
| 294 | **speech** | 1 | 13,090.19 | 5.982217 | 🟠 very high — domain-specific |
| 295 | **granted** | 1 | 13,060.82 | 5.968794 | 🟠 very high — domain-specific |
| 296 | **moving** | 1 | 12,786.94 | 5.843631 | 🟠 very high — domain-specific |
| 297 | **away** | 1 | 12,711.04 | 5.808946 | 🟠 very high — domain-specific |
| 298 | **opening** | 1 | 12,409.54 | 5.671162 | 🟠 very high — domain-specific |
| 299 | **together** | 1 | 12,387.99 | 5.66131 | 🟠 very high — domain-specific |
| 300 | **others** | 1 | 12,366.64 | 5.651553 | 🟠 very high — domain-specific |
| 301 | **having** | 1 | 12,324.56 | 5.632322 | 🟠 very high — domain-specific |
| 302 | **various** | 1 | 12,303.81 | 5.622843 | 🟠 very high — domain-specific |
| 303 | **times** | 1 | 12,262.91 | 5.604151 | 🟠 very high — domain-specific |
| 304 | **activity** | 1 | 12,163.88 | 5.558895 | 🟠 very high — domain-specific |
| 305 | **head** | 1 | 11,943.04 | 5.457969 | 🟠 very high — domain-specific |
| 306 | **greater** | 1 | 11,726.54 | 5.359029 | 🟠 very high — domain-specific |
| 307 | **able** | 1 | 11,573.46 | 5.28907 | 🟠 very high — domain-specific |
| 308 | **holds** | 1 | 11,573.46 | 5.28907 | 🟠 very high — domain-specific |
| 309 | **local** | 1 | 11,322.31 | 5.174295 | 🟠 very high — domain-specific |
| 310 | **gold** | 1 | 10,647.15 | 4.865747 | 🟠 very high — domain-specific |
| 311 | **whether** | 1 | 10,162.75 | 4.644375 | 🟠 very high — domain-specific |
| 312 | **within** | 1 | 10,005.58 | 4.57255 | 🟠 very high — domain-specific |
| 313 | **levels** | 1 | 9,640.59 | 4.405749 | 🟡 high — specialist register |
| 314 | **off** | 1 | 9,562.54 | 4.37008 | 🟡 high — specialist register |
| 315 | **state** | 1 | 9,359.89 | 4.277469 | 🟡 high — specialist register |
| 316 | **lower** | 1 | 8,551.11 | 3.907856 | 🟡 high — specialist register |
| 317 | **world** | 1 | 8,539.99 | 3.902776 | 🟡 high — specialist register |
| 318 | **end** | 1 | 8,069.53 | 3.687773 | 🟡 high — specialist register |

---

*Corpus reference: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth\_idf=True, lowercase=True).*  
*Generated 2026-09-24 by `generate_termbase.py`.*