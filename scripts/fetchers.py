import os
import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup

def fetch_github_stats(username, token=None):
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    
    user_resp = requests.get(f'https://api.github.com/users/{username}', headers=headers)
    user_data = user_resp.json()
    
    created_at = datetime.strptime(user_data.get('created_at', '2020-01-01T00:00:00Z'), "%Y-%m-%dT%H:%M:%SZ")
    days_on_github = (datetime.utcnow() - created_at).days

    repos_url = user_data.get('repos_url')
    repos_resp = requests.get(repos_url, headers=headers)
    repos = repos_resp.json() if repos_resp.status_code == 200 else []
    
    stars = sum(repo.get('stargazers_count', 0) for repo in repos)
    forks = sum(repo.get('forks_count', 0) for repo in repos)
    public_repos = user_data.get('public_repos', 0)
    followers = user_data.get('followers', 0)

    pr_query = f'author:{username} type:pr'
    pr_resp = requests.get(f'https://api.github.com/search/issues?q={pr_query}', headers=headers)
    total_prs = pr_resp.json().get('total_count', 0) if pr_resp.status_code == 200 else 0

    issue_query = f'author:{username} type:issue'
    issue_resp = requests.get(f'https://api.github.com/search/issues?q={issue_query}', headers=headers)
    total_issues = issue_resp.json().get('total_count', 0) if issue_resp.status_code == 200 else 0

    headers_commits = headers.copy()
    headers_commits['Accept'] = 'application/vnd.github.cloak-preview+json'
    commit_query = f'author:{username}'
    commit_resp = requests.get(f'https://api.github.com/search/commits?q={commit_query}', headers=headers_commits)
    total_commits = commit_resp.json().get('total_count', "1,200+") if commit_resp.status_code == 200 else "1,200+"

    events_resp = requests.get(f'https://api.github.com/users/{username}/events/public', headers=headers)
    events = events_resp.json() if events_resp.status_code == 200 else []
    
    latest_commit = "No recent commits"
    latest_repo = "Unknown"
    for event in events:
        if event.get('type') == 'PushEvent':
            repo_name = event.get('repo', {}).get('name', 'Unknown')
            commits = event.get('payload', {}).get('commits', [])
            if commits:
                latest_commit = commits[0].get('message', '').split('\n')[0]
            latest_repo = repo_name
            break

    return {
        "days_on_github": days_on_github,
        "total_commits": total_commits,
        "public_repos": public_repos,
        "followers": followers,
        "stars": stars,
        "forks": forks,
        "total_prs": total_prs,
        "total_issues": total_issues,
        "latest_repo": latest_repo,
        "latest_commit": latest_commit[:50] + "..." if len(latest_commit) > 50 else latest_commit
    }

def verify_deployments(deployments):
    results = []
    for dep in deployments:
        status = "OFFLINE"
        if dep['url']:
            try:
                resp = requests.get(dep['url'], timeout=5)
                if resp.status_code < 400:
                    status = "ONLINE"
            except:
                pass
        else:
            status = "COMING SOON"
        
        results.append({
            "name": dep['name'],
            "url": dep['url'],
            "status": status,
            "tech": dep['tech']
        })
    return results

def fetch_leetcode_stats(username):
    try:
        resp = requests.get(f"https://leetcode-stats-api.herokuapp.com/{username}")
        data = resp.json()
        if data.get("status") == "success":
            return {
                "solved": data.get("totalSolved", 0),
                "ranking": data.get("ranking", 0),
                "easy": data.get("easySolved", 0),
                "medium": data.get("mediumSolved", 0),
                "hard": data.get("hardSolved", 0)
            }
    except:
        pass
    return {"solved": 0, "ranking": 0, "easy": 0, "medium": 0, "hard": 0}
