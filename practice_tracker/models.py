from django.db import models

# Create your models here.

class Performer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__ (self):
        return f"{self.name}"

class Practice_session(models.Model):
    length = models.PositiveIntegerField(default=0)

    # Foreign Key
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE)

    def __str__(self):
        return f"I am {self.performer} and this practice session was {self.length} minute(s) long."