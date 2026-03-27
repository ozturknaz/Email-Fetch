# Gmail Reader Module

This module is designed to connect to Gmail's IMAP server and fetch the latest emails securely.

## Features
- Secure connection via SSL.
- Fetches and displays the last 5 emails from the inbox.
- Decodes email headers (Subject, Sender) automatically.

## Requirements
- Python 3.x
- IMAP access enabled in Gmail settings.
- An **App Password** generated from your Google Account.

## Usage
1. Configure your credentials in mail_check.py.
2. Run the script:
   python mail_check.py
