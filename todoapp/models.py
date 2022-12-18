from django.db import models

# Create your models here.
class todo(models.Model):
    task=models.CharField(max_length=35)
    description=models.CharField(max_length=250)
    completed=models.BooleanField(default=False)
    class Meta:
        ordering=['-task','-description']
    def __str__(self):
        return self.task
    