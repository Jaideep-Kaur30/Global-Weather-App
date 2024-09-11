import tkinter as tk
from tkinter import messagebox, font
import requests

# Function to retrieve weather data
def get_weather():
    api_key = 'my_api_key'
    user_input = city_entry.get()

    try:
        # Make API request
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
        )

        # Check if request was successful
        if weather_data.status_code == 200:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])

            # Display weather information
            weather_label.config(text=f"The weather in {user_input} is: {weather}")
            temp_label.config(text=f"The temperature in {user_input} is: {temp}°F")
        else:
            messagebox.showerror("Error", "City not found. Please enter a valid city name.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
window = tk.Tk()
window.title("Weather App")
window.geometry("400x300")  # Set initial window size

# Set custom fonts
title_font = font.Font(family="Helvetica", size=20, weight="bold")
label_font = font.Font(family="Helvetica", size=12)

# Create and pack widgets
title_label = tk.Label(window, text="Weather App", font=title_font)
title_label.pack(pady=10)

city_label = tk.Label(window, text="Enter city:", font=label_font)
city_label.pack()

city_entry = tk.Entry(window, width=30, font=label_font)
city_entry.pack(pady=5)

get_weather_btn = tk.Button(window, text="Get Weather", command=get_weather, font=label_font, bg="#4CAF50", fg="white")
get_weather_btn.pack(pady=10)

weather_label = tk.Label(window, text="", font=label_font)
weather_label.pack()

temp_label = tk.Label(window, text="", font=label_font)
temp_label.pack()

# Run the main loop
window.mainloop()
