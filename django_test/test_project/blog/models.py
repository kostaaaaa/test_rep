from django.db import models


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    username = models.CharField(max_length=60, default='Anonymous')

    def __str__(self):
        return f'{self.id}, {self.text[:7]}, {self.pub_date}'
