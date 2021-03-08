from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from root.settings import AUTH_USER_MODEL

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username= username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email,  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
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


class Projeto(models.Model):
    name = models.CharField(max_length=255,default="Projeto")
    users = models.ManyToManyField(AUTH_USER_MODEL)
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projeto'

    def get_users_id(self):
        return [p.id for p in self.users.all()]

    def __str__(self):
        return self.name

class Naver(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    birthdate = models.DateField()
    admission_date = models.DateField()
    job_role = models.CharField(max_length=255)
    projetos = models.ManyToManyField(Projeto)

    class Meta:
        verbose_name = 'Naver'
        verbose_name_plural = 'Navers'

    def get_projects(self):
        return ",".join([p.name for p in self.projetos.all()])

    def __str__(self):
        return self.fullname