import pandas as pd
import os

print("--- Starting Excel Dataset Generation ---")

# This is the full, expanded dataset. You can easily add more items here later.
data = {
    'message': [
        "I forgot my password and I can't log in", "how do i reset my password", "i need to change my login credentials",
        "my password has expired and I need a new one", "can't remember my login details", "locked out of my account please help",
        "my account is locked after too many failed attempts", "can't access my account, it says it's locked",
        "account is disabled, how to enable it?", "my computer is running really slow",
        "everything is lagging and apps take forever to open", "my pc is so sluggish what can I do",
        "why is my laptop so slow all of a sudden", "opening files takes a very long time", "I can't connect to the wifi",
        "the internet is not working on my device", "my wifi shows connected but there's no internet", "no internet access",
        "the wifi connection keeps dropping", "the printer is not working", "i can't print my document",
        "my computer won't detect the printer", "getting a printer offline error", "how do I install the new software update",
        "need help installing the accounting application", "the software installation failed with an error",
        "cannot update the application", "my mouse stopped working", "the keyboard is not typing anything",
        "my screen is flickering", "the monitor is black and won't turn on", "my webcam is not detected in meetings",
        "I think I deleted an important file by accident", "is it possible to recover a deleted folder",
        "i accidentally emptied the recycle bin", "my email is not sending or receiving messages", "i am not getting new emails",
        "getting an error when I try to send an email", "my outlook is not syncing", "emails are stuck in my outbox",
        "my computer shut down and now it's showing a blue screen", "i got a blue screen with an error code",
        "computer crashes with a bsod", "The main software keeps freezing", "my application is not responding",
        "the program hangs and I have to force quit", "excel is frozen and I can't click anything",
        "I can't connect to the company VPN", "the vpn is not working", "getting an error when connecting to the VPN",
        "my vpn connection is very slow", "I got a security alert about a virus", "my antivirus says it found a threat",
        "i think my computer has a virus", "received a suspicious phishing email", "how do I back up my data",
        "i need to back up my computer before an update", "what is the procedure for backing up my files",
        "how to restore files from a backup", "my login is taking too long", "it takes five minutes to log into my computer",
        "after entering my password the screen is black for a long time"
    ],
    'category': [
        "password_reset", "password_reset", "password_reset", "password_reset", "password_reset", "account_lockout",
        "account_lockout", "account_lockout", "account_lockout", "slow_computer", "slow_computer", "slow_computer",
        "slow_computer", "slow_computer", "internet_issue", "internet_issue", "internet_issue", "internet_issue",
        "internet_issue", "printer_issue", "printer_issue", "printer_issue", "printer_issue", "software_install",
        "software_install", "software_install", "software_install", "hardware_issue", "hardware_issue", "hardware_issue",
        "hardware_issue", "hardware_issue", "data_recovery", "data_recovery", "data_recovery", "email_issue",
        "email_issue", "email_issue", "email_issue", "email_issue", "blue_screen", "blue_screen", "blue_screen",
        "software_freeze", "software_freeze", "software_freeze", "software_freeze", "vpn_issue", "vpn_issue",
        "vpn_issue", "vpn_issue", "security_alert", "security_alert", "security_alert", "security_alert",
        "system_backup", "system_backup", "system_backup", "system_backup", "slow_login", "slow_login", "slow_login"
    ]
}

# Create a pandas DataFrame from our data dictionary
df = pd.DataFrame(data)

# Define the path where the Excel file will be saved
output_folder = 'ml_model'
output_filename = 'support_data.xlsx'
output_path = os.path.join(output_folder, output_filename)

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Save the DataFrame to an Excel file
# The index=False part is important to avoid writing row numbers into the file
df.to_excel(output_path, index=False)

print(f"\n--- ✅ SUCCESS! ---")
print(f"Excel file '{output_filename}' has been created successfully in the '{output_folder}' folder.")