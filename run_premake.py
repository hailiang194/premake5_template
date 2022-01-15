import sys
import os
import platform
import subprocess

PLATFROM_FOLDER = {
    "Windows" : "windows",
    "Linux"   : "linux",
    "Darwin"  : "macosx"
}

platform_name = platform.system()

print("Detected platform: " + platform_name)

premake_file_path = os.path.join("vendors", "premake", PLATFROM_FOLDER[platform_name], "premake5")
print("Premake file path: " + premake_file_path)
print("Argv: " + sys.argv[1])

subprocess.run([premake_file_path, sys.argv[1]])
