import tkinter as tk

calculator_window = tk.Tk()
calculator_window.title("Simple Calculator")
calculator_window.geometry("300x400")

n1 = tk.StringVar()
n2 = tk.StringVar()
n3 = tk.StringVar()


def add():
    num1 = float(n1.get())
    num2 = float(n2.get())
    sum = num1 + num2
    n3.set(str(sum))


# create Widgets
label1 = tk.Label(calculator_window, text="Enter 1st number:", font=["Arial", 12])
label2 = tk.Label(calculator_window, text="Enter 2nd number:", font=["Arial", 12])
label3 = tk.Label(calculator_window, text="Result:", font=["Arial", 12])

entry1 = tk.Entry(calculator_window, textvariable=n1)
entry2 = tk.Entry(calculator_window, textvariable=n2)
entry3 = tk.Entry(calculator_window, textvariable=n3)

button_add = tk.Button(calculator_window, text="Add", command=add)
label_result = tk.Label(calculator_window, text="Result:", font=["Arial", 12])
entry_result = tk.Entry(calculator_window, textvariable=n3)

# place Widgets
label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

button_add.grid(row=2, columnspan=2, padx=10, pady=10)

label3.grid(row=3, column=0, padx=10, pady=10)
entry3.grid(row=3, column=1, padx=10, pady=10)


calculator_window.mainloop()
