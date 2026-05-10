import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for setEncryptionKey("some_string")
matches = re.findall(r'setEncryptionKey\s*\(\s*["\']([^"\']+)["\']\s*\)', content)
if matches:
    print(f"KEY_FOUND: {matches[0]}")
else:
    print("Key not found with simple regex. Let's try alternative patterns.")
    # Maybe it's obfuscated or passed as a variable
    matches2 = re.findall(r'setEncryptionKey\((.*?)\)', content)
    print("Alternative matches:", matches2[:5])
