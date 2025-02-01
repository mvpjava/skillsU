import sys      # Official docs: https://docs.python.org/3/library/sys.html
import os       # Will be used to execute shell commands (note: take a look at 'subprocess' module too!)

# packages to install provided as a list
packagesToInstallList = ['tree', 'wget', 'nano', 'curl', 'express']

print(f"Starting my script: {sys.argv[0]}")
print(f"All packages in list: {packagesToInstallList}")
print(f"Length of package list: {len(packagesToInstallList)}")
print(f"First package in list is: {packagesToInstallList[0]}")
print(f"last package in list is: {packagesToInstallList[-1]}")

# List slices
print (f"slice 1:4] {packagesToInstallList[1:4]}") #dont get ''git'' since always stops before 2nd index (4 in this case)
print (f"slice [:3] {packagesToInstallList[:3]}") # when 1st index missing, defaults to zero
print (f"slice [1:-1] {packagesToInstallList[1:-1]}") # -1 in slice is element right before end of list (not same behaviour when -1 is used in list index)
print (f"slice [1:] {packagesToInstallList[1:]}") #default to end of list (will actually get last item in list - not like explicit -1 in slide as above example)


# Ask user if they want to install the package
userConfirmation = input(f"Please confirm you want to install all packages on platform '{sys.platform}' (Y/N)? ").upper()

if userConfirmation == "Y":
    print("Proceeding with installation...")

    #For loop. Loop through all items packages) in list
    for index in range(len(packagesToInstallList)):
        print (f"in loop with package: {packagesToInstallList[index]}")
        os.system(f"sudo yum install -y {packagesToInstallList[index]}")

    # do we really need the index though?
    input ("Press any key to continue ...")  # Pause

    for package in packagesToInstallList:
        print (f"in loop with package: {package}")
        os.system(f"sudo yum install -y {package}")

elif userConfirmation == "N":
    print("Installation canceled.")
    sys.exit(0)  # Exit successfully
else:
    print("Invalid input. Exiting...")
    sys.exit(1)  # Exit with error

sys.exit(0)