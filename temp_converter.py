import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    """
    Handles the temperature conversion logic and updates the UI.
    """
    try:
        # Get the input value and validate it as a number
        temp_str = entry_temp.get()
        if not temp_str:
            messagebox.showerror("Invalid Input", "Please enter a temperature.")
            return

        temp = float(temp_str)
        unit = var_unit.get()
        
        converted_temp = None
        converted_unit = ""

        if unit == "fahrenheit":
            # Convert Fahrenheit to Celsius
            converted_temp = (temp - 32) * 5/9
            converted_unit = "°C"
        elif unit == "celsius":
            # Convert Celsius to Fahrenheit
            converted_temp = (temp * 9/5) + 32
            converted_unit = "°F"

        # Update the result label with the converted temperature
        result_label.config(text=f"{converted_temp:.2f}{converted_unit}")
        
    except ValueError:
        # Show an error if the input is not a valid number
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Set up the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")
root.config(padx=20, pady=20)

# Main label
title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input frame
input_frame = tk.Frame(root)
input_frame.pack()

# Input field for temperature
label_temp = tk.Label(input_frame, text="Enter Temperature:", font=("Arial", 10))
label_temp.pack(side=tk.LEFT)
entry_temp = tk.Entry(input_frame, width=10)
entry_temp.pack(side=tk.LEFT, padx=5)

# Radio buttons for unit selection
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

var_unit = tk.StringVar(value="fahrenheit") # Default value

radio_fahrenheit = tk.Radiobutton(radio_frame, text="Fahrenheit", variable=var_unit, value="fahrenheit")
radio_fahrenheit.pack(side=tk.LEFT, padx=5)

radio_celsius = tk.Radiobutton(radio_frame, text="Celsius", variable=var_unit, value="celsius")
radio_celsius.pack(side=tk.LEFT, padx=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature, font=("Arial", 12))
convert_button.pack(pady=10)

# Display area for the result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack()

# Start the main event loop
root.mainloop()