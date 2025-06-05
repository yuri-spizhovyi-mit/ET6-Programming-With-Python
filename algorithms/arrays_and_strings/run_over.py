import requests

# Target contributors
target_contributors = {"Safa-Saber", "Safi222", "Mr-Glucose", "ayhm01", "tamarasaqer"}

# Result mapping
contributor_groups = {name: [] for name in target_contributors}

# Loop through groups
for i in range(34):
    group_id = f"{i:02}"  # Ensures 00, 01, ..., 33
    url = f"https://github.com/MIT-Emerging-Talent/ET6-foundations-group-{group_id}/graphs/contributors-data"

    try:
        res = requests.get(url)
        res.raise_for_status()
        json_data = res.json()

        for contributor in json_data:
            username = contributor.get("author", {}).get("login", "")
            if username in target_contributors:
                contributor_groups[username].append(group_id)

        print(f"Group {group_id} checked.")

    except Exception as e:
        print(f"Failed to fetch group {group_id}: {e}")

# Print final result
print("\nContributor Group Membership:")
for user, groups in contributor_groups.items():
    if groups:
        print(f"{user} contributed to group(s): {groups}")
    else:
        print(f"{user} was not found in any group.")
