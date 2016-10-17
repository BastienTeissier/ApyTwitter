import flag
import tweet


class FlagManager:
    def __init__(self, flags):
        self.flags = flags

    def putFlags(self, tweets):
        for current_flag in self.flags:
            for current_tweet in tweets:
                if all(key_word in current_tweet.text.lower() for key_word in current_flag.key_words):
                    current_tweet.etiquettes.append(current_flag.name)

    def setFlags(self, flags):
        self.flags = flags

if __name__ == "__main__":
    tweet1 = tweet.Tweet("Hello, I am Donald #Hi", "Donald", "yesterday", "New York", "Toto", 150)
    tweet2 = tweet.Tweet("Hello, I am John #6", "John", "today", "New York", "Toto", 150)
    tweets = [tweet1, tweet2]

    flag1 = flag.Flag("Flag1", ["#hi"])
    flags = [flag1]

    Manager = FlagManager(flags)
    Manager.putFlags(tweets)
