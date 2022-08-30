from django.db import models
from django.contrib.auth import get_user_model

class Animal(models.Model):
    name = models.CharField(max_length=24)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    species = models.CharField(max_length=24)
    description = models.TextField()
    recieved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name