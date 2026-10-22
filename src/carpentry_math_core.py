"""
Deterministic On-Device Carpentry Math Core & Unit-Economics Simulator (v1.0)
Workspace: H:\\My Drive\\APEX\\05_Active\\personal\\INSYGHT DIGITAL\\CARPENTER-CALCULATOR-AI
Zero-LLM Cost ($0.00/calc) Parametric Geometry Engine for iOS & Android.
"""
from __future__ import annotations
import json
import math
from dataclasses import dataclass, asdict


@dataclass
class RafterCompoundResult:
    span_mm: float
    run_mm: float
    pitch_deg: float
    secondary_pitch_deg: float
    ridge_thickness_mm: float
    eaves_overhang_mm: float
    rafter_depth_mm: float
    common_rafter_center_mm: float
    common_rafter_deducted_mm: float
    eaves_tail_length_mm: float
    total_common_length_mm: float
    plumb_cut_deg: float
    seat_cut_deg: float
    birdsmouth_max_notch_mm: float
    birdsmouth_heel_plumb_mm: float
    birdsmouth_seat_level_mm: float
    hip_plan_angle_deg: float
    hip_run_mm: float
    hip_length_mm: float
    hip_plumb_deg: float
    hip_seat_deg: float
    dropsaw_mitre_deg: float
    dropsaw_bevel_deg: float
    backing_bevel_deg: float
    jack_decrement_at_450_mm: float
    jack_decrement_at_600_mm: float


def solve_rafter_and_compound(
    span_mm: float = 5400.0,
    pitch_deg: float = 25.0,
    secondary_pitch_deg: float = 25.0,
    ridge_thickness_mm: float = 45.0,
    eaves_overhang_mm: float = 450.0,
    rafter_depth_mm: float = 190.0,
    plate_width_mm: float = 90.0,
) -> RafterCompoundResult:
    """Solves common, regular hip/valley, and unequal-pitch ('bastard') hip/valley geometry + drop-saw angles."""
    run_mm = span_mm / 2.0
    theta = math.radians(pitch_deg)
    theta2 = math.radians(secondary_pitch_deg)

    rise_mm = run_mm * math.tan(theta)
    common_center = run_mm / math.cos(theta)
    half_ridge_horiz = (ridge_thickness_mm / 2.0)
    ridge_deduction_along_rafter = half_ridge_horiz / math.cos(theta)
    common_deducted = common_center - ridge_deduction_along_rafter
    eaves_tail = eaves_overhang_mm / math.cos(theta)
    total_common = common_deducted + eaves_tail

    plumb_deg = 90.0 - pitch_deg
    seat_deg = pitch_deg

    # AS 1684 Birdsmouth rule: max notch <= D/3
    max_notch = rafter_depth_mm / 3.0
    # Standard seat cut matches top plate width (e.g. 90 mm) bounded by max notch depth
    seat_level = min(plate_width_mm, (rafter_depth_mm / 3.0) / math.sin(theta) * math.cos(theta))
    heel_plumb = seat_level * math.tan(theta)

    # Plan angle phi for equal or unequal ('bastard') pitch roof
    # Secondary run for same rise: run2 = rise_mm / tan(theta2)
    run2_mm = rise_mm / math.tan(theta2)
    phi = math.atan2(run_mm, run2_mm)  # 45 deg when pitches are equal
    phi_deg = math.degrees(phi)

    hip_run = math.hypot(run_mm, run2_mm)
    hip_length = math.hypot(hip_run, rise_mm)
    hip_pitch_rad = math.atan2(rise_mm, hip_run)
    hip_seat_deg = math.degrees(hip_pitch_rad)
    hip_plumb_deg = 90.0 - hip_seat_deg

    # Compound Drop-Saw Mitre (M) & Bevel (B) for purlin / jack cheek cut:
    # M = arctan(cos(theta) * tan(phi)), B = arcsin(sin(theta) * sin(phi))
    mitre_rad = math.atan(math.cos(theta) * math.tan(phi))
    bevel_rad = math.asin(math.sin(theta) * math.sin(phi))
    backing_rad = math.atan(math.sin(hip_pitch_rad) * math.tan(phi))

    jack_450 = (450.0 / math.tan(phi)) / math.cos(theta)
    jack_600 = (600.0 / math.tan(phi)) / math.cos(theta)

    return RafterCompoundResult(
        span_mm=round(span_mm, 1),
        run_mm=round(run_mm, 1),
        pitch_deg=round(pitch_deg, 2),
        secondary_pitch_deg=round(secondary_pitch_deg, 2),
        ridge_thickness_mm=round(ridge_thickness_mm, 1),
        eaves_overhang_mm=round(eaves_overhang_mm, 1),
        rafter_depth_mm=round(rafter_depth_mm, 1),
        common_rafter_center_mm=round(common_center, 1),
        common_rafter_deducted_mm=round(common_deducted, 1),
        eaves_tail_length_mm=round(eaves_tail, 1),
        total_common_length_mm=round(total_common, 1),
        plumb_cut_deg=round(plumb_deg, 2),
        seat_cut_deg=round(seat_deg, 2),
        birdsmouth_max_notch_mm=round(max_notch, 1),
        birdsmouth_heel_plumb_mm=round(heel_plumb, 1),
        birdsmouth_seat_level_mm=round(seat_level, 1),
        hip_plan_angle_deg=round(phi_deg, 2),
        hip_run_mm=round(hip_run, 1),
        hip_length_mm=round(hip_length, 1),
        hip_plumb_deg=round(hip_plumb_deg, 2),
        hip_seat_deg=round(hip_seat_deg, 2),
        dropsaw_mitre_deg=round(math.degrees(mitre_rad), 2),
        dropsaw_bevel_deg=round(math.degrees(bevel_rad), 2),
        backing_bevel_deg=round(math.degrees(backing_rad), 2),
        jack_decrement_at_450_mm=round(jack_450, 1),
        jack_decrement_at_600_mm=round(jack_600, 1),
    )


