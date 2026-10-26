/**
 * MetaSticker AI — Interactive Core & Agent Orchestration (v1.0 Apex)
 * Connects 3D card physics, scratch-off voucher engine, Meta Muse Code simulation,
 * and live sandbox micro-app deployment.
 */

// Preset Templates by Hackathon Theme
const THEME_PRESETS = {
  world: [
    {
      id: "bakery",
      title: "🥐 Artisan Bakery Inventory & Assistant",
      desc: "Order forecasting, sourdough baking schedules, and an interactive customer assistant for local retail.",
      prompt: "Build an elegant, dark-mode artisan bakery inventory and order management system with an interactive AI ordering assistant that calculates sourdough proofing times and tracks daily croissant batches."
    },
    {
      id: "salon",
      title: "💇‍♀️ Boutique Salon Booking & Style Quiz",
      desc: "Live appointment scheduler, personalized haircut style recommendation quiz, and customer loyalty tracker.",
      prompt: "Create an ultra-luxurious boutique salon appointment booking site with an interactive AI hair style consultation quiz that suggests cuts based on face shape and hair texture."
    },
    {
      id: "fitness",
      title: "🏋️ Personal Trainer Workout & Meal Macro Tracker",
      desc: "Client progress dashboard, dynamic macro calculator, and automated workout session logger.",
      prompt: "Generate a high-energy fitness trainer client hub with an interactive workout routine generator and real-time caloric macro calculator with weekly progress graphs."
    }
  ],
  frontier: [
    {
      id: "robotics",
      title: "🤖 Robot Fleet Telemetry & Joint Sensor Viewer",
      desc: "Real-time ROS2 joint velocity charts, battery thermals, and motor torque anomaly detector.",
      prompt: "Build an aerospace-grade robotics telemetry mission control dashboard showing 6-axis robotic arm joint positions, motor torque waveforms, battery thermals, and instant emergency stop overrides."
    },
    {
      id: "solar",
      title: "⚡ Microgrid Solar & Battery Dispatch System",
      desc: "Photovoltaic generation curve modeling, battery charge state, and dynamic time-of-use tariff optimizer.",
      prompt: "Create a clean-energy microgrid dispatch controller that visualizes solar array output, battery storage state-of-charge, and automated grid feed-in arbitrage under dynamic hourly electricity pricing."
    },
    {
      id: "lab",
      title: "🔬 Chemistry Mass Spec Peak Matcher",
      desc: "Tandem mass spectrometry peak centroid visualizer, neutral loss annotator, and molecular formula candidate ranker.",
      prompt: "Generate an interactive mass spectrometry MS2 spectrum analyzer displaying precursor m/z ion peaks, automated neutral loss annotations (H2O, CO2), and top chemical candidate matches."
    }
  ]
};

