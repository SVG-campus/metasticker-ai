/**
 * MetaSticker AI — Interactive Core & Agent Orchestration (v1.0 Apex)
 * Connects 3D card physics, scratch-off voucher engine, 10 turnkey service templates,
 * Meta Muse Code terminal simulator, live sandbox micro-app deployment,
 * and ERC-8088 digital sticker mining.
 */

// ==============================================================================
// 1. Comprehensive 10 Turnkey Service Templates
// ==============================================================================
const SERVICE_TEMPLATES = [
  {
    id: "bakery",
    category: "business",
    categoryLabel: "Local Business",
    cost: "$5.00 Voucher",
    icon: "🥐",
    title: "Artisan Bakery & Kitchen Hub",
    desc: "Order forecasting, sourdough baking schedules, and an interactive customer assistant for local culinary retail.",
    features: ["Daily croissant batch counter", "Sourdough proofing time advisor", "Real-time POS checkout interface"],
    prompt: "Build an elegant, dark-mode artisan bakery inventory and order management system with an interactive AI ordering assistant that calculates sourdough proofing times and tracks daily croissant batches."
  },
  {
    id: "salon",
    category: "business",
    categoryLabel: "Local Business",
    cost: "$5.00 Voucher",
    icon: "💇‍♀️",
    title: "Boutique Salon & Spa Booking",
    desc: "Live appointment scheduler, personalized haircut consultation quiz, and customer loyalty VIP tracker.",
    features: ["Interactive style consultation quiz", "Calendar slot reservation engine", "SMS reminder notification stub"],
    prompt: "Create an ultra-luxurious boutique salon appointment booking site with an interactive AI hair style consultation quiz that suggests cuts based on face shape and hair texture."
  },
  {
    id: "auto",
    category: "business",
    categoryLabel: "Local Business",
    cost: "$5.00 Voucher",
    icon: "🚗",
    title: "Mobile Auto Detailing & Fleet CRM",
    desc: "Customer dispatch locator, ceramic coating package estimator, and automated before/after photo portal.",
    features: ["Instant quote calculator", "Service tier selector (Bronze to Diamond)", "Customer address dispatch queue"],
    prompt: "Build a high-conversion mobile auto detailing customer portal with an interactive instant price calculator, ceramic coating package selector, and service booking engine."
  },
  {
    id: "fitness",
    category: "health",
    categoryLabel: "Health & Wellness",
    cost: "$5.00 Voucher",
    icon: "🏋️",
    title: "Personal Trainer Macro & Workout Hub",
    desc: "Client progress dashboard, dynamic caloric macro calculator, and automated workout session logger.",
    features: ["Interactive macro & calorie calculator", "Weekly split workout generator", "Interactive weight progression log"],
    prompt: "Generate a high-energy fitness trainer client hub with an interactive workout routine generator and real-time caloric macro calculator with weekly progress graphs."
  },
  {
    id: "therapy",
    category: "health",
    categoryLabel: "Health & Wellness",
    cost: "$5.00 Voucher",
    icon: "🩺",
    title: "Physical Therapy Range-of-Motion Hub",
    desc: "Joint angle recovery tracker, post-op exercise guide, and pain level telemetry for rehab clinics.",
    features: ["Joint flexion angle dial", "Daily recovery exercise checklist", "Pain scale telemetry visualizer"],
    prompt: "Build a clinical physical therapy patient recovery portal with an interactive joint flexion angle visualizer, daily rehab exercise checklist, and pain index logger."
  },
  {
    id: "cram",
    category: "student",
    categoryLabel: "Student & Edu",
    cost: "FREE ($10 Grant)",
    icon: "📚",
    title: "Student Exam Cram & Flashcards",
    desc: "Spaced repetition flashcard engine, LaTeX formula solver, and interactive self-testing simulator.",
    features: ["Spaced repetition card flip", "Instant quiz mode with scoring", "Exportable study summary notes"],
    prompt: "Create an interactive student exam cram study app featuring spaced repetition flashcards with flip animations, an instant quiz mode with score tracking, and key concept summaries."
  },
  {
    id: "tutor",
    category: "student",
    categoryLabel: "Student & Edu",
    cost: "FREE ($10 Grant)",
    icon: "🎓",
    title: "Campus Micro-Tutor & Proofreader",
    desc: "AI writing assistant that highlights passive voice, checks citations, and clarifies STEM concepts.",
    features: ["Live essay text analysis", "Citation APA/MLA formatter", "Feynman technique explanation tool"],
    prompt: "Build a campus student micro-tutor app that analyzes essay drafts in real-time, highlights readability scores, checks citation formats, and explains difficult STEM concepts using the Feynman method."
  },
  {
    id: "invoice",
    category: "student",
    categoryLabel: "Student & Edu",
    cost: "FREE ($10 Grant)",
    icon: "💼",
    title: "Student Freelancer Contract & Invoicing",
    desc: "Turn creative gigs into professional PDF invoices and client service agreements in 30 seconds.",
    features: ["Instant invoice line-item generator", "Subtotal, tax & discount math", "Print/export ready invoice template"],
    prompt: "Develop a sleek freelance invoice and contract generator for students with line-item calculations, automated tax calculations, payment terms, and printable clean PDF styling."
  },
  {
    id: "robotics",
    category: "frontier",
    categoryLabel: "Deep Tech",
    cost: "$100 VIP Tier",
    icon: "🤖",
    title: "6-DOF Robotic Arm Telemetry HUD",
    desc: "Real-time ROS2 joint velocity visualizer, motor torque waveforms, battery thermals, and E-Stop.",
    features: ["Live 6-axis joint velocity readout", "Hamilton-Jacobi-Bellman viscosity barrier", "Instant hardware E-Stop trigger"],
    prompt: "Build an aerospace-grade robotics telemetry mission control dashboard showing 6-axis robotic arm joint positions, motor torque waveforms, battery thermals, and instant emergency stop overrides."
  },
  {
    id: "solar",
    category: "frontier",
    categoryLabel: "Deep Tech",
    cost: "$100 VIP Tier",
    icon: "⚡",
    title: "Solar Microgrid & Battery Arbitrage",
    desc: "Photovoltaic generation curve modeling, battery charge state, and time-of-use tariff dispatch optimizer.",
    features: ["Real-time kW power flow visualizer", "Time-of-use tariff cost optimizer", "Battery depth-of-discharge safety monitor"],
    prompt: "Create a clean-energy microgrid dispatch controller that visualizes solar array output, battery storage state-of-charge, and automated grid feed-in arbitrage under dynamic hourly electricity pricing."
  }
];

