# import os
# import requests

# pr_number = os.getenv("PR_NUMBER")
# repo = os.getenv("GITHUB_REPOSITORY")
# token = os.getenv("GITHUB_TOKEN")

# with open("load_test_results.txt", "r") as f:
#     body = f.read()

# url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
# headers = {"Authorization": f"token {token}"}
# payload = {"body": f"### Load Test Results\n```\n{body}\n```"}

# r = requests.post(url, headers=headers, json=payload)
# r.raise_for_status()



import os
import sys
import requests

PR_NUMBER = os.getenv("PR_NUMBER")
if not PR_NUMBER:
    print("PR_NUMBER not set. Skipping posting comment.")
    sys.exit(0)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPOSITORY")  # e.g., "Rafay-devsinc/Test-project"

with open("load_test_results.txt") as f:
    body = f.read()

url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

r = requests.post(url, headers=headers, json={"body": body})
r.raise_for_status()
print("Comment posted successfully!")
