import json
import random

# Load user accounts from the provided JSON file
with open('CSIT314.UserAccount.json', 'r') as f:
    user_accounts = json.load(f)

# Sample data to choose from
roles = ["buyer", "seller", "rea"]
descriptions = {
    "buyer": "I am a buyer",
    "seller": "I am a seller",
    "rea": "I am a real estate agent"
}

# Generate user profiles
user_profiles = []

for i, account in enumerate(user_accounts):
    # Cycle through roles in a repeating manner
    role = roles[i % len(roles)]
    user_profile = {
        "userAccountId": account["_id"]["$oid"],
        "name": f"{role.capitalize()} {i // len(roles) + 1}",
        "role": role,
        "description": descriptions[role],
        "status": True
    }
    user_profiles.append(user_profile)

# Write user profiles to a JSON file
with open('test_userProfiles.json', 'w') as f:
    json.dump(user_profiles, f, indent=4)

print("Generated user profiles and saved to test_userProfiles.json")