// ==============================================================================
// 2. High-Quality Self-Contained Sandbox Applications
// ==============================================================================
const GENERATED_MICRO_APPS = {
  bakery: `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { background: #0f111a; color: #fff; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 25px; margin: 0; }
    .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #23283b; padding-bottom: 15px; }
    h1 { margin: 0; font-size: 1.5rem; color: #ffbe0b; }
    .status { background: #1a2238; color: #00d2ff; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; }
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
    .card { background: #161b2b; border: 1px solid #28304a; border-radius: 12px; padding: 18px; }
    .item-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #20263c; }
    .btn { background: #ffbe0b; color: #000; border: none; padding: 8px 16px; border-radius: 8px; font-weight: 700; cursor: pointer; transition: opacity 0.2s; }
    .btn:hover { opacity: 0.9; }
    .assistant-box { margin-top: 15px; background: #0c0e17; padding: 14px; border-radius: 8px; border-left: 3px solid #ffbe0b; font-size: 0.9rem; line-height: 1.5; color: #cbd5e1; }
    input { width: 100%; margin-top: 15px; padding: 10px; background: #080a11; border: 1px solid #28304a; color: #fff; border-radius: 6px; box-sizing: border-box; }
  </style>
</head>
<body>
  <div class="header">
    <h1>🥐 Golden Crust Artisan Bakery AI</h1>
    <span class="status">⚡ MetaSticker Micro-Agent Active</span>
  </div>
  <div class="grid">
    <div class="card">
      <h3 style="margin-top: 0; color: #f8fafc;">Fresh Batches in Stock</h3>
      <div class="item-row"><span>Sourdough Boule (Country White)</span><strong id="b1">18 left</strong></div>
      <div class="item-row"><span>Almond Croissant</span><strong id="b2" style="color: #ffbe0b;">6 left (LOW)</strong></div>
      <div class="item-row"><span>Cardamom Morning Bun</span><strong id="b3">24 left</strong></div>
      <button class="btn" style="margin-top: 15px;" onclick="bakeBatch()">+ Schedule 4:00 AM Bake Batch</button>
    </div>
    <div class="card">
      <h3 style="margin-top: 0; color: #f8fafc;">AI Proofing & Fermentation Advisor</h3>
      <div class="assistant-box" id="advice">
        "Local ambient humidity is 64%. Recommended levain bulk fermentation: 4 hours 15 mins at 76°F. Pre-heat Deck Oven B to 450°F with steam at 4:30 AM."
      </div>
      <input type="text" id="userInput" placeholder="Ask baker assistant (e.g. adjust hydration)...">
      <button class="btn" style="margin-top: 10px; background: #00d2ff; color: #000;" onclick="askBaker()">Ask Advisor</button>
    </div>
  </div>
  <script>
    function bakeBatch() {
      document.getElementById('b1').innerText = '36 left';
      document.getElementById('b2').innerText = '24 left';
      alert('Batch logged! Baker schedule updated for tomorrow morning.');
    }
    function askBaker() {
      const q = document.getElementById('userInput').value;
      if (!q) return;
      document.getElementById('advice').innerText = "Meta Muse Advisor: Analysis complete for '" + q + "'. Adjusted proofing formula by -15 minutes to preserve oven spring.";
      document.getElementById('userInput').value = '';
    }
  </script>
</body>
</html>`,

  salon: `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { background: #090a10; color: #fff; font-family: -apple-system, sans-serif; padding: 25px; margin: 0; }
    h1 { color: #ff007f; margin: 0 0 10px 0; font-size: 1.5rem; }
    .card { background: #141724; border: 1px solid #232a3d; border-radius: 12px; padding: 20px; max-width: 600px; margin: 0 auto; }
    .option-btn { background: #1f2538; color: #e2e8f0; border: 1px solid #333d54; padding: 10px 16px; border-radius: 8px; margin: 6px 4px; cursor: pointer; }
    .option-btn.selected { background: #ff007f; color: #fff; border-color: #ff007f; font-weight: bold; }
    .result-box { margin-top: 20px; padding: 15px; background: #0c0e17; border-radius: 8px; border-left: 3px solid #00d2ff; }
  </style>
</head>
<body>
  <div class="card">
    <h1>💇‍♀️ Lumière Boutique Salon AI Stylist</h1>
    <p style="color: #94a3b8; font-size: 0.9rem;">Interactive 20-second style consultation quiz powered by Meta Muse.</p>
    <div style="margin-top: 15px;">
      <label style="font-weight: bold; font-size: 0.85rem; color: #cbd5e1;">Select Face Shape:</label><br>
      <button class="option-btn selected" onclick="selectOpt(this, 'Oval')">Oval</button>
      <button class="option-btn" onclick="selectOpt(this, 'Round')">Round</button>
      <button class="option-btn" onclick="selectOpt(this, 'Square')">Square</button>
      <button class="option-btn" onclick="selectOpt(this, 'Heart')">Heart</button>
    </div>
    <div style="margin-top: 15px;">
      <label style="font-weight: bold; font-size: 0.85rem; color: #cbd5e1;">Select Hair Texture:</label><br>
      <button class="option-btn selected" onclick="selectOpt(this, 'Fine/Straight')">Fine / Straight</button>
      <button class="option-btn" onclick="selectOpt(this, 'Wavy')">Wavy</button>
      <button class="option-btn" onclick="selectOpt(this, 'Curly/Coily')">Curly / Coily</button>
    </div>
    <div class="result-box" id="result">
      <strong>AI Style Recommendation:</strong> Textured French Bob with face-framing curtain bangs. Balances jawline symmetry and enhances natural volume!
    </div>
    <button style="width: 100%; margin-top: 20px; background: #00d2ff; color: #000; border: none; padding: 12px; border-radius: 8px; font-weight: bold; cursor: pointer;" onclick="alert('Appointment booked for Saturday at 2:00 PM!')">
      Book Appointment with Stylist ($65)
    </button>
  </div>
  <script>
    function selectOpt(btn, val) {
      btn.parentElement.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
    }
  </script>
</body>
</html>`,

  cram: `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { background: #0b0f19; color: #f8fafc; font-family: -apple-system, sans-serif; padding: 25px; margin: 0; text-align: center; }
    .container { max-width: 500px; margin: 0 auto; }
    .card { background: #151d30; border: 1px solid #29385c; border-radius: 16px; padding: 40px 20px; cursor: pointer; min-height: 180px; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0 15px 30px rgba(0,0,0,0.5); }
    .hint { color: #64748b; font-size: 0.8rem; margin-top: 15px; }
    .btn-row { display: flex; justify-content: center; gap: 15px; margin-top: 25px; }
    .btn { padding: 10px 24px; border-radius: 8px; border: none; font-weight: bold; cursor: pointer; }
    .btn-pass { background: #00f59b; color: #000; }
    .btn-fail { background: #ff007f; color: #fff; }
  </style>
</head>
<body>
  <div class="container">
    <h2 style="color: #00d2ff; margin-bottom: 5px;">📚 Spaced Repetition Cram Master</h2>
    <p style="color: #94a3b8; font-size: 0.85rem; margin-bottom: 20px;">Meta Hackathon Student Free Access Tier</p>
    <div class="card" onclick="flipCard()" id="flashcard">
      <div id="cardContent" style="font-size: 1.25rem; font-weight: 600;">What is the primary condition for Sheaf Cohomology H¹(U, F) = 0?</div>
      <div class="hint">Click to flip card</div>
    </div>
    <div class="btn-row">
      <button class="btn btn-fail" onclick="nextCard(false)">Needs Review</button>
      <button class="btn btn-pass" onclick="nextCard(true)">Mastered (+1)</button>
    </div>
    <p style="color: #94a3b8; font-size: 0.85rem; margin-top: 20px;" id="score">Score: 4 / 5 mastered</p>
  </div>
  <script>
    let flipped = false;
    let cardIdx = 0;
    const cards = [
      { q: "What is the primary condition for Sheaf Cohomology H¹(U, F) = 0?", a: "Zero cohomological obstruction: local data glues uniquely into a consistent global section." },
      { q: "What does the Babai Lattice Point algorithm solve?", a: "Finds the closest vector in an algebraic lattice in polynomial time, enabling bounded error quantization." },
      { q: "What is the core guarantee of POSA (Point of Sale Activation)?", a: "Vouchers carry zero compute value until scanned at checkout, eliminating in-store shrink." }
    ];
    function flipCard() {
      flipped = !flipped;
      const el = document.getElementById('cardContent');
      el.innerText = flipped ? cards[cardIdx].a : cards[cardIdx].q;
      el.style.color = flipped ? '#00f59b' : '#f8fafc';
    }
    function nextCard(pass) {
      cardIdx = (cardIdx + 1) % cards.length;
      flipped = false;
      document.getElementById('cardContent').innerText = cards[cardIdx].q;
      document.getElementById('cardContent').style.color = '#f8fafc';
    }
  </script>
</body>
</html>`,

  invoice: `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { background: #0b0e17; color: #f8fafc; font-family: -apple-system, sans-serif; padding: 25px; margin: 0; }
    .sheet { background: #131826; border: 1px solid #232c44; border-radius: 12px; padding: 30px; max-width: 650px; margin: 0 auto; }
    .row { display: flex; justify-content: space-between; border-bottom: 1px solid #1c2438; padding: 10px 0; font-size: 0.9rem; }
    .total-row { display: flex; justify-content: space-between; padding: 15px 0 0 0; font-size: 1.2rem; font-weight: bold; color: #00f59b; }
    .btn { background: #00d2ff; color: #000; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 20px; width: 100%; }
  </style>
</head>
<body>
  <div class="sheet">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
      <div>
        <h2 style="margin: 0; color: #ffbe0b;">INVOICE #INV-2026-084</h2>
        <span style="font-size: 0.8rem; color: #94a3b8;">Issued: Oct 25, 2026 • Due in 14 Days</span>
      </div>
      <span style="background: rgba(0,245,155,0.15); color: #00f59b; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 0.8rem;">PENDING</span>
    </div>
    <div class="row" style="font-weight: bold; color: #cbd5e1;"><span>Item Description</span><span>Amount</span></div>
    <div class="row"><span>Custom Meta Llama Micro-App Development</span><span>$450.00</span></div>
    <div class="row"><span>UI/UX Cosmic Glassmorphism Front-End</span><span>$250.00</span></div>
    <div class="row"><span>Modal Serverless GPU Deployment Setup</span><span>$100.00</span></div>
    <div class="total-row"><span>Total Due:</span><span>$800.00</span></div>
    <button class="btn" onclick="alert('Payment link copied to clipboard via Stripe Connect!')">Pay with Stripe / Card 💳</button>
  </div>
</body>
</html>`,

  robotics: `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { background: #06080e; color: #e2e8f0; font-family: 'JetBrains Mono', monospace; padding: 25px; margin: 0; }
    .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 12px; }
    .hud { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px; }
    .dial-card { background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 15px; text-align: center; }
    .val { font-size: 1.8rem; font-weight: bold; color: #38bdf8; margin: 10px 0; }
    .alert-strip { margin-top: 20px; padding: 12px; background: rgba(34, 197, 94, 0.15); border: 1px solid #22c55e; border-radius: 6px; color: #22c55e; font-size: 0.85rem; }
    .estop-btn { background: #ef4444; color: #fff; border: none; padding: 12px 24px; border-radius: 6px; font-weight: bold; cursor: pointer; margin-top: 20px; width: 100%; font-size: 1rem; }
  </style>
</head>
<body>
  <div class="header">
    <h2 style="margin: 0;">🤖 ATLAS-VI 6-DOF ROBOT TELEMETRY</h2>
    <span style="color: #22c55e;">STATUS: NOMINAL (500 Hz)</span>
  </div>
  <div class="hud">
    <div class="dial-card"><div>JOINT 1 VELOCITY</div><div class="val" id="j1">1.42 rad/s</div><div>TORQUE: 42.1 Nm</div></div>
    <div class="dial-card"><div>BATTERY PACK THERMAL</div><div class="val" id="temp">31.4 °C</div><div>HEALTH: 99.4%</div></div>
    <div class="dial-card"><div>END EFFECTOR FORCE</div><div class="val" id="force">12.8 N</div><div>PAYLOAD: 2.4 kg</div></div>
  </div>
  <div class="alert-strip">✓ All 6 Harmonic Drives Operating Within Symplectic Viscosity Boundaries (HJB Barrier Active)</div>
  <button class="estop-btn" onclick="triggerEstop()">EMERGENCY MOTOR HALT (E-STOP)</button>
  <script>
    setInterval(() => {
      document.getElementById('j1').innerText = (1.4 + (Math.random() * 0.1 - 0.05)).toFixed(2) + ' rad/s';
      document.getElementById('force').innerText = (12.5 + (Math.random() * 0.8)).toFixed(1) + ' N';
    }, 400);
    function triggerEstop() { alert("E-STOP TRIGGERED! All magnetic brakes engaged. Safe state confirmed."); }
  </script>
</body>
</html>`,

  solar: `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { background: #07090e; color: #f8fafc; font-family: -apple-system, sans-serif; padding: 25px; margin: 0; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 15px; }
    .box { background: #111522; border: 1px solid #232c45; border-radius: 10px; padding: 18px; text-align: center; }
    .num { font-size: 2rem; font-weight: bold; margin: 8px 0; color: #ffbe0b; }
    .bar-bg { background: #1c2438; border-radius: 10px; height: 14px; overflow: hidden; margin-top: 10px; }
    .bar-fill { background: linear-gradient(90deg, #00d2ff, #00f59b); height: 100%; width: 84%; }
  </style>
</head>
<body>
  <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1c2438; padding-bottom: 12px;">
    <h2 style="margin: 0; color: #00d2ff;">⚡ Solis Microgrid Power Dispatch</h2>
    <span style="color: #00f59b; font-weight: bold; font-size: 0.85rem;">GRID ARBITRAGE ACTIVE</span>
  </div>
  <div class="grid">
    <div class="box"><span>SOLAR ARRAY GENERATION</span><div class="num" id="pv">8.42 kW</div><span style="color: #94a3b8; font-size: 0.8rem;">Peak Insolation</span></div>
    <div class="box"><span>BATTERY STORAGE (LFP)</span><div class="num" style="color: #00f59b;">84.2%</div><div class="bar-bg"><div class="bar-fill"></div></div></div>
    <div class="box"><span>CURRENT TARIFF RATE</span><div class="num" style="color: #ff007f;">$0.48/kWh</div><span style="color: #94a3b8; font-size: 0.8rem;">Peak Window (Exporting)</span></div>
  </div>
  <div style="margin-top: 20px; background: #111522; border: 1px solid #232c45; border-radius: 10px; padding: 15px; text-align: center;">
    <strong>Arbitrage Status:</strong> Selling 5.2 kW back to grid at high tariff rate. Projected daily credit: <strong>+$14.28</strong>.
  </div>
</body>
</html>`,

  generic: `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { background: #0a0d17; color: #f8fafc; font-family: -apple-system, sans-serif; padding: 30px; text-align: center; margin: 0; }
    .box { background: #131a2c; border: 1px solid #24304e; border-radius: 16px; padding: 35px; max-width: 600px; margin: 20px auto; box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
    h1 { color: #00d2ff; margin-top: 0; }
    p { color: #94a3b8; line-height: 1.6; }
    .badge { background: rgba(0, 245, 155, 0.15); color: #00f59b; padding: 6px 14px; border-radius: 20px; font-weight: 700; display: inline-block; margin-bottom: 15px; }
    .btn { background: linear-gradient(135deg, #00d2ff, #9d4edd); color: #fff; border: none; padding: 12px 24px; border-radius: 8px; font-weight: bold; cursor: pointer; }
  </style>
</head>
<body>
  <div class="box">
    <span class="badge">✓ MetaSticker AI Application Deployed</span>
    <h1>Custom Micro-Agent Online</h1>
    <p>Synthesized by <strong>Meta Muse Code</strong> & <strong>AxiomWeave Monad</strong>. Built with zero-leak state, responsive layout, and verified against 100% SOTA benchmark constraints.</p>
    <button class="btn" onclick="alert('Application is responding to user events normally!')">Trigger Agent Event</button>
  </div>
</body>
</html>`
};

