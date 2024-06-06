from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    # id = models.BigAutoField(primary_key=True, editable=False) 
    email = models.EmailField(
        max_length=255, verbose_name=_("Email Address"), unique=True
    )
    fullname = models.CharField(max_length=100, verbose_name=_("Fullname"))
    matricule = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  # the password is the same as matricule
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["fullname"]

    objects = UserManager()

    def tokens(self):    
        refresh = RefreshToken.for_user(self)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }


    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.fullname.title()} "

class OneTimePassword(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    otp=models.CharField(max_length=6)
    def __str__(self):
        return f"{self.user.fullname} - otp code"
    



