import os,platform
os.system("git pull")
##os.system("xdg-open https://chat.whatsapp.com/D3Xd6IztOyi9Jg53G98Cjx")
os.system('clear')
bit = platform.architecture()[0]
if bit=='64bit':
    import DemoPaid
elif bit=='32bit':
    import DemoPaid
