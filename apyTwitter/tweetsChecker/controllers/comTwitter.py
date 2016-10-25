import json, base64, requests

from ..controllers.config import userKey, secretKey

from ..controllers.tweet import Tweet

class ComTwitter:

    def __init__(self):
        s = userKey + ':' + secretKey
        print(s)
        s64 = base64.b64encode(bytes(s.encode()))
        print(s64)
        s = str(s64.decode())
        print(s)
        headers = {
            'Authorization' : 'Basic ' + s,
            'Content-Type' : 'application/x-www-form-urlencoded',
            'User-Agent' : 'ApyTwitter v1.0'
        }
        data = {
            'grant_type' : 'client_credentials'
        }
        r = requests.post('https://api.twitter.com/oauth2/token', headers = headers, data = data)
        print(r.text)
        self.token_bearer = json.loads(r.text)['access_token']

    def tokenBearer(self):
        print(self.token_bearer)

    # Corriger les erreurs, faire marcher filtre
    def makeGetRequest(self, url, filt):
        data = filt
        headers = {
            'Authorization' : 'Bearer ' + self.token_bearer,
            'Content-Type' : 'application/x-www-form-urlencoded',
            'User-Agent' : 'ApyTwitter v1.0'
        }
        r = requests.get(url, headers = headers, params=data)
        print(r)
        return self.generateTweet(r)

    def extractHashtags(self, hashtags):
        r = []
        for l in hashtags:
            r.append(l["text"])
        return r

    # Genère les objets tweet à partir des données reçues de Tweeter <!> Encodage
    def generateTweet(self, r):
        j = json.loads(r.text)
        ts = j["statuses"]
        l = []
        for t in ts:
            l.append(Tweet(
                str(t["text"].encode('utf-8')),
                self.extractHashtags(t["entities"]["hashtags"]),
                str(t["created_at"].encode('utf-8')),
                t["geo"],
                str(t["user"]["name"].encode('utf-8')),
                int(t["user"]["followers_count"])
            ))
        print(l)
        return l


if __name__ == "__main__":
    cT = ComTwitter()
    cT.tokenBearer()
    tweets = cT.makeGetRequest('https://api.twitter.com/1.1/search/tweets.json', {
    "q" : "Trump+Hillary",
    "count" : "1000"
    })
    for tweet in tweets:
        print(tweet.text)
        print(tweet.hashtags)
