# smart-store-loile
## First project for Module 1 of BI and Analytics

Execute all commands from a PowerShell terminal in the root project folder.

### Part 2 (04) - Git Add-Commit-Push

```shell
git add .
git commit -m "Add .gitignore and requirements.txt files"
git push -u origin main
```
After subsequent changes, you may be able to use a simpler version of the last command:
```shell
git push
```

### Part 2 (05) - Create Virtual Environment

```shell
py -m venv .venv
```

### Part 3 (01) - Git Pull Before Changes

Before making any changes to a project, ALWAYS pull the latest changes from the remote repository on GitHub. Keep both locations up-to-date and in sync.

Pulling ensures that: You work with the latest code. Merge conflicts are minimized. Collaboration stays smooth.

```shell
git pull origin main
```

### Part 3 (02) - Activate Virtual Environment

ALWAYS activate the .venv before working on the project.Activate whenever you open a new terminal.

```shell
.venv\Scripts\activate
```
