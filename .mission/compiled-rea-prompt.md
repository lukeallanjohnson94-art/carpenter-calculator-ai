<!-- outcome-engine compiled prompt | profile=generic v0 | model=gemini | sha256=0ff4f1946651a07d3cac3d40e4d87db45ff78526a4e34f9182308615ead4d0b6 | bullets= -->
<role_and_context>
Purpose: Generic outcome
Audience: Luke Allan Johnson (Founder & Director, INSYGHT DIGITAL / ONSYGHT CONSTRUCTION & CONCEPTS)
</role_and_context>

<documents>
- H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI\research\02-VERIFIED-STORE-STATS-AND-EMULATORS.md
- A:\APEX Storage\25_Skills_And_Repos\cold-skills\chippykit-carpentry-calculators\SKILL.md
- H:\My Drive\APEX\03_Harness\skills-registry\reverse-engineer-anything\SKILL.md
</documents>

<outcome_spec>
{
  "intent": "Install and operate genuine OS-level mobile emulators (Google Android SDK Emulator + ADB + BlueStacks 5 + ResponsivelyApp), download and decompile actual market carpentry/construction calculator binaries (.apk/.xapk and live production web bundles like @chippykit) using JADX + /reverse-engineer-anything + /website-api-review, isolate the project in its own dedicated GitHub/Vercel repository (carpenter-calculator-ai) completely separate from luke-justin-ai-bridge, and quarantine any premature CutCoach UI builds until full reverse-engineering of both the emulators and the market calculators is complete and approved.",
  "deliverable_type": "Decompiled market calculator evidence vault (rea-decompiled/), installed OS-level emulator & ADB toolchain, standalone repository (lukeallanjohnson94-art/carpenter-calculator-ai), and prompt-engineered /mission plan.",
  "format": "Decompiled Java/Kotlin/JS/manifest artifacts in rea-decompiled/, verified JSON summary in rea-decompiled/rea_setup_and_decompile_summary.json, compiled prompt in .mission/compiled-rea-prompt.md, and clean-room REA dossier in docs/05-REAL-BINARY-AND-BUNDLE-AUTOPSY.md",
  "must": [
    "Strip all cutcoach files out of luke-justin-ai-bridge and host CARPENTER-CALCULATOR-AI in its own dedicated repository (https://github.com/lukeallanjohnson94-art/carpenter-calculator-ai)",
    "Quarantine and stop opening the premature HTML/WebView2 CutCoach desktop mockup (CutCoachAI.exe) until all emulators and market calculators have been genuinely reverse-engineered",
    "Download and install actual emulators and Android SDK tooling (platform-tools adb.exe, cmdline-tools sdkmanager/avdmanager, emulator.exe, BlueStacks 5, ResponsivelyApp) so real Play Store / APK calculators can be loaded and tested",
    "Download actual market calculator packages (Fraction Calculator Plus, Chippy Tools AU, Handyman Calculator, DEWALT Mobile Pro, RedX Roof/Stair, and @chippykit https://chippykit.com production bundle) and decompile/dissect them using JADX + /reverse-engineer-anything + reverse-api-engineer",
    "Use /mission, /plan, /deep-research, and outcome_engine.py (Prompt Engineer compiler) to govern the reverse-engineering and build pipeline"
  ],
  "must_not": [
    "MUST NOT recycle or pollute luke-justin-ai-bridge with calculator files or URLs",
    "MUST NOT pop up CutCoachAI.exe or spam Launch Native Desktop Application links while in the Emulator & Calculator Reverse-Engineering phase",
    "MUST NOT pretend a static/HTML drawing of an iPhone bezel is an OS-level iPhone or Android emulator"
  ],
  "constraints": [
    "Zero console popups on Windows (CREATE_NO_WINDOW)",
    "Strict Clean-Room separation between decompiled evidence (rea-decompiled/) and clean mathematical/architectural specifications (docs/)"
  ],
  "assumed": [
    "Android APKs/XAPKs can be decompiled locally on Windows x64 via JADX + Java 25 and run inside Google Android Emulator / BlueStacks 5; iOS App Store binaries (.ipa) require macOS/Xcode Simulator or Appetize.io cloud iOS runner for native Mach-O execution while their shared React Native / Flutter / Web bundles and REST APIs can be dissected on Windows."
  ]
}
</outcome_spec>

