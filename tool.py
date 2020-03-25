#--- Color  ---#
N = '\033[0m'    # Normal
Y = '\033[1;33m' # Yellow
R = '\033[1;31m' # Red
G = '\033[1;32m' # Green
W = '\033[1;37m' # White
D = '\033[1;9;31m'  # DelBold
#---        ---#
print("%sDEVELOPED BY TANISHQ MISHRA%s" % (Y,N))
print('''%s
 _____ ______   ________  _________  ___  ___  ________           _____ ______   ________  ________  _________  _______   ________     
|\   _ \  _   \|\   __  \|\___   ___\\  \|\  \|\   ____\         |\   _ \  _   \|\   __  \|\   ____\|\___   ___\\  ___ \ |\   __  \    
\ \  \\\__\ \  \ \  \|\  \|___ \  \_\ \  \\\  \ \  \___|_        \ \  \\\__\ \  \ \  \|\  \ \  \___|\|___ \  \_\ \   __/|\ \  \|\  \   
 \ \  \\|__| \  \ \   __  \   \ \  \ \ \   __  \ \_____  \        \ \  \\|__| \  \ \   __  \ \_____  \   \ \  \ \ \  \_|/_\ \   _  _\  
  \ \  \    \ \  \ \  \ \  \   \ \  \ \ \  \ \  \|____|\  \        \ \  \    \ \  \ \  \ \  \|____|\  \   \ \  \ \ \  \_|\ \ \  \\  \| 
   \ \__\    \ \__\ \__\ \__\   \ \__\ \ \__\ \__\____\_\  \        \ \__\    \ \__\ \__\ \__\____\_\  \   \ \__\ \ \_______\ \__\\ _\ 
    \|__|     \|__|\|__|\|__|    \|__|  \|__|\|__|\_________\        \|__|     \|__|\|__|\|__|\_________\   \|__|  \|_______|\|__|\|__|
                                                 \|_________|                                \|_________|                              
                                                                                                                                       
                                                                                                                                       
 %s ''' % (R,N))
print("%sDEVELOPER:- Tanishq Mishra%s" % (Y,N))
print("Hello world")
print("I am computer")
print("%sI can help you in Mathematics%s" % (G,N))
# This is Just a programme
print("[1] Addition")
print("[2] Subtraction")
print("[3] Multiplication")
print("[4] Division")
a=input("Enter Your Operation ")
if (a is 1) : 
   import A
if (a is 2) : 
   import S
if (a is 3) : 
   import M
if (a is 4) : 
   import D
