import config, json, base64, requests

class ComTwitter:

    def __init__(self):
        s = config.userKey + ':' + config.secretKey
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

    # Genère les objets tweet à partir des données reçues de Tweeter <!> Encodage
    def generateTweet(self, r):
        return r

if __name__ == "__main__":
    cT = ComTwitter()
    cT.tokenBearer()
    r = cT.makeGetRequest('https://api.twitter.com/1.1/search/tweets.json', {
        'q' : '#Samsung+Explosion',
        'count' : '100'
    })
    j = json.loads(r.text)
    tweets = j["statuses"]
    for tweet in tweets:
        print(str(tweet['text'].encode('utf-8')))
