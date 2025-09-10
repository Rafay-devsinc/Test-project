import os
import requests

pr_number = os.getenv("PR_NUMBER")
repo = os.getenv("GITHUB_REPOSITORY")
token = os.getenv("GITHUB_TOKEN")

with open("load_test_results.txt", "r") as f:
    body = f.read()

url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
headers = {"Authorization": f"token {token}"}
payload = {"body": f"### Load Test Results\n```\n{body}\n```"}

r = requests.post(url, headers=headers, json=payload)
r.raise_for_status()
