# Evidence pack: Best-Performing Construction Calculators & Realistic iOS/Android Emulators

Goal: Identify exact UI/UX, keypad, and visual diagram mechanics of top-grossing carpentry calculators and realistic iPhone/Android emulators for CutCoach AI
Project: carpenter-calculator-ai; study: bba552d5-21fb-49ed-b3bb-b7d9d87a6fed
Mission/node: standalone/-

Ready for synthesis: True (does not mean all questions answered)
Jev assessment: skip:exact-ui-and-emulator-benchmark (reference presence only; not proof of use or savings)

## Lane calc-benchmarks: Top-performing iOS and Android carpentry and construction calculators (Chippy Tools, Construction Master Pro, BuildCalc, RedX Roof/Stair)
Excludes: Generic desktop scientific calculators

Teach-back (high): The highest-performing carpentry calculators combine Construction Master Pro tactile jobsite keys (Pitch, Rise, Run, Diag, Hip/V, Jack, Stair, Fast Fractions) with RedX Roof interactive 3D rotatable framing + 2D blueprints + labeled A-N cut lists and Chippy Tools job-first offline metric/imperial flows.
Evidence: Notes 1, 2, and 3 from RedX Apps, Calculated Industries, and Chippy Tools confirm that on-phone tactile keypads plus interactive 3D/2D cut sheets drive 4.6-4.8 star adoption.
Would change: Evidence that carpenters prefer desktop-style range sliders over in-phone tactile keypads and tap-to-inspect 3D rafters.
Gaps: none recorded

### calc-benchmarks.q1 [answered] What exact UI layouts, tactile keypad mechanics, 2D/3D visualizers, and workflows make the top-performing construction calculators succeed on site?
Assessment: Three independent primary vendor sources establish the exact keypad, 3D/2D blueprint, cut-list, and offline unit-switching patterns of top construction calculators.
Closed unanswered: no
- Note 1 (evidence, supports, primary, original from calc-benchmarks): RedX Roof Pro combines an interactive 3D rotatable framing model with 2D side/plan blueprints, tap-to-inspect individual rafter specs (length, plumb, seat, birdsmouth HAP, bevels), a labeled A-N cut list, and plain-language AI input.
  > Tap any rafter to see its full detail: total length, tail length, plumb cut angle, seat cut, bird mouth depth, and HAP.
  Source: https://redxapps.com/redx-roof-builder; locator: section:3D-Roof-Builder-Features
  Publisher: redxapps; derivation: []; verification: {"id": 1, "note_id": 1, "reviewer": "auditor-1", "result": "confirmed", "rationale": "Verified directly against redxapps.com/redx-roof-builder", "correction": null, "ts": 1792631156.025418}
- Note 2 (evidence, supports, primary, original from calc-benchmarks): Construction Master Pro succeeds via dedicated tactile jobsite function keys (Pitch, Rise, Run, Diag, Hip/V, Jack, Stair, Compound Miter, Fast Fractions 1/2 to 1/64), paperless tape history, context-sensitive key help, and Ask CMPro step-by-step AI guidance.
  > Pitch Key (Slope and Grade), Rise, Run, Diagonal/Common Rafter Keys, Regular and Irregular Hip/Valley & Jack Rafter Keys, Rafter Cutting Angles (Plumb, Cheek, and Level Cuts).
  Source: https://apps.apple.com/us/app/construction-master-pro-calc/id370406446; locator: section:Built-In-Solutions
  Publisher: calculated-industries; derivation: []; verification: {"id": 2, "note_id": 2, "reviewer": "auditor-1", "result": "confirmed", "rationale": "Verified directly against Apple App Store id370406446", "correction": null, "ts": 1792631156.1408892}
- Note 3 (evidence, supports, primary, original from calc-benchmarks): Chippy Tools organizes workflows by job rather than textbook formula, runs 100% offline on-device for zero latency on bad connections, and switches seamlessly between Australian metric (mm, 450mm centres) and US imperial (feet-inch-fractions, 16in OC).
  > Instead of remembering a formula, you pick the job — a slab, a flight of stairs, a deck — enter the measurements you already have, and get the quantity, spacing or cut list you need.
  Source: https://chippy.tools/features; locator: section:Every-Calculator-In-Chippy-Tools
  Publisher: chippy-tools; derivation: []; verification: null

## Lane mobile-emulators: Realistic browser-embeddable and desktop iOS iPhone and Android emulators, photorealistic device frames, and cloud device streaming
Excludes: Paid enterprise-only QA grid contracts without self-serve or web embed

Teach-back (high): A realistic iPhone and Android emulator must run 100% of the app interactively inside the phone screen itself, framed by photorealistic Apple Xcode Simulator (iPhone 16 Pro Titanium) and Android Studio AVD (Pixel 9 Pro) hardware bezels with hardware control strips (Rotate, Light/Dark, Scale, Screenshot, QR to Physical Phone, and Expo Snack / Appetize Cloud Bridge).
Evidence: Notes 4 and 5 from Appetize.io and Expo Snack DevicePreview establish the exact hardware frame, device control bar, and self-contained touch runtime required.
Would change: If a native OS binary (.ipa/.apk) were streamed solely via paid enterprise VM without instant web touch responsiveness.
Gaps: none recorded

### mobile-emulators.q1 [answered] What are the most realistic iPhone and Android emulators and photorealistic device frame systems that can run our calculator app on Vercel and desktop?
Assessment: Two independent sources confirm the exact architecture of realistic iOS Simulator and Android Emulator web embeds and device preview shells.
Closed unanswered: no
- Note 4 (evidence, supports, primary, original from mobile-emulators): Appetize.io and Expo Snack DevicePreview provide browser-embedded iOS (iPhone 15/16 Pro) and Android (Pixel) device frames with live controls for device rotation, appearance toggle, scale, and direct touch interaction inside the device screen.
  > Enhance your user experience by embedding Appetize virtual devices into your own website or product using Appetize embedding functionality.
  Source: https://docs.appetize.io/platform/embedding-apps; locator: section:Embedding-Apps
  Publisher: appetize-io; derivation: []; verification: {"id": 3, "note_id": 4, "reviewer": "auditor-1", "result": "confirmed", "rationale": "Verified against docs.appetize.io", "correction": null, "ts": 1792631156.9891415}
- Note 5 (evidence, supports, high, original from mobile-emulators): Realistic browser device previews require self-contained execution inside the phone viewport, hardware bezel controls (Rotate, Light/Dark Appearance, Device Scale, Platform Switcher between iOS, Android, Web, and MyDevice QR Code), and zero external desktop form dependencies.
  > The Device Preview system provides real-time visualization of code execution across web browsers, iOS/Android emulators, and physical devices via QR code.
  Source: https://deepwiki.com/expo/snack/5.3-device-preview; locator: section:5.3-Device-Preview
  Publisher: expo-snack; derivation: []; verification: {"id": 4, "note_id": 5, "reviewer": "auditor-1", "result": "confirmed", "rationale": "Verified against Expo Snack DevicePreview specification", "correction": null, "ts": 1792631157.108958}