// Generated Sample Micro-Applications for Instant Live Sandboxing
const GENERATED_MICRO_APPS = {
  bakery: `<!DOCTYPE html>
<html>
<head>
  <style>
    body { background: #0f111a; color: #fff; font-family: -apple-system, sans-serif; padding: 25px; margin: 0; }
    .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #23283b; padding-bottom: 15px; }
    h1 { margin: 0; font-size: 1.5rem; color: #ffbe0b; }
    .status { background: #1a2238; color: #00d2ff; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; }
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
    .card { background: #161b2b; border: 1px solid #28304a; border-radius: 12px; padding: 18px; }
    .item-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #20263c; }
    .btn { background: #ffbe0b; color: #000; border: none; padding: 8px 16px; border-radius: 8px; font-weight: 700; cursor: pointer; }
    .assistant-box { margin-top: 15px; background: #0c0e17; padding: 12px; border-radius: 8px; border-left: 3px solid #ffbe0b; font-size: 0.9rem; }
  </style>
</head>
<body>
  <div class="header">
    <h1>🥐 Golden Crust Bakery AI</h1>
    <span class="status">⚡ Monad-Muse Micro-Agent Active</span>
  </div>
  <div class="grid">
    <div class="card">
      <h3>Today's Fresh Batches</h3>
      <div class="item-row"><span>Sourdough Boule</span><strong>18 remaining</strong></div>
      <div class="item-row"><span>Almond Croissant</span><strong>6 remaining (LOW)</strong></div>
      <div class="item-row"><span>Cardamom Bun</span><strong>24 remaining</strong></div>
      <button class="btn" style="margin-top: 15px;" onclick="bakeBatch()">+ Bake New Batch</button>
    </div>
    <div class="card">
      <h3>AI Proofing & Oven Advisor</h3>
      <div class="assistant-box" id="advice">
        "Humidity is 64% today in Denver. Recommended sourdough bulk fermentation: 4 hours 15 mins at 76°F. Pre-heat Deck Oven B to 450°F with steam at 4:30 AM."
      </div>
      <input type="text" id="userInput" placeholder="Ask baker assistant..." style="width: 100%; margin-top: 15px; padding: 10px; background: #080a11; border: 1px solid #28304a; color: #fff; border-radius: 6px; box-sizing: border-box;">
      <button class="btn" style="margin-top: 10px; background: #00d2ff;" onclick="askBaker()">Send Query</button>
    </div>
  </div>
  <script>
    function bakeBatch() { alert("Batch order logged! Sourdough prep scheduled for 5:00 AM."); }
    function askBaker() {
      const q = document.getElementById('userInput').value;
      if (!q) return;
      document.getElementById('advice').innerText = "Meta Muse Advisor: Analysis complete for '" + q + "'. Adjusted proofing formula by -15 minutes to preserve oven spring.";
      document.getElementById('userInput').value = '';
    }
  </script>
</body>
</html>`,

  robotics: `<!DOCTYPE html>
<html>
<head>
  <style>
    body { background: #06080e; color: #e2e8f0; font-family: monospace; padding: 25px; margin: 0; }
    .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 12px; }
    .hud { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-top: 20px; }
    .dial-card { background: #0f172a; border: 1px solid #334155; border-radius: 8px; padding: 15px; text-align: center; }
    .val { font-size: 1.8rem; font-weight: bold; color: #38bdf8; margin: 10px 0; }
    .alert-strip { margin-top: 20px; padding: 12px; background: rgba(34, 197, 94, 0.15); border: 1px solid #22c55e; border-radius: 6px; color: #22c55e; font-size: 0.9rem; }
    .estop-btn { background: #ef4444; color: #fff; border: none; padding: 12px 24px; border-radius: 6px; font-weight: bold; cursor: pointer; margin-top: 20px; width: 100%; }
  </style>
</head>
<body>
  <div class="header">
    <h2>🤖 ATLAS-VI 6-DOF ROBOT TELEMETRY</h2>
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
    function triggerEstop() { alert("E-STOP TRIGGERED! All magnetic brakes engaged."); }
  </script>
</body>
</html>`,

  generic: `<!DOCTYPE html>
<html>
<head>
  <style>
    body { background: #0a0d17; color: #f8fafc; font-family: -apple-system, sans-serif; padding: 30px; text-align: center; }
    .box { background: #131a2c; border: 1px solid #24304e; border-radius: 16px; padding: 30px; max-width: 600px; margin: 0 auto; box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
    h1 { color: #00d2ff; }
    p { color: #94a3b8; line-height: 1.6; }
    .badge { background: rgba(0, 245, 155, 0.15); color: #00f59b; padding: 6px 14px; border-radius: 20px; font-weight: 700; display: inline-block; margin-bottom: 15px; }
    .btn { background: linear-gradient(135deg, #00d2ff, #9d4edd); color: #fff; border: none; padding: 12px 24px; border-radius: 8px; font-weight: bold; cursor: pointer; }
  </style>
</head>
<body>
  <div class="box">
    <span class="badge">✦ MetaSticker Deployed App</span>
    <h1>Your Micro-Agent Is Live!</h1>
    <p>Synthesized by <strong>Meta Muse Code</strong> & fine-tuned with <strong>AxiomWeave Monad</strong>. This application is linked to physical NFC sticker voucher <code>MUSE-TARGET-8842-APEX</code>.</p>
    <button class="btn" onclick="alert('Micro-agent interaction verified!')">Test Interactive Agent</button>
  </div>
</body>
</html>`
};

document.addEventListener("DOMContentLoaded", () => {
  init3DCardTilt();
  initScratchOffCanvas();
  initThemeSwitcher();
  initCompilerAndDeploy();
});

