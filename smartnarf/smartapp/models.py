from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.


class Group(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number


class Teacher(models.Model):
    FIO = models.CharField(max_length=255)

    def __str__(self):
        return self.FIO


class Discipline(models.Model):
    disc_title = models.CharField(max_length=255)

    def __str__(self):
        return self.disc_title


class Torrent(models.Model):
    idGroup = models.ForeignKey(Group, on_delete=models.CASCADE)
    idDiscipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    idTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return str(self.datetime)


class User(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    perms = models.CharField(default='user', max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.username

