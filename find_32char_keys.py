import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for potential keys: 32 chars of alphanumeric
# [a-zA-Z0-9]{32}
print("Searching for 32-char alphanumeric strings...")
matches = re.findall(r'["\']([a-zA-Z0-9]{32})["\']', content)
for m in set(matches):
    print(m)
