import os
import sys
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
load_dotenv(env_path)

user = os.getenv("GMAIL_USER")
pwd = os.getenv("GMAIL_APP_PASSWORD")

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(user, pwd)

def decode_mime(val):
    if not val:
        return ""
    parts = decode_header(val)
    out = []
    for text, enc in parts:
        if isinstance(text, bytes):
            out.append(text.decode(enc or "utf-8", errors="replace"))
        else:
            out.append(str(text))
    return "".join(out)

# Check Sent Mail
mail.select('"[Gmail]/Sent Mail"')
status, msgs = mail.search(None, "ALL")
ids = msgs[0].split()
print(f"Total Sent Mail messages: {len(ids)}")

print("\n--- Recent Sent Messages ---")
for i in ids[-15:]:
    s, data = mail.fetch(i, "(RFC822.HEADER)")
    msg = email.message_from_bytes(data[0][1])
    subj = decode_mime(msg.get("Subject", ""))
    to_ = decode_mime(msg.get("To", ""))
    date = msg.get("Date", "")
    print(f"Sent ID {i.decode()} | To: {to_} | Subj: {subj[:50]} | Date: {date}")

# Check INBOX for failure / delivery status
mail.select("INBOX")
status, msgs = mail.search(None, "ALL")
ids = msgs[0].split()
print(f"\nTotal INBOX messages: {len(ids)}")
print("\n--- Inbound Delivery / Bounce Reports in INBOX ---")
for i in ids[-15:]:
    s, data = mail.fetch(i, "(RFC822)")
    msg = email.message_from_bytes(data[0][1])
    subj = decode_mime(msg.get("Subject", ""))
    sender = decode_mime(msg.get("From", ""))
    to_ = decode_mime(msg.get("To", ""))
    date = msg.get("Date", "")
    body = ""
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True).decode("utf-8", errors="replace")
            break
    if not body and not msg.is_multipart():
        body = msg.get_payload(decode=True).decode("utf-8", errors="replace")

    print(f"\n[INBOX ID {i.decode()}] From: {sender} | To: {to_} | Subj: {subj}")
    print(f"Date: {date}")
    # print relevant snippet
    first_lines = "\n".join([line for line in body.splitlines() if line.strip()][:6])
    print(f"Snippet:\n{first_lines}")
