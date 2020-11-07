import tkinter as tk 
from tkinter import ttk
import numpy as np
from metaheuristics.bees import BeesAlgorithm
from metaheuristics.bat import BatAlgorithm
from metaheuristics.firefly import FireflyAlgorithm

rosenbrock_fct = lambda x: sum([100*(x[i+1]-x[i])**2+(1-x[i])**2 for i in range(len(x)-1)])
sphere_fct = lambda x: x[0]**2 + x[1]**2
rastrigin_fct = lambda x: 10*len(x)+sum([x[i]**2-10*np.cos(2*np.pi*x[i]) for i in range(len(x))])
himmelblau_fct = lambda x: (x[0]**2+x[1]-11)**2+(x[0]+x[1]**2-7)**2
beale_fct = lambda x: (1.3-x[0]+x[0]*x[1])**2+(2.25-x[0]+x[0]*x[1]**2)**2+(2.625-x[0]+x[0]+x[1]**3)**2
x_fct = lambda x: 1/x[0] + 1/x[1]

def firefly_second():
    objective_fct = rastrigin_fct
    window = tk.Tk() 
    window.title('Firefly Algorithm') 
    window.geometry('850x600')
    window.config(bg="White")

    ttk.Label(window, text = "FirefLy Algorithm",  background = 'White', foreground ="#8b0bdb",  font = ("Comic Sans MS", 25)).grid(row = 0,column = 0,columnspan=5,padx =16)
    # FF = open(r'overview-txt/about_firefly.txt','r')
    # ttk.Label(window,text = FF.read(),background='White',foreground= 'Black', font = ('Comic Sans MS',10)).grid(row=1,column = 0,columnspan=5,padx=16)
    ttk.Label(window, text = "Select the function to be optimised :",  
        font = ("Comic Sans MS", 10, 'bold')).grid(column = 0,row = 1, padx = 10, pady = 20) 
  
    n = tk.StringVar() 
    algochoosen = ttk.Combobox(window, width = 27, textvariable = n)  
    algochoosen['values'] = ('Rosenbrock Function','Sphere Function', 'Rastrigin Function', 'Himmelblau Function','Beale Function','x**2+ 2*x +1') 
    algochoosen.grid(row= 1, column =1,padx=16,pady=20)
    def hello(self):
        if algochoosen.get() == 'Rosenbrock Function':
            objective_fct = rosenbrock_fct
        if algochoosen.get() == 'Sphere Function':
            objective_fct = sphere_fct
        if algochoosen.get() == 'Rastrigin Function':
            objective_fct = rastrigin_fct
        if algochoosen.get() == 'Himmelblau Function':
            objective_fct = himmelblau_fct
        if algochoosen.get() == 'Beale Function':
            objective_fct = beale_fct
        if algochoosen.get() == 'x**2+ 2*x +1':
            objective_fct = x_fct
    algochoosen.bind("<<ComboboxSelected>>", hello)
    objective = 'min'
    n, d = 50, 2
    range_min, range_max = (-5, -5), (5, 5)
    T = 150
    def firefly_work():

        firefly1 = FireflyAlgorithm(d=d, n=n, range_min=range_min, range_max=range_max,alpha=0.5, beta_max=1.0, gamma=0.5)
        solution, latency = firefly1.search(objective, objective_fct, T)
        firefly1.plot_history(window)
        algo.generate_gif()
        text = str(firefly1.best_solution)
        tk.Label(window,text=text).grid(row=2,column=5)
    tk.Button(window,text = 'Start', command = firefly_work).grid(row=1,column = 2,padx=16,pady=20)
    window.mainloop()

