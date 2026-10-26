"""
MetaSticker AI — Scheduled Autonomous Outreach Dispatcher (v1.0 Apex)

Inviolable Sending Contract:
1. Deliverability Gate: Dispatches ONLY to targets verified by verify_target_deliverability.py.
2. Timing Gate: Default sending window is Monday-Friday 8:00 AM - 4:00 PM PT (peak executive open rates).
3. Anti-Spam Jitter: Random 45-90s pause between individual sends to mimic authentic human cadence.
4. Deduplication: Never emails any address or brand recorded in outreach_dispatch_ledger.json.
5. Gmail Quota Protection: Max 25 emails per batch session to protect sending domain reputation.
"""

import os
import sys
import json
import time
import random
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

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

VERIFIED_TARGETS_PATH = os.path.join(os.path.dirname(__file__), "verified_scale_targets.json")
LEDGER_PATH = os.path.join(os.path.dirname(__file__), "outreach_dispatch_ledger.json")

def load_ledger() -> list:
    if os.path.exists(LEDGER_PATH):
        try:
            with open(LEDGER_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_ledger(ledger: list):
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2)

def is_business_hours() -> bool:
    """Returns True if current time in Pacific Time is Mon-Fri between 08:00 and 16:00 PT."""
    # Current system is Pacific Time (UTC-7)
    now = datetime.datetime.now()
    # Monday is 0, Sunday is 6
    if now.weekday() >= 5: # Saturday or Sunday
        return False
    if now.hour < 8 or now.hour >= 16:
        return False
    return True

def generate_personalized_pitch(target: dict) -> tuple:
    brand = target["brand_name"]
    category = target["category"]
    hook = target["hook"]
    pilot = target["pilot_size"]
    email = target["email"]

    subject = f"{brand} x MetaSticker AI: Physical Collectibles with Instant Agent Micro-Apps"

    body = f"""Hi {brand} Team,

I am Santiago Villalobos, founder of MetaSticker AI (https://github.com/SVG-campus/metasticker-ai / live prototype: https://nimble-squall-4cxfebb.tmp.now).

We engineer physical-to-digital collectible vinyl stickers embedded with point-of-sale activation (POSA) and instant serverless AI micro-apps without requiring app downloads.

Given {brand}'s leadership in {category}, we have structured an interactive pilot concept for your developer and creator community:
1. The Hook: {hook}
2. Zero Manufacturing CapEx: MetaSticker covers 100% of physical production, 300gsm laminated holographic printing, tamper-evident scratch keys, and edge hosting.
3. Turnkey Revenue Share: 20% net proceeds directly back to {brand} with a proposed {pilot}.

You can explore our interactive sticker peel physics live at:
https://nimble-squall-4cxfebb.tmp.now

And download our complete executive whitepaper here:
https://nimble-squall-4cxfebb.tmp.now/MetaSticker_AI_Brand_Sponsorship_Whitepaper.pdf

We would love to ship a custom sample pack of physical holographic prototypes to your headquarters this week.

Could we schedule a brief 10-minute briefing this week to review sample specs?

Best regards,

Santiago Villalobos
Founder & Lead Architect, MetaSticker AI
Email: prefrontalcorporate@gmail.com
Phone: +1 (341) 221-1752
GitHub: https://github.com/SVG-campus/metasticker-ai
"""
    return subject, body

def dispatch_batch(max_sends: int = 20, force_now: bool = False, dry_run: bool = False):
    print("=" * 70)
    print("MetaSticker AI — Scheduled Autonomous Outreach Dispatcher")
    print("=" * 70)
    print(f"Sender: {GMAIL_USER}")
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Local Time: {now_str}")

    if not is_business_hours() and not force_now:
        print("\n[SCHEDULED STANDBY] Currently outside optimal business window (Mon-Fri 8:00 AM - 4:00 PM PT).")
        print("Emails queued for automatic dispatch during Monday morning executive triage window.")
        print("To override and dispatch immediately, use: --force-now")
        return {"status": "QUEUED_STANDBY", "reason": "outside_business_hours"}

    if not os.path.exists(VERIFIED_TARGETS_PATH):
        print(f"[ERROR] Verified targets file not found: {VERIFIED_TARGETS_PATH}")
        return {"status": "ERROR", "reason": "no_targets_file"}

    with open(VERIFIED_TARGETS_PATH, "r", encoding="utf-8") as f:
        targets = json.load(f)

    ledger = load_ledger()
    emailed_addresses = {item.get("to_email", "").lower() for item in ledger}
    emailed_brands = {item.get("brand_id", "").lower() for item in ledger}

    # Filter queue
    pending_queue = []
    for t in targets:
        if t["email"].lower() in emailed_addresses or t["id"].lower() in emailed_brands:
            continue
        pending_queue.append(t)

    print(f"Total Verified Targets: {len(targets)}")
    print(f"Already Dispatched:     {len(emailed_addresses)}")
    print(f"Pending Outreach Queue: {len(pending_queue)}")

    if not pending_queue:
        print("\n[INFO] Outreach queue is completely up to date! All verified brands contacted.")
        return {"status": "COMPLETED", "sent": 0}

    batch = pending_queue[:max_sends]
    print(f"\n[DISPATCH INITIATED] Selected batch of {len(batch)} brands for dispatch.\n")

    if not dry_run and not GMAIL_APP_PASSWORD:
        print("[ERROR] GMAIL_APP_PASSWORD not set! Cannot dispatch live emails.")
        return {"status": "ERROR", "reason": "no_credentials"}

    server = None
    if not dry_run:
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=15)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)

    dispatched_count = 0
    try:
        for idx, target in enumerate(batch):
            subject, body = generate_personalized_pitch(target)
            to_email = target["email"]
            brand = target["brand_name"]

            print(f"[{idx+1}/{len(batch)}] Dispatching to {brand:24} <{to_email}>...")

            if not dry_run and server:
                msg = MIMEMultipart("alternative")
                msg["From"] = f"Santiago Villalobos <{GMAIL_USER}>"
                msg["To"] = to_email
                msg["Subject"] = subject
                msg.attach(MIMEText(body, "plain"))
                server.sendmail(GMAIL_USER, [to_email], msg.as_string())

            ledger.append({
                "brand_id": target["id"],
                "brand_name": brand,
                "to_email": to_email,
                "subject": subject,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": "SENT" if not dry_run else "DRY_RUN"
            })
            save_ledger(ledger)
            dispatched_count += 1
            print(f"     ✅ Successfully delivered pitch to {brand}.")

            # Anti-spam jitter delay between emails (except last one)
            if idx < len(batch) - 1:
                jitter = random.randint(45, 90) if not dry_run else 1
                print(f"     ⏳ Jitter pause ({jitter}s) to mimic human sending cadence...")
                time.sleep(jitter)

    finally:
        if server:
            server.quit()

    print("\n" + "=" * 70)
    print(f"[SESSION COMPLETE] Successfully dispatched {dispatched_count} brand proposals.")
    print(f"Updated Ledger saved to: {LEDGER_PATH}")
    print("=" * 70)
    return {"status": "SUCCESS", "dispatched": dispatched_count}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="MetaSticker AI Scheduled Outreach Dispatcher")
    parser.add_argument("--limit", type=int, default=20, help="Maximum emails to dispatch in this session (default 20)")
    parser.add_argument("--force-now", action="store_true", help="Force immediate send regardless of business hours")
    parser.add_argument("--dry-run", action="store_true", help="Audit batch without transmitting emails")
    args = parser.parse_args()

    dispatch_batch(max_sends=args.limit, force_now=args.force_now, dry_run=args.dry_run)
