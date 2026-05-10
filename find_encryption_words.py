import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for "encryption" or "key"
print("Searching for encryption related words...")
for word in ["encryption", "encryptionKey", "masterKey"]:
    for m in re.finditer(word, content, re.IGNORECASE):
        start = max(0, m.start() - 100)
        end = min(len(content), m.end() + 100)
        print(f"--- {word} ---")
        print(content[start:end])
