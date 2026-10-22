#!/usr/bin/env python3
"""
CutCoach AI — 12-Endpoint REST API & Model Context Protocol (MCP) Server (v1.0)
Workspace: H:\\My Drive\\APEX\\05_Active\\personal\\INSYGHT DIGITAL\\CARPENTER-CALCULATOR-AI
Implements deterministic clean-room engines across all 9 benchmarked calculators:
  1. GET  /api/v1/health                  (carpenter_health_and_catalog)
  2. POST /api/v1/rafter-compound         (solve_rafter_and_bastard_hip)
  3. POST /api/v1/polygonal-roof          (solve_polygonal_and_blind_valley)
  4. POST /api/v1/stair-straight          (solve_straight_stair_and_headroom)
  5. POST /api/v1/stair-spiral            (solve_spiral_helical_stair)
  6. POST /api/v1/kerf-bending            (solve_kerf_bending_and_arch)
  7. POST /api/v1/fraction-triple-pad     (solve_fraction_triple_pad)
  8. POST /api/v1/raked-wall-and-spacing  (solve_raked_wall_and_balusters)
  9. POST /api/v1/trig-and-squaring       (solve_framing_trig_and_squaring)
 10. POST /api/v1/joinery-and-crown       (solve_woodshop_joinery_and_crown)
 11. POST /api/v1/voice-and-jig-blueprint (parse_jobsite_voice_and_generate_jig)
 12. POST /api/v1/paywall-and-economics   (evaluate_paywall_and_unit_economics)
"""
from __future__ import annotations
import argparse
from dataclasses import asdict
from fractions import Fraction
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import math
import pathlib
import re
import sys
import threading
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from carpentry_math_core import (  # noqa: E402
    solve_rafter_and_compound,
    solve_spiral_stair,
    solve_kerf_bending,
    simulate_unit_economics,
)

SPECIES_MOVEMENT = {
    "spotted_gum": {"name": "Spotted Gum (Corymbia maculata)", "c_tan": 0.00330, "c_rad": 0.00220, "density_kg_m3": 990},
    "blackbutt": {"name": "Blackbutt (Eucalyptus pilularis)", "c_tan": 0.00370, "c_rad": 0.00230, "density_kg_m3": 900},
    "tasmanian_oak": {"name": "Tasmanian Oak / Vic Ash (E. regnans)", "c_tan": 0.00420, "c_rad": 0.00220, "density_kg_m3": 680},
    "jarrah": {"name": "Jarrah (Eucalyptus marginata)", "c_tan": 0.00350, "c_rad": 0.00240, "density_kg_m3": 820},
    "merbau": {"name": "Merbau / Kwila (Intsia bijuga)", "c_tan": 0.00220, "c_rad": 0.00120, "density_kg_m3": 830},
    "radiata_pine": {"name": "Radiata Pine (MGP10 / Dressed)", "c_tan": 0.00270, "c_rad": 0.00160, "density_kg_m3": 510},
    "white_oak": {"name": "American White Oak (Quercus alba)", "c_tan": 0.00365, "c_rad": 0.00180, "density_kg_m3": 750},
    "black_walnut": {"name": "American Black Walnut (Juglans nigra)", "c_tan": 0.00274, "c_rad": 0.00190, "density_kg_m3": 640},
    "hard_maple": {"name": "Hard Sugar Maple (Acer saccharum)", "c_tan": 0.00353, "c_rad": 0.00165, "density_kg_m3": 705},
}


def ep_01_health(_params: dict | None = None) -> dict:
    return {
        "status": "ok",
        "service": "CutCoach AI REST & MCP Geometry Server",
        "version": "1.0.0",
        "zero_llm_math_cost_aud": 0.0,
        "supported_units": ["AU_MM", "US_IMP", "UK_MM"],
        "supported_codes": ["AS_1684_NCC", "IRC_2024", "BS_5268"],
        "benchmarked_calculators_dissected": 9,
        "endpoint_count": 12,
        "endpoints": list(ROUTES.keys()),
    }


