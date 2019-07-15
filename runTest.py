# pytest -s -v test_aa.py --html=report.html
import os

from sendReport.sendReport import send

os.system("pytest -s -v action/test_baseUser.py --html=report/report.html --tb=long --junitxml=F:\\code\\apitest\\report\\report.xml  --self-contained-html")
send()