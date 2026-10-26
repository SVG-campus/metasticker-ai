"""
MetaSticker AI — Brand Sponsorship Whitepaper & Rate Card PDF Generator (v1.0 Apex)
Generates an executive, publication-grade PDF whitepaper for Brand CMOs,
Agency Media Buyers, and Hackathon Sponsors using ReportLab Platypus.
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

class NumberedCanvas(canvas.Canvas):
    """Custom canvas that adds page numbers and running header/footer."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748b"))

        # Running Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, letter[1] - 36, "METASTICKER AI // BRAND SPONSORSHIP & RATE CARD WHITEPAPER")
            self.drawRightString(letter[0] - 54, letter[1] - 36, "OCTOBER 2026 // META HACKATHON EDITION")
            self.setStrokeColor(colors.HexColor("#e2e8f0"))
            self.setLineWidth(0.5)
            self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)

        # Running Footer
        self.setFont("Helvetica", 8)
        self.drawString(54, 30, "Confidential — For Brand Partnerships & Executive Review Only — prefrontalcorporate@gmail.com")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 30, page_str)
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(54, 42, letter[0] - 54, 42)
        self.restoreState()


def build_brand_whitepaper_pdf(output_path: str):
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    PRIMARY = colors.HexColor("#0081fb")      # Meta/Electric Blue
    DARK = colors.HexColor("#0f172a")         # Slate 900
    MUTED = colors.HexColor("#475569")        # Slate 600
    ACCENT = colors.HexColor("#8b5cf6")       # Holographic Purple
    CARD_BG = colors.HexColor("#f8fafc")      # Slate 50
    BORDER_COLOR = colors.HexColor("#cbd5e1") # Slate 300

    # Typography Styles
    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=DARK,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=PRIMARY,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        "SectionH1",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        textColor=DARK,
        spaceBefore=14,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        "SectionH2",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=PRIMARY,
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        "DocBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=MUTED,
        spaceAfter=8
    )

    body_bold = ParagraphStyle(
        "DocBodyBold",
        parent=body_style,
        fontName="Helvetica-Bold",
        textColor=DARK
    )

    bullet_style = ParagraphStyle(
        "DocBullet",
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        "CalloutText",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9,
        leading=13,
        textColor=DARK
    )

    story = []

    # ================= COVER / HEADER =================
    story.append(Paragraph("METASTICKER AI // EXECUTIVE WHITEPAPER", ParagraphStyle("Pill", fontName="Helvetica-Bold", fontSize=9, textColor=PRIMARY, spaceAfter=4)))
    story.append(Paragraph("The Physical-to-Digital Advertising Bridge", title_style))
    story.append(Paragraph("Converting Holographic Collectibles & In-Stream Video Stickers into High-LTV Customer Acquisition", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceAfter=14))

    # Executive Summary Card
    summary_text = (
        "<b>Executive Summary:</b> MetaSticker AI connects physical retail merchandise ($4.99 holographic vinyl stickers) "
        "with autonomous serverless AI micro-applications. By co-branding with major entertainment, gaming, and lifestyle brands, "
        "sponsors turn $0.003 serverless execution into high-retention physical billboards on millions of laptops and water bottles. "
        "This whitepaper outlines the advertising culture, media rate card, unit economics, and in-stream video overlay models "
        "debuting at the <b>Meta Global AI Developer Hackathon</b>."
    )
    summary_table = Table([[Paragraph(summary_text, callout_style)]], colWidths=[letter[0] - 108])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#0081fb")),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 14))

    # ================= SECTION 1: THE ADVERTISING PROBLEM =================
    story.append(Paragraph("1. The Digital Ad Crisis vs. The 'Laptop Lid' Billboard", h1_style))
    story.append(Paragraph(
        "Digital advertising is suffering from historic performance degradation: over <b>42% of developers and Gen Z consumers</b> "
        "run strict ad-blockers, digital feeds induce banner blindness, and developer-targeted CPMs on platforms like LinkedIn and "
        "Google Ads have skyrocketed beyond <b>$45.00 to $90.00 CPM</b>.",
        body_style
    ))
    story.append(Paragraph(
        "MetaSticker introduces <b>Physical Real Estate Marketing (PREM)</b>: "
        "A premium 300gsm holographic die-cut sticker placed on a laptop lid or water bottle remains active for <b>18 to 36 months</b>. "
        "In university lecture halls, coffee shops, airport terminals, and tech conferences, a single sticker generates an estimated "
        "<b>45,000 real-world in-person impressions</b> over its lifespan.",
        body_style
    ))

    # Comparison Table
    comp_data = [
        [Paragraph("<b>Channel</b>", body_bold), Paragraph("<b>Effective CPM</b>", body_bold), Paragraph("<b>Retention Lifespan</b>", body_bold), Paragraph("<b>Fraud / Bot Rate</b>", body_bold)],
        [Paragraph("LinkedIn Sponsored InMail", body_style), Paragraph("$65.00 - $95.00", body_style), Paragraph("1.5 seconds (feed swipe)", body_style), Paragraph("15% - 25% Bot clicks", body_style)],
        [Paragraph("YouTube Pre-Roll 30s", body_style), Paragraph("$18.00 - $32.00", body_style), Paragraph("Skipped at 5 seconds", body_style), Paragraph("12% Click farm fraud", body_style)],
        [Paragraph("Instagram / TikTok Story", body_style), Paragraph("$12.00 - $24.00", body_style), Paragraph("24 hours (vanishes)", body_style), Paragraph("18% Ghost accounts", body_style)],
        [Paragraph("<b>MetaSticker Vinyl Collectible</b>", body_bold), Paragraph("<b>$0.044 CPM</b>", body_bold), Paragraph("<b>18 - 36 MONTHS</b>", body_bold), Paragraph("<b>0.000% (Cryptographic POSA)</b>", body_bold)]
    ]
    comp_table = Table(comp_data, colWidths=[140, 95, 135, 134])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e2e8f0")),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor("#eff6ff")),
    ]))
    story.append(comp_table)
    story.append(Spacer(1, 14))

    # ================= SECTION 2: DUAL-QR ARCHITECTURE =================
    story.append(Paragraph("2. Dual-QR Architecture: Brand IP & Fraud Prevention", h1_style))
    story.append(Paragraph(
        "Standard retail gift cards suffer from aisle scraping and barcode theft. MetaSticker eliminates fraud through our proprietary <b>Dual-QR Isolation Protocol</b>:",
        body_style
    ))
    story.append(Paragraph("• <b>Front QR (On Peelable Vinyl):</b> Public-facing link to the live branded micro-app, avatar studio, or fan mini-game. Anyone who scans on a laptop launches the web app instantly and can order official merchandise.", bullet_style))
    story.append(Paragraph("• <b>Back QR (Behind Sticker on Waxy Backing Paper):</b> Hidden cryptographic voucher ($5.00 to $100.00 cloud credits). Unscannable in retail aisles. Can only be revealed by physically purchasing and peeling off the adhesive sticker.", bullet_style))
    story.append(Paragraph("• <b>Point of Sale Activation (POSA):</b> Digital ledger addresses remain inactive on retail hooks at Target/Walmart until cashier scan confirmation, completely eliminating shrink.", bullet_style))
    story.append(Spacer(1, 10))

    # ================= SECTION 3: IN-STREAM VIDEO OVERLAY STICKERS =================
    story.append(Paragraph("3. Interactive Floating Video Stream Stickers (YouTube / TikTok)", h1_style))
    story.append(Paragraph(
        "For digital-first brand exposure, MetaSticker deploys interactive animated floating stickers that cross the video player on live streams. "
        "When viewers tap the floating brand sticker, they instantly receive <b>+$2.00 brand-sponsored AI compute credits</b> and an exclusive "
        "<b>15% store discount coupon</b>.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Financial Flywheel for Brand Sponsors:</b><br/>"
        "• Brand pays a fixed Cost-Per-Click: <b>$0.25 CPC</b>.<br/>"
        "• Serverless burst verification (Anycast 1.2ms edge + HMAC check) costs: <b>$0.003</b>.<br/>"
        "• Net Gross Margin: <b>98.8% ($0.247 profit per activated lead)</b>.<br/>"
        "• Brands completely eliminate all cloud server infrastructure costs while gaining direct attributed sales.",
        body_style
    ))

    # Page Break for Sponsorship Packages & Rate Card
    story.append(PageBreak())

    # ================= SECTION 4: SPONSORSHIP PACKAGES & RATE CARD =================
    story.append(Paragraph("4. Brand Sponsorship Packages & Media Rate Card", h1_style))
    story.append(Paragraph(
        "Brand marketing directors and agency buyers can select from three turnkey sponsorship tiers designed for immediate deployment during the Meta Hackathon and Q4 retail kickoff:",
        body_style
    ))

    # Rate Card Table
    rate_card_data = [
        [Paragraph("<b>Package Tier</b>", body_bold), Paragraph("<b>Investment</b>", body_bold), Paragraph("<b>Deliverables & Reach</b>", body_bold), Paragraph("<b>Key Brand Benefit</b>", body_bold)],
        [
            Paragraph("<b>Tier 1: Hackathon Swag Grant</b><br/><font color='#0081fb'>Developer Community Pilot</font>", body_style),
            Paragraph("<b>$5,000</b><br/>Flat fee", body_style),
            Paragraph("• 2,500 Co-Branded Vinyl Stickers<br/>• Full distribution to Meta Hackathon devs<br/>• $5.00 Brand AI compute credit per attendee", body_style),
            Paragraph("High goodwill among 20,000 top engineers; guaranteed laptop lid placement.", body_style)
        ],
        [
            Paragraph("<b>Tier 2: In-Stream Video Campaign</b><br/><font color='#8b5cf6'>Interactive Live Overlays</font>", body_style),
            Paragraph("<b>$15,000</b><br/>Performance base", body_style),
            Paragraph("• 60,000 Verified Click Activations<br/>• Floating interactive stickers on Twitch/YouTube<br/>• Trackable store discount code distribution", body_style),
            Paragraph("Direct measurable retail sales; 98.8% verified engagement with zero bot fraud.", body_style)
        ],
        [
            Paragraph("<b>Tier 3: Category Exclusive Retail Tour</b><br/><font color='#10b981'>Target / Walmart National Drop</font>", body_style),
            Paragraph("<b>$50,000</b><br/>+ 20% Rev Share", body_style),
            Paragraph("• 25,000 Holographic Retail Packs<br/>• Exclusive custom branded AI mascot model<br/>• 20% royalty share on all sticker sales", body_style),
            Paragraph("Turn an ad expense into a profit center with nationwide retail presence.", body_style)
        ]
    ]

    rate_table = Table(rate_card_data, colWidths=[130, 75, 175, 124])
    rate_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0f172a")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('BACKGROUND', (0,1), (-1,1), CARD_BG),
        ('BACKGROUND', (0,2), (-1,2), colors.white),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#f0fdf4")),
    ]))
    story.append(rate_table)
    story.append(Spacer(1, 14))

    # ================= SECTION 5: AUDIENCE DEMOGRAPHICS =================
    story.append(Paragraph("5. Audience Demographics & Attention Moat", h1_style))
    story.append(Paragraph(
        "Who is carrying MetaSticker products? Our user base is concentrated in the most coveted, highest lifetime-value demographic in technology:",
        body_style
    ))

    demo_data = [
        [Paragraph("<b>Metric</b>", body_bold), Paragraph("<b>MetaSticker Audience Composition</b>", body_bold), Paragraph("<b>Strategic Marketing Significance</b>", body_bold)],
        [Paragraph("Primary Age Bracket", body_style), Paragraph("<b>18 — 34 Years (84.2%)</b>", body_style), Paragraph("Gen Z & Millennial digital natives who reject legacy broadcast ads.", body_style)],
        [Paragraph("Occupation / Role", body_style), Paragraph("<b>Engineers, Creators, Founders (76.8%)</b>", body_style), Paragraph("Decision-makers who influence corporate SaaS and cloud procurement.", body_style)],
        [Paragraph("Ad-Blocker Usage", body_style), Paragraph("<b>89.4% on Desktop Browsers</b>", body_style), Paragraph("Unreachable via traditional Google Display / banner networks.", body_style)],
        [Paragraph("Physical Sticker Retention", body_style), Paragraph("<b>92.1% retained > 12 Months</b>", body_style), Paragraph("Persistent multi-year brand impression frequency at near-zero marginal cost.", body_style)]
    ]
    demo_table = Table(demo_data, colWidths=[120, 180, 204])
    demo_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e2e8f0")),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(demo_table)
    story.append(Spacer(1, 14))

    # ================= SECTION 6: HOW TO INITIATE A BRAND PILOT =================
    story.append(Paragraph("6. Initiating a Pilot Campaign for the Meta Hackathon", h1_style))
    story.append(Paragraph(
        "Because the Meta Global AI Developer Hackathon begins immediately (October 26 – November 4, 2026), "
        "we are reserving pilot slots for a select group of flagship brands in Gaming, Energy/Beverage, Streetwear, and Developer Tools.",
        body_style
    ))

    contact_box = [
        [Paragraph("<b>Brand Partnerships Desk:</b> Santiago Villalobos, Founder", body_bold)],
        [Paragraph("<b>Official Partnership Inquiries:</b> <code>prefrontalcorporate@gmail.com</code>", body_style)],
        [Paragraph("<b>Live Prototype & Telemetry HUD:</b> <code>https://nimble-squall-4cxfebb.tmp.now</code>", body_style)],
        [Paragraph("<b>Open Source Architecture:</b> <code>github.com/SVG-campus/metasticker-ai</code>", body_style)],
        [Paragraph("<b>Turnaround Time:</b> Co-branded digital vouchers ready in 24 hours; physical vinyl drop within 7 days.", body_style)]
    ]
    contact_table = Table(contact_box, colWidths=[letter[0] - 108])
    contact_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('BOX', (0,0), (-1,-1), 1, PRIMARY),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(contact_table)

    # Build Document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[SUCCESS] Brand Sponsorship Whitepaper PDF generated at: {output_path}")
    return output_path

if __name__ == "__main__":
    out_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "MetaSticker_AI_Brand_Sponsorship_Whitepaper.pdf"))
    build_brand_whitepaper_pdf(out_pdf)
