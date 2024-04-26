#from modules.login_steps import enter_username, enter_password
from modules.login_steps import *
# from <source pacakge> import <function, class name or simply *>

import time

#Calling the functions/execution
enter_username('john')
enter_password()
click_login()
time.sleep(2) #hold the execution for 15 seconds
logout()
