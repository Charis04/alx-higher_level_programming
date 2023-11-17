#!/usr/bin/python3

track = []
for i in range(10):
    for j in range(10):
        track.append((f"{i}{j}"))
        if f"{j}{i}" in track:
            continue
        if i != j:
            print("{}{}".format(i, j), end=", " if i < 8 else "\n")