def ep_02_rafter_compound(p: dict) -> dict:
    span = float(p.get("span_mm", 5400.0))
    pitch1 = float(p.get("pitch_deg", 25.0))
    pitch2 = float(p.get("secondary_pitch_deg", pitch1))
    ridge = float(p.get("ridge_thickness_mm", 45.0))
    overhang = float(p.get("eaves_overhang_mm", 450.0))
    depth = float(p.get("rafter_depth_mm", 190.0))
    plate = float(p.get("plate_width_mm", 90.0))

    res = asdict(solve_rafter_and_compound(span, pitch1, pitch2, ridge, overhang, depth, plate))
    t1, t2 = math.radians(pitch1), math.radians(pitch2)
    coplanar_overhang_2 = overhang * (math.tan(t1) / math.tan(t2))
    plate_offset = overhang * (math.tan(t1) - math.tan(t2))
    hap_mm = (depth / math.cos(t1)) - res["birdsmouth_heel_plumb_mm"]
    res["coplanar_secondary_overhang_mm"] = round(coplanar_overhang_2, 1)
    res["equal_overhang_plate_offset_mm"] = round(plate_offset, 1)
    res["height_above_plate_hap_mm"] = round(hap_mm, 1)
    res["redx_callouts_A_to_J"] = {
        "A_total_length_mm": res["total_common_length_mm"],
        "B_deducted_common_mm": res["common_rafter_deducted_mm"],
        "C_eaves_tail_mm": res["eaves_tail_length_mm"],
        "D_plumb_angle_deg": res["plumb_cut_deg"],
        "E_seat_angle_deg": res["seat_cut_deg"],
        "F_hap_mm": round(hap_mm, 1),
        "G_seat_cut_mm": res["birdsmouth_seat_level_mm"],
        "H_heel_plumb_mm": res["birdsmouth_heel_plumb_mm"],
        "J_dropsaw_mitre_bevel_deg": [res["dropsaw_mitre_deg"], res["dropsaw_bevel_deg"]],
    }
    return res


def ep_03_polygonal_roof(p: dict) -> dict:
    sides = max(3, int(p.get("sides", 8)))
    flat_span = float(p.get("flat_span_mm", 3600.0))
    pitch_deg = float(p.get("pitch_deg", 30.0))
    dormer_pitch_deg = float(p.get("dormer_pitch_deg", 35.0))

    run_common = flat_span / 2.0
    theta = math.radians(pitch_deg)
    rise = run_common * math.tan(theta)
    common_len = math.hypot(run_common, rise)

    half_vertex_deg = 180.0 / sides
    phi_rad = math.radians(half_vertex_deg)
    hip_run = run_common / math.sin(phi_rad)
    hip_len = math.hypot(hip_run, rise)
    hip_pitch_rad = math.atan2(rise, hip_run)
    backing_rad = math.atan(math.sin(hip_pitch_rad) / math.tan(phi_rad))

    purlin_mitre_rad = math.atan(math.sin(theta) / math.tan(phi_rad))
    purlin_bevel_rad = math.asin(math.cos(theta) * math.cos(phi_rad))

    t_dormer = math.radians(dormer_pitch_deg)
    phi_val = math.atan(math.tan(theta) / math.tan(t_dormer))
    sleeper_bevel_rad = math.atan(math.sin(theta) * math.cos(phi_val))

    return {
        "sides": sides, "polygon_name": {4: "Square", 6: "Hexagonal", 8: "Octagonal", 10: "Decagonal", 12: "Dodecagonal"}.get(sides, f"{sides}-gon"),
        "half_vertex_plan_angle_deg": round(half_vertex_deg, 2), "common_run_mm": round(run_common, 1), "rise_mm": round(rise, 1),
        "common_rafter_length_mm": round(common_len, 1), "hip_run_mm": round(hip_run, 1), "hip_rafter_length_mm": round(hip_len, 1),
        "hip_pitch_deg": round(math.degrees(hip_pitch_rad), 2), "hip_plumb_deg": round(90.0 - math.degrees(hip_pitch_rad), 2),
        "hip_backing_bevel_deg": round(math.degrees(backing_rad), 2), "purlin_mitre_deg": round(math.degrees(purlin_mitre_rad), 2),
        "purlin_bevel_deg": round(math.degrees(purlin_bevel_rad), 2), "california_blind_valley_sleeper_bevel_deg": round(math.degrees(sleeper_bevel_rad), 2),
    }