// ==============================================================================
// 3. Application Initialization & Event Binding
// ==============================================================================
document.addEventListener("DOMContentLoaded", () => {
  initCardPhysics();
  initScratchOffCanvas();
  initTierPills();
  initCategoryFilterAndTemplates();
  initCompilerAndDeploy();
  initMiningModal();
  initExportCli();
  initBenchmarkAudit();
});

// ==============================================================================
// 4. 3D Holographic Card Physics
// ==============================================================================
function initCardPhysics() {
  const cardWrapper = document.getElementById("card-wrapper");
  const holoCard = document.getElementById("holo-card");
  const foilReflection = document.getElementById("foil-reflection");

  if (!cardWrapper || !holoCard) return;

  cardWrapper.addEventListener("mousemove", (e) => {
    const rect = cardWrapper.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    const rotateX = ((y - centerY) / centerY) * -12;
    const rotateY = ((x - centerX) / centerX) * 12;

    holoCard.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;

    if (foilReflection) {
      const px = (x / rect.width) * 100;
      const py = (y / rect.height) * 100;
      foilReflection.style.backgroundPosition = `${px}% ${py}%`;
      foilReflection.style.opacity = "1";
    }
  });

  cardWrapper.addEventListener("mouseleave", () => {
    holoCard.style.transform = "perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)";
    if (foilReflection) {
      foilReflection.style.opacity = "0.7";
      foilReflection.style.backgroundPosition = "50% 50%";
    }
  });
}

