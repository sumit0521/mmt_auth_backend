from django.db import models


class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=255, null=False)

    gender = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'user'
        managed = True
        app_label = 'mmt_backend'
