import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import test

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1, _w2, _w3
    _top1 = root
    _w1 = test.root(_top1)
    _w2 = test.root(_top1)
    _w3 = test.root(_top1)
    root.mainloop()

def open_file(*args):
    print('test_support.open_file')
    for arg in args:
        print ('	another arg:', arg)
    sys.stdout.flush()

def play(*args):
    print('test_support.play')
    for arg in args:
        print ('	another arg:', arg)
    sys.stdout.flush()

def record(*args):
    print('test_support.record')
    for arg in args:
        print ('	another arg:', arg)
    sys.stdout.flush()

def save_file(*args):
    print('test_support.save_file')
    for arg in args:
        print ('	another arg:', arg)
    sys.stdout.flush()

if __name__ == '__main__':
    test.start_up()