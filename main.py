from tkinter import *
import requests

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
WHITE = "white"
GREEN = "#9bdeac"
FONT_NAME = "Courier"

# ---------------------------- FUNCTIONALITY ------------------------------- #

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_data():
    # Get city from the input field
    city = location_input.get()

    # Check if a city is entered
    if city:
        api_key = 'baaf32ea8d411f79c96498916c8fd970'
        base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        # Make the API request
        response = requests.get(base_url)
        data = response.json()

        # Display the weather information on the GUI
        display_weather_info(data)
    else:
        print("Please enter a city.")

def display_weather_info(data):
    # Extract relevant weather information
    temperature_kelvin = data.get('main', {}).get('temp', 0)
    temperature_celsius = kelvin_to_celsius(temperature_kelvin)
    precipitation = data.get('weather', [{}])[0].get('description')
    wind_speed = data.get('wind', {}).get('speed')

    # Update the UI with weather information
    temperature_label.config(text=f'Temperature: {temperature_celsius:.2f} °C')
    precipitation_label.config(text=f'Precipitation: {precipitation}')
    wind_speed_label.config(text=f'Wind Speed: {wind_speed} m/s')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Weather App")
window.config(padx=100, pady=50, bg=WHITE)

title_label = Label(text="Enter your City Name", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=WHITE)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=WHITE, highlightthickness=0)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

enter_button = Button(width=25, height=2, text="Enter", highlightthickness=0, command=get_data)
enter_button.grid(column=1, row=3)

location_input = Entry()
location_input.grid(column=1, row=1, pady=10)
location_input.config(width=25)

# Labels to display weather information
temperature_label = Label(text="Temperature: ", font=(FONT_NAME, 12), bg=WHITE)
precipitation_label = Label(text="Precipitation: ", font=(FONT_NAME, 12), bg=WHITE)
wind_speed_label = Label(text="Wind Speed: ", font=(FONT_NAME, 12), bg=WHITE)

# Place labels in the window
temperature_label.grid(column=1, row=4)
precipitation_label.grid(column=1, row=5)
wind_speed_label.grid(column=1, row=6)

window.mainloop()
