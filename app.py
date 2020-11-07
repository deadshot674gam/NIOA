import tkinter as tk 
from tkinter import ttk
from secondpage import *


def main():
    # Creating tkinter window 
      window = tk.Tk() 
      window.title('Nature Inspired Optimization Algorithms') 
      window.geometry('850x500') 
      main_icon = tk.PhotoImage(file = r'icons/main icon.png')
      window.iconphoto(False,main_icon)
      window.config(bg="White")
      # label text for title 
      ttk.Label(window, text = "Nature Inspired Optimization Algorithms",  background = 'White', foreground ="#8b0bdb",  font = ("Comic Sans MS", 25)).grid(row = 0,column = 0,columnspan=5,padx =16)
      NIOA = open(r'overview-txt/NIOA-main.txt','r')
      ttk.Label(window,text = NIOA.read(),background='White',foreground= 'Black', font = ('Helvetica',8)).grid(row=1,column = 0,columnspan=10,padx=16)
      ffI = tk.PhotoImage(file = r'icons/firefly_button.png')
      ttk.Button(window,text = 'Firefly',image = ffI,command=firefly_second).grid(row=3,column=0, pady = 25,padx=40)
      bees = tk.PhotoImage(file = r'icons/bees_icon.png')
      ttk.Button(window,text = 'Bees',image = bees,command=Bees_second).grid(row=3,column = 1, pady=25,padx = 40)
      bat = tk.PhotoImage(file = r'icons/bat_icon.png')
      ttk.Button(window,text = 'Bat', image = bat).grid(row = 3,column = 2, pady = 25 , padx= 40)    
      window.mainloop() 
main()
