from django.db import models


class Lesson(models.Model):
    timeStatus = models.FloatField(default=True)
    watched = models.BooleanField(default=True)

    def __str__(self):
        return self.title
