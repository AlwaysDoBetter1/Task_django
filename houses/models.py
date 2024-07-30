from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from humans.models import Profile
from guardian.shortcuts import assign_perm
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField

class Notifications(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

class House(MPTTModel):
    """ Create home data """
    address = models.CharField(max_length=255, unique=True, verbose_name='address of home')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    manager = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_houses',
        limit_choices_to={'groups__name': 'HouseManager'}
    )

    def assign_manager(self, user):
        assign_perm('view_house', user, self)
        assign_perm('change_house', user, self)

    class MPTTMeta:
        order_insertion_by = ['address']

    def __str__(self):
        return self.address

class Entrance(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='entrances')
    entrance_number = models.PositiveIntegerField()
    num_of_floors = models.PositiveIntegerField(null=True, blank=True)
    guard = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='guarded_entrances',
        limit_choices_to = {'groups__name': 'Guard'}
    )
    history = AuditlogHistoryField()

    def assign_guard(self, user):
        assign_perm('view_entrance', user, self)
        assign_perm('change_entrance', user, self)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['house', 'entrance_number'], name='unique_entrance_per_house')
        ]

    def __str__(self):
        return f"Entrance {self.entrance_number}, {self.house.address}"

auditlog.register(Entrance)

class Apartment(models.Model):
    entrance = models.ForeignKey(Entrance, on_delete=models.CASCADE, related_name='apartments')
    apartment_number = models.PositiveIntegerField()
    floor_number = models.PositiveIntegerField(null=True, blank=True)
    num_of_rooms = models.PositiveIntegerField(null=True, blank=True)
    resident = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='residents',
        limit_choices_to={'groups__name': 'Resident'}
    )
    history = AuditlogHistoryField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entrance', 'apartment_number'], name='unique_apartment')
        ]

    def __str__(self):
        return f"Apartment {self.apartment_number}, Floor {self.floor_number}, {self.entrance.house.address}"

auditlog.register(Apartment)
