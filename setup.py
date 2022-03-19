from os import system
import platform


try:
    import git
    print("The 'GitPython' module is already installed.")

except ModuleNotFoundError:
    system("pip install gitpython")

print()
print()

system("python GitRepoPuller.py")

# If the command above does not work, you can try replacing 'python' with:
#   + python3
#   + py 
# 
# Or, you need to install python.
#
#
# sudo apt install python3
# https://python.org
