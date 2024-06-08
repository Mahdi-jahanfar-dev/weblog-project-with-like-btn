from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return (f'{self.name} : {self.message[:10]}')