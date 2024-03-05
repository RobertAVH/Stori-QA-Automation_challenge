#-*- coding: utf8 -*-
from Config.Config_execution import config_execution
import sys


# Execution file.
# This function is to configurate and run execution

def main():

    if sys.argv[1:]:
        config_execution(sys.argv[1:])
    else:
        config_execution("opera")

if __name__ == '__main__':
    main()
