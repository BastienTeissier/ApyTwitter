import json, base64, requests

from ..controllers.config import userKey, secretKey, logging
from ..controllers.tweet import Tweet


class ComTwitter:

    def __init__(self):

        #Génération de la clé et authentification auprès de Twitter
        logging.info('Creation d\'un ComTwitter')
        s = userKey + ':' + secretKey
        logging.debug('userKey : secretKey = %s',s)
        s64 = base64.b64encode(bytes(s.encode()))
        logging.debug('After encoding : %s', s64)
        s = str(s64.decode())
        logging.debug('s = %s', s)
        headers = {
            'Authorization' : 'Basic ' + s,
            'Content-Type' : 'application/x-www-form-urlencoded',
            'User-Agent' : 'ApyTwitter v1.0'
        }
        data = {
            'grant_type' : 'client_credentials'
        }
        r = requests.post('https://api.twitter.com/oauth2/token', headers = headers, data = data)
        logging.info('r.text : %s', r.text)
        self.token_bearer = json.loads(r.text)['access_token']

    def tokenBearer(self):
        print(self.token_bearer)

    # Fonction gérant la requête à Twitter
    def makeGetRequest(self, url, filt):
        logging.info('Fait une requête GET avec le filtre %s', filt)
        data = filt
        headers = {
            'Authorization' : 'Bearer ' + self.token_bearer,
            'Content-Type' : 'application/x-www-form-urlencoded',
            'User-Agent' : 'ApyTwitter v1.0'
        }
        r = requests.get(url, headers = headers, params=data)
        logging.info('Résultat obtenu = %s', r)
        return self.generateTweet(r)

    def extractHashtags(self, hashtags):
        r = []
        for l in hashtags:
            r.append(l["text"])
        return r

    # Genère les objets tweet à partir des données reçues de Tweeter
    def generateTweet(self, r):
        logging.info('Generating Tweets')
        j = json.loads(r.text)
        ts = j["statuses"]
        l = []
        for t in ts:
            l.append(Tweet(
                str(t["text"]),
                self.extractHashtags(t["entities"]["hashtags"]),
                str(t["created_at"].encode('utf-8')),
                t["geo"],
                str(t["user"]["name"]),
                int(t["user"]["followers_count"])
            ))
        logging.info('%s Tweets ont été générés', len(l))
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
