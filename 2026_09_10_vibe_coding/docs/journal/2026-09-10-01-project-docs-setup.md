# הקמת שלד התיעוד לפרויקט משותף של אנשים וסוכנים

| | |
|---|---|
| **תאריך** | 2026-09-10 |
| **מבצע** | `claude/tomer` (Claude Code, לבקשת תומר) |
| **סשן** | `docs/sessions/2026-09-10-01-tomer-claude-project-docs-setup.md` |

## מה נעשה

תיקיית השיעור `2026_09_10_vibe_coding` הייתה ריקה. נוצר בה שלד תיעוד מלא
לעבודה משותפת של כמה בני אדם וכמה סוכני AI, בלי קוד:

- **שורש:** `AGENTS.md` (הוראות לכל סוכן בכל כלי), `CLAUDE.md` (מייבא את
  `AGENTS.md` ומוסיף תזכורת), `README.md` (שער הפרויקט ומבנהו)
- **`docs/README.md`** — מפת התיעוד: ארבעה סוגי מסמכים ומה כל אחד עונה
- **`docs/team.md`** — טבלת אנשים וסוכנים, עם כלל התחומים
- **`docs/conventions/collaboration-rules.md`** — המסמך המחייב: קרא, רשום,
  עבוד בתחום, כתוב, שחרר. כולל טבלה של מה מהצ׳אט חייב להגיע למסמך
- **`docs/conventions/documentation-rules.md`** — פורמט של יומן, סשן,
  החלטה, טבלת מעקב ודיונים
- **`docs/journal/`** — `_template.md`, `00-tracking.md` (נעילה רכה),
  `discussions.md` (ערוץ אסינכרוני, עם הודעת פתיחה), והרשומה הזו
- **`docs/sessions/`** — `_template.md` והרשומה הראשונה, שמתעדת את
  בקשת תומר בלשונו ואת ההנחות שהסוכן הניח
- **`docs/decisions/`** — `_template.md` ו-`0001`: התיעוד הוא הזיכרון
  המשותף, עם שלוש החלופות שנשקלו

לא הורץ קוד. לא בוצע קומיט.

## למה

תומר ביקש, בהודעה אחת, פרויקט שבו עובדים כמה אנשים וכמה סוכנים, שכל מה
שנכתב בצ׳אט מתועד במסמכים. הבעיה שהתיעוד פותר: צ׳אט הוא זיכרון פרטי
שנעלם, וצוות מעורב בלי זיכרון משותף סובל מדריסה, חזרה על עבודה וסתירות
שקטות. ההחלטה על המבנה והחלופות:
`docs/decisions/0001-documentation-is-shared-memory.md`.

המבנה יושר עם כללי התיעוד הכלליים של תומר (יומן ממוספר לפי יום, תבנית,
טבלת מעקב, `discussions.md`), אך הועתק לתוך ה-repo כי הסטודנטים משכפלים
רק אותו. התוספת היחידה על הכללים הכלליים: `docs/sessions/`, שנולדה ישירות
מהדרישה "כל מה שנכתב בצ׳אט יש לתעד".

## קבצים שהושפעו

כולם נוצרו, יחסית ל-`2026_09_10_vibe_coding/`:

- `AGENTS.md`, `CLAUDE.md`, `README.md`
- `docs/README.md`, `docs/team.md`
- `docs/conventions/collaboration-rules.md`, `docs/conventions/documentation-rules.md`
- `docs/journal/_template.md`, `docs/journal/00-tracking.md`, `docs/journal/discussions.md`, `docs/journal/2026-09-10-01-project-docs-setup.md`
- `docs/sessions/_template.md`, `docs/sessions/2026-09-10-01-tomer-claude-project-docs-setup.md`
- `docs/decisions/_template.md`, `docs/decisions/0001-documentation-is-shared-memory.md`

## מה צריך לדעת כדי להמשיך

- **`AGENTS.md` הוא המקור, `CLAUDE.md` מייבא אותו** בשורת `@AGENTS.md`.
  שינוי בכללים לסוכנים נעשה ב-`AGENTS.md` בלבד
- **אין קוד עדיין.** סעיף "איך מריצים" ב-`README.md` מראה רק בדיקת שלמות
  תיעוד. כשיתווסף קוד, הסעיף חייב להתעדכן בפקודה ובפלט אמיתיים
- **כלל ה-Git** (ענף לכל משימה, merge בלבד ל-`main`) הוא הנחה של הסוכן,
  מחמירה מה-README של ה-repo. ממתין לאישור תומר
- **`git status` בשורש ה-repo** מכיל שינויים לא קשורים לשיעור הזה:
  `.gitignore` שונה ותיקייה `_2026_08_13_Functions_Lambdas_And_Files/` לא
  עוקבת. לא לכלול אותם בקומיט של השלד בלי לשאול

## פתוח / הבא בתור

- [ ] אישור תומר לכלל ה-Git
- [ ] קומיט, כשתומר יבקש
- [ ] סטודנטים וסוכניהם ב-`docs/team.md`
- [ ] קוד ראשון + עדכון "איך מריצים"

## מקורות

- ייבוא קובץ ב-`CLAUDE.md` בתחביר `@path` — אומת ב-10 בספטמבר 2026 מול
  התיעוד הרשמי של Claude Code, עמוד Memory:
  https://code.claude.com/docs/en/memory.md
  (סעיף "Import additional files"). נתיב יחסי נפתר ביחס לקובץ המייבא;
  עומק רקורסיה עד 4; נתיב בתוך backticks אינו מיובא
