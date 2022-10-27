from turtle import width
import pyautogui
import pynput
import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("700x100")
    root.title("Python HID Automator")
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0,weight=1)
    buttonframe.columnconfigure(1,weight=1)
    buttonframe.columnconfigure(2,weight=1)
    buttonframe.columnconfigure(3,weight=1)
    btn_record = tk.Button(buttonframe, text="Record")
    btn_record.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
    btn_play = tk.Button(buttonframe, text="Play")
    btn_play.grid(row=0, column=1, sticky=tk.W+tk.E+tk.N+tk.S)
    btn_save = tk.Button(buttonframe, text="Save")
    btn_save.grid(row=0, column=2, sticky=tk.W+tk.E+tk.N+tk.S)
    btn_open = tk.Button(buttonframe, text="Open")
    btn_open.grid(row=0, column=3, sticky=tk.W+tk.E+tk.N+tk.S)
    buttonframe.pack(fill='both')
    root.mainloop()

if __name__ == "__main__":
    main()