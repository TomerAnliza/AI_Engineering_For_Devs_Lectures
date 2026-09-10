# סשן: בקשה לאפליקציית קריאות שירות → spec בלבד

| | |
|---|---|
| **תאריך** | 2026-09-10 |
| **אדם** | תומר |
| **סוכן** | `claude/tomer` |
| **כלי** | Claude Code (Claude Fable 5.1) |

## מה התבקש

> "I want to build an internal app for managing service tickets in a
> company. Users should be able to submit a new service request by filling
> in the title, description, and location. Each request should have a
> status (Open, In Progress, Resolved) and be assigned to a technician.
> Technicians should have a dashboard showing only the requests assigned to
> them, with the ability to update the status. There should also be an
> admin panel for assigning technicians and viewing all requests. Please
> create the database structure, basic UI, and logic flows."

## מה הוחלט

- הסוכן לא כתב קוד, מבנה בסיס נתונים או ממשק. נכתב spec וההמשך ממתין
  לאישור אדם. זו לא החלטה חדשה אלא יישום של
  `docs/decisions/0002-work-channels-and-spec-first.md`
- הבקשה קיבלה מספר רץ **0005** (issue + spec), ולא 0003, כי 0003 הוא
  משימה גנרית ("קוד ראשון") ואילו זה רכיב מוגדר. 0005 יסגור גם את 0003

## הנחות שהסוכן הניח בלי לשאול

- **spec אחד לכל האפליקציה**, ולא spec לכל זרימה. הנימוק: שלוש הזרימות
  חולקות מודל נתונים אחד וכללי הרשאה אחדים, ופיצול היה מכפיל את הטקסט.
  התוכנית יכולה לפצל את המימוש לשלבים
- **שלושה תפקידים נפרדים** (`requester`, `technician`, `admin`), תפקיד יחיד
  לכל משתמש. הבקשה אמרה "users", "technicians", "admin" ולא אמרה אם אדם
  יכול להיות גם וגם
- **קריאה נוצרת ללא טכנאי**, והשיוך הוא פעולה נפרדת של מנהל. הבקשה אמרה
  "be assigned to a technician" בלי לומר מתי ועל ידי מי, אבל "admin panel
  for assigning technicians" מרמז שזה תפקיד המנהל
- **מגבלות אורך** (כותרת 3–120, תיאור עד 2000, מיקום עד 120). המספרים
  שרירותיים וסבירים; תומר יכול לשנות
- **`In Progress` דורש טכנאי משויך**, ו-`Resolved` סופי לטכנאי. לא
  התבקש. נכתב כדי שיהיה כלל שאפשר לבדוק, וסומן בשאלה פתוחה 3
- ההצעות בשאלות הפתוחות (אין login, אין מסך למגיש, עברית) הן הצעות
  בלבד, לא הנחות שהוטמעו כעובדה

## מה לא נעשה, ולמה

- **לא נכתב קוד, סכמת DB או UI** — אין spec מאושר. `AGENTS.md`: "סוכן
  שמתבקש לכתוב קוד לרכיב בלי spec מאושר כותב את ה-spec ועוצר"
- **לא נכתבה תוכנית** (`plans/0005`) — תוכנית באה אחרי spec מאושר, כי
  בחירת ספריות ואחסון תלויה בתשובה לשאלת הזהות
- **לא נבחרה טכנולוגיה** — שייך לתוכנית

## תוצרים

- `issues/0005-service-tickets-app.md`
- `specs/0005-service-tickets-app.md` (טיוטה)
- `docs/journal/2026-09-10-04-service-tickets-spec.md`

## פתוח

- [ ] תומר: אישור ה-spec ותשובות ל-7 השאלות הפתוחות. גם ב-`discussions.md`
- [ ] אחרי האישור: `plans/0005`, ועצירה נוספת לאישור התוכנית
