class Tweet:
    def __init__(self, text, hashtags, date, location, user_name, user_follower_count):
        self.text = text
        self.hashtags = hashtags
        self.date = date
        self.location = location
        self.user_name = user_name
        self.user_follower_count = user_follower_count
        self.etiquettes=[]

    # Créer des properties pour tous les attributs sauf etiquette
    
