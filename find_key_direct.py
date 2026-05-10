import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for setEncryptionKey
# It might be called like: someModule.setEncryptionKey("...")
print("Searching for calls to setEncryptionKey...")
# Find the string "setEncryptionKey"
pos = content.find("setEncryptionKey")
while pos != -1:
    print(f"Found setEncryptionKey at {pos}")
    # Print a large chunk around it
    start = max(0, pos - 1000)
    end = min(len(content), pos + 1000)
    print(content[start:end])
    print("-" * 50)
    pos = content.find("setEncryptionKey", pos + 1)
