from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length = 200  , null=False)
    finished = models.BooleanField(default = False)


    class Meta:
        db_table = 'Todo'
