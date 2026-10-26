# MetaSticker AI — Payments, Authentication & Student Pass Setup Guide
## Production Integration Specification for Stripe, Auth0/Clerk, and Private Coin

> **System Tag:** `AW-METASTICKER-PAYMENTS-AUTH-SPEC-V1`  
> **Status:** Turnkey Ready — Configurable via Environment Variables

---

## 1. Authentication Architecture: Zero-Friction Web3 + Web2 OAuth

MetaSticker AI uses a **hybrid identity model**:
1. **Frictionless Anonymous Onboarding (Default):**
   - Users who buy a physical sticker at Target/Walmart scratch off the foil and enter their burner code (`MUSE-TARGET-XXXX-XXXX`).
   - They do **not need to create an account or provide an email**. The cryptographic private key acts as their session token and bearer asset.
2. **Account Persistence (Optional Upgrade for Students, Founders, and Teams):**
   - Providers Supported: **Auth0**, **Clerk**, or **Supabase Auth**.
   - One-Click Social Login:
     - Log in with Meta (Facebook / Instagram developer accounts)
     - Log in with Google
     - Log in with GitHub

### Environment Configuration (`.env.local`)
```env
# Clerk / Auth0 Configuration (Configure with your dashboard credentials)
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key_here
CLERK_SECRET_KEY=your_clerk_secret_key_here

# Or Auth0:
AUTH0_SECRET=your_auth0_secret_here
AUTH0_BASE_URL=https://metasticker.vercel.app
AUTH0_ISSUER_BASE_URL=https://metasticker.us.auth0.com
AUTH0_CLIENT_ID=your_auth0_client_id_here
AUTH0_CLIENT_SECRET=your_auth0_client_secret_here
```

---

## 2. Payment Gateway: Stripe Checkout & POSA Retail Integration

### Retail Packs & Online Refills
- **Retail Packs:** Sold at physical checkout (Target / Walmart) via POSA (Point of Sale Activation) barcodes. Zero transaction fee to MetaSticker on purchase; cash registers settle through Blackhawk Network / InComm.
- **In-App Top-Ups & Digital Packs:**
  - $4.99: 1 Digital Sticker Pack ($5.00 Compute + 1 Micro-App)
  - $19.99: Creator 5-Pack ($25.00 Compute + Custom Subdomain)
  - $49.99: Business 15-Pack ($75.00 Compute + Custom Domain Mapping + iOS/Android App Store Export)

### Stripe Integration (`backend/stripe_checkout.py`)
```python
import stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_sticker_checkout_session(tier: str, return_url: str):
    prices = {
        "creator": 499,     # $4.99
        "pro": 1999,        # $19.99
        "business": 4999    # $49.99
    }
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': f'MetaSticker AI Pack ({tier.upper()})'},
                'unit_amount': prices.get(tier, 499),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=return_url + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=return_url,
    )
    return session.url
```

---

## 3. Student & Edu Grant Access Program

- **Target Audience:** High school, college, and university students building their first startup or class project.
- **Grant Terms:** Every verified `.edu` email receives **1 Free Student Pack per Semester** ($10.00 compute grant + 3 printable digital stickers).
- **Verification Pipeline:**
  1. User inputs student email (`@university.edu`).
  2. Automated magic-link verification verifies institutional MX records.
  3. Optional Student ID card OCR via **Meta SAM 3.1** for instant zero-wait approval.

---

## 4. Digital Sticker Mining & Private Coin Protocol (ERC-8088 PAP)

- **The Token:** Every generated micro-agent is minted as an **ERC-8088 Physical Agent Protocol (PAP)** token.
- **Metadata Encoded On-Chain:**
  - `app_slug`: e.g. `artisan-bakery`
  - `model_weights_hash`: SHA-256 of the Monad LoRA adapter matrix
  - `deploy_url`: Live Vercel edge endpoint
  - `owner_address`: The creator's custodial or self-custodial wallet address
- **Sharing & Trading:**
  - Users can text or tweet their sticker link (`https://metasticker.vercel.app/claim?token=MUSE-...`).
  - Anyone scanning the physical sticker or opening the link can fork the agent, interact with it, or tip the creator in crypto/USD.
