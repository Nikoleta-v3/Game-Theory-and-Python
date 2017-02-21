import glob
import subprocess
import os

ipynbs = glob.glob("*ipynb")

for ipynb in ipynbs:
    tex = ipynb[:-6] + ".tex"
    pdf = ipynb[:-6] + ".pdf"
    subprocess.call(["jupyter-nbconvert", "--to", "latex", ipynb])
    subprocess.call(["latexmk", "--xelatex", tex])
    subprocess.call(["latexmk", "-c"])
