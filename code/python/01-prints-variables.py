# Variable declaration and assignment - CONSTANTS
PACKAGE_TO_INSTALL='tree'
NUM_OF_PACKAGES_TO_INTSALL=1

# variables (not constants)
userConfirmation = ''   # Holds response from user on command line interface (CLI)

print ("Will install package " + PACKAGE_TO_INSTALL)
print ("Total number of packages to install: {} ".format(NUM_OF_PACKAGES_TO_INTSALL))

userConfirmation = input("Please confirm you want to install (Y/N)? ")

print (f'User confirmation answer is "{userConfirmation}" for package "{PACKAGE_TO_INSTALL}"')

# What do you think, could come next?

exit(0)