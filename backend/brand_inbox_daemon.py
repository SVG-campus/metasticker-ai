"""
MetaSticker AI — Autonomous Brand Inbox & Positive Reply Forwarder Daemon (v1.0 Apex)
Polls prefrontalcorporate@gmail.com via IMAP, classifies replies using Monad NLP Intent Sieve,
and automatically forwards positive sponsor leads to daboldflex@gmail.com via TLS SMTP.
"""

import os
import sys
import time
import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header
import json
import re
from monad_brand_conversational_engine import process_inbound_message

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def load_env():
    env_paths = [
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env")),
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".env")),
        os.path.abspath(".env")
    ]
    for p in env_paths:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
            break

load_env()

GMAIL_USER = os.getenv("GMAIL_USER", "prefrontalcorporate@gmail.com")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "")
VIP_ALERT_RECIPIENT = os.getenv("VIP_ALERT_RECIPIENT", "daboldflex@gmail.com")
PROCESSED_IDS_PATH = os.path.join(os.path.dirname(__file__), "processed_email_ids.json")

def load_processed_ids() -> set:
    if os.path.exists(PROCESSED_IDS_PATH):
        try:
            with open(PROCESSED_IDS_PATH, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()

def save_processed_ids(ids: set):
    with open(PROCESSED_IDS_PATH, "w", encoding="utf-8") as f:
        json.dump(list(ids)[-5000:], f)

AUTOMATED_SENDERS = [
    "noreply", "no-reply", "donotreply", "notifications@", "googlealerts",
    "nextdoor.com", "boostmobile", "tmobile", "mailchimp", "substack",
    "facebookmail", "linkedin.com", "quora.com", "tradethepool"
]

HIGH_INTENT_KEYWORDS = [
    r"\bpartnership(s)?\b", r"\bsponsor(ship)?(s)?\b", r"\brate card\b",
    r"\bpilot\b", r"\blicensing\b", r"\bbrand deal\b", r"\bmedia kit\b",
    r"\bmeta hackathon\b", r"\bcustom stickers?\b", r"\bco-brand(ed)?\b",
    r"\bpricing quote\b", r"\bzoom call\b", r"\bschedule a (call|chat|demo)\b",
    r"\binterested in (partnering|sponsoring|working)\b", r"\bsend (over )?the deck\b",
    r"\bwhitepaper\b", r"\brev(-)?share\b", r"\bad space\b"
]

def decode_mime_header(header_val):
    if not header_val:
        return ""
    decoded_parts = decode_header(header_val)
    res = ""
    for part, enc in decoded_parts:
        if isinstance(part, bytes):
            res += part.decode(enc or "utf-8", errors="ignore")
        else:
            res += str(part)
    return res

def analyze_intent(from_addr: str, subject: str, text: str) -> dict:
    """Monad Intent Sieve: scores intent and filters automated newsletters."""
    from_lower = from_addr.lower()
    for bad in AUTOMATED_SENDERS:
        if bad in from_lower:
            return {"is_positive": False, "score": 0, "matched_signals": [], "reason": f"automated_sender_{bad}"}

    combined = f"{subject}\n{text}".lower()
    matches = [kw for kw in HIGH_INTENT_KEYWORDS if re.search(kw, combined)]
    score = len(matches)
    is_positive = score >= 1
    return {
        "is_positive": is_positive,
        "score": score,
        "matched_signals": matches
    }

def forward_positive_lead(from_addr: str, original_subject: str, body: str, signals: list):
    """Dispatches instant VIP alert to daboldflex@gmail.com."""
    alert_subject = f"🚨 [METASTICKER LEAD] Positive Reply from {from_addr}: {original_subject}"
    
    html_content = f"""
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 650px; color: #0f172a; line-height: 1.6;">
      <div style="background: linear-gradient(135deg, #0081fb, #8b5cf6); padding: 18px 24px; border-radius: 8px 8px 0 0; color: #ffffff;">
        <h2 style="margin: 0; font-size: 1.3rem;">⚡ MetaSticker AI — High-Intent Brand Sponsor Alert</h2>
        <p style="margin: 4px 0 0; opacity: 0.9; font-size: 0.85rem;">Autonomous Monad Lead Detection System</p>
      </div>

      <div style="border: 1px solid #e2e8f0; border-top: none; padding: 24px; border-radius: 0 0 8px 8px; background: #ffffff;">
        <p style="font-size: 1rem;">A potential brand partner or sponsor has replied with <strong>positive engagement</strong>!</p>

        <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
          <tr>
            <td style="padding: 8px; background: #f8fafc; font-weight: bold; width: 140px; border-bottom: 1px solid #e2e8f0;">From:</td>
            <td style="padding: 8px; border-bottom: 1px solid #e2e8f0;"><code>{from_addr}</code></td>
          </tr>
          <tr>
            <td style="padding: 8px; background: #f8fafc; font-weight: bold; border-bottom: 1px solid #e2e8f0;">Subject:</td>
            <td style="padding: 8px; border-bottom: 1px solid #e2e8f0;">{original_subject}</td>
          </tr>
          <tr>
            <td style="padding: 8px; background: #f8fafc; font-weight: bold; border-bottom: 1px solid #e2e8f0;">Intent Signals:</td>
            <td style="padding: 8px; border-bottom: 1px solid #e2e8f0; color: #16a34a; font-weight: bold;">{', '.join(signals)}</td>
          </tr>
        </table>

        <h3 style="font-size: 1rem; color: #334155; margin-top: 20px;">Email Body:</h3>
        <div style="background: #f1f5f9; padding: 15px; border-radius: 6px; font-family: monospace; font-size: 0.85rem; white-space: pre-wrap; color: #1e293b; max-height: 350px; overflow-y: auto;">
{body}
        </div>

        <div style="margin-top: 25px; padding-top: 15px; border-top: 1px solid #e2e8f0; font-size: 0.85rem; color: #64748b;">
          <strong>Quick Action:</strong> Reply directly to <code>{from_addr}</code> from prefrontalcorporate@gmail.com, or attach the <a href="https://nimble-squall-4cxfebb.tmp.now/MetaSticker_AI_Brand_Sponsorship_Whitepaper.pdf">Executive Whitepaper PDF</a> to confirm the pilot.
        </div>
      </div>
    </div>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = alert_subject
    msg["From"] = f"MetaSticker AI Lead Bot <{GMAIL_USER}>"
    msg["To"] = VIP_ALERT_RECIPIENT
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_USER, VIP_ALERT_RECIPIENT, msg.as_string())
        print(f"[ALERT SENT] Successfully forwarded positive lead from {from_addr} to {VIP_ALERT_RECIPIENT}!")
        return True
    except Exception as e:
        print(f"[ALERT ERROR] Failed to forward lead to {VIP_ALERT_RECIPIENT}: {e}")
        return False

def check_inbox_and_process(max_recent=25, dry_run=False):
    """Scans recent emails for brand responses and forwards positive ones."""
    if not GMAIL_APP_PASSWORD:
        print("[ERROR] GMAIL_APP_PASSWORD not set in scratch/.env!")
        return {"status": "NO_AUTH"}

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        mail.select("inbox")

        # Search for recent emails
        status, messages = mail.search(None, "ALL")
        if status != "OK" or not messages[0]:
            print("[INFO] No messages found in inbox.")
            mail.close()
            mail.logout()
            return {"status": "EMPTY"}

        email_ids = messages[0].split()
        target_ids = email_ids[-max_recent:]
        print(f"[INBOX] Polling {len(target_ids)} most recent emails (out of {len(email_ids)} total)...")

        processed_ids = load_processed_ids()
        processed_leads = []
        for e_id in reversed(target_ids):
            e_id_str = e_id.decode()
            if e_id_str in processed_ids:
                continue
            processed_ids.add(e_id_str)

            status, data = mail.fetch(e_id, "(RFC822)")
            if status != "OK" or not data or not data[0]:
                continue
            
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            from_hdr = decode_mime_header(msg.get("From", ""))
            subject_hdr = decode_mime_header(msg.get("Subject", ""))
            date_hdr = msg.get("Date", "")

            # Extract text body
            body_text = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition", ""))
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        payload = part.get_payload(decode=True)
                        if payload:
                            body_text = payload.decode("utf-8", errors="ignore")
                            break
            else:
                payload = msg.get_payload(decode=True)
                if payload:
                    body_text = payload.decode("utf-8", errors="ignore")

            # Ignore emails sent by ourselves or alerts to avoid echo loops
            if GMAIL_USER.lower() in from_hdr.lower() or "metasticker ai lead bot" in from_hdr.lower():
                continue

            # Process message through Monad Conversational & Handover Engine
            proc_res = process_inbound_message(from_hdr, subject_hdr, body_text, dry_run=dry_run)
            if proc_res.get("status") in ["HANDOVER_TRIGGERED", "AUTONOMOUS_REPLY_SENT"]:
                processed_leads.append({
                    "from": from_hdr,
                    "subject": subject_hdr,
                    "date": date_hdr,
                    "engine_status": proc_res.get("status")
                })

        save_processed_ids(processed_ids)
        mail.close()
        mail.logout()
        print(f"[CYCLE COMPLETE] Checked {len(target_ids)} messages. Forwarded {len(processed_leads)} positive leads.")
        return {"status": "SUCCESS", "leads_found": len(processed_leads)}

    except Exception as e:
        print(f"[IMAP ERROR] Failed during inbox check: {e}")
        return {"status": "ERROR", "error": str(e)}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="MetaSticker AI Autonomous Brand Inbox Daemon")
    parser.add_argument("--daemon", action="store_true", help="Run continuously in background polling every N seconds")
    parser.add_argument("--interval", type=int, default=300, help="Polling interval in seconds (default 300s = 5m)")
    parser.add_argument("--dry-run", action="store_true", help="Audit inbox without sending alert emails")
    args = parser.parse_args()

    print("=== METASTICKER AI AUTONOMOUS BRAND INBOX DAEMON ===")
    print(f"Monitoring:  {GMAIL_USER}")
    print(f"VIP Forward: {VIP_ALERT_RECIPIENT}")

    if args.daemon:
        print(f"[DAEMON STARTED] Polling every {args.interval}s. Press Ctrl+C to terminate.")
        while True:
            check_inbox_and_process(dry_run=args.dry_run)
            time.sleep(args.interval)
    else:
        check_inbox_and_process(dry_run=args.dry_run)
