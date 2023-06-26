import os
import sys
import json

def parse_facebook_messages(data):
    # sender_name = data["participants"][0]["name"].encode('latin-1').decode('utf-8')+"\n"
    sender_name = data["participants"][0]["name"]
    messages = [sender_name.encode('latin-1').decode('utf-8') + "\n"]

    sorted_messages = sorted(data["messages"], key=lambda x: x["timestamp_ms"])

    for message in sorted_messages:
        if "content" in message:
            sender = "U" if message.get("sender_name") == sender_name else "S"
            content = message["content"]
            # messages.append(sender + " : " + content + "\n")
            messages.append(sender + " : " + message["content"].encode('latin-1').decode('utf-8')+"\n")


    messages.append("\n----------------------------------------------------\n\n")
    return messages

def write_messages_to_file(messages, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for message in messages:
            f.write(message)
def process_facebook_json_files(directory):
    output_file = directory.rstrip('/') + '.txt'

    all_files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.json'):
                all_files.append(os.path.join(root, filename))

    all_files.sort()  # Sort the files alphabetically for consistent order

    messages = []
    for file in all_files:
        with open(file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            parsed_messages = parse_facebook_messages(data)
            messages.extend(parsed_messages)

    write_messages_to_file(messages, output_file)

# Check if directory argument is provided
if len(sys.argv) < 2:
    print("Please provide the directory path as an argument.")
    sys.exit(1)

directory_path = sys.argv[1]
process_facebook_json_files(directory_path)


