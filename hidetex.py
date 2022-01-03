import os
import sys

assert len(sys.argv) >= 2, "Usage: hidetex.py <tex file>"
tex_file = sys.argv[1]
dirnameTex = os.path.dirname(tex_file)
basenameTex = os.path.split(tex_file)[1]
basenameNoExtensionTex = os.path.splitext(basenameTex)[0]
extensionTex = os.path.splitext(basenameTex)[1]
assert extensionTex == ".tex", "File must be a .tex file"

for f in os.listdir(os.path.dirname(tex_file)):
    basename = os.path.basename(f)
    basenameNoExtension = basename.split(".")[0]  # os.path.splitext(basename)[0]
    extension = "".join(basename.split(".")[1:])
    print(
        "considering",
        f,
        basename,
        basenameNoExtension,
        extension,
        os.path.join(dirnameTex, f),
    )
    if basenameNoExtension == basenameNoExtensionTex and not (
        extension in ["tex", "pdf"]
    ):
        if len(sys.argv) == 2 or (len(sys.argv) >= 3 and sys.argv[2] != "--dry-run"):
            print("Removing " + f)
            os.system("chflags hidden " + os.path.join(dirnameTex, f))
