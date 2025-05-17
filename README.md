# Solar Challenge Week 1
A project for learning Git and CI/CD.

## Setup
1. Clone: `git clone https://github.com/your-username/solar-challenge-week1.git`
2. Create venv: `python3 -m venv .venv`
3. Activate: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows)
4. Install: `pip install -r requirements.txt`

  ## Git Version Control Usage
This project followed Git best practices for version control:

Branching: Each major task (EDA per country) was done on its own branch:

eda-benin, eda-sierra_leone, and eda-togo

Commits: Meaningful and atomic commits were made regularly to document progress.

Pull Requests: Each branch was pushed 

## Git Commit Log Snapshot
* a1c3e2f (HEAD -> eda-togo) feat: complete EDA for Togo
* 84bce1a (eda-sierra_leone) feat: cleaned Sierra Leone dataset
* 1f2e4bd (eda-benin) feat: add time series plots for Benin
* 53a10ab (main) chore: initial setup and .gitignore