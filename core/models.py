from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    registration_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title

class TeamMember(models.Model):

    ROLE_CHOICES = [
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Event Head', 'Event Head'),
        ('Management Head', 'Management Head'),
        ('Secretary', 'Secretary'),
        ('Core Committee Member', 'Core Committee Member'),
        ('Coordinator', 'Coordinator'),
        ('Design Team Member', 'Design Team Member'),
        ('Committee Member', 'Committee Member'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    gender = models.CharField(
    max_length=1,
    choices=GENDER_CHOICES,
    default='M'
)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
