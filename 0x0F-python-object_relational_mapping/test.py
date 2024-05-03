dict = {
    "shirt": "shirt",
    "trousers": "trousers",
    "tie": "tie",
    "shoe": "shoe"
}

key = "underwear"
if key in dict.keys():
    print(f"modifying {key}")
    dict["underware"] = "singlet"
else:
    print(f"creating {key}")
    dict["underware"] = "singlet"

print(dict)