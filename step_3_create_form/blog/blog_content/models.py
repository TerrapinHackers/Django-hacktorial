from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now = True)
    content = models.TextField()

    def __str__(self):
        return ("Blog Post: " + self.title)

class Comment(models.Model):
    article_id = models.IntegerField()
    date = models.DateTimeField(auto_now = True)
    name = models.CharField(max_length = 100)
    content = models.TextField()
    
    def __str__(self):
        return ("Comment by: " + self.name)
