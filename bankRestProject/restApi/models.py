from django.db import models


class Bank(models.Model):
    name=models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return "{} - {}".format(self.name, self.address)
