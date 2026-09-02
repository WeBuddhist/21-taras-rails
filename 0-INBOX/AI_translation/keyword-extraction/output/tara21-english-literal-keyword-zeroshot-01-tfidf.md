---
title: TF-IDF Vocabulary Analysis — tara21-english-literal-keyword-zeroshot-01
source: /Users/tashitsering/Desktop/work/Obsidian/21-taras-rails/0-INBOX/AI_translation/english/tara21-english-literal-keyword-zeroshot_split_chapters/tara21-english-literal-keyword-zeroshot-01.md
corpus: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth_idf=True)
method: TF × IDF — term frequency in translation vs. inverse document frequency in Reuters corpus
generated: 2026-08-09
unique_terms: 316
total_content_tokens: 461
status: draft
---

# TF-IDF Vocabulary Analysis — tara21-english-literal-keyword-zeroshot-01

Generated **2026-08-09** · source: `tara21-english-literal-keyword-zeroshot-01.md` · **316 unique content terms** ranked.

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
| 🔴 extremely high — text-exclusive | 24 | 7.6% |
| 🟠 very high — domain-specific | 283 | 89.6% |
| 🟡 high — specialist register | 9 | 2.8% |
| 🟢 medium — moderately distinctive | 0 | 0.0% |
| 🔵 low — common in general English | 0 | 0.0% |
| ⚪ very low — function / universal word | 0 | 0.0% |

---

## Most Distinctive Words (highest TF-IDF)

Words that appear **frequently in this text** yet are **rare or absent in general English**.

**1. homage** — count: 23, TF-IDF: 478,460, IDF: 9.59 🔴 extremely high — text-exclusive
**2. completely** — count: 8, TF-IDF: 120,069, IDF: 6.918987 🔴 extremely high — text-exclusive
**3. praise** — count: 5, TF-IDF: 104,047, IDF: 9.593135 🔴 extremely high — text-exclusive
**4. blazing** — count: 5, TF-IDF: 104,047, IDF: 9.593135 🔴 extremely high — text-exclusive
**5. tara** — count: 5, TF-IDF: 104,013, IDF: 9.59 🔴 extremely high — text-exclusive
**6. thoroughly** — count: 5, TF-IDF: 92,131, IDF: 8.494523 🔴 extremely high — text-exclusive
**7. twenty-one** — count: 4, TF-IDF: 83,210, IDF: 9.59 🔴 extremely high — text-exclusive
**8. hum** — count: 4, TF-IDF: 73,705, IDF: 8.494523 🔴 extremely high — text-exclusive
**9. exception** — count: 4, TF-IDF: 62,432, IDF: 7.19524 🔴 extremely high — text-exclusive
**10. exceedingly** — count: 3, TF-IDF: 62,428, IDF: 9.593135 🔴 extremely high — text-exclusive
**11. homages** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**12. water-born** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**13. brilliant** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**14. adorned** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**15. tuttara** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**16. syllables** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**17. destroys** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**18. ture** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**19. enemies** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**20. joyful** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**21. endowed** — count: 3, TF-IDF: 62,408, IDF: 9.59 🔴 extremely high — text-exclusive
**22. worlds** — count: 3, TF-IDF: 59,790, IDF: 9.18767 🔴 extremely high — text-exclusive
**23. light** — count: 5, TF-IDF: 59,197, IDF: 5.457969 🔴 extremely high — text-exclusive
**24. assemblies** — count: 3, TF-IDF: 56,465, IDF: 8.676844 🔴 extremely high — text-exclusive
**25. like** — count: 4, TF-IDF: 45,055, IDF: 5.192532 🟠 very high — domain-specific
**26. obtained** — count: 3, TF-IDF: 44,592, IDF: 6.852295 🟠 very high — domain-specific
**27. infectious** — count: 2, TF-IDF: 41,619, IDF: 9.593135 🟠 very high — domain-specific
**28. remembering** — count: 2, TF-IDF: 41,619, IDF: 9.593135 🟠 very high — domain-specific
**29. hand** — count: 3, TF-IDF: 41,613, IDF: 6.394462 🟠 very high — domain-specific
**30. summon** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**31. hosts** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**32. yakshas** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**33. phat** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**34. maras** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**35. frowning** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**36. moon** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**37. dispels** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**38. poisons** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**39. gods** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**40. demons** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**41. buddha** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**42. desiring** — count: 2, TF-IDF: 41,605, IDF: 9.59 🟠 very high — domain-specific
**43. without** — count: 4, TF-IDF: 40,970, IDF: 4.721762 🟠 very high — domain-specific
**44. eyes** — count: 2, TF-IDF: 39,860, IDF: 9.18767 🟠 very high — domain-specific
**45. perfect** — count: 2, TF-IDF: 39,860, IDF: 9.18767 🟠 very high — domain-specific
**46. directions** — count: 2, TF-IDF: 38,612, IDF: 8.899988 🟠 very high — domain-specific
**47. fierce** — count: 2, TF-IDF: 38,612, IDF: 8.899988 🟠 very high — domain-specific
**48. son** — count: 2, TF-IDF: 38,612, IDF: 8.899988 🟠 very high — domain-specific
**49. surrounded** — count: 2, TF-IDF: 37,644, IDF: 8.676844 🟠 very high — domain-specific
**50. peace** — count: 2, TF-IDF: 37,644, IDF: 8.676844 🟠 very high — domain-specific

