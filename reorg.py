# -*- coding: utf-8 -*-
import json, os, shutil, glob

base = r"C:\클로드실습(김영은)\skills\overseas-steel-analysis-workspace\iteration-1"
for eval_dir in glob.glob(os.path.join(base, "eval-*")):
    for config in ("with_skill", "without_skill"):
        cdir = os.path.join(eval_dir, config)
        if not os.path.isdir(cdir):
            continue
        gpath = os.path.join(cdir, "grading.json")
        if not os.path.exists(gpath):
            continue
        with open(gpath, encoding="utf-8") as f:
            grading = json.load(f)
        exps = grading.get("expectations", [])
        passed = sum(1 for e in exps if e.get("passed"))
        total = len(exps)
        grading["summary"] = {
            "pass_rate": round(passed/total, 4) if total else 0.0,
            "passed": passed, "failed": total-passed, "total": total,
        }
        run_dir = os.path.join(cdir, "run-1")
        os.makedirs(run_dir, exist_ok=True)
        with open(os.path.join(run_dir, "grading.json"), "w", encoding="utf-8") as f:
            json.dump(grading, f, ensure_ascii=False, indent=2)
        # copy timing.json into run-1
        tsrc = os.path.join(cdir, "timing.json")
        if os.path.exists(tsrc):
            shutil.copy(tsrc, os.path.join(run_dir, "timing.json"))
        print(f"{os.path.basename(eval_dir)}/{config}: {passed}/{total}")
print("done")
