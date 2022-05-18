from django.db import models


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.id}, {self.text[:7]}, {self.pub_date}'
