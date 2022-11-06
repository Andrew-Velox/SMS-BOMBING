import os, platform
os.system('git pull')
try:
    import requests
except:
    os.system('pip2 install requests')

import V3_BOMBING
V3_BOMBING.main()
