import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for potential keys: 16, 24, or 32 character alphanumeric strings
# Usually keys are hex or base64 or just random chars
# Let's look for anything that looks like a password or key
print("Searching for potential keys...")
# Pattern for 16-64 chars of random-looking stuff
potential_keys = re.findall(r'["\']([a-zA-Z0-9_/+=]{16,64})["\']', content)

# Filter out common strings
filtered_keys = [k for k in potential_keys if not k.startswith('http') and len(k) >= 16]

print(f"Found {len(filtered_keys)} potential keys. Printing first 50...")
for k in filtered_keys[:50]:
    print(k)
