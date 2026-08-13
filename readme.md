# AI Engineering for Developers — Class A619

Course contents, exercises, and code samples.

---

## Push a new project to an empty GitHub repo

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin <URL>
git push -u origin main
```

## When the GitHub repo already has files

```bash
git fetch origin
git rebase origin/main
git push -u origin main
```

Unrelated histories? Merge instead:

```bash
git merge origin/main --allow-unrelated-histories
```

## Daily

```bash
git status
git add .
git commit -m "message"
git push
```

## Inspect

```bash
git log --oneline --graph
git diff
git remote -v
git branch -a
```

## .gitignore

Write it before the first commit.

```gitignore
.env
__pycache__/
venv/
node_modules/
.DS_Store
```

Already committed a secret? Rotate the key, then:

```bash
git rm --cached <file>
```
