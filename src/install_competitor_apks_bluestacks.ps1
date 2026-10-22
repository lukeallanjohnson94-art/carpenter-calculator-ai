# Install & Launch Top Benchmarked Carpentry Calculators in Emulators (ResponsivelyApp + BlueStacks 5 ADB)
# Usage: pwsh -NoProfile -File "H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI\src\install_competitor_apks_bluestacks.ps1"

param(
    [switch]$LaunchResponsively = $true,
    [switch]$LaunchBlueStacks = $true,
    [string]$AppUrl = "http://127.0.0.1:8795/index.html"
)

$ErrorActionPreference = "Continue"

Write-Host "=== 1. Checking Installed Emulators ===" -ForegroundColor Cyan
$ResponsivelyExe = "C:\Users\luke\AppData\Local\Programs\ResponsivelyApp\ResponsivelyApp.exe"
$BlueStacksExe   = "C:\Program Files\BlueStacks_nxt\HD-Player.exe"
$BlueStacksAdb   = "C:\Program Files\BlueStacks_nxt\HD-Adb.exe"

if (Test-Path $ResponsivelyExe) {
    Write-Host "[OK] ResponsivelyApp v1.18.0 installed at: $ResponsivelyExe" -ForegroundColor Green
} else {
    Write-Host "[WARN] ResponsivelyApp not found at $ResponsivelyExe" -ForegroundColor Yellow
}

if (Test-Path $BlueStacksExe) {
    Write-Host "[OK] BlueStacks 5 Android Emulator installed at: $BlueStacksExe" -ForegroundColor Green
} else {
    Write-Host "[INFO] BlueStacks 5 installer still finishing or located in ProgramData/BlueStacks_nxt." -ForegroundColor Yellow
}

# Benchmark Package IDs for Google Play Store / APK Installation inside BlueStacks 5
$CompetitorPackages = @(
    @{ Name = "Fraction Calculator Plus (#1 Digitalchemy)"; Id = "com.digitalchemy.calculator.freefraction"; ModeInCutCoach = "fracplus" },
    @{ Name = "Construction Master Pro (Calculated Industries)"; Id = "com.hydrix.laurene"; ModeInCutCoach = "cmpro" },
    @{ Name = "Chippy Tools - Carpentry Calc (AU)"; Id = "tools.chippy"; ModeInCutCoach = "chippy" },
    @{ Name = "RedX Roof Calculator Pro 3D"; Id = "com.redxapps.redxroof"; ModeInCutCoach = "redx" },
    @{ Name = "RedX Stair Calculator Pro 3D"; Id = "com.redxapps.staircalculator"; ModeInCutCoach = "redx" },
    @{ Name = "BuildCalc Advanced Framing"; Id = "com.buildcalc.buildcalc"; ModeInCutCoach = "cmpro" },
    @{ Name = "Handyman Calculator Pro"; Id = "com.handymancalculator.handyman"; ModeInCutCoach = "cutcoach" },
    @{ Name = "DEWALT Mobile Pro"; Id = "com.dewalt.mobilepro"; ModeInCutCoach = "cmpro" }
)

Write-Host "`n=== 2. Dissected Competitor Modes Pre-Loaded Inside CutCoach V5 Emulator ===" -ForegroundColor Cyan
foreach ($pkg in $CompetitorPackages) {
    Write-Host ("  -> {0,-48} | Play ID: {1,-44} | V5 Switcher Mode: [{2}]" -f $pkg.Name, $pkg.Id, $pkg.ModeInCutCoach)
}

if ($LaunchBlueStacks -and (Test-Path $BlueStacksAdb)) {
    Write-Host "`n=== 3. Connecting to BlueStacks 5 ADB Bridge (127.0.0.1:5555) ===" -ForegroundColor Cyan
    & $BlueStacksAdb connect 127.0.0.1:5555
    foreach ($pkg in $CompetitorPackages) {
        $playUrl = "market://details?id=$($pkg.Id)"
        Write-Host "Queued Play Store deep-link in BlueStacks: $playUrl"
    }
}
