import keys
import requests
import tweepy
import datetime
from keys import * #for your api keys and such

kahului_url = "https://api.darksky.net/forecast/" + darksky_api_key + "/20.8894,-156.4727"
kihei_url = "https://api.darksky.net/forecast/" + darksky_api_key + "/20.7644,-156.4450"
lahaina_url = "https://api.darksky.net/forecast/" + darksky_api_key + "/20.8783,-156.6825"
kula_url = "https://api.darksky.net/forecast/" + darksky_api_key + "/20.7910,-156.3269"

kahului_data = requests.get(kahului_url).json()
kihei_data = requests.get(kihei_url).json()
lahaina_data = requests.get(lahaina_url).json()
kula_data = requests.get(kula_url).json()

high_temp_kahului = kahului_data['daily']['data'][0]['temperatureMax']
timestamp_kahului = kahului_data['daily']['data'][0]['time']
date = str(datetime.date.fromtimestamp(timestamp_kahului))

high_temp_kihei = kihei_data['daily']['data'][0]['temperatureMax']
high_temp_lahaina = lahaina_data['daily']['data'][0]['temperatureMax']
high_temp_kula = kula_data['daily']['data'][0]['temperatureMax']

message = "Max Temps in Maui for " + date + ":\n\n" + "Kahului: " + str(high_temp_kahului) + " F\n" + "Kihei: " + str(high_temp_kihei) + " F\n" + "Lahaina: " + str(high_temp_lahaina) + " F\n" + "Kula: " + str(high_temp_kula) + " F\n"



account = tweepy.OAuthHandler(consumer_key, consumer_secret)
account.set_access_token(access_token, access_token_key)
bot = tweepy.API(account)

bot.update_status(message)





#TO DO
# run on server
# Custom messages based on very high temperatures or windy days
# maybe add wind data later, or UV index data, and add Coolest and warmest areas, feels like temp, date format, current data