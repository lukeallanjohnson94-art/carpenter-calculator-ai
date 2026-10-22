# Real Market Binary & Bundle Reverse-Engineering Autopsy (`JADX v1.5.1` + `Hermes HBC v96` + `Android SDK`)

- **Project**: `H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI`
- **Dedicated Standalone Repository**: `https://github.com/lukeallanjohnson94-art/carpenter-calculator-ai` (completely decoupled from `luke-justin-ai-bridge`)
- **Installed Reverse-Engineering & Emulator Toolchain**:
  - **JADX Decompiler (`v1.5.1`)**: `A:\APEX Storage\25_Skills_And_Repos\android-rea-tools\jadx\bin\jadx.bat`
  - **Java Runtime (`JDK 25.0.3 Hotspot`)**: `C:\Program Files\Eclipse Adoptium\jdk-25.0.3.9-hotspot\bin\java.exe`
  - **Official Google Android SDK (`adb.exe`, `sdkmanager.bat`, `avdmanager.bat`)**: `C:\Users\luke\AppData\Local\Android\Sdk`
  - **Responsively App (`v1.18.0`)**: `C:\Users\luke\AppData\Local\Programs\ResponsivelyApp\ResponsivelyApp.exe`
  - **BlueStacks 5 (`v5.22.166.1003`) Extracted Engine**: `C:\Users\luke\AppData\Local\Temp\BlueStacksExtracted\BlueStacks-Installer_5.22.166.1003_amd64_native.exe`