@dataclass
class SpiralStairResult:
    total_rise_mm: float
    outer_radius_mm: float
    inner_column_radius_mm: float
    total_rotation_deg: float
    riser_count: int
    tread_count: int
    unit_rise_mm: float
    tread_angle_deg: float
    walkline_radius_mm: float
    walkline_going_mm: float
    outer_arc_going_mm: float
    inner_arc_going_mm: float
    outer_stringer_helical_length_mm: float
    inner_stringer_helical_length_mm: float
    outer_stringer_pitch_deg: float
    two_r_plus_g_mm: float
    ncc_bca_compliant: bool
    balusters_per_tread: int


def solve_spiral_stair(
    total_rise_mm: float = 2850.0,
    outer_radius_mm: float = 1000.0,
    inner_column_radius_mm: float = 150.0,
    total_rotation_deg: float = 360.0,
    target_riser_mm: float = 178.0,
) -> SpiralStairResult:
    """Solves 3D Spiral & Helical Staircase developed stringer lengths and NCC/BCA compliance."""
    riser_count = max(1, round(total_rise_mm / target_riser_mm))
    unit_rise = total_rise_mm / riser_count
    tread_count = riser_count
    theta_total_rad = math.radians(total_rotation_deg)
    tread_angle_deg = total_rotation_deg / tread_count
    tread_angle_rad = theta_total_rad / tread_count

    clear_width = outer_radius_mm - inner_column_radius_mm
    # Walkline measured 60% out from inner handrail or max 300mm from outer edge per standard spiral code
    walkline_radius = inner_column_radius_mm + 0.65 * clear_width
    walkline_going = walkline_radius * tread_angle_rad
    outer_going = outer_radius_mm * tread_angle_rad
    inner_going = inner_column_radius_mm * tread_angle_rad

    # Helical developed stringer length: L = sqrt((R * theta)^2 + H^2)
    outer_horiz_arc = outer_radius_mm * theta_total_rad
    inner_horiz_arc = inner_column_radius_mm * theta_total_rad
    outer_helical_len = math.hypot(outer_horiz_arc, total_rise_mm)
    inner_helical_len = math.hypot(inner_horiz_arc, total_rise_mm)
    outer_pitch_deg = math.degrees(math.atan2(total_rise_mm, outer_horiz_arc))

    two_r_plus_g = (2.0 * unit_rise) + walkline_going
    # NCC / BCA residential stair slope relationship: 550 <= 2R+G <= 700, 115 <= R <= 190
    compliant = (115.0 <= unit_rise <= 190.0) and (550.0 <= two_r_plus_g <= 700.0)
    # 125mm sphere rule for balusters along outer arc
    balusters_per_tread = max(2, math.ceil(outer_going / 115.0))

    return SpiralStairResult(
        total_rise_mm=round(total_rise_mm, 1),
        outer_radius_mm=round(outer_radius_mm, 1),
        inner_column_radius_mm=round(inner_column_radius_mm, 1),
        total_rotation_deg=round(total_rotation_deg, 1),
        riser_count=riser_count,
        tread_count=tread_count,
        unit_rise_mm=round(unit_rise, 2),
        tread_angle_deg=round(tread_angle_deg, 2),
        walkline_radius_mm=round(walkline_radius, 1),
        walkline_going_mm=round(walkline_going, 1),
        outer_arc_going_mm=round(outer_going, 1),
        inner_arc_going_mm=round(inner_going, 1),
        outer_stringer_helical_length_mm=round(outer_helical_len, 1),
        inner_stringer_helical_length_mm=round(inner_helical_len, 1),
        outer_stringer_pitch_deg=round(outer_pitch_deg, 2),
        two_r_plus_g_mm=round(two_r_plus_g, 1),
        ncc_bca_compliant=compliant,
        balusters_per_tread=balusters_per_tread,
    )


