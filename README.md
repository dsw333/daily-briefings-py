# Weather SMS Service (Python)

Sends you a customized SMS message, with information of interest based on the upcoming weather forecast.

## Setup

Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/daily-briefings-py/
```

Create and activate a new Anaconda virtual environment, perhaps named "briefings-env":

```sh
conda create -n briefings-env python=3.7
conda activate briefings-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt

Make sure that you pip install Twilio 
```

Obtain API Keys from the [Open Weather](https://home.openweathermap.org/api_keys), and [Twilio](https://www.twilio.com/docs/sms/quickstart/python) services. Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# .env example

APP_ENV="development" # or set to "production" on Heroku server

OPEN_WEATHER_API_KEY="___________"
MY_ZIP="10017"

account_sid = 'ACXXXXXXXXXXX'
auth_token = 'acXXXXXXXXXXX'

SENDER_SMS = "+12058272450"
RECIPIENT_SMS = "+XXXXXXXXXXXXX"
#MY_NAME="DAN"
```

> IMPORTANT: remember to save the ".env" file :-D

## Usage

From within the virtual environment, ensure you can run each of the following files and see them produce their desired results of: printing today's weather forecast, and sending an example SMS, respectively.

```sh
python -m app.weather_service # note the module-syntax invocation
#> TODAY'S WEATHER FORECAST IS ...
```

```sh
python -m app.sms_service # note the module-syntax invocation
#> SENDING SMS TO ...
```

As long as each of those scripts works by itself, you can send the daily briefing email:

```sh
python -m app.daily_briefing # note the module-syntax invocation
```
