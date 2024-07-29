from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class Profile(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'HomeManager'),
        ('guard', 'Guard'),
        ('resident', 'Resident'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='resident')

    def save(self, *args, **kwargs):
        if self.role != 'resident':
            self.is_staff = True
        super().save(*args, **kwargs)
        self.update_group()

    def update_group(self):
        self.groups.clear()
        role_to_group = {
            'admin': 'Admin',
            'manager': 'HouseManager',
            'guard': 'Guard',
            'resident': 'Resident'
        }
        group_name = role_to_group.get(self.role)
        if group_name:
            group, created = Group.objects.get_or_create(name=group_name)
            group.user_set.add(self)

    def get_group_name(self):
        return ', '.join(self.groups.values_list('name', flat=True)) if self.groups.exists() else 'No group'

    get_group_name.short_description = 'Group'

    def __str__(self):
        return self.username