- **Downloaded Real Market APK / XAPK Vault**: `A:\APEX Storage\25_Skills_And_Repos\carpenter-calc-apks\`
  1. `tools.chippy.apk` (**Chippy Tools**, `13,140,636` bytes) $\rightarrow$ Decompiled to `rea-decompiled/ChippyTools_AU_probe/`
  2. `com.chippykit.app.apk` (**ChippyKit**, `55,971,006` bytes XAPK / `37,540,954` bytes inner APK) $\rightarrow$ Unpacked & extracted to `rea-decompiled/ChippyKit_App_Binary/` + `rea-decompiled/chippykit-live/`
  3. `com.digitalchemy.calculator.freefraction.apk` (**Fraction Calculator Plus #1**, `21,937,481` bytes XAPK) $\rightarrow$ Decompiled to `rea-decompiled/FractionCalcPlus_Digitalchemy/`

---

## 1. Binary Autopsy #1: `Chippy Tools` (`tools.chippy.apk` — `13.14 MB`)

### 1.1 Real Technology Stack (Seen in `classes.dex`)
- **UI Framework**: **100% Native Kotlin (`mv = {2, 4, 0}`) + Jetpack Compose** (`androidx.compose.runtime.internal.StabilityInferred`) with **Dagger Hilt** dependency injection (`Hilt_MainActivity.java`).
- **Networking & Backend**: `retrofit2` + `okhttp3` + Firebase Crashlytics + Firebase Cloud Messaging (`ChippyMessagingService.java`).
- **Billing & Paywall Engine**: **RevenueCat UI (`revenuecatui_purchase`, `revenuecatui_restore_purchases`)** + **Web Direct Purchase & Team-Seat Magic-Link Redemption** (`MainActivity$WebRedemption$1$1.java`, `subscription_source_web`, `subscription_source_team_seat`, `code_enter_title`).
  - *Why this matters*: Selling annual/lifetime plans and multi-chippy team seats on the web via Stripe and redeeming them in-app via a 6-digit code or magic link legally bypasses the 15–30% Apple/Google store commission on web-originated sales.
- **Paid Acquisition & Attribution**: Embedded **Meta App Events SDK (`com.facebook.appevents.iap.InAppPurchaseConstants`)** + **TikTok Business SDK (`com.tiktok.appevents.contents.TTContentsEventConstants`)** + custom `AttributionRetryWorker.java`.

### 1.2 Declarative Calculator Form Engine (`tools.chippy.models.*`)
Instead of cramming 50 tiny calculator buttons onto one screen, `Chippy Tools` drives every calculator screen from a declarative `CalculationComponentConfig` list built by `CalculationComponents.java`:
- `header(String title)`
- `inputField(String label, String hint, String defaultValue, String focusKey, boolean showError, k21 errorColor, String unit, MeasurementInputType inputType, boolean isLastField, FieldId fieldId)`
- `plusMinusControl(String label, String value)`
- `result(String label, String value, String unit)`
- **OS Keyboard Blocker + Custom Bottom Numpad**: `CalculationComponentKt$CalculationComponent$1$2$4$6$1$interceptStartInputMethod$1.java` intercepts Android's `startInputMethod` so the native OS keyboard never pops up; instead, it routes taps through `PadAction.java` (`PadAction.Digit(char)`, `PadAction.Backspace(int)`, `PadAction.Clear`) and `FractionAccuracy.java` (`1/2`, `1/4`, `1/8`, `1/16` default, `1/32`, `1/64`).

### 1.3 Every Calculator Module Discovered in `tools/chippy/R.java` (`572` String IDs)
Decompiling `R.java` revealed modules and sub-modes that are not listed on their public website:
1. **Raked Walls (`raked_walls`)**: Supports two distinct input modes:
   - `using_pitch`: `low_side_height`, `run_length`, `pitch`, `stud_spacing`, `bottom_plate_thickness`, `top_plate_thickness`
   - `using_two_heights`: `low_side_height`, `high_side_height`, `run_length`, `stud_spacing`
   - Outputs `stud_lengths`, `stud_measurements`, `top_plate_length`, plus **Hands-Free Voice Readout (`SpeakActionButtonKt.java`)**: `speak_centres_measurements` vs `speak_leading_measurements` with adjustable `speech_speed` (`slow`, `medium`, `fast`).
2. **Dumpy Level / Laser Level Reduced Level (`dumpy_level`)**:
   - Inputs: `benchmark_rl`, `benchmark_rl_on_ground` / `benchmark_rl_not_on_ground`, `staff_at_benchmark`, `staff_at_measure_level` $\rightarrow$ Outputs `measure_level_rl`.
3. **9-Mode Triangle Solver (`triangles`)**:
   - Prompts `which_values_of_the_triangle_do_you_have` across 9 explicit combinations (`triangle_title_base_lower`, `base_rise`, `base_upper`, `hypotenuse_base`, `hypotenuse_lower`, `hypotenuse_rise`, `hypotenuse_upper`, `rise_lower`, `rise_upper`).
4. **Equal & Baluster Spacing (`baluster_spacing`, `equal_spacings`)**:
   - Inputs: `baluster_width`, `max_spacing`, `target_spacing` $\rightarrow$ Outputs `balusters_needed`, `spacing_between_balusters`, `spacing_on_centres`.
5. **Stairs (`stairs`)**:
   - Inputs: `total_rise`, `rise_height`, `going` $\rightarrow$ Outputs `number_of_rises`, `number_of_going`, `stringer_length`, `stairs_measurement_ins_for_metric`.
6. **Check Square (`check_square`)** & **Running Measurements (`running_calculations`)**.
7. **Decking (`decking`)** & **Concrete / Asphalt / Gravel / Soil Tonnage (`concrete_holes`, `concrete_slab`, `asphalt`, `gravel`, `soil`)**:
   - Computes `requiredConcretePlusPercentage`, `required_asphalt_plus_buffer` (`asphalt_density`), `required_gravel_plus_buffer`, and `required_soil_plus_buffer`.

### 1.4 First-Launch Onboarding & Paywall Funnel (`PreferenceHelper$Key`)
- Tracks `appLaunchCount`, `completedCalculationCount`, `firstInstallMillis`, and `isPaywallShownOnFirstLaunched`.
- Runs a 4-step first-launch questionnaire (`questionnaire_units_*` $\rightarrow$ `questionnaire_pain_check_square` / `material_waste` / `mental_math` $\rightarrow$ `questionnaire_attribution_tiktok` / `instagram` $\rightarrow$ `questionnaire_testimonial_*`) before presenting 7 RevenueCat plan options (`weekly`, `monthly`, `two_month`, `three_month`, `six_month`, `annual`, `lifetime`).

---

## 2. Binary Autopsy #2: `ChippyKit` (`com.chippykit.app.apk` — `55.97 MB` XAPK)

### 2.1 Real Technology Stack (Seen in `assets/app.config` & `assets/index.android.bundle`)
- **Framework**: **Expo SDK 54.0.0 + React Native New Architecture (`newArchEnabled: true`, Bridgeless Mode) + `expo-router` + Hermes Bytecode v96 (`0xc61fbc03`, `2.86 MB` bundle)**.
- **Color & Typography Tokens (`chippykit.com.au` + `app.config`)**:
  - Background: `#0F1115` (`--black`), Card Panel: `#171A20` (`--panel`), Input Well: `#1E2229` (`--panel-2`), Border: `#2A2F38` (`--line`), Primary Accent: `#FF5C00` (`--orange`).
  - Fonts: `Archivo Black` (headings/numbers) + `Archivo` (UI labels).
