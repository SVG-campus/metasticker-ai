import os
import sys
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
load_dotenv(load_env_path)

user = os.getenv("GMAIL_USER")
pwd = os.getenv("GMAIL_APP_PASSWORD")
print("Connecting to IMAP for", user)
try:
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(user, pwd)
    mail.select("inbox")
    status, msgs = mail.search(None, "ALL")
    ids = msgs[0].split()
    print("Total messages in inbox:", len(ids))
    recent_ids = ids[-10:]
    for i in reversed(recent_ids):
        s, data = mail.fetch(i, "(RFC822.HEADER)")
        msg = email.message_from_bytes(data[0][1])
        def dec(h):
            if not h: return ""
            d = decode_header(h)
            res = ""
            for p, e in d:
                if isinstance(p, bytes):
                    res += p.decode(e or "utf-8", errors="ignore")
                else:
                    res += str(p)
            return res
        print(f"[{i.decode()}] From: {dec(msg.get('From'))[:45]} | Subj: {dec(msg.get('Subject'))[:50]}")
    mail.close()
    mail.logout()
except Exception as e:
    print("Error:", e)
