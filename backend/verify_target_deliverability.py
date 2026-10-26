"""
MetaSticker AI — Brand Deliverability & MX Verification Engine (v1.0 Apex)

Verifies every target domain in the scale roster via DNS-over-HTTPS (Google 8.8.8.8 API),
checks against known failure codes in bounced_emails.json, and exports verified_scale_targets.json.
"""

import os
import sys
import json
import urllib.request
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

INPUT_ROSTER = os.path.join(os.path.dirname(__file__), "scale_brand_targets.json")
OUTPUT_VERIFIED = os.path.join(os.path.dirname(__file__), "verified_scale_targets.json")
BOUNCES_PATH = os.path.join(os.path.dirname(__file__), "bounced_emails.json")

def load_bounced_recipients() -> set:
    if os.path.exists(BOUNCES_PATH):
        try:
            with open(BOUNCES_PATH, "r", encoding="utf-8") as f:
                bounces = json.load(f)
                return {b.get("recipient", "").lower() for b in bounces if b.get("recipient")}
        except Exception:
            return set()
    return set()

def query_mx(domain: str) -> list:
    url = f"https://dns.google/resolve?name={domain}&type=MX"
    req = urllib.request.Request(url, headers={"User-Agent": "MetaSticker-Verifier/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            answers = data.get("Answer", [])
            return [a.get("data") for a in answers if a.get("type") == 15]
    except Exception as e:
        return []

def run_verification():
    print("=" * 70)
    print("MetaSticker AI — Pre-Flight MX & Deliverability Audit")
    print("=" * 70)

    if not os.path.exists(INPUT_ROSTER):
        print(f"[ERROR] Roster file not found: {INPUT_ROSTER}")
        return

    with open(INPUT_ROSTER, "r", encoding="utf-8") as f:
        targets = json.load(f)

    bounced_set = load_bounced_recipients()
    print(f"Loaded {len(targets)} targets. Blacklisted bounced recipients: {len(bounced_set)}\n")

    verified_targets = []
    failed_targets = []

    for t in targets:
        domain = t.get("domain", "")
        email = t.get("email", "").lower()
        brand = t.get("brand_name", "")

        # 1. Check blacklist
        if email in bounced_set:
            print(f"[REJECTED - BLACKLIST] {brand:24} | {email} (Known failure)")
            failed_targets.append({**t, "reason": "Known bounce in bounced_emails.json"})
            continue

        # 2. Check MX
        mx_records = query_mx(domain)
        if not mx_records:
            print(f"[REJECTED - NO MX]    {brand:24} | {domain} (No active MX records)")
            failed_targets.append({**t, "reason": "No MX records found"})
            continue

        primary_mx = mx_records[0]
        t["primary_mx"] = primary_mx
        t["mx_count"] = len(mx_records)
        t["verified"] = True
        verified_targets.append(t)
        print(f"[VERIFIED DELIVERABLE] {brand:24} | {email:30} | MX: {primary_mx[:32]}")
        time.sleep(0.05)

    print("\n" + "=" * 70)
    print(f"Total Targets Evaluated: {len(targets)}")
    print(f"Deliverable Verified:    {len(verified_targets)} ({len(verified_targets)/len(targets)*100:.1f}%)")
    print(f"Rejected / Suppressed:   {len(failed_targets)}")

    with open(OUTPUT_VERIFIED, "w", encoding="utf-8") as f:
        json.dump(verified_targets, f, indent=2)

    print(f"[EXPORT] Saved verified targets to: {OUTPUT_VERIFIED}")
    print("=" * 70)

if __name__ == "__main__":
    run_verification()
