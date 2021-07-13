from django.db import models


class Service(models.Model):
    service = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='images/service', null=True, blank=True)

    def __str__(self):
        return self.service
