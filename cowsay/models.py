from django.db import models

# Create your models here.


class SubmittedText(models.Model):
    input_text = models.CharField(max_length=100)
