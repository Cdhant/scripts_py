import os
import json

all_file = []
messages = []
for dirname, _, filenames in os.walk('./inbox'):
    for filename in filenames:
        # print(os.path.join(dirname, filename))
        extention = os.path.splitext(os.path.join(dirname, filename))[1]
        if (extention == '.json'):
            all_file.append(os.path.join(dirname, filename))
            # print(extention)
    # print(filenames)
# print(all_file)
for file in all_file:
    data = json.load(open(file))
    print(data["participants"][0]["name"].encode('latin-1').decode('utf-8'))
    # print(data["participants"][1]["name"].encode('latin-1').decode('utf-8'))
    messages.insert(0,data["participants"][0]["name"].encode('latin-1').decode('utf-8') +"\n")

    messages.reverse()

    print(data["messages"])
    for message in data["messages"]:
    # if reverse_message:
        # for message in reverse_message:    
        if "content" in message:
            # print(message["sender_name"].encode('latin-1').decode('utf-8'))
            if message["sender_name"].encode('latin-1').decode('utf-8') == "बुटवल उप-महानगरपालिका, रुपन्देही, Butwal Sub-Metropolitan City, Rupandehi":
                sender = "S"
            else:
                sender = "U"
            print(sender, ":", message["content"].encode('latin-1').decode('utf-8'))
        
            messages.append(sender + " : " + message["content"].encode('latin-1').decode('utf-8')+"\n")
    print("----------------------------------------------------")
    messages.append("\n ----------------------------------------------------\n\n")
    with open('herveda_dump.txt','w') as f:
        print(messages)
        for item in messages:
            f.write(item)

