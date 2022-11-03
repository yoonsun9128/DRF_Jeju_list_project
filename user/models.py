from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            #이메일이 아니라면? -> username 검사 해봐 -> 없어? -> 에러 띄워 '이메일이나 아이디를 확인해라'

            raise ValueError('Users must have an username')

        user = self.model(
            username=self.normalize_username(username),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
            username=username
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True, verbose_name = 'username')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # favorite
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

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