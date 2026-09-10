# הקמת שלד הפרויקט

| | |
|---|---|
| **תאריך** | {{DATE}} |
| **מבצע** | `{{AGENT_ID}}` ({{TOOL}}, לבקשת {{OWNER}}) |
| **סשן** | `docs/sessions/{{DATE}}-01-project-setup.md` |

## מה נעשה

הוקם שלד הפרויקט "{{PROJECT_NAME}}" באמצעות הסקיל `sdd-project`: הוראות
סוכנים (`AGENTS.md`, `CLAUDE.md`), שער (`README.md`), חמישה ערוצי עבודה
(`progress/`, `issues/`, `specs/`, `plans/`, `docs/`), תבניות, כללים,
החלטה 0001, issue 0001 (סגור) ו-issues 0002–0003 (פתוחים), plan 0001.

לא נכתב קוד. לא בוצע קומיט.

## למה

{{OWNER}} ביקש/ה פרויקט משותף לאנשים וסוכנים שעובד לפי Spec Driven
Development. הנימוק והחלופות: `docs/decisions/0001-documentation-is-shared-memory.md`.

## קבצים שהושפעו

כל הקבצים בשלד נוצרו. הרשימה: `plans/0001-project-scaffold.md`.

## מה צריך לדעת כדי להמשיך

- `AGENTS.md` הוא המקור לכללי הסוכנים; `CLAUDE.md` מייבא אותו
- אין קוד עדיין. הרכיב הראשון מתחיל ב-`specs/0003-...`
- המספר הרץ הבא הפנוי: `0004`

## פתוח / הבא בתור

- [ ] `issues/0002` — רישום הצוות
- [ ] `issues/0003` — spec ראשון
