import os
import subprocess

output = str(subprocess.check_output("clingo --time-limit=20 asp.lp", shell=True))

out = output.split("\\n")

solution = []
for i in range(len(out)):
    if out[i] == "SATISFIABLE":
        solution = out[i-1].split(" ")

print(solution)

