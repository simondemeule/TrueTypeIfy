import os
import fontTools.ttLib.woff2 as translator

source = "input"
destination = "output"

count_success = 0
count_failure = 0

if not os.path.isdir("output"):
    os.mkdir("output")

for root, directories, files in os.walk(source):
    for item in files:
        if ".woff2" in item and root == source:
            name = item.replace(".woff2", "")
            print(f"Converting: {item}")
            try:
                translator.decompress(f"{root}/{name}.woff2", f"{destination}/{name}.ttf")
                count_success += 1
            except Exception as exc:
                print(f"Conversion failed: {str(exc)}")
                count_failure += 1

count_total = count_success + count_failure
print(f"Done. Converted {count_success} of {count_total} fonts successfully.")
