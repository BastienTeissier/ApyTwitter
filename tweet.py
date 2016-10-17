class Tweet:
    def __init__(self, text, hashtags, date, location, user_name, user_follower_count):
        self._text = text
        self._hashtags = hashtags
        self._date = date
        self._location = location
        self._user_name = user_name
        self._user_follower_count = user_follower_count
        self.etiquettes=[]

    # Créer des properties pour tous les attributs sauf etiquette

    @property
    def text(self):
        return self._text
  
    @property
    def hashtags(self):
        return self._hashtags
    
    @property
    def date(self):
        return self._date
    
    @property
    def location(self):
        return self._location
    
    @property
    def user_name(self):
        return self._user_name
        
    @property
    def user_follower_count(self):
        return self._user_follower_count
