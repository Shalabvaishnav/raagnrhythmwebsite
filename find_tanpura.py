import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for TANPURA
print("Searching for TANPURA constants in JS...")
for m in re.finditer(r'["\']TANPURA["\']', content):
    start = max(0, m.start() - 500)
    end = min(len(content), m.end() + 500)
    print(f"--- MATCH ---")
    print(content[start:end])
