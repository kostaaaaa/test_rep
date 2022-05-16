from django.db import models


class Message(models.Model):
    message_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.id}, {self.message_text[:7]}, {self.pub_date}'
