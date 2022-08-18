from django.db import models


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    user = models.ForeignKey('members.CustomUser', on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField('members.CustomUser', related_name='liked_posts', blank=True)

    def __str__(self):
        return f'{self.text[:7]}, {self.pub_date}'
