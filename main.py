import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(sys.path)

from ui.main_window import main_window


def main():

    root = main_window()
    root.mainloop()
    
if __name__ == '__main__': 
    main()