import os
import json

category_map = {
    "crypto": "cry",
    "forensics": "for",
    "pwn": "pwn",
    "rev": "rev",
    "web": "web",
    "misc": "misc"
}

def export_database(path):
    challenges = []
    level_four_details = {}
    for root, dirs, files in os.walk(path):
        parts = root.split(os.sep)
        if len(parts) - len(path.split(os.sep)) == 4:
            # Extract each of the parent levels leading up to the fourth level
            chal_path = os.sep.join(parts)
            year = parts[1]
            event = parts[2]
            category = parts[3]
            challenge = parts[4]
            with open(os.path.join(chal_path, "challenge.json"), 'r') as f:
                print(chal_path)
                meta_data = json.load(f)
                chal_name = meta_data["name"]
                chal_key = f"{year}{'q' if event == 'CSAW-Quals' else 'f'}" + "-" + category_map[category] + "-" + meta_data["name"].lower().replace(" ", "_")
            # chal_keys = year + "q" if event == "CSAW-Quals" else "f" + "-" + "category" + "-" + challenge
            level_four_details[chal_key] = {
                'year': year,
                'event': event,
                'category': category,
                'challenge': chal_name,
                'path': chal_path
            }

    return level_four_details

def write_json(name, chals):
    with open(name+".json", "w") as f:
        json.dump(chals, f, indent=2)

if __name__ == "__main__":
    directory_path = "competition"
    deep_folders = export_database(directory_path)
    write_json("competition24", deep_folders)