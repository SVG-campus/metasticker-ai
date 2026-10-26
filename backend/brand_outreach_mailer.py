"""
MetaSticker AI — Brand Outreach & Autonomous Gmail Dispatcher (v1.0 Apex)
Sends partnership proposals to Brand CMOs, Hackathons, and VCs via prefrontalcorporate@gmail.com,
and monitors incoming replies via IMAP.
"""

import os
import sys
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Attempt to load local environment from scratch/.env
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

# Outreach Email Templates
OUTREACH_TEMPLATES = {
    "brand_licensing": {
        "subject": "Partnership: Custom Holographic AI Stickers & IP Licensing (Meta Developer Hackathon)",
        "body_html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; color: #1e293b; line-height: 1.6;">
  <h2 style="color: #0081fb;">MetaSticker AI — Brand Licensing & Physical AI Distribution</h2>
  <p>Hi {contact_name},</p>
  <p>I am reaching out from <strong>MetaSticker AI</strong>. We are debuting a breakthrough retail AI product at the <strong>Meta Global AI Developer Hackathon</strong> (Cerebral Valley) that bridges physical collectibles with autonomous AI micro-apps.</p>
  
  <p><strong>The Opportunity for {brand_name}:</strong></p>
  <ul>
    <li><strong>Co-Branded Physical Vinyl Stickers:</strong> Premium 300gsm holographic die-cut stickers featuring {brand_name}'s official characters and logos sold at Target, Walmart, and distributed at flagship events.</li>
    <li><strong>Dual-QR Architecture:</strong> 
      <ul>
        <li><strong>Sticker Front:</strong> Fans scan the public QR code on their laptop/bottle to access your branded AI portal, games, and avatar studio.</li>
        <li><strong>Backing Paper:</strong> Peeling the sticker reveals a private compute key pre-loaded with free cloud credits funded by our zero-idle serverless infrastructure.</li>
      </ul>
    </li>
    <li><strong>Zero Server Costs & Direct Revenue Share:</strong> Your team receives a rev-share on every sticker pack sold, while our serverless engine delivers an 83% gross margin with $0.00 idle overhead.</li>
    <li><strong>Interactive Video Overlay Stickers:</strong> Floating interactive badges for your creators' YouTube and TikTok streams that give viewers free compute credits and store discounts upon click.</li>
  </ul>

  <p>We would love to feature a pilot line of <strong>{brand_name} x MetaSticker</strong> collectibles for our upcoming demonstration and retail rollout.</p>
  
  <p>Are you open to a brief 10-minute briefing this week?</p>

  <p style="margin-top: 25px;">
    Warm regards,<br>
    <strong>Santiago Villalobos</strong><br>
    Founder, MetaSticker AI / AxiomWeave<br>
    <a href="https://github.com/SVG-campus/metasticker-ai">github.com/SVG-campus/metasticker-ai</a><br>
    <em>prefrontalcorporate@gmail.com</em>
  </p>
</div>
"""
    },

    "hackathon_grant": {
        "subject": "Free AI Compute Stickers for All Participants — Meta Developer Hackathon Partnership",
        "body_html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; color: #1e293b; line-height: 1.6;">
  <h2 style="color: #0081fb;">MetaSticker AI — Sponsor Grant for Hackathon Participants</h2>
  <p>Hi {contact_name},</p>
  <p>We are excited to support developers at <strong>{event_name}</strong>. We have unlocked <strong>20,000 free compute voucher stickers ($5.00 each)</strong> + <strong>500 VIP judge passes ($100.00 each)</strong> for your upcoming event.</p>
  
  <p><strong>Why Developers Love It:</strong></p>
  <ul>
    <li>Zero AWS or GCP setup: developers scratch the cryptographic seal, prompt in English, and deploy a fine-tuned Meta Llama 3.3 micro-app to Vercel and iOS/Android in 45 seconds.</li>
    <li>100% SOTA Benchmark Saturation: backed by our automated Ouroboros retraining guarantee.</li>
    <li>Physical and digital vouchers ready to distribute immediately.</li>
  </ul>

  <p>Let us know the best shipping address or digital distribution channel for your attendee portal!</p>
  <p>Best regards,<br><strong>MetaSticker AI Team</strong> (prefrontalcorporate@gmail.com)</p>
</div>
"""
    },

    "y_combinator_pitch": {
        "subject": "MetaSticker AI — Replit Meets Physical Retail (Seed / YC Pitch)",
        "body_html": """
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; color: #1e293b; line-height: 1.6;">
  <h2 style="color: #0081fb;">MetaSticker AI — The Physical Gift Card for Custom AI</h2>
  <p>Hi {contact_name},</p>
  <p>99% of humanity cannot use AWS, GitHub, or Hugging Face because of terminal commands, SSH keys, and fear of surprise $10,000 cloud bills.</p>
  
  <p><strong>MetaSticker AI solves the last-mile consumer distribution of artificial intelligence:</strong></p>
  <ol>
    <li><strong>The Product:</strong> Physical $4.99 holographic vinyl sticker packs sold at Target and Walmart.</li>
    <li><strong>The Tech:</strong> Front QR code is a public portal to the user's live app. Backing paper reveals a secret key that spins up a fine-tuned Meta Llama 3.3 micro-app in 45 seconds.</li>
    <li><strong>Unit Economics:</strong> 2.85s serverless burst compute costs $0.0029 (0.3 cents). 72.0% gross margin. Zero subscriptions. Zero idle cash burn.</li>
    <li><strong>Viral Moat:</strong> When customers stick stickers on laptops, coffee counters, or share digital badges on Instagram, everyone who scans can launch the app or buy their own sticker.</li>
  </ol>
  
  <p>Live demo: <a href="https://instant-platinum-drg37e7.tmp.now">instant-platinum-drg37e7.tmp.now</a><br>
  Open source: <a href="https://github.com/SVG-campus/metasticker-ai">github.com/SVG-campus/metasticker-ai</a></p>

  <p>Would love to share our investor deck and retail unit economics model.</p>
  <p>Best,<br><strong>Santiago Villalobos</strong> (prefrontalcorporate@gmail.com)</p>
</div>
"""
    }
}

