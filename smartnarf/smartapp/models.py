from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

# модель группы обучающегося
class Group(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number


# модель дисциплины
class Discipline(models.Model):
    disc_title = models.CharField(max_length=255)

    def __str__(self):
        return self.disc_title


# модель подгрупп для дисциплин
class SubGroup(models.Model):
    name = models.CharField(max_length=45)
    idDiscipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# модель преподавателя
class Teacher(models.Model):
    FIO = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.FIO


# модель домашнего задания для каждой пары
class Homework(models.Model):
    description = models.CharField(max_length=255)
    folderPath = models.CharField(max_length=255)

    def __str__(self):
        return self.description


# модель комментариев для каждой пары
class Comment(models.Model):
    text = models.CharField(max_length=255)
    #idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# модель пары, для вывода на view
class Lesson(models.Model):
    idGroup = models.ForeignKey(Group, on_delete=models.CASCADE)
    idDiscipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    idTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    idHomework = models.ForeignKey(Homework, blank=True, null=True, on_delete=models.CASCADE)
    idComment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return str(self.datetime)



