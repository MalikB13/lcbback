from django.db import models


# Create your models here.
class Message(models.Model):
    text = models.TextField()

    def _str_(self):
        return self.text