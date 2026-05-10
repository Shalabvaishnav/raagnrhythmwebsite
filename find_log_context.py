import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Search for "[Encryption] Key passed to native module"
log_msg = "[Encryption] Key passed to native module"
pos = content.find(log_msg)
if pos != -1:
    print(f"Log message found at {pos}")
    start = max(0, pos - 1000)
    end = min(len(content), pos + 1000)
    print("Context around log message:")
    print(content[start:end])
else:
    print("Log message not found.")
