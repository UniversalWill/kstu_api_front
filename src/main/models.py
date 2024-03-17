from django.db import models


class Request(models.Model):
    username = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    response = models.TextField()

    def __str__(self):
        return f"Request by {self.username} at {self.time}"
