from django.db import models
from django.utils import timezone

class Recommendation(models.Model):
    address     = models.CharField(max_length=200)
    title       = models.CharField(max_length=200, blank=True)
    tag         = models.CharField(max_length=35, blank=True)
    recommender = models.CharField(max_length=100, blank=True)
    recorder    = models.CharField(max_length=100, blank=True)
    created_at  = models.DateTimeField(editable=False, default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        return super(Recommendation, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class Article(Recommendation):
    pass

class Video(Recommendation):
    pass

class Podcast(Recommendation):
    pass
