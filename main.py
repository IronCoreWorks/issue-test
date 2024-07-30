from github import Github
import os


github_token = os.getenv("GITHUB_TOKEN")
g = Github(github_token)
repo = g.get_repo("IronCoreWorks/issue-test")

keyword = "GitHub Actions"
assignee_username = "IronCore864"

existing_issue = None
for issue in repo.get_issues(state="open"):
    if keyword in issue.title:
        existing_issue = issue
        break

if existing_issue:
    existing_issue.create_comment("A new update for this issue.")
    print(f"Existing issue found and updated: {existing_issue.html_url}")
    existing_issue.edit(assignee=assignee_username)
else:
    new_issue = repo.create_issue(
        title="New Issue Created by GitHub Actions",
        body="This issue was created using a Python script running in GitHub Actions.",
        assignee=assignee_username,
    )
    print(f"New issue created: {new_issue.html_url}")
