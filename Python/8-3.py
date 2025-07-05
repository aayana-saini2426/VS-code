setx={"red", "black"}
sety={"black", "cyan"}

print("original sets", "set1", setx, "set2", sety)
setz=setx.intersection(sety)
print("intersected sets", setz)