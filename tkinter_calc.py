import tkinter as tk

root = tk.Tk()
root.title('Calculator')
root.geometry('500x500')

display_box = tk.Entry(root, width=50)
display_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    #display_box.delete(0, tk.END)
    current = display_box.get()
    display_box.insert(0, str(current) + str(number))


button1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=1)


def arithmetics():
    pass


button_sum = tk.Button(root, text="+", padx=40, pady=20, command=lambda: arithmetics)
button_sub = tk.Button(root, text="-", padx=40, pady=20, command=lambda: arithmetics)
button_div = tk.Button(root, text="/", padx=40, pady=20, command=lambda: arithmetics)
button_mult = tk.Button(root, text="*", padx=40, pady=20, command=lambda: arithmetics)
button_equal = tk.Button(root, text="=", padx=40, pady=20, command=lambda: arithmetics)
button_erase = tk.Button(root, text="E", padx=40, pady=20, command=lambda: arithmetics)
button_clear = tk.Button(root, text="C", padx=40, pady=20, command=lambda: arithmetics)

button_sum.grid(row=4, column=0)
button_sub.grid(row=4, column=2)
button_div.grid(row=2, column=3)
button_mult.grid(row=1, column=3)
button_equal.grid(row=5, column=3)
button_erase.grid(row=3, column=3)
button_clear.grid(row=4, column=3)


root.mainloop()
