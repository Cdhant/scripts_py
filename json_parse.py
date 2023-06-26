import os
import json

all_files = []
messages = []

# Recursively search for JSON files in the "inbox" directory
for root, dirs, files in os.walk('./inbox'):
    for file in files:
        if file.endswith('.json'):
            all_files.append(os.path.join(root, file))

# Process each JSON file
for file in all_files:
    with open(file, 'r') as json_file:
        data = json.load(json_file)
        
        # Extract sender name and add it to the messages list
        sender_name = data["participants"][0]["name"]
        messages.append(sender_name + "\n")
        
        # Sort messages based on timestamp
        sorted_messages = sorted(data["messages"], key=lambda x: x["timestamp_ms"])
        
        # Iterate over sorted messages
        for message in sorted_messages:
            if "content" in message:
                sender = "S" if message["sender_name"] == "बुटवल उप-महानगरपालिका, रुपन्देही, Butwal Sub-Metropolitan City, Rupandehi" else "U"
                content = message["content"]
                print(sender, ":", content)
                messages.append(sender + " : " + content + "\n")
        
        messages.append("\n----------------------------------------------------\n\n")

# Write messages to the output file
with open('herveda_dump.txt', 'w', encoding='utf-8') as f:
    f.writelines(messages)
