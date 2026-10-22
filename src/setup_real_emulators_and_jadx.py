#!/usr/bin/env python3
"""
Downloads and installs:
1. JADX v1.5.1 Android APK/DEX Decompiler (into A:\\APEX Storage\\25_Skills_And_Repos\\android-rea-tools\\jadx)
2. Official Google Android SDK Platform-Tools (adb.exe) & Command-Line Tools (sdkmanager.bat, avdmanager.bat)
   into C:\\Users\\luke\\AppData\\Local\\Android\\Sdk (100% user-space, zero UAC block)
3. Pulls real market calculator packages & live web/PWA bundles (including @chippykit https://chippykit.com
   and Android calculator APKs) for genuine binary/bundle reverse engineering via JADX + rea-agents.
"""

import json
import os
import pathlib
import shutil
import subprocess
import urllib.request
import zipfile

ANDROID_SDK_ROOT = pathlib.Path(r"C:\Users\luke\AppData\Local\Android\Sdk")
REA_TOOLS_DIR = pathlib.Path(r"A:\APEX Storage\25_Skills_And_Repos\android-rea-tools")
APK_VAULT_DIR = pathlib.Path(r"A:\APEX Storage\25_Skills_And_Repos\carpenter-calc-apks")
PROJECT_REA_DIR = pathlib.Path(
    r"H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI\rea-decompiled"
)

JAVA_HOME = r"C:\Program Files\Eclipse Adoptium\jdk-25.0.3.9-hotspot"


def download_file(url: str, dest: pathlib.Path) -> pathlib.Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 100_000:
        print(f"[CACHE HIT] {dest} ({dest.stat().st_size:,} bytes)")
        return dest
    print(f"[DOWNLOADING] {url} -> {dest}")
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36"
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp, open(dest, "wb") as f:
        shutil.copyfileobj(resp, f)
    print(f"[DONE] {dest} ({dest.stat().st_size:,} bytes)")
    return dest


def install_jadx() -> pathlib.Path:
    jadx_dir = REA_TOOLS_DIR / "jadx"
    jadx_bat = jadx_dir / "bin" / "jadx.bat"
    if jadx_bat.exists():
        print(f"[OK] JADX already installed at {jadx_bat}")
        return jadx_bat
    zip_path = download_file(
        "https://github.com/skylot/jadx/releases/download/v1.5.1/jadx-1.5.1.zip",
        REA_TOOLS_DIR / "jadx-1.5.1.zip",
    )
    jadx_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as zf:
        zf.extractall(jadx_dir)
    print(f"[OK] Extracted JADX v1.5.1 to {jadx_dir}")
    return jadx_bat


def install_android_sdk_core() -> dict:
    ANDROID_SDK_ROOT.mkdir(parents=True, exist_ok=True)
    adb_exe = ANDROID_SDK_ROOT / "platform-tools" / "adb.exe"
    if not adb_exe.exists():
        pt_zip = download_file(
            "https://dl.google.com/android/repository/platform-tools-latest-windows.zip",
            REA_TOOLS_DIR / "platform-tools-latest-windows.zip",
        )
        with zipfile.ZipFile(pt_zip, "r") as zf:
            zf.extractall(ANDROID_SDK_ROOT)
        print(f"[OK] Installed Android platform-tools (adb.exe) at {adb_exe}")

    cmdline_latest = ANDROID_SDK_ROOT / "cmdline-tools" / "latest" / "bin" / "sdkmanager.bat"
    if not cmdline_latest.exists():
        cmd_zip = download_file(
            "https://dl.google.com/android/repository/commandlinetools-win-11076708_latest.zip",
            REA_TOOLS_DIR / "commandlinetools-win-11076708_latest.zip",
        )
        tmp_extract = ANDROID_SDK_ROOT / "cmdline-tools-tmp"
        if tmp_extract.exists():
            shutil.rmtree(tmp_extract)
        with zipfile.ZipFile(cmd_zip, "r") as zf:
            zf.extractall(tmp_extract)
        latest_dir = ANDROID_SDK_ROOT / "cmdline-tools" / "latest"
        latest_dir.parent.mkdir(parents=True, exist_ok=True)
        if latest_dir.exists():
            shutil.rmtree(latest_dir)
        shutil.move(str(tmp_extract / "cmdline-tools"), str(latest_dir))
        shutil.rmtree(tmp_extract, ignore_errors=True)
        print(f"[OK] Installed Android cmdline-tools at {cmdline_latest}")

    return {
        "adb_exe": str(adb_exe),
        "sdkmanager_bat": str(cmdline_latest),
        "avdmanager_bat": str(ANDROID_SDK_ROOT / "cmdline-tools" / "latest" / "bin" / "avdmanager.bat"),
    }


