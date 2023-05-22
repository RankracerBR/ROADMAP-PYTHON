d1 = {"1":1,"1":2}
print(d1)

print(d1["1"])

d1 = {}

d2 = {"John": {"Age": 27, "Hometown": "Boston"}, "Rebecca": {"Age": 31, "Hometown": "Chicago"}}

d3 = dict()

d4 = dict([["one",1], ["two",2]])

print(f"Dictionary d1: {d1}")
print(f"Dictionary d2: {d2}")
print(f"Dictionary d3: {d3}")
print(f"Dictionary d4: {d4}")

print("Jhons personal data is:")
print(d2["John"])

d2["Violet"] = {"Age":34, "HomeTown": "Los Angeles"}
print(d2)

delet = d2.pop("Violet") 
print(delet)