// ==============================================================================
// 1. 3D Holographic Card Interactive Physics & Tilt
// ==============================================================================
function init3DCardTilt() {
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

    const rotateX = ((y - centerY) / centerY) * -16;
    const rotateY = ((x - centerX) / centerX) * 16;

    holoCard.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.03, 1.03, 1.03)`;

    if (foilReflection) {
      const posX = (x / rect.width) * 100;
      const posY = (y / rect.height) * 100;
      foilReflection.style.backgroundPosition = `${posX}% ${posY}%`;
      foilReflection.style.opacity = "0.9";
    }
  });

  cardWrapper.addEventListener("mouseleave", () => {
    holoCard.style.transform = "rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)";
    if (foilReflection) {
      foilReflection.style.opacity = "0.7";
      foilReflection.style.backgroundPosition = "50% 50%";
    }
  });
}

// ==============================================================================
// 2. Interactive Metallic Scratch-Off Canvas
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

  // Draw security foil watermark pattern
  ctx.fillStyle = "rgba(0, 0, 0, 0.15)";
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
    if (scratchedPixels / totalPixels > 0.4) {
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
      hint.innerText = "✓ Foil Redeemed: $5.00 Loaded";
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
      appendTerminalLine("[VOUCHER] Key 'MUSE-TARGET-8842-APEX' redeemed successfully.", "success");
      appendTerminalLine("[WALLET] $5.00 compute balance applied. Ready for synthesis.", "info");
    });
  }
}

// ==============================================================================
// 3. Theme Switcher & Preset Prompts
// ==============================================================================
function initThemeSwitcher() {
  const tabWorld = document.getElementById("tab-theme-1");
  const tabFrontier = document.getElementById("tab-theme-2");
  const presetsContainer = document.getElementById("presets-container");
  const promptInput = document.getElementById("prompt-input");

  function renderPresets(theme) {
    if (!presetsContainer) return;
    presetsContainer.innerHTML = "";
    const items = THEME_PRESETS[theme] || [];

    items.forEach((item, idx) => {
      const card = document.createElement("div");
      card.className = `preset-card ${idx === 0 ? "active" : ""}`;
      card.innerHTML = `
        <div class="preset-title">${item.title}</div>
        <div class="preset-desc">${item.desc}</div>
      `;
      card.addEventListener("click", () => {
        document.querySelectorAll(".preset-card").forEach(c => c.classList.remove("active"));
        card.classList.add("active");
        if (promptInput) {
          promptInput.value = item.prompt;
          promptInput.focus();
        }
      });
      presetsContainer.appendChild(card);
    });

    if (items.length > 0 && promptInput) {
      promptInput.value = items[0].prompt;
    }
  }

  if (tabWorld && tabFrontier) {
    tabWorld.addEventListener("click", () => {
      tabWorld.classList.add("active");
      tabFrontier.classList.remove("active");
      renderPresets("world");
    });

    tabFrontier.addEventListener("click", () => {
      tabFrontier.classList.add("active");
      tabWorld.classList.remove("active");
      renderPresets("frontier");
    });
  }

  renderPresets("world");
}

// ==============================================================================
// 4. Meta Muse Code Agent Compiler & Deployment Simulator
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
    
    await wait(800);
    appendTerminalLine("[MONAD] Applying Babai Lattice Low-Rank Quantization (rank=16, alpha=32)...", "info");
    appendTerminalLine("[TOPOS] Checking Sheaf Cohomology H¹(U, F) = 0 for HTML/CSS/JS interfaces...", "success");

    await wait(1000);
    appendTerminalLine("[MUSE CODE] Generating UI Components: responsive grid, state store, interactive handlers...", "");
    appendTerminalLine("[MUSE CODE] Compiling self-contained single-page micro-agent...", "info");

    await wait(1200);
    appendTerminalLine("[VERCEL] Packaging bundle into Edge Serverless Container...", "info");
    const appSlug = "metasticker-" + Math.random().toString(36).substring(2, 8);
    const liveUrl = `https://${appSlug}.vercel.app`;
    appendTerminalLine(`[DEPLOY] Deployed live to ${liveUrl} in 3.12 seconds!`, "success");
    appendTerminalLine("[NFC TAG] Minted ERC-8088 Physical Agent Protocol record for sticker.", "success");
    appendTerminalLine("==================================================", "info");

    if (statusBadge) {
      statusBadge.innerText = "DEPLOYED";
    }

    // Select suitable HTML preview based on prompt contents
    let htmlContent = GENERATED_MICRO_APPS.generic;
    const lower = prompt.toLowerCase();
    if (lower.includes("bakery") || lower.includes("croissant") || lower.includes("bread")) {
      htmlContent = GENERATED_MICRO_APPS.bakery;
    } else if (lower.includes("robot") || lower.includes("telemetry") || lower.includes("joint")) {
      htmlContent = GENERATED_MICRO_APPS.robotics;
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

function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
