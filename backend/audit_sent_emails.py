import os
import sys
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env")))
user = os.getenv("GMAIL_USER")
pwd = os.getenv("GMAIL_APP_PASSWORD")

try:
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user, pwd)

    # List mailboxes to get exact Sent Mail name
    typ, data = mail.list()
    sent_box = None
    for line in data:
        decoded = line.decode("utf-8", errors="ignore")
        if "Sent" in decoded or "Enviados" in decoded:
            # Match the mailbox name inside quotes or at the end
            parts = decoded.split(' "/" ')
            if len(parts) > 1:
                sent_box = parts[1].strip('"')
            break

    if not sent_box:
        sent_box = "[Gmail]/Sent Mail"

    print(f"Selecting Sent Mailbox: '{sent_box}'")
    status, count = mail.select(f'"{sent_box}"')
    if status != "OK":
        status, count = mail.select(sent_box)

    status, msgs = mail.search(None, "ALL")
    ids = msgs[0].split()
    print(f"Total Sent Emails Found: {len(ids)}\n")

    def decode_str(val):
        if not val:
            return ""
        parts = decode_header(val)
        res = ""
        for p, enc in parts:
            if isinstance(p, bytes):
                res += p.decode(enc or "utf-8", errors="ignore")
            else:
                res += str(p)
        return res

    recent_ids = ids[-15:]
    for i in reversed(recent_ids):
        s, data = mail.fetch(i, "(RFC822.HEADER)")
        msg = email.message_from_bytes(data[0][1])
        to_addr = decode_str(msg.get("To"))
        subject = decode_str(msg.get("Subject"))
        date = msg.get("Date")
        print(f"• Date: {date}\n  To:   {to_addr}\n  Subj: {subject}\n")

    mail.close()
    mail.logout()

except Exception as e:
    print(f"Error checking sent mail: {e}")
