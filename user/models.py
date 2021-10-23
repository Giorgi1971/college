from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from django.urls import reverse, reverse_lazy
# Create your models here.


# class Subject(models.Model):
#     name = models.CharField(max_length=256)

#     def __str__(self) -> str:
#         return self.name

class Subject(models.TextChoices):
    GEOGRAPHY = 'GRF'
    CHEMISTRY = 'CHE'
    PHYSICS = 'PHY'
    MATHEMATICS = 'MAT'
    NATURE = 'NAT'
    ENGLISH = 'ENG'
    GEORGIAN = 'GEO'
    MUSIC = 'MUS'
    BIOLOGY = 'BIO'

    SUBJECT_IN_SCHOOL_CHOICES = [
        (GEOGRAPHY, 'Geography'),
        (CHEMISTRY, 'chemistry'),
        (PHYSICS, 'physics'),
        (MATHEMATICS, 'Mathematics'),
        (NATURE, 'Nature'),
        (ENGLISH, 'English'),
        (GEORGIAN, 'Georgian'),
        (MUSIC, 'Music'),
        (BIOLOGY, 'Biology'),  
    ]

    name = models.CharField(
            choices=SUBJECT_IN_SCHOOL_CHOICES,
            default=GEORGIAN,
        )

    def __str__(self) -> str:
        return self.name



class Teacher(User):
    subject = models.CharField(choices=Subject.choices, max_length=248)
    salary = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='user/teachers', blank=True)

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self) -> str:
        return self.last_name + ' ' +self.first_name

    def get_absolute_url(self):
        return reverse('user:teacher', kwargs={'pk':self.pk})


class Group(models.Model):
    name = models.CharField(max_length=256)
    men_teacher = models.ForeignKey('teacher', on_delete=models.SET_NULL, blank=True, related_name='group_meneger', null=True)
    teachers = models.ManyToManyField(Teacher)
    subjects = models.CharField(choices=Subject.choices, max_length=248)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

class Pupil(User):
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=CASCADE, related_name='pupils')
    
    class Meta:
        verbose_name = _('Pupil')
        verbose_name_plural = _('Pupils')


    def __str__(self) -> str:
        return self.last_name + ' ' +self.first_name