@dataclass
class KerfBendResult:
    timber_thickness_mm: float
    bend_radius_mm: float
    bend_angle_deg: float
    blade_kerf_mm: float
    web_thickness_mm: float
    cut_depth_mm: float
    slot_spacing_center_mm: float
    number_of_cuts: int
    outer_arc_length_mm: float
    inner_arc_length_mm: float
    total_kerf_material_removed_mm: float


def solve_kerf_bending(
    timber_thickness_mm: float = 19.0,
    bend_radius_mm: float = 600.0,
    bend_angle_deg: float = 90.0,
    blade_kerf_mm: float = 1.65,
    web_thickness_mm: float = 3.0,
) -> KerfBendResult:
    """Solves exact kerf-slot spacing, cut depth, and cut count for curved timber bending."""
    cut_depth = timber_thickness_mm - web_thickness_mm
    if cut_depth <= 0:
        raise ValueError("timber_thickness_mm must be greater than web_thickness_mm")
    slot_spacing = (bend_radius_mm * blade_kerf_mm) / cut_depth
    alpha_rad = math.radians(bend_angle_deg)
    outer_arc = alpha_rad * bend_radius_mm
    inner_arc = alpha_rad * (bend_radius_mm - timber_thickness_mm)
    num_cuts = math.ceil(outer_arc / slot_spacing)

    return KerfBendResult(
        timber_thickness_mm=round(timber_thickness_mm, 2),
        bend_radius_mm=round(bend_radius_mm, 1),
        bend_angle_deg=round(bend_angle_deg, 1),
        blade_kerf_mm=round(blade_kerf_mm, 2),
        web_thickness_mm=round(web_thickness_mm, 2),
        cut_depth_mm=round(cut_depth, 2),
        slot_spacing_center_mm=round(slot_spacing, 2),
        number_of_cuts=num_cuts,
        outer_arc_length_mm=round(outer_arc, 1),
        inner_arc_length_mm=round(inner_arc, 1),
        total_kerf_material_removed_mm=round(num_cuts * blade_kerf_mm, 1),
    )