- **Billing**: **RevenueCat (`goog_GfpxWFogsjDPCWIAztHfeGpxvqi`)** in-app + **Stripe Direct Checkout (`$79 AUD once-off Founders Lifetime` at `buy.stripe.com/5kQ3cx97XeRf8FV8e208g00`)** linked by account email.

### 2.2 Decompiled `expo-router` Screen Map (`assets/index.android.bundle`)
- `./_layout.tsx` & `./(tabs)/_layout.tsx` (5-Tab Bottom Bar: `Home`, `Calc`, `Refs`, `Jobs`, `Profile`)
- `./(tabs)/index.tsx` — Home / Quick Actions
- `./(tabs)/calculators.tsx` — Decking (`decking-result-boards`, `decking-result-lm`, screws, wastage), Sub-floor Stumps/Bearers/Joists (`subfloorSpans`, `stumpSpacing`, `bearerSpacing`, `joistSpan`), Stairs (`Riser/going`, `stringer length` + 2 mark-out methods), Rafters, Studs, Concrete Volume, Square Check
- `./(tabs)/references.tsx` — 5 Offline Australian Standard Reference Cards:
  1. **Installation Heights (`AS 1428.1` DDA)**
  2. **Floor Joist Spans (`AS 1684` / Wesbeam `MGP10` single-span tables + `1.5 kN` point load)**
  3. **Screw & Bolt Sizing**
  4. **Concrete Curing**
  5. **Safe Load Limits (`AS/NZS 1170`)**
- `./(tabs)/jobs.tsx`, `./job/new.tsx`, `./job/preview.tsx`, `./templates.tsx` — 3-Minute Site Quoting & 1-Tap Tax Invoice Generator (`ABN`, `10% GST`, bank details, quick-tap day chips `Mon 27 / Tue 28 / Wed 29` for labour/material entry, and PDF export).
- `./(tabs)/profile.tsx`, `./login.tsx`, `./signup.tsx`, `./paywall.tsx`, `./billing/success.tsx`.

---

## 3. Binary Autopsy #3: `Fraction Calculator Plus #1` (`com.digitalchemy.calculator.freefraction.apk` — `21.94 MB`)

### 3.1 Real Technology Stack & Monetization Engine (Seen in `com.digitalchemy.*`)
- **Multi-Network Ad Mediation Stack**:
  - `com.digitalchemy.foundation.advertising.admob` (`AdMobAppOpenAdConfiguration`, `AdMobInterstitialAdConfiguration`, `AdMobNativeAdConfiguration`, `BannerAdUnitInfo`)
  - `com.digitalchemy.foundation.advertising.fyber` (DT Exchange / Fyber)
  - `com.digitalchemy.foundation.advertising.inmobi` (InMobi)
  - `com.digitalchemy.foundation.advertising.admob.adapter.facebook` (Meta Audience Network)
  - `com.digitalchemy.foundation.advertising.crosspromo` (`CrossPromoAppOpenApp`, `CrossPromoBannerApp`, `BlackFridayBannerDrawer`)
- **Proprietary 5-Star Rating Gate (`EmpowerRatingAlgorithmParams.java`)**:
  - Uses `EmpowerRatingAlgorithmParams(sessionsAfter5Stars=30, daysAfter5Stars=30, sessionsAfter4Stars=30, daysAfter4Stars=30)` with an internal satisfaction pre-screen (`RatingLevelsConfig.java`) so only happy repeat users are routed to the Google Play / App Store review prompt.
- **Follow-Up Offer & Dynamic Paywall (`FollowupOffer.java`, `PurchaseConfig.java`, `SubscriptionConfig.java`)**:
  - When a user closes the primary subscription or ad-removal sheet, `FollowupOffer.java` triggers a discounted fallback offer.
- **Camera Photo-Math Pipeline (`com.digitalchemy.photocalc.*`)**:
  - Uses `MathPixRequest(src, formats=["text", "data", "html"])` for camera OCR of printed/handwritten fractions and `WolframRequest(input, mag, width, output="JSON", format="image,plaintext")` to render step-by-step solution pods (`ItemPodTitleBinding`, `ItemSubpodBinding`).