def Bees_second():
    objective_fct = rastrigin_fct
    window = tk.Tk() 
    window.title('Bee Colony Optimisation') 
    window.geometry('850x600')
    window.config(bg="White")

    ttk.Label(window, text = "Bee Colony Optimsation",  background = 'White', foreground ="#8b0bdb",  font = ("Comic Sans MS", 25)).grid(row = 0,column = 0,columnspan=5,padx =16)
    # FF = open(r'overview-txt/about_firefly.txt','r')
    # ttk.Label(window,text = FF.read(),background='White',foreground= 'Black', font = ('Comic Sans MS',10)).grid(row=1,column = 0,columnspan=5,padx=16)
    ttk.Label(window, text = "Select the function to be optimised :",  
        font = ("Comic Sans MS", 10, 'bold')).grid(column = 0,row = 1, padx = 10, pady = 20) 
  
    n = tk.StringVar() 
    algochoosen = ttk.Combobox(window, width = 27, textvariable = n)  
    algochoosen['values'] = ('Rosenbrock Function','Sphere Function', 'Rastrigin Function', 'Himmelblau Function','Beale Function','x**2+ 2*x +1') 
    algochoosen.grid(row= 1, column =1,padx=16,pady=20)
    def hello(self):
        if algochoosen.get() == 'Rosenbrock Function':
            objective_fct = rosenbrock_fct
        if algochoosen.get() == 'Sphere Function':
            objective_fct = sphere_fct
        if algochoosen.get() == 'Rastrigin Function':
            objective_fct = rastrigin_fct
        if algochoosen.get() == 'Himmelblau Function':
            objective_fct = himmelblau_fct
        if algochoosen.get() == 'Beale Function':
            objective_fct = beale_fct
        if algochoosen.get() == 'x**2+ 2*x +1':
            objective_fct = x_fct
    algochoosen.bind("<<ComboboxSelected>>", hello)
    
    objective = 'min'
    n, d = 50, 2
    range_min, range_max = (-5, -5), (5, 5)
    T = 150
    def bee_work():

        bees1 = BeesAlgorithm(d=d, n=n, range_min=range_min, range_max=range_max,
                     nb=int(0.3*n), ne=int(0.1*n), nrb=int(0.1*n), nre=int(0.2*n))
        solution, latency = bees1.search(objective, objective_fct, T)
        bees1.plot_history(window)
        bees1.generate_gif()
        text = str(bees1.best_solution)
        tk.Label(window,text=text).grid(row=2,column=5)
    tk.Button(window,text = 'Start', command = bee_work).grid(row=2,column = 2,padx=16,pady=20)
    window.mainloop()
    
def Bat_second():
    objective_fct = rastrigin_fct
    window = tk.Tk() 
    window.title('Bat Optimisation') 
    window.geometry('850x600')
    window.config(bg="White")

    ttk.Label(window, text = "Bat Optimsation",  background = 'White', foreground ="#8b0bdb",  font = ("Comic Sans MS", 25)).grid(row = 0,column = 0,columnspan=5,padx =16)
    # FF = open(r'overview-txt/about_firefly.txt','r')
    # ttk.Label(window,text = FF.read(),background='White',foreground= 'Black', font = ('Comic Sans MS',10)).grid(row=1,column = 0,columnspan=5,padx=16)
    ttk.Label(window, text = "Select the function to be optimised :",  
        font = ("Comic Sans MS", 10, 'bold')).grid(column = 0,row = 1, padx = 10, pady = 20) 
  
    n = tk.StringVar() 
    algochoosen = ttk.Combobox(window, width = 27, textvariable = n)  
    algochoosen['values'] = ('Rosenbrock Function','Sphere Function', 'Rastrigin Function', 'Himmelblau Function','Beale Function','x**2+ 2*x +1') 
    algochoosen.grid(row= 1, column =1,padx=16,pady=20)
    def hello(self):
        if algochoosen.get() == 'Rosenbrock Function':
            objective_fct = rosenbrock_fct
        if algochoosen.get() == 'Sphere Function':
            objective_fct = sphere_fct
        if algochoosen.get() == 'Rastrigin Function':
            objective_fct = rastrigin_fct
        if algochoosen.get() == 'Himmelblau Function':
            objective_fct = himmelblau_fct
        if algochoosen.get() == 'Beale Function':
            objective_fct = beale_fct
        if algochoosen.get() == 'x**2+ 2*x +1':
            objective_fct = x_fct
    algochoosen.bind("<<ComboboxSelected>>", hello)
    
    objective = 'min'
    n, d = 50, 2
    range_min, range_max = (-5, -5), (5, 5)
    T = 150
    def bat_work():

        bat1 = BatAlgorithm(d=d, n=n, range_min=range_min, range_max=range_max,a=10.0, r_min=0.5, r_max=1.0, alpha=0.99, gamma=0.9, f_min=1.0, f_max=5.0)

        solution, latency = bat1.search(objective, objective_fct, T)
        bat1.plot_history(window)
        bat1.generate_gif()
        text = str(bees1.best_solution)
        tk.Label(window,text=text).grid(row=2,column=5)
    tk.Button(window,text = 'Start', command = bee_work).grid(row=2,column = 2,padx=16,pady=20)
    window.mainloop()


