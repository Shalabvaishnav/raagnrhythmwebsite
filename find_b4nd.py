import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for any string that looks like B4nd...
print("Searching for strings starting with B4nd...")
matches = re.findall(r'["\'](B4nd[^"\']*)["\']', content)
for m in set(matches):
    print(m)