def ep_04_stair_straight(p: dict) -> dict:
    total_rise, total_run = float(p.get("total_rise_mm", 2700.0)), float(p.get("total_run_mm", 3500.0))
    target_riser, tread_thick = float(p.get("target_riser_mm", 180.0)), float(p.get("tread_thickness_mm", 35.0))
    stringer_width, floor_thick, min_headroom = float(p.get("stringer_width_mm", 240.0)), float(p.get("floor_thickness_mm", 300.0)), float(p.get("min_headroom_mm", 2000.0))

    riser_count = max(1, round(total_rise / target_riser))
    unit_rise, tread_count = total_rise / riser_count, max(1, riser_count - 1)
    unit_going, first_riser_cut = total_run / tread_count, unit_rise - tread_thick

    stringer_len, incline_rad = math.hypot(total_rise, total_run), math.atan2(total_rise, total_run)
    throat_depth = stringer_width - (unit_rise * math.cos(incline_rad))
    min_well_opening = unit_going * ((min_headroom + floor_thick) / unit_rise)
    two_r_plus_g = 2.0 * unit_rise + unit_going
    ncc_ok = (115.0 <= unit_rise <= 190.0) and (240.0 <= unit_going <= 355.0) and (550.0 <= two_r_plus_g <= 700.0) and (throat_depth >= 90.0)

    return {
        "total_rise_mm": round(total_rise, 1), "total_run_mm": round(total_run, 1), "riser_count": riser_count, "tread_count": tread_count,
        "unit_rise_mm": round(unit_rise, 2), "unit_going_mm": round(unit_going, 2), "first_riser_dropped_cut_mm": round(first_riser_cut, 2),
        "stringer_total_length_mm": round(stringer_len, 1), "incline_angle_deg": round(math.degrees(incline_rad), 2),
        "effective_throat_depth_mm": round(throat_depth, 1), "min_stairwell_opening_mm": round(min_well_opening, 1),
        "two_r_plus_g_mm": round(two_r_plus_g, 1), "ncc_bca_compliant": ncc_ok,
    }


def ep_05_stair_spiral(p: dict) -> dict:
    return asdict(
        solve_spiral_stair(
            total_rise_mm=float(p.get("total_rise_mm", 2850.0)),
            outer_radius_mm=float(p.get("outer_radius_mm", 1000.0)),
            inner_column_radius_mm=float(p.get("inner_column_radius_mm", 150.0)),
            total_rotation_deg=float(p.get("total_rotation_deg", 360.0)),
            target_riser_mm=float(p.get("target_riser_mm", 178.0)),
        )
    )


def ep_06_kerf_bending(p: dict) -> dict:
    res = asdict(
        solve_kerf_bending(
            timber_thickness_mm=float(p.get("timber_thickness_mm", 19.0)),
            bend_radius_mm=float(p.get("bend_radius_mm", 600.0)),
            bend_angle_deg=float(p.get("bend_angle_deg", 90.0)),
            blade_kerf_mm=float(p.get("blade_kerf_mm", 1.65)),
            web_thickness_mm=float(p.get("web_thickness_mm", 3.0)),
        )
    )
    spacing = res["slot_spacing_center_mm"]
    res["cumulative_tape_marks_mm"] = [round((i + 1) * spacing, 1) for i in range(res["number_of_cuts"])]
    return res


def _to_inches(ft: int, inch: int, num: int, den: int) -> Fraction:
    return Fraction(ft * 12 + inch, 1) + Fraction(num, max(1, den))


