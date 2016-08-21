from django.db import models

class Recommendation(models.Model):
    address = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True)
    tag = models.CharField(max_length=35, blank=True)
    recommender = models.CharField(max_length=100, blank=True)
    recorder = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True

class Article(Recommendation):
    pass

class Video(Recommendation):
    pass

class Podcast(Recommendation):
    pass
