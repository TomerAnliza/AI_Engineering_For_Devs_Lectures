# הוספת ערוצי העבודה progress / plans / issues / specs לשלד

| | |
|---|---|
| **תאריך** | 2026-09-10 |
| **מבצע** | `claude/tomer` (Claude Code, לבקשת תומר) |
| **סשן** | `docs/sessions/2026-09-10-02-tomer-claude-work-channels-and-sdd.md` |

## מה נעשה

לשלד שהוקם ברשומה `2026-09-10-01-project-docs-setup.md` נוספו ארבע תיקיות
בשורש הפרויקט, כל אחת עם `README.md` שמסביר את תפקידה ו-`_template.md`:

- **`progress/`** — `status.md`: קובץ מצב חי עם ארבעה סעיפים (גמור, בעבודה,
  חסום, הבא). מאוכלס במצב הנוכחי
- **`issues/`** — אינדקס ב-`README.md`, ושלושה issues שנפתחו מהפריטים
  הפתוחים של סשן 01: `0001` כלל ה-Git (ממתין להכרעה), `0002` רישום צוות,
  `0003` קוד ראשון
- **`plans/`** — `0001-project-docs-scaffold.md`, תוכנית שנכתבה בדיעבד
  כדוגמה לפורמט ומסומנת כך
- **`specs/`** — מימוש Spec Driven Development: README עם הכלל "אין קוד
  בלי spec מאושר", ותבנית עם קלט, פלט, מקרי קצה, מה אסור, איך יודעים
  שעובד

נוספה החלטה `docs/decisions/0002-work-channels-and-spec-first.md`.

עודכנו כל המסמכים שמתארים את המבנה: `AGENTS.md` (חובות + מפה + זרימה),
`CLAUDE.md`, `README.md`, `docs/README.md` (מפה של חמישה ערוצים וההבדלים
המבלבלים), `docs/conventions/collaboration-rules.md` (סעיפים 1, 3, 4 וסעיף
9 חדש), `docs/conventions/documentation-rules.md` (פורמטים לארבעת הערוצים).

לא הורץ קוד. לא בוצע קומיט.

## למה

תומר הודיע, בשתי הודעות, שהצוות עובד עם `progress`, `docs`, `plans`
ו-`issues`, ושלפני יצירת מערכת, קוד או רכיב תוכנה יוצרים תיעוד של
הדרישות ממנו. השלד הראשון ענה על "מה קרה ולמה" בלבד; הערוצים החדשים
עונים על "איפה אנחנו", "מה שבור", "מה בדיוק לבנות" ו"איך". החלופות
שנשקלו והנימוק: החלטה 0002.

## קבצים שהושפעו

יחסית ל-`2026_09_10_vibe_coding/`:

**נוצרו:**
- `progress/README.md`, `progress/status.md`
- `issues/README.md`, `issues/_template.md`, `issues/0001-git-workflow-approval.md`, `issues/0002-team-registration.md`, `issues/0003-first-code-and-run-section.md`
- `plans/README.md`, `plans/_template.md`, `plans/0001-project-docs-scaffold.md`
- `specs/README.md`, `specs/_template.md`
- `docs/decisions/0002-work-channels-and-spec-first.md`
- `docs/sessions/2026-09-10-02-tomer-claude-work-channels-and-sdd.md`
- רשומה זו

**עודכנו:**
- `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/README.md`
- `docs/conventions/collaboration-rules.md`, `docs/conventions/documentation-rules.md`

## מה צריך לדעת כדי להמשיך

- **הזרימה מחייבת:** `issues → specs → plans → קוד → journal → progress`.
  סוכן שמתבקש לכתוב קוד לרכיב בלי spec מאושר כותב את ה-spec ועוצר
- **מספר רץ אחד** לנושא דרך `issues/`, `specs/`, `plans/`. המספר הבא
  הפנוי: `0004`
- **`progress/status.md` מתעדכן בכל סיום סשן.** תאריך ישן בראשו אומר
  שמישהו סיים בלי לעדכן
- **פורמט הסטטוסים** של issue / spec / plan הוא הצעת הסוכן. שינוי דורש
  עדכון ב-README של הערוץ וב-`documentation-rules.md`
- `git status` בשורש ה-repo עדיין מכיל שינויים לא קשורים לשיעור

## פתוח / הבא בתור

- [ ] אישור תומר למיקום הערוצים ולחריג של כלל ה-spec
- [ ] `issues/0001` — כלל ה-Git
- [ ] קומיט, כשתומר יבקש