def ep_07_fraction_triple_pad(p: dict) -> dict:
    lhs = _to_inches(int(p.get("left_ft", 14)), int(p.get("left_in", 11)), int(p.get("left_num", 11)), int(p.get("left_den", 16)))
    rhs = _to_inches(int(p.get("right_ft", 3)), int(p.get("right_in", 6)), int(p.get("right_num", 5)), int(p.get("right_den", 8)))
    op = str(p.get("operator", "+")).strip()
    snap_den = int(p.get("snap_den", 16))

    ops = {"+": lhs + rhs, "-": lhs - rhs, "*": lhs * rhs, "x": lhs * rhs, "×": lhs * rhs, "/": lhs / (rhs or Fraction(1, 1)), "÷": lhs / (rhs or Fraction(1, 1))}
    if op not in ops:
        raise ValueError(f"Unsupported operator: {op}")
    total_in = ops[op]

    sign = -1 if total_in < 0 else 1
    abs_in = abs(total_in)
    whole_total_in = int(abs_in)
    rem_frac = abs_in - whole_total_in
    ft_out, in_out = divmod(whole_total_in, 12)

    dec_in = float(total_in)
    snap_frac = Fraction(round(float(rem_frac) * snap_den), snap_den)
    if snap_frac == 1:
        in_out += 1
        snap_frac = Fraction(0, 1)
        if in_out >= 12:
            ft_out += 1
            in_out -= 12

    frac_str = f" {snap_frac.numerator}/{snap_frac.denominator}" if snap_frac.numerator else ""
    prefix = "-" if sign < 0 else ""
    return {
        "formatted_mixed_imperial": f"{prefix}{ft_out}' {in_out}{frac_str}\"",
        "exact_rational_inches": f"{total_in.numerator}/{total_in.denominator}",
        "decimal_inches": round(dec_in, 4),
        "exact_mm": round(dec_in * 25.4, 2),
        "snap_denominator": snap_den,
        "rounding_error_inches": round(float(rem_frac) - float(snap_frac), 5),
    }


def ep_08_raked_wall_and_spacing(p: dict) -> dict:
    wall_len = float(p.get("wall_length_mm", 3600.0))
    h_start = float(p.get("start_height_mm", 2400.0))
    h_end = float(p.get("end_height_mm", 3300.0))
    spacing = float(p.get("stud_spacing_mm", 450.0))
    stud_w = float(p.get("stud_width_mm", 45.0))
    plate_t = float(p.get("plate_thickness_mm", 45.0))

    theta_rad = math.atan2(h_end - h_start, wall_len)
    theta_deg = math.degrees(theta_rad)
    plate_deduct = plate_t + (plate_t / math.cos(theta_rad))

    stations = [0.0]
    x = spacing
    while x < wall_len - stud_w:
        stations.append(x)
        x += spacing
    stations.append(max(0.0, wall_len - stud_w))

    studs = [
        {
            "stud_number": idx,
            "station_mm": round(pos, 1),
            "short_point_mm": round(h_start + pos * math.tan(theta_rad) - plate_deduct, 1),
            "long_point_mm": round(h_start + (pos + stud_w) * math.tan(theta_rad) - plate_deduct, 1),
        }
        for idx, pos in enumerate(stations, start=1)
    ]

    bal_open, bal_w, max_gap = float(p.get("baluster_opening_mm", 2400.0)), float(p.get("baluster_width_mm", 19.0)), float(p.get("max_gap_mm", 125.0))
    n_bal = math.ceil((bal_open - max_gap) / (bal_w + max_gap))
    actual_gap = (bal_open - n_bal * bal_w) / (n_bal + 1)

    return {
        "raked_pitch_deg": round(theta_deg, 2), "top_plate_bevel_deg": round(theta_deg, 2), "vertical_plate_deduction_mm": round(plate_deduct, 1),
        "stud_count": len(studs), "stud_cut_list": studs, "baluster_count": n_bal, "baluster_equal_gap_mm": round(actual_gap, 2),
        "baluster_centre_pitch_mm": round(actual_gap + bal_w, 2), "tts_running_tape_marks_mm": [round((k + 1) * actual_gap + k * bal_w, 1) for k in range(n_bal)],
    }


def ep_09_trig_and_squaring(p: dict) -> dict:
    rise, run = float(p.get("rise_mm", 1200.0)), float(p.get("run_mm", 2400.0))
    side_a, side_b = float(p.get("deck_side_a_mm", 3000.0)), float(p.get("deck_side_b_mm", 4000.0))
    meas_diag, slab_thick = float(p.get("measured_diag_mm", 5012.0)), float(p.get("slab_thickness_mm", 100.0))

    hyp, pitch_rad, true_diag = math.hypot(rise, run), math.atan2(rise, run), math.hypot(side_a, side_b)
    cos_gamma = max(-1.0, min(1.0, (side_a**2 + side_b**2 - meas_diag**2) / (2.0 * side_a * side_b)))
    vol_m3 = (side_a / 1000.0) * (side_b / 1000.0) * (slab_thick / 1000.0) * 1.05

    return {
        "hypotenuse_mm": round(hyp, 1), "pitch_deg": round(math.degrees(pitch_rad), 2), "pitch_imperial_x_in_12": round(math.tan(pitch_rad) * 12.0, 2),
        "pitch_ratio_1_in_y": round(run / rise, 2) if rise else 0.0, "grade_pct": round(math.tan(pitch_rad) * 100.0, 2),
        "square_diagonal_mm": round(true_diag, 1), "diagonal_error_mm": round(meas_diag - true_diag, 1),
        "actual_corner_angle_deg": round(math.degrees(math.acos(cos_gamma)), 2),
        "concrete_volume_m3_with_5pct_waste": round(vol_m3, 3), "bags_20kg_count": math.ceil(vol_m3 / 0.009),
    }


