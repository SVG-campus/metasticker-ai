import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
load_dotenv(env_path)

user = os.getenv("GMAIL_USER")
pwd = os.getenv("GMAIL_APP_PASSWORD")

targets = [
    {
        "email": "creator.program@razer.com",
        "name": "Razer Creator & Streamer Program",
        "subject": "Partnership: Razer Chroma Holographic Decals & Interactive Creator Video Stickers",
        "body": """Hi Razer Creator Program Team,

I am Santiago Villalobos, founder of MetaSticker AI (https://github.com/SVG-campus/metasticker-ai / live prototype: https://nimble-squall-4cxfebb.tmp.now).

We engineer next-generation physical collectible vinyl stickers embedded with point-of-sale activation (POSA) and instant AI agent micro-apps.

We would love to collaborate with the Razer Creator Program on a dedicated line of Razer Chroma holographic physical collectibles for streamers and gamers:
1. Chroma-Sync Hologram Decals: Physical die-cut badges that link directly to creator overlays, automated OBS highlights, and Razer Synapse profiles.
2. Zero Manufacturing CapEx for Razer: MetaSticker handles full on-demand physical production, tamper-evident scratch-off activation, and edge hosting.
3. Creator Rev-Share: 20% net proceeds directly back to participating creators and the Razer ecosystem.

We would be thrilled to ship a custom sample batch of physical holographic proof-of-concept decals to your Singapore or Irvine design headquarters this week.

Are you open to a brief 10-minute introductory call this Tuesday or Thursday?

Warm regards,

Santiago Villalobos
Founder & Lead Architect, MetaSticker AI
Email: prefrontalcorporate@gmail.com
Direct: +1 (341) 221-1752
Repo: https://github.com/SVG-campus/metasticker-ai
"""
    },
    {
        "email": "press@duolingo.com",
        "name": "Duolingo Media & Partnerships",
        "subject": "Duolingo x MetaSticker AI: Physical Duo the Owl Stickers with Instant AI Language Coaches",
        "body": """Hi Duolingo Media & Brand Team,

I am Santiago Villalobos, founder of MetaSticker AI (https://github.com/SVG-campus/metasticker-ai / live prototype: https://nimble-squall-4cxfebb.tmp.now).

We have developed a physical-to-digital merchandising bridge that transforms collectible vinyl stickers into instant AI software experiences without requiring app downloads.

Given Duolingo's iconic mascot culture, we have prepared an interactive prototype for official physical Duo the Owl holographic stickers:
1. Physical Retail & Event Collectibles: Premium die-cut holographic vinyl stickers designed for university campuses, book fairs, and retail point-of-sale.
2. The Frictionless AI Hook: Peeling or scanning the sticker instantly launches a lightweight, browser-based Duo language mini-coach (powered by Llama 3.3 and ElevenLabs audio) directly on mobile web in under 3 seconds.
3. Zero Manufacturing Overhead: MetaSticker covers 100% of physical production, packaging, and edge infrastructure with a 20% brand licensing rev-share.

We would love to mail a free sample pack of proof-of-concept Duo stickers directly to your Pittsburgh office.

Could we schedule a quick 10-minute chat this week to explore collaboration?

Best regards,

Santiago Villalobos
Founder, MetaSticker AI
Email: prefrontalcorporate@gmail.com
Phone: +1 (341) 221-1752
GitHub: https://github.com/SVG-campus/metasticker-ai
"""
    }
]

print(f"Connecting to SMTP for {user}...")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user, pwd)

for t in targets:
    msg = MIMEMultipart("alternative")
    msg["From"] = f"Santiago Villalobos <{user}>"
    msg["To"] = t["email"]
    msg["Subject"] = t["subject"]
    msg.attach(MIMEText(t["body"], "plain"))
    server.sendmail(user, [t["email"]], msg.as_string())
    print(f"Successfully sent to {t['name']} <{t['email']}>")

server.quit()
print("All verified channel dispatches completed.")
