# 60-Second Setup: Connecting `prefrontalcorporate@gmail.com` for Automated Outreach

> **Why this method?** Google App Passwords allow Python scripts to send and read emails securely over TLS (`smtp.gmail.com:587` and `imap.gmail.com:993`) without requiring OAuth consent screens or exposing your master account password.

---

### Step 1: Open Google Security Settings
1. Open your browser and log into [**`prefrontalcorporate@gmail.com`**](https://mail.google.com).
2. Go to: [**https://myaccount.google.com/security**](https://myaccount.google.com/security).
3. Under **"How you sign in to Google"**, verify that **2-Step Verification** is turned **ON** (if not, follow Google's 1-minute prompt with your phone).

---

### Step 2: Generate a 16-Character App Password
1. In the search bar at the top of Google Account, type: **App passwords**  
   *(or navigate directly to: [**https://myaccount.google.com/apppasswords**](https://myaccount.google.com/apppasswords))*.
2. For **App Name**, enter: `MetaSticker Outreach`.
3. Click **Create**.
4. Google will display a yellow modal with a **16-character password** (example: `abcd efgh ijkl mnop`).

---

### Step 3: Add to Local `scratch/.env`
Open or create `C:\Users\svillalobosgonzalez1\.gemini\antigravity-ide\scratch\.env` and add:

```env
# MetaSticker AI Automated Gmail Dispatcher
GMAIL_USER=prefrontalcorporate@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop
```
*(Spaces in the 16 characters can be kept or removed; both work).*

---

### Step 4: Dispatch Brand Emails & Monitor Replies!
Run the outreach engine in PowerShell:

```powershell
# 1. Test inbox connection
python backend/brand_outreach_mailer.py

# 2. Dispatch a live outreach proposal to a brand licensing director
python -c "import backend.brand_outreach_mailer as m; m.send_outreach_email('partnerships@redbull.com', 'Alex Rivers', 'Red Bull', template_type='brand_licensing', dry_run=False)"
```

Once connected, the agent can autonomously monitor replies from brand CMOs, track interest, and alert you whenever a brand responds!
