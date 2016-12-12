# smart_alarm
Alarm clock to run off of a raspberry pi

Before running for the first time, ensure that you have a client_secret file for your google calendar.

Next, ensure that you have a secret_config.json file in this directory. An easy solution is just `cp example_config.json secret_config.json` and fill in the appropriate fields. 

To setup everything for your pi, run `setup`. 

## Testing

`python3 TestAlarm.py` will allow you to easily test the application without having to wait for the alarm to go off.

# APIS

All services are found in the Alarm initialization. You can add or remove services in the initialization.

## Google Calendar

https://calendar.google.com

Google Calendar API communicates using the OAuth protocol. Follow the steps outlined [here](https://developers.google.com/identity/protocols/OAuth2) to enable OAuth 2 for your Google Account. You will need to [create credentials](https://console.developers.google.com/apis/credentials) and download the JSON formatted key. Name this file `client_secret.json` and place it at the root of the directory.

The first time you run the application, you will need to click a confirmation screen in order to allow access to your google account. After this initial consent, you will no longer be prompted.

## Weather API

WeatherAPI uses https://openweathermap.org/api You'll need to setup an api key to use this.

## Quote of the Day

Quote of the day brought to us by 
<span style="z-index:50;font-size:0.9em;"><img
src="https://theysaidso.com/branding/theysaidso.png" height="20" width="20"
alt="theysaidso.com"/><a href="https://theysaidso.com" title="Powered by quotes
from theysaidso.com" style="color: #9fcc25; margin-left: 4px; vertical-align:
middle;">theysaidso.com</a></span> There is no api key associated with this, so it should have no problem using this as a test.

# Demo

You can see the alarm in action at https://www.youtube.com/watch?v=4ISQs9f4q-Y

# Authors

Brought to you by Shayde Nofziger and Bryon Wilkins for CMPE-240 final project.