---

## Least Distinctive Words (lowest TF-IDF)

Words that appear in this text but are also extremely common in general English.

**1. end** — count: 1, TF-IDF: 7,999.51, IDF: 3.687773 🟡 high — specialist register
**2. world** — count: 1, TF-IDF: 8,465.89, IDF: 3.902776 🟡 high — specialist register
**3. lower** — count: 1, TF-IDF: 8,476.91, IDF: 3.907856 🟡 high — specialist register
**4. most** — count: 1, TF-IDF: 8,849.69, IDF: 4.079706 🟡 high — specialist register
**5. full** — count: 1, TF-IDF: 9,013.14, IDF: 4.155056 🟡 high — specialist register
**6. state** — count: 1, TF-IDF: 9,278.67, IDF: 4.277469 🟡 high — specialist register
**7. completed** — count: 1, TF-IDF: 9,433.29, IDF: 4.348746 🟡 high — specialist register
**8. levels** — count: 1, TF-IDF: 9,556.94, IDF: 4.405749 🟡 high — specialist register
**9. within** — count: 1, TF-IDF: 9,918.76, IDF: 4.57255 🟡 high — specialist register
**10. whether** — count: 1, TF-IDF: 10,074.57, IDF: 4.644375 🟠 very high — domain-specific
**11. range** — count: 1, TF-IDF: 10,819.88, IDF: 4.987965 🟠 very high — domain-specific
**12. power** — count: 1, TF-IDF: 11,443.92, IDF: 5.275647 🟠 very high — domain-specific
**13. holds** — count: 1, TF-IDF: 11,473.04, IDF: 5.28907 🟠 very high — domain-specific
**14. complete** — count: 1, TF-IDF: 11,839.41, IDF: 5.457969 🟠 very high — domain-specific
**15. head** — count: 1, TF-IDF: 11,839.41, IDF: 5.457969 🟠 very high — domain-specific
**16. fully** — count: 1, TF-IDF: 11,964.42, IDF: 5.515598 🟠 very high — domain-specific
**17. times** — count: 1, TF-IDF: 12,156.51, IDF: 5.604151 🟠 very high — domain-specific
**18. stable** — count: 1, TF-IDF: 12,156.51, IDF: 5.604151 🟠 very high — domain-specific
**19. various** — count: 1, TF-IDF: 12,197.06, IDF: 5.622843 🟠 very high — domain-specific
**20. having** — count: 1, TF-IDF: 12,217.62, IDF: 5.632322 🟠 very high — domain-specific
**21. opening** — count: 1, TF-IDF: 12,301.87, IDF: 5.671162 🟠 very high — domain-specific
**22. giving** — count: 1, TF-IDF: 12,389.52, IDF: 5.711571 🟠 very high — domain-specific
**23. every** — count: 1, TF-IDF: 12,576.24, IDF: 5.797646 🟠 very high — domain-specific
**24. actions** — count: 1, TF-IDF: 12,600.75, IDF: 5.808946 🟠 very high — domain-specific
**25. quickly** — count: 1, TF-IDF: 12,625.54, IDF: 5.820374 🟠 very high — domain-specific
**26. negative** — count: 1, TF-IDF: 12,780.55, IDF: 5.891833 🟠 very high — domain-specific
**27. speech** — count: 1, TF-IDF: 12,976.61, IDF: 5.982217 🟠 very high — domain-specific
**28. single** — count: 1, TF-IDF: 13,036.04, IDF: 6.009616 🟠 very high — domain-specific
**29. india** — count: 1, TF-IDF: 13,257.91, IDF: 6.111895 🟠 very high — domain-specific
**30. ten** — count: 1, TF-IDF: 13,360.41, IDF: 6.159148 🟠 very high — domain-specific
**31. bad** — count: 1, TF-IDF: 13,395.68, IDF: 6.175409 🟠 very high — domain-specific
**32. practices** — count: 1, TF-IDF: 13,581.20, IDF: 6.260931 🟠 very high — domain-specific
**33. highly** — count: 1, TF-IDF: 13,581.20, IDF: 6.260931 🟠 very high — domain-specific
**34. palm** — count: 1, TF-IDF: 13,620.28, IDF: 6.278949 🟠 very high — domain-specific
**35. center** — count: 1, TF-IDF: 13,660.08, IDF: 6.297298 🟠 very high — domain-specific
**36. clearly** — count: 1, TF-IDF: 13,700.63, IDF: 6.31599 🟠 very high — domain-specific
**37. extremely** — count: 1, TF-IDF: 13,741.95, IDF: 6.335039 🟠 very high — domain-specific
**38. expanded** — count: 1, TF-IDF: 13,784.07, IDF: 6.354457 🟠 very high — domain-specific
**39. beyond** — count: 1, TF-IDF: 13,915.58, IDF: 6.415081 🟠 very high — domain-specific
**40. goes** — count: 1, TF-IDF: 13,961.25, IDF: 6.436135 🟠 very high — domain-specific
**41. arrangement** — count: 1, TF-IDF: 14,104.32, IDF: 6.502093 🟠 very high — domain-specific
**42. sun** — count: 1, TF-IDF: 14,104.32, IDF: 6.502093 🟠 very high — domain-specific
**43. million** — count: 1, TF-IDF: 14,257.51, IDF: 6.57271 🟠 very high — domain-specific
**44. twice** — count: 1, TF-IDF: 14,311.07, IDF: 6.597403 🟠 very high — domain-specific
**45. presence** — count: 1, TF-IDF: 14,365.99, IDF: 6.622721 🟠 very high — domain-specific
**46. strikes** — count: 1, TF-IDF: 14,422.33, IDF: 6.648696 🟠 very high — domain-specific
**47. autumn** — count: 1, TF-IDF: 14,663.61, IDF: 6.759922 🟠 very high — domain-specific
**48. desire** — count: 1, TF-IDF: 14,728.36, IDF: 6.789775 🟠 very high — domain-specific
**49. destroyed** — count: 1, TF-IDF: 14,795.11, IDF: 6.820546 🟠 very high — domain-specific
**50. exceeding** — count: 1, TF-IDF: 15,084.77, IDF: 6.954078 🟠 very high — domain-specific

