ctemp = [-100, -40, 0, 40, 100]
ftemp = (((9*c) / 5) + 32 for c in ctemp)

print(" ".join(str(temp) for temp in ftemp))
