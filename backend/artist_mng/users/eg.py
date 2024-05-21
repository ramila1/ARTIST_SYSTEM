# from django.db import migrations

# def create_admin_group(apps, schema_editor):
#     Group = apps.get_model('auth', 'Group')
#     Permission = apps.get_model('auth', 'Permission')

#     # Create Admin group
#     admin_group, created = Group.objects.get_or_create(name='Admin')

#     # Add all permissions to the Admin group
#     permissions = Permission.objects.all()
#     admin_group.permissions.set(permissions)
#     admin_group.save()

# class Migration(migrations.Migration):

#     dependencies = [
#         ('users', '0001_initial'),  # Adjust to your initial migration name
#     ]

#     operations = [
#         migrations.RunPython(create_admin_group),
#     ]
# 5. Create and Assign Admin Group via Data Migration
# users/migrations/0002_create_admin_group.py