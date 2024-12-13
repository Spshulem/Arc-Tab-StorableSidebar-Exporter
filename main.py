import json
import csv
from datetime import datetime, timezone

# Apple epoch offset (2001-01-01 00:00:00 UTC)
APPLE_EPOCH_OFFSET = 978307200

json_file_path = 'input'
output_csv_path = 'output.csv'

with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

containers = data.get("sidebar", {}).get("containers", [])

columns = ["id", "title", "parentID", "createdAt", "savedTitle", "savedURL", "savedMuteStatus"]
rows = []

for container in containers:
    if "items" in container:
        for i in container["items"]:
            if isinstance(i, dict) and "id" in i:
                item_id = i.get("id", "")
                title = i.get("title", "")
                parentID = i.get("parentID", "")
                
                # Convert createdAt from Apple absolute time to human-readable
                createdAt_raw = i.get("createdAt", "")
                if isinstance(createdAt_raw, (int, float)) and createdAt_raw != "":
                    # Convert Apple CFAbsoluteTime to UNIX time
                    unix_ts = createdAt_raw + APPLE_EPOCH_OFFSET
                    dt = datetime.fromtimestamp(unix_ts, tz=timezone.utc)
                    createdAt = dt.strftime("%Y-%m-%d %H:%M:%S %Z")
                else:
                    createdAt = ""

                data_field = i.get("data", {})
                tab_data = data_field.get("tab", {})
                savedTitle = tab_data.get("savedTitle", "")
                savedURL = tab_data.get("savedURL", "")
                savedMuteStatus = tab_data.get("savedMuteStatus", "")

                rows.append([
                    item_id,
                    title,
                    parentID,
                    createdAt,
                    savedTitle,
                    savedURL,
                    savedMuteStatus
                ])

with open(output_csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(rows)

print(f"CSV written to {output_csv_path}")