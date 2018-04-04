from django.db import models
# from twstock import Stock
from datetime import datetime
# Create your models here.

class Stockdatas(models.Model):
    created_at = models.DateTimeField(default = datetime.now, blank=True)
