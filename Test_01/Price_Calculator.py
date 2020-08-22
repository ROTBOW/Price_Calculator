
### Price calculator for 3D printing micro business ###
import tkinter as tk

window = tk.Tk(); window.title('Bear-Printing Price Calculator')

# x is for hours, y is for minutes
def time_convert( x, y ):
    hours = x * 60
    minutes = y
    time_in_mins = hours + minutes
    return(time_in_mins)

# x is for time, y is for plastic cost
def cost_cal( x, y ):
    time_cost = x * float(0.03)
    plastic_cost = y * float(1.5)
    total_cost = time_cost + plastic_cost
    return(total_cost)

def Quit(event):
    window.destroy()

# Main math cal
def working(event):
    hours = e1.get(); minutes = e2.get(); plastic = e3.get()
    time_in_min = time_convert(float(hours), float(minutes))
    Cost = cost_cal(float(time_in_min), float(plastic))
    l1.config(text = 'Bear-Printing Calculator!\nPlease enter the time and plastic cost\n Estimated cost: $' + str(round(Cost, 2)))


# GUI setup
f1 = tk.Frame(master = window,
              width = 250,
              height = 250, 
              relief = tk.RAISED,
              borderwidth = 5
              ); f1.pack(fill = tk.BOTH)

f2 = tk.Frame(master = window,
              width = 250,
              height = 250,
              relief = tk.GROOVE,
              borderwidth = 5
              ); f2.pack(fill = tk.BOTH, side = 'right')

l1 = tk.Label(master = f1,
              width = 50,
              height = 5,
              relief = tk.SUNKEN,
              borderwidth = 5,
              text = 'Bear-Printing Calculator!\nPlease enter the time and plastic cost\n Estimated cost: $0.0'
              ); l1.pack(side = 'top', fill = tk.BOTH)

e1 = tk.Entry(master = f2,
              width = 10
              ); e1.insert(0, '0') ;e1.grid(row = 0, column = 1)

l2 = tk.Label(master = f2,
               width = 10,
               height = 1,
               text = 'Time (Hours)',
               ); l2.grid(row = 0, column = 0)

e2 = tk.Entry(master = f2,
              width = 10,
              ); e2.insert(0, '0');e2.grid(row = 1, column = 1)

l3 = tk.Label(master = f2,
              width = 11,
              height = 1,
              text = 'Time (minutes)',
              ); l3.grid(row = 1, column = 0)

e3 = tk.Entry(master = f2,
              width = 10,
              ); e3.insert(0, '0');e3.grid(row = 2, column = 1)

l4 = tk.Label(master = f2,
              width = 10,
              height = 1,
              text = 'Plastic Cost',
              ); l4.grid(row = 2, column = 0)


f3 = tk.Frame(master = window); f3.pack(side = 'left')

b1 = tk.Button(master = f3,
               width = 30,
               height = 2,
               text = 'Compute',
               relief = tk.RAISED,
               borderwidth = 2
               ); b1.pack(fill = tk.BOTH, expand = True)


b2 = tk.Button(master = f3,
               width = 30,
               height = 2,
               text = 'Quit',
               relief = tk.RAISED,
               borderwidth = 2
               ); b2.pack(side = 'bottom', fill = tk.BOTH, expand = True)

b2.bind('<ButtonRelease-1>', Quit)

b1.bind('<Button-1>', working)

window.mainloop()