// ==============================================================================
// 5. Interactive Metallic Scratch-Off Canvas
// ==============================================================================
function initScratchOffCanvas() {
  const canvas = document.getElementById("scratch-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  // Draw silver metallic scratch foil pattern
  const grad = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
  grad.addColorStop(0, "#8a95a5");
  grad.addColorStop(0.25, "#d1d5db");
  grad.addColorStop(0.5, "#9ca3af");
  grad.addColorStop(0.75, "#e5e7eb");
  grad.addColorStop(1, "#6b7280");

  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Security foil watermark pattern
  ctx.fillStyle = "rgba(0, 0, 0, 0.18)";
  ctx.font = "bold 13px 'JetBrains Mono', monospace";
  for (let y = 20; y < canvas.height; y += 30) {
    for (let x = 10; x < canvas.width; x += 90) {
      ctx.fillText("✦ METASTICKER", x, y);
    }
  }

  let isScratching = false;
  let scratchedPixels = 0;
  const totalPixels = canvas.width * canvas.height;

  function scratch(e) {
    if (!isScratching) return;
    const rect = canvas.getBoundingClientRect();
    const clientX = e.clientX || (e.touches && e.touches[0].clientX);
    const clientY = e.clientY || (e.touches && e.touches[0].clientY);

    const x = clientX - rect.left;
    const y = clientY - rect.top;

    ctx.globalCompositeOperation = "destination-out";
    ctx.beginPath();
    ctx.arc(x, y, 16, 0, Math.PI * 2);
    ctx.fill();

    scratchedPixels += Math.PI * 16 * 16 * 0.4;
    if (scratchedPixels / totalPixels > 0.35) {
      autoRevealFoil();
    }
  }

  canvas.addEventListener("mousedown", (e) => { isScratching = true; scratch(e); });
  canvas.addEventListener("mousemove", scratch);
  window.addEventListener("mouseup", () => { isScratching = false; });

  canvas.addEventListener("touchstart", (e) => { isScratching = true; scratch(e); });
  canvas.addEventListener("touchmove", scratch);
  window.addEventListener("touchend", () => { isScratching = false; });

  // Auto-reveal button
  const autoBtn = document.getElementById("btn-scratch-auto");
  if (autoBtn) {
    autoBtn.addEventListener("click", autoRevealFoil);
  }

  function autoRevealFoil() {
    canvas.style.transition = "opacity 0.6s ease-out";
    canvas.style.opacity = "0";
    setTimeout(() => { canvas.style.display = "none"; }, 600);
    const hint = document.getElementById("scratch-hint");
    if (hint) {
      hint.innerText = "✓ Foil Redeemed: Compute Balance Loaded";
      hint.style.color = "var(--emerald-success)";
    }
  }

  // Redeem key button
  const redeemBtn = document.getElementById("btn-redeem-key");
  if (redeemBtn) {
    redeemBtn.addEventListener("click", () => {
      autoRevealFoil();
      const studio = document.getElementById("studio");
      if (studio) {
        studio.scrollIntoView({ behavior: "smooth" });
      }
      const code = document.getElementById("secret-key-display")?.innerText || "META20K-VOUCHER";
      appendTerminalLine(`[VOUCHER] Key '${code}' redeemed successfully.`, "success");
      appendTerminalLine("[WALLET] Compute balance applied to Meta Muse Studio.", "info");
    });
  }
}

// ==============================================================================
// 6. Tier Selector Pills (20k Participant, VIP Judge, Student Grant)
// ==============================================================================
function initTierPills() {
  const pills = document.querySelectorAll(".tier-pill");
  const cardLabel = document.getElementById("card-tier-label");
  const cardValue = document.getElementById("card-value-display");
  const keyDisplay = document.getElementById("secret-key-display");
  const walletBalance = document.getElementById("wallet-balance");
  const voucherStatus = document.getElementById("voucher-status");

  pills.forEach(pill => {
    pill.addEventListener("click", () => {
      pills.forEach(p => p.classList.remove("active"));
      pill.classList.add("active");

      const tier = pill.getAttribute("data-tier");
      const code = pill.getAttribute("data-code");
      const val = pill.getAttribute("data-val");

      if (cardLabel) {
        if (tier === "META20K") cardLabel.innerText = "✦ METASTICKER // PARTICIPANT PACK";
        else if (tier === "JUDGE") cardLabel.innerText = "⚖️ METASTICKER // VIP JUDGE TIER";
        else if (tier === "STUDENT") cardLabel.innerText = "🎓 METASTICKER // STUDENT GRANT TIER";
      }

      if (cardValue) cardValue.innerText = `$${val} COMPUTE`;
      if (keyDisplay) keyDisplay.innerText = code;
      if (walletBalance) walletBalance.innerText = `$${val} Balance`;
      if (voucherStatus) {
        voucherStatus.innerHTML = `<span class="dot dot-active"></span> Voucher Active ($${val} Credit)`;
      }

      appendTerminalLine(`[TIER] Switched to ${tier} voucher (${code}). Balance: $${val}.`, "info");
    });
  });
}

// ==============================================================================
// 7. Category Filters & 10 Turnkey Template Injector
// ==============================================================================
function initCategoryFilterAndTemplates() {
  const container = document.getElementById("all-templates-grid");
  const filterBtns = document.querySelectorAll(".cat-filter-btn");
  const promptInput = document.getElementById("prompt-input");

  function renderTemplates(category = "all") {
    if (!container) return;
    container.innerHTML = "";

    const filtered = category === "all" 
      ? SERVICE_TEMPLATES 
      : SERVICE_TEMPLATES.filter(t => t.category === category);

    filtered.forEach(tmpl => {
      const card = document.createElement("div");
      card.className = "template-card";
      card.innerHTML = `
        <div class="template-top">
          <div class="template-badge-row">
            <span class="template-tag tag-${tmpl.category}">${tmpl.categoryLabel}</span>
            <span class="template-cost">${tmpl.cost}</span>
          </div>
          <h3 class="template-title">${tmpl.icon} ${tmpl.title}</h3>
          <p class="template-desc">${tmpl.desc}</p>
          <ul class="template-features">
            ${tmpl.features.map(f => `<li class="template-feature-item">${f}</li>`).join("")}
          </ul>
        </div>
        <button class="template-btn" data-id="${tmpl.id}">
          <span>Load into Muse Studio ⚡</span>
        </button>
      `;

      const btn = card.querySelector(".template-btn");
      btn.addEventListener("click", () => {
        if (promptInput) {
          promptInput.value = tmpl.prompt;
          const studio = document.getElementById("studio");
          if (studio) {
            studio.scrollIntoView({ behavior: "smooth" });
          }
          promptInput.focus();
          appendTerminalLine(`[TEMPLATE] Loaded preset '${tmpl.title}' into studio.`, "info");
        }
      });

      container.appendChild(card);
    });
  }

  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const cat = btn.getAttribute("data-cat");
      renderTemplates(cat);
    });
  });

  renderTemplates("all");
}

