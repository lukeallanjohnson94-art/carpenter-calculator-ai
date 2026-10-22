window.APEX_LIVE_MISSION = {
  "updated_at": "2026-10-21T10:14:43+00:00",
  "mission_id": "research-business-plan-architect-uni-b51c9c62c9",
  "objective": "Research, business-plan, architect unit economics ($2-$3/wk subscription vs API cost margin), and build the iOS & Android AI Carpenter's Calculator, Visual Cut Coach & Jig Studio",
  "lifecycle": "active",
  "revision": 8,
  "node_counts": {
    "done": 6,
    "ready": 1,
    "pending": 4
  },
  "nodes": [
    {
      "id": "plan-capture",
      "title": "Capture the concept as explicit requirement items",
      "status": "done",
      "phase": "capture",
      "owner": "director",
      "depends_on": []
    },
    {
      "id": "plan-organise",
      "title": "Assess all asks and establish project and session context",
      "status": "done",
      "phase": "capture",
      "owner": "director",
      "depends_on": [
        "plan-capture"
      ]
    },
    {
      "id": "plan-reference",
      "title": "Study reference apps, sites, APIs, and existing tools",
      "status": "done",
      "phase": "clarify",
      "owner": "worker-plan-reference",
      "depends_on": [
        "plan-organise"
      ]
    },
    {
      "id": "plan-spec",
      "title": "Write and validate the Outcome Spec for each deliverable",
      "status": "done",
      "phase": "specify",
      "owner": "worker-plan-spec",
      "depends_on": [
        "plan-reference"
      ]
    },
    {
      "id": "plan-questions",
      "title": "Ask the user every genuinely open preference question",
      "status": "done",
      "phase": "clarify",
      "owner": "worker-plan-questions",
      "depends_on": [
        "plan-spec"
      ]
    },
    {
      "id": "plan-mockups",
      "title": "Generate visual references for look, feel, and layout",
      "status": "done",
      "phase": "clarify",
      "owner": "worker-plan-mockups",
      "depends_on": [
        "plan-questions"
      ]
    },
    {
      "id": "plan-design-approval",
      "title": "Record Luke's approval of the exact visual revision",
      "status": "ready",
      "phase": "clarify",
      "owner": null,
      "depends_on": [
        "plan-mockups"
      ]
    },
    {
      "id": "plan-decompose",
      "title": "Decompose into sections and bite-size nodes with routing",
      "status": "pending",
      "phase": "plan",
      "owner": null,
      "depends_on": [
        "plan-design-approval"
      ]
    },
    {
      "id": "plan-prompts",
      "title": "Compile a prompt for every build node",
      "status": "pending",
      "phase": "plan",
      "owner": null,
      "depends_on": [
        "plan-decompose"
      ]
    },
    {
      "id": "plan-gate",
      "title": "Stress-test the detailed plan against the approved design",
      "status": "pending",
      "phase": "verify",
      "owner": null,
      "depends_on": [
        "plan-prompts"
      ]
    },
    {
      "id": "plan-approval",
      "title": "Ask the user whether to start the build",
      "status": "pending",
      "phase": "verify",
      "owner": null,
      "depends_on": [
        "plan-gate"
      ]
    }
  ],
  "org": {
    "counts": {
      "mode": "enforced",
      "active_sessions": 3,
      "working": 1,
      "by_level": {
        "L1": 1,
        "L2": 1,
        "L3": 1
      },
      "by_role": {
        "lead": 1,
        "manager": 1,
        "worker": 1
      },
      "pending_reviews": 0,
      "ceiling": 24
    },
    "tree": [
      {
        "id": "director",
        "role": "lead",
        "level": 1,
        "managers": [],
        "status": "active",
        "doing": "idle",
        "heartbeat_at": "2026-10-21T04:34:29+00:00",
        "reports": [
          {
            "id": "manager-plan-design-approval",
            "role": "manager",
            "level": 2,
            "managers": [
              "director"
            ],
            "status": "active",
            "doing": "plan-design-approval (Record Luke's approval of the exact visual revision)",
            "heartbeat_at": "2026-10-21T10:14:43+00:00",
            "reports": [
              {
                "id": "worker-plan-design-approval",
                "role": "worker",
                "level": 3,
                "managers": [
                  "manager-plan-design-approval"
                ],
                "status": "active",
                "doing": "idle",
                "heartbeat_at": "2026-10-21T10:14:43+00:00",
                "reports": []
              }
            ]
          }
        ]
      }
    ]
  },
  "chain_liaison": {
    "total_events": 9,
    "up_chain_count": 4,
    "down_chain_count": 5,
    "recent": [
      {
        "ts": "2026-10-21T04:34:35+00:00",
        "direction": "down_chain",
        "from": "manager-plan-reference",
        "to": "wave-1-workers(2)",
        "parent_node": "plan-reference",
        "instruction": "Decomposed stage 'plan-reference' into 2 micro-tasks across 1 collision-free parallel wave(s)."
      },
      {
        "ts": "2026-10-21T04:42:48+00:00",
        "direction": "up_chain",
        "from": "worker-plan-reference",
        "to": "manager-plan-reference",
        "parent_node": "plan-reference",
        "micro_id": null,
        "status": "COMPLETED",
        "summary": "Completed 6-competitor benchmark (Construction Master Pro, BuildCalc, Chippy Tools, Stairmaker, Rafter Tools+, Handyman Calculator), built deterministic carpentry_math_core.py proving 94.85%-99.65% weekly margin after API costs at .99/wk, and authored Blue-Balls freemium paywall architecture.",
        "changed_files": [],
        "verification_output": "",
        "blocker": null
      },
      {
        "ts": "2026-10-21T04:42:48+00:00",
        "direction": "down_chain",
        "from": "manager-plan-spec",
        "to": "wave-1-workers(2)",
        "parent_node": "plan-spec",
        "instruction": "Decomposed stage 'plan-spec' into 2 micro-tasks across 1 collision-free parallel wave(s)."
      },
      {
        "ts": "2026-10-21T05:31:52+00:00",
        "direction": "up_chain",
        "from": "worker-plan-spec",
        "to": "manager-plan-spec",
        "parent_node": "plan-spec",
        "micro_id": null,
        "status": "COMPLETED",
        "summary": "Validated outcome-spec.json (0 errors), generated 1024x1024 CutCoachAI emblem & 7-layer .ico, compiled CutCoachAI.exe (119,808 bytes), and built the 5-tab interactive CutCoach AI workbench.",
        "changed_files": [],
        "verification_output": "",
        "blocker": null
      },
      {
        "ts": "2026-10-21T05:31:52+00:00",
        "direction": "down_chain",
        "from": "manager-plan-questions",
        "to": "wave-1-workers(1)",
        "parent_node": "plan-questions",
        "instruction": "Decomposed stage 'plan-questions' into 1 micro-tasks across 1 collision-free parallel wave(s)."
      },
      {
        "ts": "2026-10-21T10:13:09+00:00",
        "direction": "up_chain",
        "from": "worker-plan-questions",
        "to": "manager-plan-questions",
        "parent_node": "plan-questions",
        "micro_id": null,
        "status": "COMPLETED",
        "summary": "Completed 5-branch /grill-me interview with Luke (D-01 CutCoach AI brand, D-02 .99/wk + /yr no-trial Blue-Balls paywall, D-03 Day-One Dual Metric AS 1684/NCC + Imperial Feet-Inch-1/16 IRC code switcher, D-04 Hybrid Deterministic Photo Overlay + Dual Scrap-Ply & .STL Jig outputs, D-05 Unified Expo/React Native + Shared Deterministic Math Core under INSYGHT DIGITAL / LUX Pty Ltd ABN). Recorded in CONTEXT.md, decisions.md, ADR-0001, and docs/03-MASTER-MISSION-PLAN.md.",
        "changed_files": [],
        "verification_output": "",
        "blocker": null
      },
      {
        "ts": "2026-10-21T10:13:09+00:00",
        "direction": "down_chain",
        "from": "manager-plan-mockups",
        "to": "wave-1-workers(1)",
        "parent_node": "plan-mockups",
        "instruction": "Decomposed stage 'plan-mockups' into 1 micro-tasks across 1 collision-free parallel wave(s)."
      },
      {
        "ts": "2026-10-21T10:14:43+00:00",
        "direction": "up_chain",
        "from": "worker-plan-mockups",
        "to": "manager-plan-mockups",
        "parent_node": "plan-mockups",
        "micro_id": null,
        "status": "COMPLETED",
        "summary": "Generated 1024x1024 CutCoach AI emblem, 7-layer LANCZOS .ico, and live 6-tab CutCoachAI.exe + inline workbench incorporating all 5 locked /grill-me decisions (D-01..D-05: CutCoach AI brand, .99/wk + /yr no-trial paywall, 1-Tap AU Metric / US Imperial Feet-Inch-1/16 switcher, 2-point Photo Markup + Scrap-Ply & .STL Jig exports, and Unified Expo/React Native + Shared Math Core).",
        "changed_files": [],
        "verification_output": "",
        "blocker": null
      },
      {
        "ts": "2026-10-21T10:14:43+00:00",
        "direction": "down_chain",
        "from": "manager-plan-design-approval",
        "to": "wave-1-workers(1)",
        "parent_node": "plan-design-approval",
        "instruction": "Decomposed stage 'plan-design-approval' into 1 micro-tasks across 1 collision-free parallel wave(s)."
      }
    ]
  },
  "token_savings": {
    "total_events": 452,
    "total_tokens_saved": 10643541
  },
  "fire_up_board": "H:\\My Drive\\APEX\\05_Active\\personal\\INSYGHT DIGITAL\\CARPENTER-CALCULATOR-AI\\.mission\\missions\\research-business-plan-architect-uni-b51c9c62c9\\DIRECTOR-BOARD.html",
  "learned_playbook_path": "H:\\My Drive\\APEX\\03_Harness\\skills-registry\\mission\\LEARNED-PLAYBOOK.md",
  "learned_rules_count": 14
};
