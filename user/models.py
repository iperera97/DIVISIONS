from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth import authenticate


TITLES = (
    ('mr', "Mr"),
    ("mrs", "Mrs"),
    ("miss", "Miss")
)


class UserManager(BaseUserManager):

    # create user method goes here
    def create_user(self, username, email, admin=False, staff=False, password=None):

        # check has email + password
        if not username:
            raise ValueError('Users must have an username')

        elif not email:
            raise ValueError('Users must have an email address')

        elif not password:
            raise ValueError("Users must have an password")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            admin=admin,
            staff=staff
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # create superuser method goes here
    def create_superuser(self, username, email, password=None):

        return self.create_user(
            username=username,
            email=email,
            admin=True,
            staff=True,
            password=password
        )

    # create staff user method goes here
    def create_staffuser(self, username, email, password=None):

        return self.create_user(
            username=username,
            email=email,
            admin=False,
            staff=True,
            password=password
        )


class User(AbstractBaseUser, PermissionsMixin):

    # FIELDS
    title = models.CharField(choices=TITLES, max_length=5, null=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255, null=True)
    lastName = models.CharField(max_length=255, null=True)
    mobile = models.CharField(max_length=10, null=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # init manager
    objects = UserManager()

    # METHODS
    def __str__(self):

        return "(#{}) {}".format(self.pk, self.firstName)

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
