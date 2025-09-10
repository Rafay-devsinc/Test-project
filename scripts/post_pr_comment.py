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






# import os
# import sys
# import requests

# PR_NUMBER = os.getenv("PR_NUMBER")
# if not PR_NUMBER:
#     print("PR_NUMBER not set. Skipping posting comment.")
#     sys.exit(0)

# GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# REPO = os.getenv("GITHUB_REPOSITORY")  # e.g., "Rafay-devsinc/Test-project"

# with open("load_test_results.txt") as f:
#     body = f.read()

# url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
# headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# r = requests.post(url, headers=headers, json={"body": body})
# r.raise_for_status()
# print("Comment posted successfully!")



import os
import sys
import requests

# Get PR number from environment
PR_NUMBER = os.getenv("PR_NUMBER")

# Demo / fallback
if not PR_NUMBER:
    print("PR_NUMBER not set. Skipping posting comment.")
    print("\n==== DEMO COMMENT ====")
    try:
        with open("load_test_results.txt") as f:
            demo_body = f.read()
        print(demo_body)
    except FileNotFoundError:
        print("No load_test_results.txt found for demo.")
    sys.exit(0)

# Normal behavior
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPOSITORY")  # e.g., "Rafay-devsinc/Test-project"

# Read the load test results
try:
    with open("load_test_results.txt") as f:
        body = f.read()
except FileNotFoundError:
    print("Error: load_test_results.txt not found!")
    sys.exit(1)

# Construct GitHub API URL
url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# Post the comment
try:
    r = requests.post(url, headers=headers, json={"body": body})
    r.raise_for_status()
    print("Comment posted successfully!")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error posting comment: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
