import re

bundle_path = "/Users/shalab/Desktop/resources/assets/index.android.bundle"

with open(bundle_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Look for the module definition or call
# In RN production, it's often referred to by a short name or ID
# but the methods are strings in the bridge metadata.

# Let's find "AndroidAudioHelper"
pos = content.find("AndroidAudioHelper")
if pos != -1:
    print(f"AndroidAudioHelper found at {pos}")
    # Let's look for calls near it
    # Search for any string that is passed as an argument to a function near here
    start = max(0, pos - 2000)
    end = min(len(content), pos + 2000)
    context = content[start:end]
    print("Context around AndroidAudioHelper:")
    print(context)
else:
    print("AndroidAudioHelper not found.")