---

## Full Ranked Table

All 316 content terms, sorted by TF-IDF descending.

| Rank | Word | Count | TF-IDF | IDF | Band |
|------|------|-------|--------|-----|------|
| 1 | **homage** | 23 | 478,459.87 | 9.59 | 🔴 extremely high — text-exclusive |
| 2 | **completely** | 8 | 120,069.19 | 6.918987 | 🔴 extremely high — text-exclusive |
| 3 | **praise** | 5 | 104,047.02 | 9.593135 | 🔴 extremely high — text-exclusive |
| 4 | **blazing** | 5 | 104,047.02 | 9.593135 | 🔴 extremely high — text-exclusive |
| 5 | **tara** | 5 | 104,013.02 | 9.59 | 🔴 extremely high — text-exclusive |
| 6 | **thoroughly** | 5 | 92,131.49 | 8.494523 | 🔴 extremely high — text-exclusive |
| 7 | **twenty-one** | 4 | 83,210.41 | 9.59 | 🔴 extremely high — text-exclusive |
| 8 | **hum** | 4 | 73,705.19 | 8.494523 | 🔴 extremely high — text-exclusive |
| 9 | **exception** | 4 | 62,431.58 | 7.19524 | 🔴 extremely high — text-exclusive |
| 10 | **exceedingly** | 3 | 62,428.21 | 9.593135 | 🔴 extremely high — text-exclusive |
| 11 | **homages** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 12 | **water-born** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 13 | **brilliant** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 14 | **adorned** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 15 | **tuttara** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 16 | **syllables** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 17 | **destroys** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 18 | **ture** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 19 | **enemies** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 20 | **joyful** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 21 | **endowed** | 3 | 62,407.81 | 9.59 | 🔴 extremely high — text-exclusive |
| 22 | **worlds** | 3 | 59,789.61 | 9.18767 | 🔴 extremely high — text-exclusive |
| 23 | **light** | 5 | 59,197.06 | 5.457969 | 🔴 extremely high — text-exclusive |
| 24 | **assemblies** | 3 | 56,465.36 | 8.676844 | 🔴 extremely high — text-exclusive |
| 25 | **like** | 4 | 45,054.51 | 5.192532 | 🟠 very high — domain-specific |
| 26 | **obtained** | 3 | 44,591.94 | 6.852295 | 🟠 very high — domain-specific |
| 27 | **infectious** | 2 | 41,618.81 | 9.593135 | 🟠 very high — domain-specific |
| 28 | **remembering** | 2 | 41,618.81 | 9.593135 | 🟠 very high — domain-specific |
| 29 | **hand** | 3 | 41,612.55 | 6.394462 | 🟠 very high — domain-specific |
| 30 | **summon** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 31 | **hosts** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 32 | **yakshas** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 33 | **phat** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 34 | **maras** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 35 | **frowning** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 36 | **moon** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 37 | **dispels** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 38 | **poisons** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 39 | **gods** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 40 | **demons** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 41 | **buddha** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 42 | **desiring** | 2 | 41,605.21 | 9.59 | 🟠 very high — domain-specific |
| 43 | **without** | 4 | 40,969.74 | 4.721762 | 🟠 very high — domain-specific |
| 44 | **eyes** | 2 | 39,859.74 | 9.18767 | 🟠 very high — domain-specific |
| 45 | **perfect** | 2 | 39,859.74 | 9.18767 | 🟠 very high — domain-specific |
| 46 | **directions** | 2 | 38,611.66 | 8.899988 | 🟠 very high — domain-specific |
| 47 | **fierce** | 2 | 38,611.66 | 8.899988 | 🟠 very high — domain-specific |
| 48 | **son** | 2 | 38,611.66 | 8.899988 | 🟠 very high — domain-specific |
| 49 | **surrounded** | 2 | 37,643.57 | 8.676844 | 🟠 very high — domain-specific |
| 50 | **peace** | 2 | 37,643.57 | 8.676844 | 🟠 very high — domain-specific |
| 51 | **wealth** | 2 | 37,643.57 | 8.676844 | 🟠 very high — domain-specific |
| 52 | **feet** | 3 | 37,584.10 | 5.775423 | 🟠 very high — domain-specific |
| 53 | **earth** | 2 | 36,852.59 | 8.494523 | 🟠 very high — domain-specific |
| 54 | **face** | 3 | 36,409.55 | 5.594934 | 🟠 very high — domain-specific |
| 55 | **diseases** | 2 | 36,183.83 | 8.340372 | 🟠 very high — domain-specific |
| 56 | **arisen** | 2 | 35,604.52 | 8.206841 | 🟠 very high — domain-specific |
| 57 | **destroying** | 2 | 35,604.52 | 8.206841 | 🟠 very high — domain-specific |
| 58 | **indeed** | 2 | 32,597.37 | 7.513694 | 🟠 very high — domain-specific |
| 59 | **language** | 2 | 32,334.36 | 7.453069 | 🟠 very high — domain-specific |
| 60 | **supreme** | 2 | 31,022.94 | 7.150788 | 🟠 very high — domain-specific |
| 61 | **making** | 3 | 29,628.68 | 4.552941 | 🟠 very high — domain-specific |
| 62 | **fire** | 2 | 28,015.80 | 6.457641 | 🟠 very high — domain-specific |
| 63 | **sides** | 2 | 26,863.07 | 6.191938 | 🟠 very high — domain-specific |
| 64 | **moving** | 2 | 25,351.98 | 5.843631 | 🟠 very high — domain-specific |
| 65 | **benefits** | 2 | 24,869.44 | 5.732405 | 🟠 very high — domain-specific |
| 66 | **together** | 2 | 24,561.00 | 5.66131 | 🟠 very high — domain-specific |
| 67 | **itself** | 2 | 24,476.75 | 5.641891 | 🟠 very high — domain-specific |
| 68 | **activity** | 2 | 24,116.68 | 5.558895 | 🟠 very high — domain-specific |
| 69 | **left** | 2 | 23,784.21 | 5.482261 | 🟠 very high — domain-specific |
| 70 | **extended** | 2 | 23,508.67 | 5.418748 | 🟠 very high — domain-specific |
| 71 | **able** | 2 | 22,946.07 | 5.28907 | 🟠 very high — domain-specific |
| 72 | **right** | 2 | 22,319.39 | 5.144619 | 🟠 very high — domain-specific |
| 73 | **form** | 2 | 22,319.39 | 5.144619 | 🟠 very high — domain-specific |
| 74 | **letter** | 2 | 21,428.09 | 4.939175 | 🟠 very high — domain-specific |
| 75 | **ati** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 76 | **flash** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 77 | **stars** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 78 | **retracted** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 79 | **intensely** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 80 | **wheel** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 81 | **hair** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 82 | **garland** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 83 | **joy** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 84 | **stamps** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 85 | **destroyer** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 86 | **herself** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 87 | **meru** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 88 | **shedding** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 89 | **dawn** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 90 | **utterly** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 91 | **attaining** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 92 | **afflicted** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 93 | **perfected** | 1 | 20,809.40 | 9.593135 | 🟠 very high — domain-specific |
| 94 | **nama** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 95 | **tāre** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 96 | **ekaviṃ** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 97 | **stotra** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 98 | **guṇahitasāka** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 99 | **tibet** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 100 | **lady** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 101 | **venerable** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 102 | **heroine** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 103 | **stamen** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 104 | **protector** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 105 | **moons** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 106 | **asceticism** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 107 | **pacification** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 108 | **meditative** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 109 | **protrusion** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 110 | **tathagata** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 111 | **perfection** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 112 | **victorious** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 113 | **treading** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 114 | **worshiped** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 115 | **indra** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 116 | **agni** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 117 | **brahma** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 118 | **vayu** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 119 | **ishvaras** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 120 | **bhutas** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 121 | **vetalas** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 122 | **gandharvas** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 123 | **trad** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 124 | **wheel-devices** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 125 | **adversaries** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 126 | **suppressing** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 127 | **swirling** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 128 | **terrifier** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 129 | **conqueror** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 130 | **heroes** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 131 | **possess** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 132 | **wrinkles** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 133 | **slayer** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 134 | **mudra** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 135 | **symbolizing** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 136 | **jewels** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 137 | **beautifully** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 138 | **adorn** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 139 | **agitates** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 140 | **masses** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 141 | **crown-ornament** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 142 | **garlands** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 143 | **laughing** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 144 | **laugh** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 145 | **subdues** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 146 | **guardians** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 147 | **wrathful** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 148 | **frown** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 149 | **liberates** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 150 | **crescent** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 151 | **ornaments** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 152 | **amitabha** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 153 | **matted** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 154 | **dwells** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 155 | **eon** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 156 | **bent** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 157 | **grimace** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 158 | **shatters** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 159 | **underworld** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 160 | **blissful** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 161 | **virtuous** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 162 | **sphere** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 163 | **sorrow** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 164 | **svaha** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 165 | **negativity** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 166 | **lamp** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 167 | **knowledge-hum** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 168 | **seed-syllable** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 169 | **mandara** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 170 | **vindhya** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 171 | **tremble** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 172 | **deer-marked** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 173 | **celestial** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 174 | **pronouncing** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 175 | **taras** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 176 | **syllable** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 177 | **kinnaras** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 178 | **splendor** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 179 | **dreams** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 180 | **uttering** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 181 | **hara** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 182 | **dispersing** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 183 | **zombies** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 184 | **mantra** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 185 | **devotion** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 186 | **goddess** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 187 | **reciting** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 188 | **dusk** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 189 | **bestows** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 190 | **fearlessness** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 191 | **pacifying** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 192 | **realms** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 193 | **seventy** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 194 | **conquerors** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 195 | **empowerment** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 196 | **conferred** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 197 | **greatness** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 198 | **sufferings** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 199 | **sentient** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 200 | **beings** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 201 | **recited** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 202 | **bhagavati** | 1 | 20,802.60 | 9.59 | 🟠 very high — domain-specific |
| 203 | **noble** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 204 | **instant** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 205 | **lotus** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 206 | **patience** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 207 | **infinite** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 208 | **attained** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 209 | **fingers** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 210 | **midst** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 211 | **constantly** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 212 | **arranges** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 213 | **stamping** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 214 | **armor** | 1 | 19,929.87 | 9.18767 | 🟠 very high — domain-specific |
| 215 | **poverty** | 1 | 19,305.83 | 8.899988 | 🟠 very high — domain-specific |
| 216 | **leg** | 1 | 19,305.83 | 8.899988 | 🟠 very high — domain-specific |
| 217 | **peaceful** | 1 | 19,305.83 | 8.899988 | 🟠 very high — domain-specific |
| 218 | **drinking** | 1 | 19,305.83 | 8.899988 | 🟠 very high — domain-specific |
| 219 | **obtains** | 1 | 19,305.83 | 8.899988 | 🟠 very high — domain-specific |
| 220 | **desires** | 1 | 19,305.83 | 8.899988 | 🟠 very high — domain-specific |
| 221 | **female** | 1 | 18,821.79 | 8.676844 | 🟠 very high — domain-specific |
| 222 | **individually** | 1 | 18,821.79 | 8.676844 | 🟠 very high — domain-specific |
| 223 | **concentration** | 1 | 18,426.30 | 8.494523 | 🟠 very high — domain-specific |
| 224 | **filling** | 1 | 18,426.30 | 8.494523 | 🟠 very high — domain-specific |
| 225 | **eating** | 1 | 18,426.30 | 8.494523 | 🟠 very high — domain-specific |
| 226 | **spoken** | 1 | 18,426.30 | 8.494523 | 🟠 very high — domain-specific |
| 227 | **lightning** | 1 | 18,091.91 | 8.340372 | 🟠 very high — domain-specific |
| 228 | **realities** | 1 | 18,091.91 | 8.340372 | 🟠 very high — domain-specific |
| 229 | **perfectly** | 1 | 17,802.26 | 8.206841 | 🟠 very high — domain-specific |
| 230 | **conflicts** | 1 | 17,802.26 | 8.206841 | 🟠 very high — domain-specific |
| 231 | **intelligent** | 1 | 17,802.26 | 8.206841 | 🟠 very high — domain-specific |
| 232 | **abiding** | 1 | 17,802.26 | 8.206841 | 🟠 very high — domain-specific |
| 233 | **gathered** | 1 | 17,546.76 | 8.089058 | 🟠 very high — domain-specific |
| 234 | **spreads** | 1 | 17,546.76 | 8.089058 | 🟠 very high — domain-specific |
| 235 | **title** | 1 | 17,318.21 | 7.983697 | 🟠 very high — domain-specific |
| 236 | **blue** | 1 | 17,318.21 | 7.983697 | 🟠 very high — domain-specific |
| 237 | **praised** | 1 | 17,111.47 | 7.888387 | 🟠 very high — domain-specific |
| 238 | **host** | 1 | 17,111.47 | 7.888387 | 🟠 very high — domain-specific |
| 239 | **causes** | 1 | 17,111.47 | 7.888387 | 🟠 very high — domain-specific |
| 240 | **root** | 1 | 17,111.47 | 7.888387 | 🟠 very high — domain-specific |
| 241 | **assembly** | 1 | 16,922.72 | 7.801376 | 🟠 very high — domain-specific |
| 242 | **swift** | 1 | 16,749.10 | 7.721333 | 🟠 very high — domain-specific |
| 243 | **relied** | 1 | 16,749.10 | 7.721333 | 🟠 very high — domain-specific |
| 244 | **sons** | 1 | 16,749.10 | 7.721333 | 🟠 very high — domain-specific |
| 245 | **ultimate** | 1 | 16,749.10 | 7.721333 | 🟠 very high — domain-specific |
| 246 | **victory** | 1 | 16,588.34 | 7.647225 | 🟠 very high — domain-specific |
| 247 | **obstacles** | 1 | 16,588.34 | 7.647225 | 🟠 very high — domain-specific |
| 248 | **mass** | 1 | 16,438.68 | 7.578232 | 🟠 very high — domain-specific |
| 249 | **bodies** | 1 | 16,438.68 | 7.578232 | 🟠 very high — domain-specific |
| 250 | **poison** | 1 | 16,438.68 | 7.578232 | 🟠 very high — domain-specific |
| 251 | **surface** | 1 | 16,298.69 | 7.513694 | 🟠 very high — domain-specific |
| 252 | **hundred** | 1 | 16,167.18 | 7.453069 | 🟠 very high — domain-specific |
| 253 | **diligence** | 1 | 16,167.18 | 7.453069 | 🟠 very high — domain-specific |
| 254 | **exist** | 1 | 16,167.18 | 7.453069 | 🟠 very high — domain-specific |
| 255 | **arising** | 1 | 16,043.19 | 7.395911 | 🟠 very high — domain-specific |
| 256 | **foot** | 1 | 15,925.91 | 7.341843 | 🟠 very high — domain-specific |
| 257 | **attended** | 1 | 15,925.91 | 7.341843 | 🟠 very high — domain-specific |
| 258 | **eliminated** | 1 | 15,814.64 | 7.29055 | 🟠 very high — domain-specific |
| 259 | **king** | 1 | 15,607.90 | 7.19524 | 🟠 very high — domain-specific |
| 260 | **ocean** | 1 | 15,511.47 | 7.150788 | 🟠 very high — domain-specific |
| 261 | **crown** | 1 | 15,330.60 | 7.067407 | 🟠 very high — domain-specific |
| 262 | **space** | 1 | 15,330.60 | 7.067407 | 🟠 very high — domain-specific |
| 263 | **elimination** | 1 | 15,330.60 | 7.067407 | 🟠 very high — domain-specific |
| 264 | **golden** | 1 | 15,245.52 | 7.028186 | 🟠 very high — domain-specific |
| 265 | **heart** | 1 | 15,163.66 | 6.990446 | 🟠 very high — domain-specific |
| 266 | **thousands** | 1 | 15,084.77 | 6.954078 | 🟠 very high — domain-specific |
| 267 | **exceeding** | 1 | 15,084.77 | 6.954078 | 🟠 very high — domain-specific |
| 268 | **destroyed** | 1 | 14,795.11 | 6.820546 | 🟠 very high — domain-specific |
| 269 | **desire** | 1 | 14,728.36 | 6.789775 | 🟠 very high — domain-specific |
| 270 | **autumn** | 1 | 14,663.61 | 6.759922 | 🟠 very high — domain-specific |
| 271 | **strikes** | 1 | 14,422.33 | 6.648696 | 🟠 very high — domain-specific |
| 272 | **presence** | 1 | 14,365.99 | 6.622721 | 🟠 very high — domain-specific |
| 273 | **twice** | 1 | 14,311.07 | 6.597403 | 🟠 very high — domain-specific |
| 274 | **million** | 1 | 14,257.51 | 6.57271 | 🟠 very high — domain-specific |
| 275 | **sun** | 1 | 14,104.32 | 6.502093 | 🟠 very high — domain-specific |
| 276 | **arrangement** | 1 | 14,104.32 | 6.502093 | 🟠 very high — domain-specific |
| 277 | **goes** | 1 | 13,961.25 | 6.436135 | 🟠 very high — domain-specific |
| 278 | **beyond** | 1 | 13,915.58 | 6.415081 | 🟠 very high — domain-specific |
| 279 | **expanded** | 1 | 13,784.07 | 6.354457 | 🟠 very high — domain-specific |
| 280 | **extremely** | 1 | 13,741.95 | 6.335039 | 🟠 very high — domain-specific |
| 281 | **clearly** | 1 | 13,700.63 | 6.31599 | 🟠 very high — domain-specific |
| 282 | **center** | 1 | 13,660.08 | 6.297298 | 🟠 very high — domain-specific |
| 283 | **palm** | 1 | 13,620.28 | 6.278949 | 🟠 very high — domain-specific |
| 284 | **highly** | 1 | 13,581.20 | 6.260931 | 🟠 very high — domain-specific |
| 285 | **practices** | 1 | 13,581.20 | 6.260931 | 🟠 very high — domain-specific |
| 286 | **bad** | 1 | 13,395.68 | 6.175409 | 🟠 very high — domain-specific |
| 287 | **ten** | 1 | 13,360.41 | 6.159148 | 🟠 very high — domain-specific |
| 288 | **india** | 1 | 13,257.91 | 6.111895 | 🟠 very high — domain-specific |
| 289 | **single** | 1 | 13,036.04 | 6.009616 | 🟠 very high — domain-specific |
| 290 | **speech** | 1 | 12,976.61 | 5.982217 | 🟠 very high — domain-specific |
| 291 | **negative** | 1 | 12,780.55 | 5.891833 | 🟠 very high — domain-specific |
| 292 | **quickly** | 1 | 12,625.54 | 5.820374 | 🟠 very high — domain-specific |
| 293 | **actions** | 1 | 12,600.75 | 5.808946 | 🟠 very high — domain-specific |
| 294 | **every** | 1 | 12,576.24 | 5.797646 | 🟠 very high — domain-specific |
| 295 | **giving** | 1 | 12,389.52 | 5.711571 | 🟠 very high — domain-specific |
| 296 | **opening** | 1 | 12,301.87 | 5.671162 | 🟠 very high — domain-specific |
| 297 | **having** | 1 | 12,217.62 | 5.632322 | 🟠 very high — domain-specific |
| 298 | **various** | 1 | 12,197.06 | 5.622843 | 🟠 very high — domain-specific |
| 299 | **stable** | 1 | 12,156.51 | 5.604151 | 🟠 very high — domain-specific |
| 300 | **times** | 1 | 12,156.51 | 5.604151 | 🟠 very high — domain-specific |
| 301 | **fully** | 1 | 11,964.42 | 5.515598 | 🟠 very high — domain-specific |
| 302 | **head** | 1 | 11,839.41 | 5.457969 | 🟠 very high — domain-specific |
| 303 | **complete** | 1 | 11,839.41 | 5.457969 | 🟠 very high — domain-specific |
| 304 | **holds** | 1 | 11,473.04 | 5.28907 | 🟠 very high — domain-specific |
| 305 | **power** | 1 | 11,443.92 | 5.275647 | 🟠 very high — domain-specific |
| 306 | **range** | 1 | 10,819.88 | 4.987965 | 🟠 very high — domain-specific |
| 307 | **whether** | 1 | 10,074.57 | 4.644375 | 🟠 very high — domain-specific |
| 308 | **within** | 1 | 9,918.76 | 4.57255 | 🟡 high — specialist register |
| 309 | **levels** | 1 | 9,556.94 | 4.405749 | 🟡 high — specialist register |
| 310 | **completed** | 1 | 9,433.29 | 4.348746 | 🟡 high — specialist register |
| 311 | **state** | 1 | 9,278.67 | 4.277469 | 🟡 high — specialist register |
| 312 | **full** | 1 | 9,013.14 | 4.155056 | 🟡 high — specialist register |
| 313 | **most** | 1 | 8,849.69 | 4.079706 | 🟡 high — specialist register |
| 314 | **lower** | 1 | 8,476.91 | 3.907856 | 🟡 high — specialist register |
| 315 | **world** | 1 | 8,465.89 | 3.902776 | 🟡 high — specialist register |
| 316 | **end** | 1 | 7,999.51 | 3.687773 | 🟡 high — specialist register |

---

*Corpus reference: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth\_idf=True, lowercase=True).*  
*Generated 2026-08-09 by `generate_termbase.py`.*