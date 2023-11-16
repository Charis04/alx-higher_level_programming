#!/usr/bin/python3

for i in range(97, 123):
    if str(chr(i)) == 'q' or str(chr(i)) == "e":
        continue
    print("{}".format(str(chr(i))), end="")
