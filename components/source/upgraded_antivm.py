import getpass
import os
import sys

#Checks if the username is george or abby becuase my tests concluded the VM's always use these usernames (george is the microsoft one and abby is Avira I think)
def check_username():
    username = getpass.getuser()
    if username.lower() in ["Abby", "george"]:
        sys.exit(1)
    else:
        return
