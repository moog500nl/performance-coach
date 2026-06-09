import json

with open("c:/Zwift Coach/performance-coach/history.json", "r") as f:
    data = json.load(f)

print("Root keys:", list(data.keys()))
for key in data.keys():
    if isinstance(data[key], dict):
        print(f"  {key} keys:", list(data[key].keys()))
    elif isinstance(data[key], list):
        print(f"  {key} length:", len(data[key]))
        if len(data[key]) > 0:
            print(f"    first item type:", type(data[key][0]))
            if isinstance(data[key][0], dict):
                print(f"    first item keys:", list(data[key][0].keys()))
    else:
        print(f"  {key}:", data[key])
