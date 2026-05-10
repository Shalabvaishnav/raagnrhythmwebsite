import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for B4nd1sh
print("Searching for B4nd1sh...")
for m in re.finditer(r'B4nd1sh', content, re.IGNORECASE):
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 100)
    print(f"--- MATCH ---")
    print(content[start:end])
