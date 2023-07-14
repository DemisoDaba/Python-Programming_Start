# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:52:57 2023

@author: Demiso
"""

import tkinter as tk

def celsius_to_fahrenheit():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32
    result_label.config(text=f"{fahrenheit}°F")

def fahrenheit_to_celsius():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"{celsius}°C")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create the temperature input label and entry widget
temperature_label = tk.Label(window, text="Temperature:")
temperature_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the conversion buttons
celsius_to_fahrenheit_button = tk.Button(window, text="Celsius to Fahrenheit", command=celsius_to_fahrenheit)
celsius_to_fahrenheit_button.pack()

fahrenheit_to_celsius_button = tk.Button(window, text="Fahrenheit to Celsius", command=fahrenheit_to_celsius)
fahrenheit_to_celsius_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
