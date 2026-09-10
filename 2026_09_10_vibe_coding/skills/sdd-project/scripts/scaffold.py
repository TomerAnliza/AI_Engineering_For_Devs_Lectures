#!/usr/bin/env python3
"""מקים שלד פרויקט SDD (Spec Driven Development) לצוות של אנשים וסוכנים.

מעתיק את התבניות מ-templates/ אל תיקיית היעד, מחליף placeholders, ונותן
לרשומות היומן והסשן הראשונות את תאריך ההקמה. אינו דורס קבצים קיימים אלא
אם התבקש במפורש (--force).

שימוש:
    python3 scaffold.py <target-dir> --name "שם הפרויקט" --owner "שם" \
        [--description "..."] [--agent-id claude/name] [--tool "Claude Code"] \
        [--model "..."] [--date YYYY-MM-DD] [--request "ציטוט הבקשה"] [--force]
"""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
import sys
from pathlib import Path

# תבניות נמצאות ליד הסקריפט, בתוך תיקיית הסקיל
TEMPLATES = Path(__file__).resolve().parent.parent / "templates"

# שמות חודשים לתאריך עברי מוחלט: "10 בספטמבר 2026"
HEBREW_MONTHS = [
    "בינואר", "בפברואר", "במרץ", "באפריל", "במאי", "ביוני",
    "ביולי", "באוגוסט", "בספטמבר", "באוקטובר", "בנובמבר", "בדצמבר",
]


def hebrew_date(d: dt.date) -> str:
    return f"{d.day} {HEBREW_MONTHS[d.month - 1]} {d.year}"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("target", help="תיקיית היעד. נוצרת אם אינה קיימת")
    p.add_argument("--name", required=True, help="שם הפרויקט, כפי שיופיע בכותרות")
    p.add_argument("--owner", required=True, help="בעל/ת הפרויקט — מי שמכריע ומאשר specs")
    p.add_argument("--description", default="פרויקט משותף לאנשים וסוכני AI.", help="משפט אחד על הפרויקט")
    p.add_argument("--agent-id", default=None, help="מזהה הסוכן המקים, בפורמט כלי/מפעיל. ברירת מחדל: claude/<owner>")
    p.add_argument("--tool", default="Claude Code", help="הכלי שבו רץ הסוכן המקים")
    p.add_argument("--model", default="Claude", help="המודל של הסוכן המקים")
    p.add_argument("--date", default=None, help="תאריך ההקמה YYYY-MM-DD. ברירת מחדל: היום")
    p.add_argument("--request", default="(ציטוט הבקשה המקורית של בעל/ת הפרויקט)", help="הבקשה בלשון האדם, לרשומת הסשן")
    p.add_argument("--force", action="store_true", help="לדרוס קבצים קיימים")
    return p.parse_args()


def main() -> int:
    a = parse_args()
    if not TEMPLATES.is_dir():
        print(f"שגיאה: תיקיית התבניות לא נמצאה: {TEMPLATES}", file=sys.stderr)
        return 2

    date = dt.date.fromisoformat(a.date) if a.date else dt.date.today()
    iso = date.isoformat()
    owner_slug = a.owner.strip().lower().replace(" ", "-")
    agent_id = a.agent_id or f"claude/{owner_slug}"

    subs = {
        "{{PROJECT_NAME}}": a.name,
        "{{PROJECT_DESCRIPTION}}": a.description,
        "{{OWNER}}": a.owner,
        "{{AGENT_ID}}": agent_id,
        "{{TOOL}}": a.tool,
        "{{MODEL}}": a.model,
        "{{DATE}}": iso,
        "{{DATE_HE}}": hebrew_date(date),
        "{{REQUEST_QUOTE}}": a.request.replace("\n", "\n> "),
    }

    target = Path(a.target).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)

    created, skipped = [], []
    for src in sorted(TEMPLATES.rglob("*")):
        if src.is_dir():
            continue
        rel = src.relative_to(TEMPLATES)
        # רשומות היומן והסשן הראשונות מקבלות את תאריך ההקמה בשם הקובץ
        rel = Path(str(rel).replace("DATE-01-", f"{iso}-01-"))
        dst = target / rel
        if dst.exists() and not a.force:
            skipped.append(rel)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8")
        for k, v in subs.items():
            text = text.replace(k, v)
        dst.write_text(text, encoding="utf-8")
        created.append(rel)

    print(f"פרויקט: {a.name}")
    print(f"יעד:    {target}")
    print(f"תאריך:  {iso} · סוכן: {agent_id} · בעלים: {a.owner}")
    print()
    print(f"נוצרו {len(created)} קבצים:")
    for r in created:
        print(f"  + {r}")
    if skipped:
        print()
        print(f"דולגו {len(skipped)} קבצים קיימים (השתמש ב---force כדי לדרוס):")
        for r in skipped:
            print(f"  = {r}")

    # בדיקה שלא נשארו placeholders שלא הוחלפו
    leftovers = [
        r for r in created
        if "{{" in (target / r).read_text(encoding="utf-8")
    ]
    if leftovers:
        print()
        print("אזהרה: נשארו placeholders בקבצים:", ", ".join(map(str, leftovers)))

    print()
    print("הצעד הבא: פתח את docs/sessions/" + f"{iso}-01-project-setup.md"
          " והשלם את סעיף 'הנחות שהסוכן הניח'. אחר כך — AGENTS.md נטען אוטומטית לכל סוכן.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
