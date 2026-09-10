# סשן: ערוצי העבודה progress / docs / plans / issues, ו-Spec Driven Development

| | |
|---|---|
| **תאריך** | 2026-09-10 |
| **אדם** | תומר |
| **סוכן** | `claude/tomer` |
| **כלי** | Claude Code (VS Code), מודל Claude Fable 5.1 |

המשך ישיר של `2026-09-10-01-tomer-claude-project-docs-setup.md`, באותו
חלון צ׳אט.

## מה התבקש

שתי הודעות של תומר, בלשונו.

הראשונה:

> "מעבר ליומן - אנחנו עובדים עם :
> progress
> docs
> plans
> issues"

השנייה, תוך כדי העבודה על הראשונה:

> "Spec Driven Development:
> לפני שיוצרים מערכת - קוד - רכיב תוכנה:
> יוצרים תיאור ותיעוד של הדרישות מהרכיב"

## מה הוחלט

- **ארבעה ערוצים בשורש הפרויקט** לצד `docs/`: `progress/`, `plans/`,
  `issues/`. `docs/` נשאר כפי שהוקם בסשן 01
- **ערוץ חמישי, `specs/`**, כמימוש של Spec Driven Development: מסמך דרישות
  לכל רכיב, שאדם מאשר לפני שנכתב קוד
- **זרימה קבועה:** `issues → specs → plans → קוד → docs/journal → progress`
- **מספר רץ אחד** (`NNNN`) מלווה נושא דרך `issues/`, `specs/` ו-`plans/`
- ההכרעה נרשמה ב-`docs/decisions/0002-work-channels-and-spec-first.md`.
  ההחלטה על הערוצים היא של תומר; הזרימה וההפרדה ביניהם הן הצעת הסוכן

## הנחות שהסוכן הניח בלי לשאול

- **מיקום:** ארבעת הערוצים הם תיקיות בשורש הפרויקט, לא תת-תיקיות של
  `docs/`, כי תומר מנה את `docs` כאחד מהם. אם הכוונה הייתה אחרת, ההזזה
  היא `mv` ועדכון קישורים
- **`progress/` הוא קובץ חי אחד** (`status.md`) שמתעדכן במקום, ולא
  רשומות מצטברות. הנימוק: יומן כבר מצטבר; הערך של progress הוא בתשובה
  מהירה ל"איפה אנחנו"
- **`specs/` הוא תיקייה נפרדת** ולא תת-סעיף ב-`plans/`, כי spec (מה) ו-plan
  (איך) עונים על שאלות שונות ומאושרים בנפרד
- **"אין קוד בלי spec מאושר"** נוסח ככלל מוחלט לרכיבים חדשים, עם חריג
  לתיקוני באגים שאינם משנים התנהגות מתועדת. תומר לא ניסח את החריג; הסוכן
  הוסיף אותו כדי שהכלל יהיה ישים
- **מחזורי חיים** (סטטוסים) ל-issue, spec ו-plan נקבעו על ידי הסוכן.
  ניתנים לשינוי
- **שלוש הפריטים הפתוחים מסשן 01** הפכו ל-issues 0001–0003, ו-plan 0001
  נכתב בדיעבד כדוגמה, ומסומן כך במפורש

## מה לא נעשה, ולמה

- **לא נכתב spec ראשון.** אין עדיין רכיב לתאר; התבנית מוכנה
- **לא בוצע קומיט.** קומיט רק לבקשת אדם
- **לא נגעתי בשינויים הלא קשורים ב-`git status`** של ה-repo

## תוצרים

- `docs/journal/2026-09-10-02-progress-plans-issues-specs.md`
- `docs/decisions/0002-work-channels-and-spec-first.md`
- `progress/README.md`, `progress/status.md`
- `issues/README.md`, `issues/_template.md`, `issues/0001`–`0003`
- `specs/README.md`, `specs/_template.md`
- `plans/README.md`, `plans/_template.md`, `plans/0001-project-docs-scaffold.md`
- עודכנו: `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/README.md`,
  `docs/conventions/collaboration-rules.md`, `docs/conventions/documentation-rules.md`

## פתוח

- [ ] תומר: לאשר את מיקום הערוצים בשורש, ואת `specs/` כערוץ נפרד
- [ ] תומר: לאשר את החריג לכלל ה-spec (תיקון באג שאינו משנה התנהגות)
- [ ] `issues/0001` עדיין ממתין: כלל ה-Git
