import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for AndroidAudioHelper
print("Searching for AndroidAudioHelper context...")
for m in re.finditer(r'AndroidAudioHelper', content):
    start = max(0, m.start() - 200)
    end = min(len(content), m.end() + 1000)
    print(f"--- MATCH ---")
    print(content[start:end])
