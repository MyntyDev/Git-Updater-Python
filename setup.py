from os import system
import platform

system("pip install -r requirements.txt")

print()
print()

if platform.system() == "Windows":
    system("py GitRepoPuller.py")

else:
    system("python3 GitRepoPuller.py")
