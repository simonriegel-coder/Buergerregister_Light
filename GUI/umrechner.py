import tkinter as tk

window2 = tk.Tk()
window2.title("Unit Converter")
window2.geometry("500x500")

km_value = tk.StringVar(value="hier erscheint das Ergebnis ")


miles_label = tk.Label(window2, text="Miles:", font=["Arial", 12])
miles_label.grid(row=0, column=0, padx=10, pady=10)

miles_entry = tk.Entry(window2, font=["Arial", 12])
miles_entry.grid(row=0, column=1, padx=10, pady=10)

km_label = tk.Label(window2, text="Kilometers:", font=["Arial", 12])
km_label.grid(row=1, column=0, padx=10, pady=10)    

km_display = tk.Label(window2, textvariable=km_value, font=["Arial", 12])
km_display.grid(row=1, column=0, padx=10, pady=10)

calculate_button = tk.Button(window2, text="Convert", font=["Arial", 12], command=lambda: convert())
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)


def convert():
    try:
        miles = float(miles_entry.get())
        kilometers = miles * 1.60934
        km_value.set(f"calculated: {kilometers:.2f}")
    except ValueError:
        km_entry.delete(0, tk.END)
        km_entry.insert(0, "Invalid input")

window2.mainloop()