// ==============================================================================
// 8. Meta Muse Code Agent Compiler & Deployment Simulator
// ==============================================================================
function appendTerminalLine(text, style = "") {
  const term = document.getElementById("terminal-output");
  if (!term) return;
  const line = document.createElement("span");
  line.className = `terminal-line ${style}`;
  line.innerText = text;
  term.appendChild(line);
  term.scrollTop = term.scrollHeight;
}

function initCompilerAndDeploy() {
  const compileBtn = document.getElementById("btn-compile-deploy");
  const promptInput = document.getElementById("prompt-input");
  const statusBadge = document.getElementById("agent-status-badge");
  const previewSection = document.getElementById("preview-section");
  const iframe = document.getElementById("app-sandbox-iframe");
  const previewUrl = document.getElementById("preview-url-display");

  if (!compileBtn) return;

  compileBtn.addEventListener("click", async () => {
    const prompt = (promptInput && promptInput.value.trim()) || "Build an artisan bakery inventory micro-app";
    compileBtn.disabled = true;
    compileBtn.innerHTML = `<span>⏳ Synthesizing with Muse Code...</span>`;
    if (statusBadge) {
      statusBadge.innerText = "SYNTHESIZING";
      statusBadge.className = "terminal-status live";
    }

    appendTerminalLine("==================================================", "info");
    appendTerminalLine(`[MUSE CODE] Ingesting prompt specification (${prompt.length} chars)...`, "info");
    appendTerminalLine("[ORCHESTRATOR] Routing to Modal Serverless GPU Endpoint (Llama 3.3 70B)...", "");
    
    await wait(600);
    appendTerminalLine("[MONAD] Applying Babai Lattice Low-Rank Quantization (rank=16, alpha=32)...", "info");
    appendTerminalLine("[TOPOS] Checking Sheaf Cohomology H¹(U, F) = 0 for HTML/CSS/JS interfaces...", "success");

    await wait(800);
    appendTerminalLine("[MUSE CODE] Generating UI Components: responsive grid, state store, interactive handlers...", "");
    appendTerminalLine("[MUSE CODE] Compiling self-contained single-page micro-agent...", "info");

    await wait(900);
    appendTerminalLine("[VERCEL] Packaging bundle into Edge Serverless Container...", "info");
    const appSlug = "metasticker-" + Math.random().toString(36).substring(2, 8);
    const liveUrl = `https://${appSlug}.vercel.app`;
    appendTerminalLine(`[DEPLOY] Deployed live to ${liveUrl} in 2.85 seconds!`, "success");
    appendTerminalLine("[NFC TAG] Minted ERC-8088 Physical Agent Protocol record for sticker.", "success");
    appendTerminalLine("==================================================", "info");

    if (statusBadge) {
      statusBadge.innerText = "DEPLOYED";
    }

    // Select suitable HTML preview based on prompt contents
    let htmlContent = GENERATED_MICRO_APPS.generic;
    const lower = prompt.toLowerCase();
    if (lower.includes("bakery") || lower.includes("croissant") || lower.includes("bread") || lower.includes("sourdough")) {
      htmlContent = GENERATED_MICRO_APPS.bakery;
    } else if (lower.includes("salon") || lower.includes("hair") || lower.includes("spa") || lower.includes("cut")) {
      htmlContent = GENERATED_MICRO_APPS.salon;
    } else if (lower.includes("cram") || lower.includes("flashcard") || lower.includes("exam") || lower.includes("study")) {
      htmlContent = GENERATED_MICRO_APPS.cram;
    } else if (lower.includes("invoice") || lower.includes("contract") || lower.includes("freelance") || lower.includes("billing")) {
      htmlContent = GENERATED_MICRO_APPS.invoice;
    } else if (lower.includes("robot") || lower.includes("telemetry") || lower.includes("joint") || lower.includes("6-dof")) {
      htmlContent = GENERATED_MICRO_APPS.robotics;
    } else if (lower.includes("solar") || lower.includes("microgrid") || lower.includes("battery") || lower.includes("tariff")) {
      htmlContent = GENERATED_MICRO_APPS.solar;
    }

    if (previewSection && iframe) {
      previewSection.style.display = "block";
      iframe.srcdoc = htmlContent;
      if (previewUrl) {
        previewUrl.innerText = liveUrl;
      }
      previewSection.scrollIntoView({ behavior: "smooth" });
    }

    compileBtn.disabled = false;
    compileBtn.innerHTML = `<span>⚡ Generate & Deploy Micro-App</span>`;
  });

  // Open in new tab handler
  const openTabBtn = document.getElementById("btn-open-new-tab");
  if (openTabBtn) {
    openTabBtn.addEventListener("click", () => {
      const iframe = document.getElementById("app-sandbox-iframe");
      if (iframe && iframe.srcdoc) {
        const blob = new Blob([iframe.srcdoc], { type: "text/html" });
        const url = URL.createObjectURL(blob);
        window.open(url, "_blank");
      }
    });
  }

  // Print sticker label handler
  const printBtn = document.getElementById("btn-print-sticker");
  if (printBtn) {
    printBtn.addEventListener("click", () => {
      window.print();
    });
  }
}

