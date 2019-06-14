from django.db import models
from datetime import datetime

class InfraVltgDetail(models.Model):
    """
    Create Infra VLTG Uses Detail table
    """
    asof = models.DateTimeField(blank=True)
    environment = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    vltg_identity = models.CharField(max_length=200)
    cvproduct = models.CharField(max_length=200)
    cvapi = models.CharField(max_length=200)
    srcip = models.CharField(max_length=200)
    typeofapi = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    create_dt = models.DateTimeField(blank=True)

    def __str__(self):
        return self.username