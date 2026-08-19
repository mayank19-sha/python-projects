# Weather App 🌤️

A simple Python command-line application that fetches the current weather information for a city using the **OpenWeatherMap API**.

## Features

* Enter any city name
* Get the current temperature
* Get humidity
* Get weather description
* Displays an error message if the request fails

## Requirements

* Python 3.x
* `requests` library
* OpenWeatherMap API key

## Installation

Install the required library:

```bash
pip install requests
```

## How to Run

Run the Python program:

```bash
python weather.py
```

Enter a city name when prompted:

```text
Enter city name: Jaipur
```

Example output:

```text
Temperature: 32.5°C
Humidity: 45%
Weather Description: clear sky
```

## API

This project uses the **OpenWeatherMap Current Weather API**.

You need to create your own API key from OpenWeatherMap and add it to the program.

**Important:** Never upload your API key to GitHub or share it publicly.

A better approach is to store the API key in an environment variable.

## Project Structure

```text
weather-app/
│
├── weather.py
└── README.md
```

## Error Handling

If the API request fails or the city cannot be found, the program displays:

```text
Error fetching weather data.
```

## Technologies Used

* Python
* Requests
* OpenWeatherMap API

## License

This project is for educational purposes.
