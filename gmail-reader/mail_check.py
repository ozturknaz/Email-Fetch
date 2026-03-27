"""
Gmail Reader Module
This script connects to Gmail using IMAP and fetches the 5 most recent emails.
It decodes headers to ensure subjects are readable in different encodings.
"""

import imaplib
import email
from email.header import decode_header

def fetch_emails():
    # Server configuration
    IMAP_SERVER = "imap.gmail.com"
    EMAIL_ADDRESS = "YOUR_EMAIL@gmail.com"
    APP_PASSWORD = "YOUR_APP_PASSWORD" # 16-character App Password

    try:
        # Establish a secure connection with Gmail
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_ADDRESS, APP_PASSWORD)
        
        # Select the folder to scan
        mail.select("inbox")
        
        # Search for all emails and get their IDs
        status, messages = mail.search(None, "ALL")
        mail_ids = messages[0].split()
        
        # Get the IDs of the last 5 emails
        last_5_ids = mail_ids[-5:]

        print(f"\n--- Latest 5 Emails ({EMAIL_ADDRESS}) ---\n")
        
        # Iterate through the IDs in reverse order (newest first)
        for m_id in reversed(last_5_ids):
            # Fetch the email content
            res, msg_data = mail.fetch(m_id, "(RFC822)")
            for response in msg_data:
                if isinstance(response, tuple):
                    # Parse the raw email bytes
                    msg = email.message_from_bytes(response[1])
                    
                    # Decode the subject header
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    
                    sender = msg.get("From")
                    print(f"FROM: {sender}\nSUBJECT: {subject}\n" + "-"*30)
        
        # Safely logout from the server
        mail.logout()
    except Exception as e:
        print(f"ERROR OCCURRED: {e}")

if __name__ == "__main__":
    fetch_emails()
