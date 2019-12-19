import sys
import platform

# Version information about the running version of Windows
print("System information from the `sys` module\n")

'''
    sys.getwindowsversion()

    Return: 
        sys.getwindowsversion(major=10, minor=0, build=18362, platform=2, service_pack='')
'''
print("sys.getwindowsversion() - " + str(sys.getwindowsversion()))


# Version information about the running version of Python.
print("sys.implementation - " + str(sys.implementation))

# Show platform information - Possible values are available - https://docs.python.org/3.3/library/sys.html#sys.platform
print("sys.platform - " + str(sys.platform))

# Shows Python version information
print("sys.version - "+str(sys.version))
print("sys.version_info - " + str(sys.version_info))


print("Platform information from the `platform` module\n")
print("platform.platform() - " + str(platform.platform()))
print("platform.system() - " + str(platform.system()))
print("platform.win32_ver() - " + str(platform.win32_ver()))
