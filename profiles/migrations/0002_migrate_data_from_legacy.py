# profiles/migrations/0002_migrate_data_from_legacy.py

"""
Data migration to move legacy profiles data into the new profiles app.
"""

from django.db import migrations


def forwards(apps, schema_editor):
    """
    Copy legacy Profile records into the new app table.
    """
    legacy_profile = apps.get_model("oc_lettings_site", "Profile")
    new_profile = apps.get_model("profiles", "Profile")

    for prof in legacy_profile.objects.all():
        new_profile.objects.create(
            user_id=prof.user_id,
            favorite_city=prof.favorite_city,
        )


def backwards(apps, schema_editor):
    """
    Reverse the data migration by clearing the new app table.
    """
    apps.get_model("profiles", "Profile").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]