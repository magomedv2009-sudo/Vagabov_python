try:
    from colorama import Fore, Style, init
    init()         
    COLOR = True   
except ImportError:
    COLOR = False  