def ep_10_joinery_and_crown(p: dict) -> dict:
    sp = SPECIES_MOVEMENT.get(str(p.get("species", "spotted_gum")).lower(), SPECIES_MOVEMENT["spotted_gum"])
    width, mc_init, mc_final = float(p.get("board_width_mm", 600.0)), float(p.get("mc_initial_pct", 10.0)), float(p.get("mc_final_pct", 15.0))
    cut_type = str(p.get("cut_type", "tangential")).lower()
    delta_w = width * (mc_final - mc_init) * (sp["c_tan"] if cut_type == "tangential" else sp["c_rad"])

    spring_deg, corner_deg = float(p.get("crown_spring_deg", 38.0)), float(p.get("wall_corner_deg", 90.0))
    sigma, half_miter = math.radians(spring_deg), math.radians((180.0 - corner_deg) / 2.0)
    crown_mitre = math.degrees(math.atan(math.sin(sigma) * math.tan(half_miter)))
    crown_bevel = math.degrees(math.asin(math.cos(sigma) * math.sin(half_miter)))
    phi = 1.61803398875

    return {
        "species": sp["name"], "cut_orientation": cut_type, "seasonal_width_change_mm": round(delta_w, 2), "final_board_width_mm": round(width + delta_w, 2),
        "crown_spring_angle_deg": spring_deg, "crown_wall_corner_deg": corner_deg, "crown_flat_mitre_deg": round(crown_mitre, 2),
        "crown_flat_bevel_deg": round(crown_bevel, 2), "golden_ratio_major_mm": round(width * phi, 1), "golden_ratio_minor_mm": round(width / phi, 1),
    }


def ep_11_voice_and_jig_blueprint(p: dict) -> dict:
    transcript = str(p.get("transcript", "Bastard hip 5400 span 25 and 32 degrees 45 mil ridge"))
    nums = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", transcript)]
    lower = transcript.lower()
    if "stair" in lower or "spiral" in lower:
        module, parsed = "stairs", {"total_rise_mm": nums[0] if nums else 2850.0, "outer_radius_mm": nums[1] if len(nums) > 1 else 1000.0}
    elif "kerf" in lower or "arch" in lower:
        module, parsed = "kerf", {"timber_thickness_mm": nums[0] if nums else 19.0, "bend_radius_mm": nums[1] if len(nums) > 1 else 600.0}
    else:
        module, parsed = "rafters", {"span_mm": nums[0] if nums else 5400.0, "pitch_deg": nums[1] if len(nums) > 1 else 25.0, "secondary_pitch_deg": nums[2] if len(nums) > 2 else 32.0}

    rafter_d, pitch_d, slot_s = float(p.get("rafter_depth_mm", 190.0)), float(p.get("pitch_deg", parsed.get("pitch_deg", 25.0))), float(p.get("slot_spacing_mm", 61.88))
    stl_ascii = f"solid CutCoach_Guide_Jig\n  facet normal 0 0 1\n    outer loop\n      vertex 0 0 0\n      vertex {rafter_d:.1f} 0 0\n      vertex 0 {slot_s:.1f} 15\n    endloop\n  endfacet\nendsolid CutCoach_Guide_Jig"
    return {
        "voice_transcript": transcript, "detected_module": module, "parsed_slots": parsed,
        "formply_jig_plan": {"plywood_thickness_mm": 17.0, "fence_batten_length_mm": 450.0, "cheek_body_width_mm": round(rafter_d + 60.0, 1), "scribed_plumb_angle_deg": round(90.0 - pitch_d, 2), "kerf_index_pin_offset_mm": round(slot_s, 2)},
        "stl_ascii_preview": stl_ascii,
    }


