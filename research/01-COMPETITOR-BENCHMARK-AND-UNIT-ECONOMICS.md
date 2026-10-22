# Competitor Benchmark, Market Gap Analysis & `$2.00–$3.00/wk` Unit-Economics Proof (`v1.0`)

- **Project**: AI Carpenter's Calculator & Visual Cut Coach (`iOS` + `Android`)
- **Workspace**: `H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI`
- **Mission ID**: `research-business-plan-architect-uni-b51c9c62c9`
- **Verification Script**: [`src/carpentry_math_core.py`](../src/carpentry_math_core.py)

---

## 1. Executive Findings Table (`[R-001]` Format)

| Finding | What it means for Luke | Source |
|---|---|---|
| **1. Incumbent apps (`Construction Master Pro`, `BuildCalc`, `Rafter Tools+`) use 1990s physical pocket-calculator button grids with zero 2D/3D cut-line visualization** | Chippies and apprentices don't fail at pressing buttons — they fail at visualizing *which side of the pencil line to cut*, how the speed square sits against the timber edge, and which way to tilt the drop-saw bevel vs mitre table on unequal-pitch ("bastard") roofs. | Subagent Market Audit (`76aed3a3`) & App Store Review Synthesis (2026-10-21) |
| **2. Zero existing carpentry apps combine Spiral/Helical Stair Stringers + Kerf-Bending Slot Spacing + Instant Scrap-Plywood Jig Blueprints** | Every site carpenter eventually hits a curved wall/archway (kerf-bending), an awkward winder/spiral stair, or a repetitive trenching/taper cut where a 5-minute scrap-plywood router/saw jig saves 2 hours. Owning all three makes this a daily site companion, not just a roof calculator. | [`src/carpentry_math_core.py`](../src/carpentry_math_core.py) & `TimberCraft` `WS-03` (`bddc3e3b`) |
| **3. Dusty-handed text entry on sunny sites is the #1 UX complaint on mobile construction apps** | One-thumb hold-to-talk speech recognition (`SFSpeechRecognizer` / quantized on-device `Whisper-tiny.en`) + High-Contrast Daylight Linen (`#F5F1EA`) & Warm Obsidian (`#131210`) modes solve outdoor glare and gloved operation at `$0.00` API cost. | `UI/UX Encyclopaedia` (`SH-M02`, `SH-M05`, `CT-01..12`) |
| **4. Hybrid On-Device Math/SVG/Voice + Flash-Tier Vision locks in `94.85%–99.65%` net margin after API costs at `$2.99/week` AUD** | By running 100% of math, 2D/3D parametric geometry, voice slot-filling, and 500+ jig blueprints deterministically on-device (`$0.00`), and routing only live camera photo markups through `Gemini 2.5 Flash` (`$0.00084 AUD/call`) with a 100-photo/wk fair-use ceiling, **0% of users can ever cost more than `$0.13 AUD/week` in API tokens**. | Deterministic Margin Simulation ([`src/carpentry_math_core.py`](../src/carpentry_math_core.py)) |

---

## 2. Deep Competitor Benchmark Matrix (6 Incumbents Audited)

| Competitor App | Pricing & Monetization | Core Strengths | Critical Jobsite Failures (Why Chippies Hate Them) | Our Unfair Advantage |
|---|---|---|---|---|
| **1. Construction Master Pro** *(Calculated Industries)* | `$30–$50 USD/yr` subscription (formerly `$34.99` one-off) | Industry-standard feet-inch-fraction math; trusted by older North American builders. | **Skinned 1995 plastic keypad** (`Conv`, `Pitch`, `Rise`, `Run`, `Diag`); zero 3D joint preview; zero kerf-bending; zero spiral stair stringer development; furious 1-star reviews over forced annual paywall with zero new features. | **Interactive 3D/2D Cut Stage + Voice Slot-Filling**: Say the span and pitch out loud, see the birdsmouth and drop-saw bevel/mitre gauges rendered live on the timber. |
| **2. BuildCalc** | `$24.99–$29.99 USD` one-off | Strong hip/valley/jack lists and baluster layouts. | Pure text-and-button matrix; intimidating 40-button layout; zero visual saw-blade setup; zero AU `AS 1684` / `NCC` compliance badges; zero photo markup. | **Visual Speed-Square & Saw-Gauge Overlay** + instant AU `AS 1684` (`D/3` birdsmouth limit) & `NCC` (`2R+G` stair slope) live pass/fail checks. |
| **3. Chippy Tools** *(AU)* | Freemium + Weekly/Annual Pro subscription | Clean modern mobile list UI; metric AU focus; good basic spacing, raked walls, and 3-4-5 squaring. | **No 3D/2D exploded timber joint models**, no unequal-pitch ("bastard") compound drop-saw gauge visualizer, no kerf-bending slot calculator, no voice input, no photo-to-cut markup, no custom shop-jig generator. | **Direct Category Upgrade for Every AU/UK/US Chippy**: Keeps metric/imperial speed while adding visual 3D cut coaching, voice input, kerf-bending, spiral stairs, and scrap-offcut jig blueprints. |
| **4. Stairmaker / Basic Stair Apps** | `$4.99–$14.99` or ad-supported web wrappers | Simple straight-flight rise/going division. | Fails on **3D Spiral/Helical stringer unwrap ($L = \sqrt{(R\theta)^2 + H^2}$)**, kite winders, router housing trench offsets, and NCC `125 mm` sphere baluster spacing. | **Full Straight, Winder & 3D Helical Stair Engine** with 1:1 stringer router template and tread walk-line compliance. |
| **5. Rafter Tools+** | `$9.99 USD` upfront | Handles complex polygon roofs and bastard hips mathematically. | Dense engineering tables with archaic UI; apprentices cannot translate the output numbers onto a Makita/DeWalt mitre saw turntable and bevel scale. | **Live Drop-Saw Turntable & Bevel Gauge Graphic**: Shows exact `Mitre M = 42.19°` and `Bevel B = 17.39°` directly on an interactive saw dial. |
| **6. Handyman Calculator** | Free w/ heavy banner ads or `$2.99–$9.99` | Huge list of 100+ mini calculators (concrete, paint, mulch). | Jack-of-all-trades bloatware; zero carpentry joinery precision, zero birdsmouth/compound bevel geometry. | **Pure Trade-Grade Carpentry & Joinery Precision Instrument** built by a real builder/joiner (`LUX` / `DISTRICT` / `TimberCraft` DNA). |

