from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser



class UserManager(BaseUserManager):
    def create_user(self, email, phone_number, password=None):


        user = self.model(
            email=email,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None):

        user = self.create_user(
            email=email,
            phone_number=phone_number,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.CharField(max_length=50, null=True, blank=True)
    fullname = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True)
    file_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
class Otp(models.Model):
    token = models.CharField(max_length=50, null=type, blank=True)
    phone = models.CharField(max_length=11)
    code = models.IntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)