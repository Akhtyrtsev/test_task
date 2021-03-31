from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'


class Operation(models.Model):
    TRANSACTION_TYPES = (
        ('Purchase', 'Purchase'),
        ('Refund', 'Refund'),
        ('Withdrawal', 'Withdrawal')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operations')
    amount = models.IntegerField(default=0)
    operation_type = models.CharField(max_length=64, choices=TRANSACTION_TYPES, default='Purchase')
    date_created = models.DateTimeField(auto_now_add=True)
