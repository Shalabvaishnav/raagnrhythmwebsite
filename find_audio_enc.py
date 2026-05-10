import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for "audio_encrypted"
print("Searching for audio_encrypted...")
for m in re.finditer(r'audio_encrypted', content):
    start = max(0, m.start() - 200)
    end = min(len(content), m.end() + 200)
    print(f"--- MATCH ---")
    print(content[start:end])