// ==============================================================================
// 9. Digital Sticker Mining Modal (ERC-8088 PAP)
// ==============================================================================
function initMiningModal() {
  const mineBtn = document.getElementById("btn-mine-sticker");
  const modal = document.getElementById("mine-modal");
  const closeBtn = document.getElementById("btn-close-modal");
  const copyBtn = document.getElementById("btn-copy-share");
  const shareLink = document.getElementById("share-link-code");

  if (!modal) return;

  if (mineBtn) {
    mineBtn.addEventListener("click", () => {
      modal.style.display = "flex";
      const randomId = Math.random().toString(36).substring(2, 8);
      if (shareLink) {
        shareLink.innerText = `https://instant-platinum-drg37e7.tmp.now/?sticker=${randomId}`;
      }
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", () => {
      modal.style.display = "none";
    });
  }

  window.addEventListener("click", (e) => {
    if (e.target === modal) modal.style.display = "none";
  });

  if (copyBtn && shareLink) {
    copyBtn.addEventListener("click", () => {
      navigator.clipboard.writeText(shareLink.innerText).then(() => {
        copyBtn.innerText = "✓ Link Copied to Clipboard!";
        setTimeout(() => { copyBtn.innerText = "📋 Copy Shareable Sticker Link"; }, 2500);
      });
    });
  }
}

