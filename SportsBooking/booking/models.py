from django.db import models

# Create your models here.

class Contact(models.Model):
    TYPES=(
        (1, 'EMAIL'),
        (2, 'PHONE'),
        )
    type = models.IntegerField(choices=TYPES)
    value = models.CharField(max_length=100)

class PType(models.Model):
    UTYPES = (
        (1, 'ADMIN'),
        (2, 'PLAYER'),
        (3, 'HALL'),
        )
    type = models.IntegerField(choices=UTYPES)

class User(models.Model):
    REGISTRATION = (
        (1, 'FACEBOOK'),
        (2, 'TWITTER'),
        (3, 'GOOGLE'),
        (4, 'YAHOO'),
        (5, 'MANUAL'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30, unique=True)
    register_type = models.IntegerField(choices=REGISTRATION)
    remote_id = models.CharField(max_length=500, default='-1')
    contact = models.ForeignKey(Contact)
    ptype = models.ForeignKey(PType)
