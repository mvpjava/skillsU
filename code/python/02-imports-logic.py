import sys      # Official docs: https://docs.python.org/3/library/sys.html
import os       # Will be used to execute shell commands (note: take a look at 'subprocess' module too!)

# Variables
packageToInstall=None  #supplied at runtime via user input argument

# The list of command line arguments passed to a Python script
# argv is Equivalent to bash $0, $1 etc  Note: Length of list is 1 even if no args explicitly provided
# due to index 0 (script name) taking up 1 spot in argv list
numOfArgs=len(sys.argv)
print(f"Starting my script: {sys.argv[0]} with # of args: {numOfArgs}")

#True or False?
if (numOfArgs == 1):
    print("No argument specified, exiting!")
    sys.exit(1);
elif (numOfArgs == 2):
    print(f"Setting package to install as per first argument: {sys.argv[1]}")
    packageToInstall = sys.argv[1]
else:
    print(f"There are more than 1 args specified, ignoring and continuing!")

# Ask user if they want to install the package
userConfirmation = input(f"Please confirm you want to install package {packageToInstall} on platform '{sys.platform}' (Y/N)? ").upper()

if userConfirmation == "Y":
    print("Proceeding with installation...")
    os.system(f"sudo yum install -y {packageToInstall}")
elif userConfirmation == "N":
    print("Installation canceled.")
    sys.exit(0)  # Exit successfully
else:
    print("Invalid input. Exiting...")
    sys.exit(1)  # Exit with error

sys.exit(0)