def harvest_chippykit_live_bundle() -> dict:
    """Downloads and dissects the real @chippykit (https://chippykit.com.au) production bundle."""
    out_dir = PROJECT_REA_DIR / "chippykit-live"
    out_dir.mkdir(parents=True, exist_ok=True)
    results = {"url": "https://chippykit.com.au", "files": []}
    try:
        req = urllib.request.Request(
            "https://chippykit.com.au",
            headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
        index_file = out_dir / "index.html"
        index_file.write_text(html, encoding="utf-8")
        results["files"].append(str(index_file))
        results["html_bytes"] = len(html)

        import re

        asset_urls = re.findall(r'(?:src|href)=["\']([^"\']+\.(?:js|css|json|webmanifest|png|mp4))["\']', html)
        for rel in asset_urls[:12]:
            full_url = rel if rel.startswith("http") else "https://chippykit.com.au/" + rel.lstrip("/")
            safe_name = rel.split("?")[0].strip("/").replace("/", "_")
            dest = out_dir / safe_name
            try:
                r2 = urllib.request.Request(full_url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(r2, timeout=30) as resp2:
                    data = resp2.read()
                dest.write_bytes(data)
                results["files"].append(str(dest))
            except Exception as e:
                results.setdefault("asset_errors", []).append(f"{full_url}: {e}")
    except Exception as e:
        results["error"] = str(e)
    return results


def download_and_decompile_sample_apks(jadx_bat: pathlib.Path) -> list:
    """Downloads open/mirror carpentry & fraction calculator APKs and decompiles with JADX."""
    APK_VAULT_DIR.mkdir(parents=True, exist_ok=True)
    PROJECT_REA_DIR.mkdir(parents=True, exist_ok=True)

    # F-Droid / Direct open APK targets + APKPure direct package probes
    apk_targets = [
        (
            "ChippyTools_AU_probe",
            "https://d.apkpure.com/b/APK/tools.chippy?version=latest",
            "tools.chippy.apk",
        ),
        (
            "FractionCalcPlus_Digitalchemy",
            "https://d.apkpure.com/b/APK/com.digitalchemy.calculator.freefraction?version=latest",
            "com.digitalchemy.calculator.freefraction.apk",
        ),
        (
            "HandymanCalculator",
            "https://d.apkpure.com/b/APK/com.handymancalculator.handyman?version=latest",
            "com.handymancalculator.handyman.apk",
        ),
        (
            "DewaltMobilePro",
            "https://d.apkpure.com/b/APK/com.dewalt.mobilepro?version=latest",
            "com.dewalt.mobilepro.apk",
        ),
    ]

    reports = []
    env = os.environ.copy()
    env["JAVA_HOME"] = JAVA_HOME
    env["PATH"] = f"{JAVA_HOME}\\bin;" + env.get("PATH", "")

    for label, url, filename in apk_targets:
        dest = APK_VAULT_DIR / filename
        entry = {"label": label, "apk_path": str(dest), "downloaded": False}
        try:
            download_file(url, dest)
            # Check if valid zip/apk/xapk
            if zipfile.is_zipfile(dest):
                entry["downloaded"] = True
                entry["size_bytes"] = dest.stat().st_size
                with zipfile.ZipFile(dest, "r") as zf:
                    namelist = zf.namelist()
                    entry["archive_entries_count"] = len(namelist)
                    entry["has_dex"] = any(n.endswith(".dex") for n in namelist)
                    entry["has_sub_apk"] = [n for n in namelist if n.endswith(".apk")]
                    entry["bundle_assets"] = [
                        n
                        for n in namelist
                        if any(
                            k in n.lower()
                            for k in ("bundle", "flutter", "react", "sqlite", ".db", ".json", "manifest.json")
                        )
                    ][:25]

                # Run JADX summary decompilation into PROJECT_REA_DIR / label
                out_decompile = PROJECT_REA_DIR / label
                if not out_decompile.exists() or not any(out_decompile.iterdir()):
                    out_decompile.mkdir(parents=True, exist_ok=True)
                    cmd = [
                        str(jadx_bat),
                        "-d",
                        str(out_decompile),
                        "--no-res",
                        "--threads-count",
                        "4",
                        str(dest),
                    ]
                    proc = subprocess.run(
                        cmd,
                        env=env,
                        capture_output=True,
                        text=True,
                        timeout=90,
                        creationflags=0x08000000,
                    )
                    entry["jadx_rc"] = proc.returncode
                java_files = list(out_decompile.rglob("*.java"))
                entry["decompiled_java_files"] = len(java_files)
                entry["sample_classes"] = [str(p.relative_to(out_decompile)) for p in java_files[:20]]
        except Exception as e:
            entry["error"] = str(e)
        reports.append(entry)
    return reports


def main():
    jadx_bat = install_jadx()
    sdk_info = install_android_sdk_core()
    chippykit_info = harvest_chippykit_live_bundle()
    apk_reports = download_and_decompile_sample_apks(jadx_bat)

    summary = {
        "jadx_bat": str(jadx_bat),
        "android_sdk": sdk_info,
        "chippykit_live": chippykit_info,
        "apk_decompilation": apk_reports,
    }
    summary_path = PROJECT_REA_DIR / "rea_setup_and_decompile_summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