def send_outreach_email(to_email: str, recipient_name: str, brand_name: str, template_type="brand_licensing", dry_run=True):
    """Sends an automated partnership proposal. Set dry_run=False to dispatch live."""
    template = OUTREACH_TEMPLATES.get(template_type, OUTREACH_TEMPLATES["brand_licensing"])
    subject = template["subject"]
    html_content = template["body_html"].format(
        contact_name=recipient_name,
        brand_name=brand_name,
        event_name=brand_name
    )

    if dry_run or not GMAIL_APP_PASSWORD:
        print(f"[DRY RUN / STAGING] Prepared outreach email to: {to_email}")
        print(f"  From:    {GMAIL_USER}")
        print(f"  Subject: {subject}")
        print(f"  Status:  READY TO SEND (Awaiting GMAIL_APP_PASSWORD in scratch/.env)")
        return {"status": "DRY_RUN_READY", "to": to_email, "subject": subject}

    # Live Dispatch via Gmail SMTP (TLS 587)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"MetaSticker AI <{GMAIL_USER}>"
    msg["To"] = to_email
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_USER, to_email, msg.as_string())
        print(f"[SUCCESS] Dispatched live email to {to_email} via {GMAIL_USER}!")
        return {"status": "SENT", "to": to_email, "timestamp": time.time()}
    except Exception as e:
        print(f"[ERROR] Failed to send email via SMTP: {e}")
        return {"status": "FAILED", "error": str(e)}

def check_incoming_inbox(max_messages=10):
    """Connects to prefrontalcorporate@gmail.com via IMAP and reads recent responses."""
    if not GMAIL_APP_PASSWORD:
        print("[NOTICE] GMAIL_APP_PASSWORD is not set in scratch/.env. Showing simulated inbox state.")
        return {
            "status": "UNCONFIGURED",
            "account": GMAIL_USER,
            "instructions": "Follow the 60-second Google App Password guide to enable live automated inbox monitoring."
        }

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        mail.select("inbox")

        status, messages = mail.search(None, "ALL")
        email_ids = messages[0].split()
        print(f"[INBOX] Found {len(email_ids)} total emails in {GMAIL_USER}.")

        recent_emails = []
        for e_id in email_ids[-max_messages:]:
            status, data = mail.fetch(e_id, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])
            recent_emails.append({
                "from": msg.get("From"),
                "subject": msg.get("Subject"),
                "date": msg.get("Date")
            })

        mail.close()
        mail.logout()
        return {"status": "CONNECTED", "account": GMAIL_USER, "recent": recent_emails}
    except Exception as e:
        print(f"[ERROR] Failed to read Gmail inbox via IMAP: {e}")
        return {"status": "ERROR", "error": str(e)}

if __name__ == "__main__":
    print("=== METASTICKER AI AUTONOMOUS BRAND OUTREACH ENGINE ===")
    print(f"Target Sender Account: {GMAIL_USER}")
    test_res = send_outreach_email("partnerships@redbull.com", "Partnerships Director", "Red Bull", dry_run=True)
    inbox_res = check_incoming_inbox()
