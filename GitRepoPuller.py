#  We want to import this module to interact with GitHub repositories.
import git

# We want to import this module to get the directory the file was run in.
from os import getcwd

# Get current working directory.
git_dir = getcwd()

print("Current directory: " + git_dir)

g = git.cmd.Git(git_dir)

try:
    # Pull contents of git repository.
    g.pull()
except git.exc.GitCommandError:
    # Prints if the current working directory is not a git repository.
    print("You are not in a git repository.")
    exit()

print("Pull successfull!")
