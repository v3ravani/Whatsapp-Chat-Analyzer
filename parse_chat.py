import re
from datetime import datetime

def parse_chat(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    chat_data = []
    message_pattern = re.compile(r"(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}\s?[APM]{2}) - ([^:]+?): (.+)")
    
    for line in lines:
        line = line.replace("\u202f", " ")  # Fixing special spaces
        match = message_pattern.match(line)
        if match:
            date_str, time_str, sender, message = match.groups()
            timestamp = datetime.strptime(date_str + ", " + time_str, "%m/%d/%y, %I:%M %p")
            chat_data.append({"timestamp": timestamp, "sender": sender, "message": message})
    
    return chat_data

# Run the parser
chat_data = parse_chat("chat.txt")

# Debug: Print first 5 parsed messages
print(f"\n📜 Total messages parsed: {len(chat_data)}")
for msg in chat_data[:5]:
    print(msg)
