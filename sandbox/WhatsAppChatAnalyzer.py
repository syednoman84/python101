import re
from collections import defaultdict
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Path to your chat file
file_path = "/Users/NomanAhmed/Documents/Noman/code/github/python101/sandbox/whatsapp_chat.txt"

# Read the WhatsApp chat file
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Regex to match messages
pattern = re.compile(
    r"^\[(\d{1,2}/\d{1,2}/\d{2}),\s+\d{1,2}:\d{2}:\d{2}\s*(?:AM|PM|am|pm|AM |PM )?\]\s+(.*?):"
)

# Count messages per user per date
message_counts = defaultdict(int)

for line in lines:
    match = pattern.match(line)
    if match:
        date_str, sender = match.groups()
        try:
            date = datetime.strptime(date_str, "%m/%d/%y").date()
        except ValueError:
            continue
        key = (str(date), sender.strip())
        message_counts[key] += 1

# --- Table 1: Messages by Date and Sender ---
daily_data = [{"Sender": k[1], "Message Count": v} for k, v in message_counts.items()]
daily_df = pd.DataFrame(daily_data)

if not daily_df.empty:
    # --- Table 2: Total Messages by Sender ---
    total_df = daily_df.groupby("Sender")["Message Count"].sum().reset_index()
    total_df.sort_values(by="Message Count", ascending=False, inplace=True)
    print("\n***** Total Messages by Sender - June 2025 *****")
    print(total_df.to_string(index=False))

    # --- Vertical Bar Chart: Total Messages per Sender ---
    plt.figure(figsize=(14, 6))
    plt.bar(total_df["Sender"], total_df["Message Count"], color='skyblue')
    plt.xticks(rotation=75, ha='right')
    plt.xlabel("Sender")
    plt.ylabel("Total Messages")
    plt.title("Total Messages by Sender - June 2025")
    plt.tight_layout()
    plt.show()
else:
    print("No messages matched the expected format.")
