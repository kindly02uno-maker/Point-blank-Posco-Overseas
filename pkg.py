# -*- coding: utf-8 -*-
import sys, runpy
SC = r"C:\Users\clearkim\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\e8dfec27-f9a9-4fbf-9edc-d0a03136e37f\8f5a7fb7-c3b0-4063-9b2a-16e87c17d9b7\skills\skill-creator"
sys.path.insert(0, SC)
SKILL = r"C:\클로드실습(김영은)\skills\overseas-steel-analysis"
OUT = r"C:\클로드실습(김영은)\skills"
sys.argv = ["package_skill.py", SKILL, OUT]
runpy.run_path(SC + r"\scripts\package_skill.py", run_name="__main__")