<tools_and_sources>
- H:\My Drive\APEX\03_Harness\skills-registry\mission\scripts\mission.py
- H:\My Drive\APEX\03_Harness\skills-registry\mission\scripts\outcome_engine.py
- H:\My Drive\APEX\03_Harness\skills-registry\reverse-engineer-anything\scripts\rea_brain.py
- H:\My Drive\APEX\03_Harness\skills-registry\reverse-engineer-anything\scripts\rea_apex_bridge.py
- H:\My Drive\APEX\03_Harness\skills-registry\reverse-api-engineer\scripts\rae_harness.py
- A:\APEX Storage\25_Skills_And_Repos\android-rea-tools\jadx\bin\jadx.bat
- C:\Users\luke\AppData\Local\Android\Sdk\platform-tools\adb.exe
</tools_and_sources>

<boundaries>
- Owned workspace: H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI and A:\APEX Storage\25_Skills_And_Repos\carpenter-calc-apks
- Prohibited workspace: C:\Users\luke\luke-justin-ai-bridge (except for removing previously placed cutcoach files)
- Main monitor (\\.\DISPLAY2) is 100% off-limits for window launches
- MUST NOT: MUST NOT recycle or pollute luke-justin-ai-bridge with calculator files or URLs
- MUST NOT: MUST NOT pop up CutCoachAI.exe or spam Launch Native Desktop Application links while in the Emulator & Calculator Reverse-Engineering phase
- MUST NOT: MUST NOT pretend a static/HTML drawing of an iPhone bezel is an OS-level iPhone or Android emulator
</boundaries>

<acceptance_checks>
- [spec] TRUE/FALSE: luke-justin-ai-bridge has zero cutcoach files remaining in api/ or public/
- [spec] TRUE/FALSE: Dedicated standalone GitHub repository https://github.com/lukeallanjohnson94-art/carpenter-calculator-ai exists and is configured as origin
- [spec] TRUE/FALSE: CutCoachAI.exe is stopped and quarantined so it never pops up unasked
- [spec] TRUE/FALSE: Real Android SDK (adb.exe, sdkmanager.bat, avdmanager.bat) and JADX v1.5.1 decompiler are installed on disk
- [spec] TRUE/FALSE: Actual market calculator binaries/bundles (including @chippykit https://chippykit.com and Android .apk/.xapk archives) are downloaded to disk and decompiled into rea-decompiled/
- [spec] TRUE/FALSE: Outcome Spec is validated and compiled via outcome_engine.py and steered into the active Mission
</acceptance_checks>

<model_rules>
- State success criteria and output format before working; treat the acceptance checks as the definition of done.
- Keep inferred requirements visibly labelled as assumptions.
- Put long source material before instructions; restate the task last.
- Distinguish verified facts (cited) from inference.
- Restate the task after long context and keep data inside tags.
</model_rules>

<task>
Install and operate genuine OS-level mobile emulators (Google Android SDK Emulator + ADB + BlueStacks 5 + ResponsivelyApp), download and decompile actual market carpentry/construction calculator binaries (.apk/.xapk and live production web bundles like @chippykit) using JADX + /reverse-engineer-anything + /website-api-review, isolate the project in its own dedicated GitHub/Vercel repository (carpenter-calculator-ai) completely separate from luke-justin-ai-bridge, and quarantine any premature CutCoach UI builds until full reverse-engineering of both the emulators and the market calculators is complete and approved.
Deliver as: Decompiled market calculator evidence vault (rea-decompiled/), installed OS-level emulator & ADB toolchain, standalone repository (lukeallanjohnson94-art/carpenter-calculator-ai), and prompt-engineered /mission plan. — Decompiled Java/Kotlin/JS/manifest artifacts in rea-decompiled/, verified JSON summary in rea-decompiled/rea_setup_and_decompile_summary.json, compiled prompt in .mission/compiled-rea-prompt.md, and clean-room REA dossier in docs/05-REAL-BINARY-AND-BUNDLE-AUTOPSY.md
Before finishing, check the output once against every acceptance check.
</task>
