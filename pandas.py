import pandas as pd
from twilio.rest import Client
import time

# Use environment variables (safer)
acc_SID = "AC6846f8d49e1d90b506e919335f5da165"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = Client(acc_SID, auth_token)

# Read Excel file
df = pd.read_excel("NEW.xlsx")

# Message templates
messages = {
    'me': "Good morning",
    'frd': "Hi da.. how are you?",
    'pisasu': "Study well"
}

# Loop through dataframe
for _, row in df.iterrows():
    name = row["Name"]
    designation = str(row["Designation"]).lower()
    number = str(row["Number"])

    msg = messages.get(designation, "Hello!")
    final_message = f"Dear {name}, {msg}"

    client.messages.create(
        from_='whatsapp:+14155238886',
        body=final_message,
        to=f'whatsapp:{number}'
    )

    print(f"Sent to {name} -> {number}")

    time.sleep(1)