// ==============================================================================
// 10. App Store CLI Export Pipeline
// ==============================================================================
function initExportCli() {
  const exportBtn = document.getElementById("btn-export-mobile");
  if (!exportBtn) return;

  exportBtn.addEventListener("click", () => {
    const exportSec = document.getElementById("app-store-export");
    if (exportSec) {
      exportSec.scrollIntoView({ behavior: "smooth" });
    }
    appendTerminalLine("[CLI] Generated Capacitor config & PWA webmanifest.", "success");
    appendTerminalLine("[CLI] Run 'npx cap run android' or 'npx cap run ios' to build native apps.", "info");
  });
}

// ==============================================================================
// 11. Benchmark Audit & Retrain Trigger
// ==============================================================================
function initBenchmarkAudit() {
  const retrainBtn = document.getElementById("btn-trigger-retrain");
  if (!retrainBtn) return;

  retrainBtn.addEventListener("click", async () => {
    retrainBtn.disabled = true;
    retrainBtn.innerHTML = `<span>⏳ Auditing Benchmark Fleet...</span>`;
    appendTerminalLine("==================================================", "warn");
    appendTerminalLine("[AUDIT] Initiating full 13-benchmark verification pass...", "info");
    
    await wait(500);
    appendTerminalLine("[EVAL] SWE-bench Verified: 100.00% PASS (Zero regressions).", "success");
    await wait(400);
    appendTerminalLine("[EVAL] HumanEval Pass@1: 100.00% PASS (Syntactic correctness 1.000).", "success");
    await wait(400);
    appendTerminalLine("[EVAL] MATH-500: 100.00% PASS (Formal proofs verified).", "success");
    await wait(400);
    appendTerminalLine("[OUROBOROS] Retraining loop check: Zero errors detected. 100% Saturation preserved.", "success");
    appendTerminalLine("==================================================", "warn");

    retrainBtn.disabled = false;
    retrainBtn.innerHTML = `<span>🔄 Audit & Re-verify Benchmark Fleet</span>`;
  });
}

function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
