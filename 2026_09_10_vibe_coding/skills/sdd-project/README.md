# sdd-project — סקיל ל-Claude Code

מקים פרויקט Spec Driven Development לצוות של אנשים וסוכנים, בסגנון
פרויקט Vibe Coding של A619 (10 בספטמבר 2026), ומנחה את העבודה השוטפת בו.

## התקנה

Claude Code מחפש סקילים ב-`.claude/skills/<name>/SKILL.md`, אישי או של
פרויקט. symlink נתמך. שלוש אפשרויות:

```bash
# אישי — זמין בכל פרויקט במחשב
ln -s "$(pwd)/skills/sdd-project" ~/.claude/skills/sdd-project

# של פרויקט — זמין רק כאן
mkdir -p .claude/skills && ln -s ../../skills/sdd-project .claude/skills/sdd-project

# העתקה לפרויקט אחר
cp -R skills/sdd-project /path/to/other/.claude/skills/
```

מה שרואים כשזה עובד: הקלדת `/sdd-project` ב-Claude Code מציעה את הסקיל
עם רמז הארגומנטים `<target-dir> [--name "שם"] [--owner "שם"]`.

## שימוש

**להקים פרויקט חדש:**

```text
/sdd-project ./my-project --name "בוט תזכורות" --owner "דנה"
```

או בשפה חופשית: "תקים לי פרויקט לעבודה עם סוכנים בשם X". הסקיל מזהה את
הבקשה מהתיאור שלו.

**לעבוד בפרויקט קיים:** בתיקייה שיש בה `AGENTS.md` ו-`specs/`, הסקיל
מנחה: issue → spec → אישור → plan → אישור → קוד → סגירת סשן.

## הרצה ידנית של הסקריפט

```bash
python3 skills/sdd-project/scripts/scaffold.py ./my-project \
  --name "בוט תזכורות" --owner "דנה" \
  --request "תבני לי בוט שמזכיר לצוות פגישות" \
  --agent-id claude/dana --model "Claude Fable 5.1"
```

פלט שנבדק ב-10 בספטמבר 2026:

```text
פרויקט: בוט תזכורות
יעד:    /.../my-project
תאריך:  2026-09-10 · סוכן: claude/dana · בעלים: דנה

נוצרו 27 קבצים:
  + AGENTS.md
  + CLAUDE.md
  + README.md
  + docs/README.md
  ...
  + specs/_template.md

הצעד הבא: פתח את docs/sessions/2026-09-10-01-project-setup.md ...
```

הרצה חוזרת על תיקייה קיימת מדפיסה `=` ליד כל קובץ שדולג ואינה דורסת.
`--force` דורס. `--help` מציג את כל הפרמטרים.

## מה בשלד

```text
AGENTS.md, CLAUDE.md, README.md
progress/status.md                 ההווה
issues/  (README + 3 ראשונים)      הבעיה
specs/   (README + תבנית)          הדרישות
plans/   (README + 0001)           הדרך
docs/    conventions, journal, sessions, decisions, team
```

27 קבצים. הרשימה המלאה: `python3 scripts/scaffold.py --help` והרצה על
תיקייה ריקה.

## איך משנים את הכללים

עורכים ב-`templates/`, לא בפרויקט מוקם. Placeholders:

| | |
|---|---|
| `{{PROJECT_NAME}}` | שם הפרויקט |
| `{{PROJECT_DESCRIPTION}}` | משפט תיאור |
| `{{OWNER}}` | בעל/ת הפרויקט |
| `{{AGENT_ID}}` | `כלי/מפעיל` |
| `{{TOOL}}`, `{{MODEL}}` | הכלי והמודל של הסוכן המקים |
| `{{DATE}}`, `{{DATE_HE}}` | `2026-09-10` / `10 בספטמבר 2026` |
| `{{REQUEST_QUOTE}}` | ציטוט הבקשה לרשומת הסשן |

קובץ תבנית ששמו מתחיל ב-`DATE-01-` מקבל את תאריך ההקמה בשם.

## מקורות

- תיעוד Claude Code, Skills: https://code.claude.com/docs/en/skills.md —
  מיקומי סקילים, שדות frontmatter, `${CLAUDE_SKILL_DIR}`, תמיכה ב-symlink.
  נבדק ב-10 בספטמבר 2026
- תיעוד Claude Code, Memory: https://code.claude.com/docs/en/memory.md —
  ייבוא `@AGENTS.md` מתוך `CLAUDE.md`. נבדק ב-10 בספטמבר 2026
