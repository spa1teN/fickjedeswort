import json
import tweepy

#Twitter Authentication
api_key = ""
api_secret = ""
bearer_token = ""
access_token = ""
access_token_secret = ""
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#Word-Picking
file = open("wortliste.txt", encoding="utf-8")

with open("stand.txt", "r") as stand:
    n = int(stand.read())
    print("Stand: " + str(n))
    stand.close()
    pass

lines=file.readlines()

line = lines[n]

output = "fick " + line

print(output)

#Closing
client.create_tweet(text=output)

with open ("stand.txt", 'w') as stand:
    nn = n + 1
    stand.write(str(nn))
    stand.close()
    pass

print("\ntweeted")

