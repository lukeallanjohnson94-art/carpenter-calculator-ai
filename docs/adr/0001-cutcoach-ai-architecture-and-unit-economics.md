# ADR 0001: CutCoach AI Hybrid On-Device Deterministic Engine, Dual Metric/Imperial Code Switcher & $2.99/wk Unit-Economics Architecture

- **Status**: Accepted (`2026-10-21`, locked via `/grill-me` in `msg-2b6e50d70287`)
- **Deciders**: Luke Allan Johnson (`INSYGHT DIGITAL` / `LUX Pty Ltd`)

## Context
Incumbent carpentry calculator apps (`Construction Master Pro`, `BuildCalc`, `Chippy Tools`, `Rafter Tools+`) rely on 1990s plastic-keypad layouts without interactive 2D/3D joint previews, unequal-pitch ("bastard") drop-saw bevel dials, 3D helical stair stringer unwrap, kerf-bending slot schedules, hands-free voice entry, or custom shop-jig blueprints. However, offering a `$2.99/week AUD` subscription with AI features risks margin erosion if standard calculations, voice commands, or photo markups invoke expensive cloud LLMs without bounds.

## Decision
1. **Zero-LLM Deterministic Math & 2D/3D Geometry Engine (`$0.00/calc`)**: All `AS 1684` / `IRC` rafters, bastard hips, `NCC` stairs, 3D helical stringers, kerf-bending schedules, and framing trig run 100% locally on the device CPU/GPU via a shared deterministic math core (`src/carpentry_math_core.py` / TypeScript / Rust).
2. **Day-One Dual Metric (`mm`) & Imperial (`Feet-Inch-1/16"`) Code Switcher**: Ship `AU/NZ (AS 1684 + NCC)`, `US/CA (IRC Feet-Inch-1/16")`, and `UK (BS Metric)` profiles from v1.0.
3. **Hybrid Deterministic Photo Overlay + Dual Jig Outputs (`Scrap-Ply Plan` + `.STL` 3D Print)**: Combine 2-point edge tap + spoken/measured reference dimensions with deterministic SVG cut/waste overlays and generate both scrap-formply workshop plans and downloadable `.STL` 3D-printable stops/gauges.
4. **"Blue-Balls" Paywall & Hard API Circuit-Breaker (`94.85%–99.65%` Net Margin)**: Free tier provides unlimited trig, basic lengths, and full 3D visual preview; `$2.99/wk` (`$49/yr`) Pro Pass unlocks exact saw mitre/bevel angles, birdsmouth millimetres, helical stringer unwrap, kerf tables, photo markup, and jig blueprints, with live `Gemini 2.5 Flash` vision calls capped at `100/wk` (`<=$0.131 AUD/wk`).

## Consequences
- **Positive**: `0.00%` probability of any user exceeding their weekly subscription margin; works 100% offline in basements and rural sites; addresses both AU metric and US imperial markets from one codebase.
- **Trade-off**: Requires maintaining deterministic parametric SVG/STL templates for all jig families rather than relying on unconstrained text generation.
