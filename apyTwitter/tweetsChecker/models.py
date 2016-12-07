from django.db import models
from .controllers.flag import Flag
from .controllers.filt import Filt

from .controllers.config import logging

class FlagModel(models.Model):
    logging.info('Creation d\'un nouveau FlagModel')
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
        logging.info('Flag %s converti en FlagModel', flag.name)

    def to_flag(self):
        key_words = self.key_words
        logging.info('Conversion du FlagModel %s en objet Flag', self.name)
        return Flag(self.name, key_words.split("+"))

    @staticmethod
    def get_saved_flags():
        logging.info('Récupération des Flags de la base de données')
        saved_flagmodels = FlagModel.objects.all()
        saved_flags = []
        for flag in saved_flagmodels:
            saved_flags.append(flag.to_flag())
        logging.info('%s flags récupérés', len(saved_flags))
        return saved_flags

    @staticmethod
    def delete_flag(name):
        FlagModel.objects.filter(name=name).delete()

    def __str__(self):
        return '{} : {}'.format(self.name, self.key_words)


class FiltModel(models.Model):
    logging.info('Creation d\'un nouveau FiltModel')
    name = models.CharField(max_length=100)
    key_words = models.CharField(max_length=500)
    count = models.IntegerField()

    def to_model(self, filt):
        self.name = filt.name
        self.count = filt.count
        key_words = ""
        for word in filt.key_words:
            if key_words == "":
                key_words = word
            else:
                key_words = key_words + "+" + word
        self.key_words = key_words
        logging.info('Filtre %s converti en FiltModel', self.name)

    def to_filt(self):
        key_words = self.key_words
        logging.info('Conversion du FiltModel %s en objet Filt', self.name)
        return Filt(self.name, key_words.split("+"), self.count)

    @staticmethod
    def get_saved_filt():
        logging.info('Récupération des Filtres de la base de données')
        saved_filtmodels = FiltModel.objects.all()
        saved_filt = []
        for filt in saved_filtmodels:
            saved_filt.append(filt.to_filt())
        logging.info('%s flags récupérés', len(saved_filt))
        return saved_filt

    @staticmethod
    def delete_filt(name):
        FiltModel.objects.filter(name=name).delete()

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.count, self.key_words)