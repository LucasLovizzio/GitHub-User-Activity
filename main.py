import requests

username = input("Enter your github username: ")

url = f"https://api.github.com/users/{username}/events/public"

response = requests.get(url)

if response.status_code == 200:
    events = response.json()
    for event in events:
        print(event)
else:
    print("Error fetching events")

# Run the script
# python main.py
# Enter your github username: your_github_username