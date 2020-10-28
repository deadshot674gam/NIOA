from tkinter import ttk 

def main():
    import tkinter as tk 
    from tkinter import ttk 
  
    # Creating tkinter window 
    window = tk.Tk() 
    window.title('Nature Inspired Optimization Algorithms') 
    window.geometry('500x500') 
  
    # label text for title 
    ttk.Label(window, text = "Nature Inspired Optimization Algorithms",  background = 'green', foreground ="white",  font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
  
    # label 
    ttk.Label(window, text = "Select the Month :", font = ("Times New Roman", 10)).grid(column = 0, row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December') 
  
monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current() 
window.mainloop() 