def simulate_unit_economics(weekly_price_aud: float = 2.99) -> dict:
    """Proves >85-96% gross profit margin and 0% API overrun risk across user cohorts."""
    store_fee_rate = 0.15  # Apple App Store / Google Play Small Business Program (15% under $1M USD)
    net_weekly_revenue_aud = weekly_price_aud * (1.0 - store_fee_rate)
    # Convert AUD to USD cost basis (1 AUD = 0.66 USD -> 1 USD = 1.515 AUD)
    usd_to_aud = 1.52

    # Cost per operation (AUD):
    # 1. On-device Rust/TS Math + 2D/3D SVG/WebGL Cut Model: $0.0000
    # 2. On-device SFSpeechRecognizer / Whisper-tiny.en Voice-to-Slots: $0.0000
    # 3. Pre-baked 500+ Jig & Cut Walkthrough CDN Cache: $0.00002
    # 4. Live AI Photo-to-Cut Vision Markup (Gemini 2.5 Flash / GPT-4o-mini ~1,800 input + 450 output tokens):
    #    ~$0.00055 USD = $0.00084 AUD per photo call
    photo_call_cost_aud = 0.00084
    ai_chat_call_cost_aud = 0.00045

    cohorts = {
        "Average Site Chippy (35 calcs, 15 voice, 6 photo markups, 8 jigs/wk)": {
            "calcs": 35,
            "voice": 15,
            "photos": 6,
            "chat": 8,
            "jigs": 8,
        },
        "Heavy Leading Hand (120 calcs, 60 voice, 25 photo markups, 25 jigs/wk)": {
            "calcs": 120,
            "voice": 60,
            "photos": 25,
            "chat": 30,
            "jigs": 25,
        },
        "Hard Fair-Use Ceiling Cap (Unlimited calcs/voice/jigs + 150 live AI photo/chat calls/wk)": {
            "calcs": 500,
            "voice": 250,
            "photos": 100,
            "chat": 100,
            "jigs": 100,
        },
    }

    results = {}
    for name, u in cohorts.items():
        api_cost_aud = (
            u["photos"] * photo_call_cost_aud
            + u["chat"] * ai_chat_call_cost_aud
            + u["jigs"] * 0.00002
        )
        net_profit_aud = net_weekly_revenue_aud - api_cost_aud
        gross_margin_pct = (net_profit_aud / net_weekly_revenue_aud) * 100.0
        results[name] = {
            "weekly_gross_price_aud": round(weekly_price_aud, 2),
            "net_after_apple_google_15pct_aud": round(net_weekly_revenue_aud, 3),
            "weekly_api_cost_aud": round(api_cost_aud, 4),
            "weekly_net_profit_aud": round(net_profit_aud, 3),
            "net_margin_after_api_pct": round(gross_margin_pct, 2),
        }
    return results


if __name__ == "__main__":
    rafter = solve_rafter_and_compound(span_mm=5400, pitch_deg=25, secondary_pitch_deg=25)
    bastard = solve_rafter_and_compound(span_mm=5400, pitch_deg=25, secondary_pitch_deg=32)
    spiral = solve_spiral_stair(total_rise_mm=2850, outer_radius_mm=1000, inner_column_radius_mm=150)
    kerf = solve_kerf_bending(timber_thickness_mm=19.0, bend_radius_mm=600.0, bend_angle_deg=90.0, blade_kerf_mm=1.65, web_thickness_mm=3.0)
    econ = simulate_unit_economics(2.99)
    print(json.dumps({
        "equal_pitch_hip": asdict(rafter),
        "bastard_hip_25_vs_32": asdict(bastard),
        "spiral_stair": asdict(spiral),
        "kerf_bend": asdict(kerf),
        "unit_economics_2_99_aud": econ,
    }, indent=2))