def ep_12_paywall_and_economics(p: dict) -> dict:
    tier = str(p.get("tier", "free")).lower()
    price = float(p.get("weekly_price_aud", 2.99))
    sample = solve_rafter_and_compound(5400.0, 25.0, 32.0)
    return {
        "tier": tier,
        "free_3d_preview_enabled": True,
        "overall_common_length_mm": sample.total_common_length_mm,
        "dropsaw_mitre_deg": sample.dropsaw_mitre_deg if tier == "pro" else "🔒 PRO PASS ($2.99/wk)",
        "dropsaw_bevel_deg": sample.dropsaw_bevel_deg if tier == "pro" else "🔒 PRO PASS ($2.99/wk)",
        "birdsmouth_heel_plumb_mm": sample.birdsmouth_heel_plumb_mm if tier == "pro" else "🔒 PRO PASS ($2.99/wk)",
        "jack_decrement_at_450_mm": sample.jack_decrement_at_450_mm if tier == "pro" else "🔒 PRO PASS ($2.99/wk)",
        "unit_economics_cohorts": simulate_unit_economics(price),
    }


ROUTES = {
    "/api/v1/health": ("GET", "carpenter_health_and_catalog", ep_01_health),
    "/api/v1/rafter-compound": ("POST", "solve_rafter_and_bastard_hip", ep_02_rafter_compound),
    "/api/v1/polygonal-roof": ("POST", "solve_polygonal_and_blind_valley", ep_03_polygonal_roof),
    "/api/v1/stair-straight": ("POST", "solve_straight_stair_and_headroom", ep_04_stair_straight),
    "/api/v1/stair-spiral": ("POST", "solve_spiral_helical_stair", ep_05_stair_spiral),
    "/api/v1/kerf-bending": ("POST", "solve_kerf_bending_and_arch", ep_06_kerf_bending),
    "/api/v1/fraction-triple-pad": ("POST", "solve_fraction_triple_pad", ep_07_fraction_triple_pad),
    "/api/v1/raked-wall-and-spacing": ("POST", "solve_raked_wall_and_balusters", ep_08_raked_wall_and_spacing),
    "/api/v1/trig-and-squaring": ("POST", "solve_framing_trig_and_squaring", ep_09_trig_and_squaring),
    "/api/v1/joinery-and-crown": ("POST", "solve_woodshop_joinery_and_crown", ep_10_joinery_and_crown),
    "/api/v1/voice-and-jig-blueprint": ("POST", "parse_jobsite_voice_and_generate_jig", ep_11_voice_and_jig_blueprint),
    "/api/v1/paywall-and-economics": ("POST", "evaluate_paywall_and_unit_economics", ep_12_paywall_and_economics),
}

MCP_TOOLS = {name: fn for _, (_, name, fn) in ROUTES.items()}


class CarpenterRequestHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        return

    def _send_json(self, code: int, payload: dict) -> None:
        raw = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self) -> None:
        if self.path in ROUTES:
            self._send_json(200, ROUTES[self.path][2]({}))
        else:
            self._send_json(404, {"error": f"Unknown endpoint {self.path}"})

    def do_POST(self) -> None:
        if self.path not in ROUTES:
            self._send_json(404, {"error": f"Unknown endpoint {self.path}"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        body = json.loads(self.rfile.read(length).decode("utf-8") or "{}") if length > 0 else {}
        self._send_json(200, ROUTES[self.path][2](body))


def handle_mcp_jsonrpc(req: dict) -> dict:
    req_id = req.get("id")
    method = req.get("method", "")
    params = req.get("params", {}) or {}
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "cutcoach-carpenter-calc-mcp", "version": "1.0.0"}, "capabilities": {"tools": {}}}}
    if method == "tools/list":
        tools = [{"name": name, "description": f"Deterministic CutCoach AI tool ({path})", "inputSchema": {"type": "object"}} for path, (_, name, _) in ROUTES.items()]
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": tools}}
    if method == "tools/call":
        t_name = params.get("name", "")
        t_args = params.get("arguments", {}) or {}
        if t_name not in MCP_TOOLS:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Unknown tool: {t_name}"}}
        out = MCP_TOOLS[t_name](t_args)
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}], "structuredContent": out}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {}}


