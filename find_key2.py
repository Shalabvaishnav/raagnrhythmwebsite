import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's search around AndroidAudioHelper which is the module receiving the key
# "AndroidAudioHelper"
matches = re.finditer(r'AndroidAudioHelper.*?setEncryptionKey', content, re.DOTALL | re.IGNORECASE)

print("Checking context around setEncryptionKey...")
# Find all occurrences of setEncryptionKey and print surrounding text
for m in re.finditer(r'setEncryptionKey', content):
    start = max(0, m.start() - 100)
    end = min(len(content), m.end() + 100)
    print(f"--- MATCH ---")
    print(content[start:end])
