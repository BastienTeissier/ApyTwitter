from django.db import models
from .controllers.flag import Flag

# Create your models here.


class FlagModel(models.Model):
    name = models.CharField(max_length=100)
    key_words = models.CharField(max_length=500)

    def to_model(self, flag):
        self.name = flag.name
        key_words = ""
        for word in flag.key_words:
            if key_words == "":
                key_words = word
            else:
                key_words = key_words + "+" + word
        self.key_words = key_words

    def to_flag(self):
        key_words = self.key_words
        return Flag(self.name, key_words.split("+"))

    @staticmethod
    def delete_flag(name):
        FlagModel.objects.filter(name=name).delete()

    def __str__(self):
        return str(self.name + ": " + self.key_words)
