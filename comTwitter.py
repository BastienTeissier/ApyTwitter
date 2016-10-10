import config, json, base64, requests

class comTwitter:

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

    def makeGetRequest(self, url, hashtag):
        data = {
            'q' : hashtag
        }
        headers = {
            'Authorization' : 'Bearer ' + self.token_bearer,
            'Content-Type' : 'application/x-www-form-urlencoded',
            'User-Agent' : 'ApyTwitter v1.0'
        }
        r = requests.get(url, headers = headers)
        return r

if __name__ == "__main__":
    cT = comTwitter()
    cT.tokenBearer()
    r = cT.makeGetRequest('https://api.twitter.com/1.1/search/tweets.json?q=Trump&count=100', 'Trump')
    j = json.loads(r.text)
    tweets = j["statuses"]
    for tweet in tweets:
        print(str(tweet['text'].encode('utf-8')))