---

## 3. Rigorous Weekly Subscription Unit-Economics & API Margin Model (`$2.00–$3.00/Week`)

### 3.1 The 4-Layer Zero-Leakage Cost Architecture
1. **Layer 1 — Deterministic On-Device Rust / TypeScript Parametric Math & 2D/3D Geometry (`$0.0000 / call`)**:
   - 100% of trigonometry, rafters, bastard hips, stairs, helical stringers, kerf-bending slot tables, and interactive 2D SVG / 3D WebGL timber diagrams execute locally on the user's iPhone/Android CPU/GPU.
2. **Layer 2 — On-Device Trade Speech-to-Parameters (`$0.0000 / call`)**:
   - Uses Apple `SFSpeechRecognizer` (`requiresOnDeviceRecognition = true`) / Android On-Device Speech + quantized `Whisper-tiny.en` (`~39 MB` model) with a deterministic regex/grammar slot extractor (`span`, `pitch`, `ridge`, `eaves`, `kerf`, `radius`, `timber_thickness`). Works 100% offline in concrete basements and rural sites at **`$0.00` cloud cost**.
3. **Layer 3 — Pre-Computed 500+ Parametric Jig & Cut-Walkthrough Vault (`$0.00002 / call`)**:
   - All standard shop jigs (circular-saw track guide, stair stringer router housing template, kerf-indexing pin sled, table-saw taper jig, 3D-printable speed-square stop) are parameterized JSON/SVG templates bundled in the app binary and cached on Cloudflare R2 (`$0.00` egress).
4. **Layer 4 — Flash-Tier Vision API + Hard Weekly Fair-Use Cap (`$0.00084 AUD / live photo call`)**:
   - Only when a Pro subscriber snaps a live site photo for **AI Photo-to-Cut Markup** or asks a bespoke freeform question outside the deterministic templates does the app hit `Gemini 2.5 Flash` (with context caching enabled).
   - **Hard Circuit-Breaker Guardrail**: Each `$2.99/wk` Pro pass includes `100` high-speed AI Vision Photo Markups + `100` custom AI Coach chats per week (more than `14` site photo markups every single day). Even if a user maxes out 100% of that hard ceiling, their total weekly API cost is **`$0.131 AUD`**, guaranteeing a **minimum `94.85%` net margin** and a **0.00% mathematical probability of any user ever costing more than their subscription**.

### 3.2 Cohort-by-Cohort Weekly Margin Table (`$2.99/wk AUD` & `$2.00/wk AUD` Floor)

| User Cohort Profile | Gross Weekly Sub (`AUD`) | Net After Apple/Google `15%` Cut (`AUD`) | Weekly On-Device Calcs / Voice / 3D (`$0.00`) | Weekly Live AI Photo + Chat Calls | Total Weekly API Cost (`AUD`) | Net Profit Per User / Week (`AUD`) | Net Margin After API (`%`) |
|---|---:|---:|---:|---:|---:|---:|---:|
| **1. Average Site Chippy (`$2.99/wk`)** | `$2.99` | `$2.542` | `35` calcs / `15` voice / `8` jigs | `6` photos + `8` chats | **`$0.0088`** | **`+$2.533 / wk`** | **`99.65%`** |
| **2. Heavy Leading Hand (`$2.99/wk`)** | `$2.99` | `$2.542` | `120` calcs / `60` voice / `25` jigs | `25` photos + `30` chats | **`$0.0350`** | **`+$2.506 / wk`** | **`98.62%`** |
| **3. Maxed-Out Fair-Use Cap (`$2.99/wk`)** | `$2.99` | `$2.542` | `500` calcs / `250` voice / `100` jigs | `100` photos + `100` chats *(Cap)* | **`$0.1310`** | **`+$2.411 / wk`** | **`94.85%`** |
| **4. Maxed-Out Fair-Use Cap (`$2.00/wk` Floor)** | `$2.00` | `$1.700` | `500` calcs / `250` voice / `100` jigs | `100` photos + `100` chats *(Cap)* | **`$0.1310`** | **`+$1.569 / wk`** | **`92.29%`** |

### 3.3 Revenue Scaling Projections (`$2.99/wk` Pro Pass + `$49/yr` Annual Option)
- **1,000 Active Pro Chippies**: `~$132,180 AUD/year` net revenue after App Store fees $\rightarrow$ **`~$130,360 AUD/year` net profit (`98.6%` margin)**.
- **5,000 Active Pro Chippies**: `~$660,900 AUD/year` net revenue after App Store fees $\rightarrow$ **`~$651,800 AUD/year` net profit**.
- **25,000 Active Pro Chippies (AU + UK + US + NZ + CA English Trade Market)**: `~$3.30M AUD/year` net profit.
