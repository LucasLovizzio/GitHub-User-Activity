#!/usr/bin/env python3

import argparse
import requests
import sys

def fetch_github_activity(username):
    """Fetch recent GitHub activity for the given username."""
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url)
        response.raise_for_status()
        events = response.json()

        if not events:
            print(f"No recent activity found for user: {username}")
            return

        print(f"Recent activity for GitHub user '{username}':\n")
        for event in events:
            if event['type'] == 'IssueCommentEvent':
                print(f"- Commented on issue {event['payload']['issue']['number']}")
            elif event['type'] == 'PushEvent':
                print(f"- Pushed {len(event['payload']['commits'])} commits to {event['repo']['name']}")
            elif event['type'] == 'IssuesEvent':
                print(f"- Created issue {event['payload']['issue']['number']}")
            elif event['type'] == 'WatchEvent':
                print(f"- Starred {event['repo']['name']}")
            elif event['type'] == 'PullRequestEvent':
                print(f"- Created pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewEvent':
                print(f"- Reviewed pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'PullRequestReviewCommentEvent':
                print(f"- Commented on pull request {event['payload']['pull_request']['number']}")
            elif event['type'] == 'CreateEvent':
                print(f"- Created {event['payload']['ref_type']} {event['payload']['ref']}")
            elif event['type'] == 'DeleteEvent':
                print(f"- Deleted {event['payload']['ref_type']} {event['payload']['ref']}")
            elif event['type'] == 'ForkEvent':
                print(f"- Forked {event['repo']['name']}")

            else:
                print(f"-  {event['type']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching activity: {e}", file=sys.stderr)
    except KeyError:
        print("Unexpected response format from GitHub API.", file=sys.stderr)

def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Fetch recent GitHub activity for a user.")
    parser.add_argument("username", help="GitHub username to fetch activity for")
    args = parser.parse_args()

    fetch_github_activity(args.username)

if __name__ == "__main__":
    main()
