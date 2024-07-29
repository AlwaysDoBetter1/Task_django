from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

def create_groups():
    # create groups
    admin_group, created = Group.objects.get_or_create(name='Admin')
    house_manager_group, created = Group.objects.get_or_create(name='HouseManager')
    guard_group, created = Group.objects.get_or_create(name='Guard')
    user_group, created = Group.objects.get_or_create(name='Resident')


    for model in apps.get_models():
        content_type = ContentType.objects.get_for_model(model)
        permissions = Permission.objects.filter(content_type=content_type)

        all_permissions = Permission.objects.all()
        admin_group.permissions.set(all_permissions)




        if model._meta.model_name == 'house':
            view_permissions = permissions.filter(codename__startswith='view_')
            house_manager_group.permissions.set(view_permissions)
        elif model._meta.model_name == 'entrance':
            view_permissions = permissions.filter(codename__startswith='view_')
            change_permissions = permissions.filter(codename__startswith='change_')
            house_manager_group.permissions.add(*view_permissions)
            house_manager_group.permissions.add(*change_permissions)
            guard_group.permissions.set(view_permissions)
        elif model._meta.model_name == 'apartment':
            view_permissions = permissions.filter(codename__startswith='view_')
            user_group.permissions.set(view_permissions)


create_groups()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'email', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Profile
        fields = ('username', 'email', 'role', 'password')

@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'email', 'role', 'is_staff')
    search_fields = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('role', )}),
        ('Group', {'fields': ('get_group_name',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('get_group_name',)
