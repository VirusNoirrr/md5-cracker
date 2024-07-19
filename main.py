import hashlib
from colorama import Fore,Style;blue = Fore.BLUE;red = Fore.RED;warn = Fore.YELLOW;green = Fore.GREEN;gray = Fore.LIGHTBLACK_EX;white_red = Fore.LIGHTRED_EX;white_green = Fore.LIGHTGREEN_EX;white_warn = Fore.LIGHTYELLOW_EX;white_blue = Fore.LIGHTBLUE_EX;reset_colors = Style.RESET_ALL; pink = Fore.MAGENTA
from datetime import datetime
import os; os.system("cls")
found = False
checkedHashes = 0
class Console:
    def __init__(self,debug=False) -> None:
        self.debug = debug
    def error(self,x):
        x = str(x)
        if self.debug:
            print(f"{red}[- ERROR -]{reset_colors} - {gray}[{datetime.now().date()} - {datetime.now().now().strftime('%H:%M:%S')}]{reset_colors} |\t {white_red}{x}{reset_colors}")
        else:
            print(f"{red}[-]{reset_colors}\t {red}{x}{reset_colors}")
    def success(self,x):
        if self.debug:
            print(f"{green}[+ Success +]{reset_colors} - {gray}[{datetime.now().date()} - {datetime.now().now().strftime('%H:%M:%S')}]{reset_colors} |\t {white_green+x}{reset_colors}")
        else:
            print(f"{green}[+]{reset_colors}\t {white_green+x}{reset_colors}")
    def warn(self,x,t=0):
        if self.debug:
            print(f"{warn}[! {'WARNING' if t == 0 else 'FAILED'} !]{reset_colors} - {gray}[{datetime.now().date()} - {datetime.now().now().strftime('%H:%M:%S')}]{reset_colors} |\t {white_warn+x}{reset_colors}")
        else:
            print(f"{warn}[!]{reset_colors}\t {white_warn+x}{reset_colors}")
    def info(self,x):
        if self.debug:
            print(f"{blue}[* INFO *]{reset_colors} - {gray}[{datetime.now().date()} - {datetime.now().now().strftime('%H:%M:%S')}]{reset_colors} |\t {white_blue+x}{reset_colors}")
        else:
            print(f"{blue}[*]{reset_colors}\t {white_blue+x}{reset_colors}")
    def input(self, x):
        if self.debug:
            x = input(f"{blue}[| INPUT |]{reset_colors} - {gray}[{datetime.now().date()} - {datetime.now().now().strftime('%H:%M:%S')}]{reset_colors} |\t {white_blue+x}{reset_colors}{white_warn}")
        else:
            x = input(f"{blue}[|]{reset_colors}\t {white_blue+x}{reset_colors}{white_warn}")
        return x
console = Console(debug=True)
print(pink+f"""
::::    ::::  :::::::::  ::::::::::       ::::::::  :::::::::      :::      ::::::::  :::    ::: :::::::::: :::::::::  {gray}By VirusNoir{pink}
+:+:+: :+:+:+ :+:    :+: :+:    :+:      :+:    :+: :+:    :+:   :+: :+:   :+:    :+: :+:   :+:  :+:        :+:    :+: 
+:+ +:+:+ +:+ +:+    +:+ +:+             +:+        +:+    +:+  +:+   +:+  +:+        +:+  +:+   +:+        +:+    +:+ 
+#+  +:+  +#+ +#+    +:+ +#++:++#+       +#+        +#++:++#:  +#++:++#++: +#+        +#++:++    +#++:++#   +#++:++#:  
+#+       +#+ +#+    +#+        +#+      +#+        +#+    +#+ +#+     +#+ +#+        +#+  +#+   +#+        +#+    +#+ 
#+#       #+# #+#    #+# #+#    #+#      #+#    #+# #+#    #+# #+#     #+# #+#    #+# #+#   #+#  #+#        #+#    #+# 
###       ### #########   ########        ########  ###    ### ###     ###  ########  ###    ### ########## ###    ### 
""")
def hashString(string):
    md5 = hashlib.md5()
    md5.update(string.encode("utf-8"))
    return md5.hexdigest()
wordlist = open("wordlist.txt").read().splitlines()
hash = console.input("MD5 Hash > ")
threads = []
for word in wordlist:
    hashed = hashString(word)
    checkedHashes += 1
    if hashed == hash:
        console.success(f"{gray} {checkedHashes}   | {white_green}Hash cracked --> {white_blue}{word} {gray}({hashed})")
        found = True
        break
    else:
        console.warn(f"{gray} {checkedHashes}   | {white_warn}Invalid : {word} ({hashed})")
console.info(f"Checked {white_green}{checkedHashes}{white_blue} hash and the hash you requested {gray}({hash}){white_blue} was {f'{red}not found' if not found else f'{white_green}found'}")
