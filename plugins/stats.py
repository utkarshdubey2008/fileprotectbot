import json

def update_stats(action):
    with open('user_data.json', 'r+') as f:
        data = json.load(f)
        # Update statistics based on action
        f.seek(0)
        json.dump(data, f)
        f.truncate()