def run_self_test() -> dict:
    srv = HTTPServer(("127.0.0.1", 0), CarpenterRequestHandler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    rest_results, mcp_results = {}, {}
    try:
        for path, (verb, tool_name, _) in ROUTES.items():
            url = f"http://127.0.0.1:{port}{path}"
            req = urllib.request.Request(url, data=None if verb == "GET" else b"{}", headers={"Content-Type": "application/json"}, method=verb)
            with urllib.request.urlopen(req, timeout=5) as r:
                rest_results[path] = json.loads(r.read().decode("utf-8"))
            mcp_resp = handle_mcp_jsonrpc({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": tool_name, "arguments": {}}})
            mcp_results[tool_name] = mcp_resp["result"]["structuredContent"]
    finally:
        srv.shutdown()
        srv.server_close()

    assert rest_results["/api/v1/health"]["endpoint_count"] == 12
    assert rest_results["/api/v1/rafter-compound"]["dropsaw_mitre_deg"] == 42.19
    assert rest_results["/api/v1/polygonal-roof"]["half_vertex_plan_angle_deg"] == 22.5
    assert rest_results["/api/v1/stair-straight"]["ncc_bca_compliant"] is True
    assert rest_results["/api/v1/stair-spiral"]["ncc_bca_compliant"] is True
    assert rest_results["/api/v1/kerf-bending"]["number_of_cuts"] == 16
    assert rest_results["/api/v1/fraction-triple-pad"]["formatted_mixed_imperial"] == '18\' 6 5/16"'
    assert rest_results["/api/v1/raked-wall-and-spacing"]["stud_count"] == 9
    assert rest_results["/api/v1/trig-and-squaring"]["square_diagonal_mm"] == 5000.0
    assert rest_results["/api/v1/joinery-and-crown"]["crown_flat_mitre_deg"] == 31.62
    assert rest_results["/api/v1/joinery-and-crown"]["crown_flat_bevel_deg"] == 33.86
    assert rest_results["/api/v1/voice-and-jig-blueprint"]["detected_module"] == "rafters"
    assert "🔒 PRO PASS" in str(rest_results["/api/v1/paywall-and-economics"]["dropsaw_mitre_deg"])

    return {
        "verified": True,
        "rest_endpoints_passed": len(rest_results),
        "mcp_tools_passed": len(mcp_results),
        "sample_assertions": {
            "rafter_mitre_deg": rest_results["/api/v1/rafter-compound"]["dropsaw_mitre_deg"],
            "octagon_half_angle_deg": rest_results["/api/v1/polygonal-roof"]["half_vertex_plan_angle_deg"],
            "straight_stair_first_riser_cut_mm": rest_results["/api/v1/stair-straight"]["first_riser_dropped_cut_mm"],
            "spiral_outer_helical_mm": rest_results["/api/v1/stair-spiral"]["outer_stringer_helical_length_mm"],
            "kerf_slot_spacing_mm": rest_results["/api/v1/kerf-bending"]["slot_spacing_center_mm"],
            "fraction_sum": rest_results["/api/v1/fraction-triple-pad"]["formatted_mixed_imperial"],
            "raked_wall_studs": rest_results["/api/v1/raked-wall-and-spacing"]["stud_count"],
            "crown_38_mitre_bevel_deg": [
                rest_results["/api/v1/joinery-and-crown"]["crown_flat_mitre_deg"],
                rest_results["/api/v1/joinery-and-crown"]["crown_flat_bevel_deg"],
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="CutCoach AI 12-Endpoint REST & MCP Server")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--serve", action="store_true")
    parser.add_argument("--port", type=int, default=8794)
    parser.add_argument("--mcp", action="store_true")
    args = parser.parse_args()

    if args.mcp:
        for line in sys.stdin:
            line = line.strip()
            if line:
                sys.stdout.write(json.dumps(handle_mcp_jsonrpc(json.loads(line))) + "\n")
                sys.stdout.flush()
        return
    if args.serve:
        HTTPServer(("127.0.0.1", args.port), CarpenterRequestHandler).serve_forever()
        return
    print(json.dumps(run_self_test(), indent=2))


if __name__ == "__main__":
    main()
