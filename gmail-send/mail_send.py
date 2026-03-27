"""
Gmail Send Module
This script sends automated emails using Gmail's SMTP server.
It uses TLS encryption for secure communication.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # --- CONFIGURATION ---
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL_ADDRESS = "YOUR_EMAIL@gmail.com" 
    APP_PASSWORD = "YOUR_APP_PASSWORD" 

    # --- EMAIL CONTENT ---
    RECIPIENT_MAIL = "RECIPIENT@gmail.com"
    SUBJECT = "Automated Message from Email-Fetch"
    MESSAGE = "Hello, this email was sent using the Python SMTP library. Everything is working perfectly!"

    try:
        # 1. Initialize the multipart message container
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_MAIL
        msg['Subject'] = SUBJECT
        
        # Attach the body text to the email
        msg.attach(MIMEText(MESSAGE, 'plain'))

        # 2. Setup the SMTP server connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() # Secure the connection using TLS

        # 3. Authenticate and send the email
        server.login(EMAIL_ADDRESS, APP_PASSWORD)
        server.send_message(msg)
        
        print(f"SUCCESS: Email sent to {RECIPIENT_MAIL}!")
        
        # Close the connection
        server.quit()
    except Exception as e:
        print(f"ERROR OCCURRED: {e}")

if __name__ == "__main__":
    send_email()
