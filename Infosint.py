from socialrecon import reconinput
from webvuln import Webvuln

cyan = "\033[1;36;40m"
green = "\033[1;32;40m"
red = "\033[1;31;40m"
Y = '\033[1;33;40m' 

def Main(a):
    if a == 1:
        reconinput()
    elif a == 2:
        Webvuln()
    else:
        print(red + "Invalid option. Please select a valid module.")

if __name__ == "__main__":
    print(cyan + """
    
$$$$$$\          $$$$$$\                  $$\          $$\     
\_$$  _|        $$  __$$\                 \__|         $$ |    
  $$ | $$$$$$$\ $$ /  \__$$$$$$\  $$$$$$$\$$\$$$$$$$\$$$$$$\   
  $$ | $$  __$$\$$$$\   $$  __$$\$$  _____$$ $$  __$$\_$$  _|  
  $$ | $$ |  $$ $$  _|  $$ /  $$ \$$$$$$\ $$ $$ |  $$ |$$ |    
  $$ | $$ |  $$ $$ |    $$ |  $$ |\____$$\$$ $$ |  $$ |$$ |$$\ 
$$$$$$\$$ |  $$ $$ |    \$$$$$$  $$$$$$$  $$ $$ |  $$ |\$$$$  |
\______\__|  \__\__|     \______/\_______/\__\__|  \__| \____/ 
    """)
    print(Y + "                           Created By : CS03")
    
    print(green + """
                Available Modules 
           
           1. Information gathering,
           2. Web vulnerability scanning,
    """) 
    print(Y + "Note : In Information gathering type 'tools' to find tools.")
    print(Y + "Note : In Web vulnerability scanning type 'help' to find tools.")
    
    try:
        a = int(input("Module >> "))
        Main(a)
    except ValueError:
        print(red + "Invalid input. Please enter a number.")
