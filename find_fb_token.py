import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for the Facebook Client Token
fb_token = "b5914ea996b1c7e6e7d13adbd306349f"
print(f"Searching for {fb_token}...")
pos = content.find(fb_token)
if pos != -1:
    print(f"Found at {pos}")
    start = max(0, pos - 200)
    end = min(len(content), pos + 200)
    print(content[start:end])
else:
    print("Not found.")
