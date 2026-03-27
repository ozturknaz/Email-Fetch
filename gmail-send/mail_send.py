import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # --- SETTINGS ---
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    # IMPORTANT: Use environment variables or leave empty for security on GitHub
    EMAIL_ADDRESS = "YOUR_EMAIL@gmail.com" 
    APP_PASSWORD = "YOUR_APP_PASSWORD" 

    # --- CONTENT ---
    RECIPIENT_MAIL = "RECIPIENT@gmail.com"
    SUBJECT = "Greetings from Email-Fetch!"
    MESSAGE = "Hello, this email was sent via Python script. Success!"

    try:
        # 1. Prepare email package
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_MAIL
        msg['Subject'] = SUBJECT
        msg.attach(MIMEText(MESSAGE, 'plain'))

        # 2. Connect and start TLS
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()

        # 3. Login and send
        server.login(EMAIL_ADDRESS, APP_PASSWORD)
        server.send_message(msg)
        
        print(f"SUCCESS: Email sent to {RECIPIENT_MAIL}!")
        
        server.quit()
    except Exception as e:
        print(f"ERROR OCCURRED: {e}")

if __name__ == "__main__":
    send_email()
