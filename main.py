import argparse
import requests
import sys

def fetch_github_activity(ussername : string):
    url = f'https://api.github.com/users/{username}/events'
    try :
        response = requests.get(url)
        response.raise_for_status()
        events = response.json()

        if not events:
            print(f'No recent activity found for user : {username}')
            return
        
        print(f"Recent activity for Github user '{username}': \n")
        for event in events[:10]
            event_type = event['type']
            repo_name = event['repo']['name']
            print(f"- {event_type} in {repo_name}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching activity: {e}", file = sys.stderr)
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