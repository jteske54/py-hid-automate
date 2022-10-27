import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import test_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class root:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("700x100+620+156")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Python HID Automator")
        top.configure(background="#d9d9d9")

        self.top = top

        self.buttonframe = tk.Frame(self.top)
        self.buttonframe.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.buttonframe.configure(relief='groove')
        self.buttonframe.configure(borderwidth="2")
        self.buttonframe.configure(relief="groove")
        self.buttonframe.configure(background="#d9d9d9")

        self.Button1 = tk.Button(self.buttonframe)
        self.Button1.place(relx=0.0, rely=0.0, height=100, width=175)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=test_support.record)
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Record''')

        self.Button2 = tk.Button(self.buttonframe)
        self.Button2.place(relx=0.25, rely=0.0, height=100, width=175)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=test_support.play)
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Play''')

        self.Button3 = tk.Button(self.buttonframe)
        self.Button3.place(relx=0.5, rely=0.0, height=100, width=175)
        self.Button3.configure(activebackground="beige")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=test_support.save_file)
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Save''')

        self.Button4 = tk.Button(self.buttonframe)
        self.Button4.place(relx=0.75, rely=0.0, height=100, width=175)
        self.Button4.configure(activebackground="beige")
        self.Button4.configure(activeforeground="black")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(command=test_support.open_file)
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Open''')
  
def start_up():
    test_support.main()

if __name__ == '__main__':
    test_support.main()
  