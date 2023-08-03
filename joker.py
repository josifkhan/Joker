from platform import architecture as arch
import sys
if '64bit' in arch():import reg
else:sys.exit('\033[38;5;208m [+] Your device is not supported for this tool.\033[38;5;188mContact admin (facebook.com/josifvai)\033[0m')
	