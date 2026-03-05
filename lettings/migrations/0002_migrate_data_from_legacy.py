# lettings/migrations/0002_migrate_data_from_legacy.py

"""
Data migration to move legacy lettings data into the new lettings app.
"""

from django.db import migrations


def forwards(apps, schema_editor):
    """
    Copy legacy Address and Letting records into the new app tables.
    """
    legacy_address = apps.get_model("oc_lettings_site", "Address")
    legacy_letting = apps.get_model("oc_lettings_site", "Letting")

    new_address = apps.get_model("lettings", "Address")
    new_letting = apps.get_model("lettings", "Letting")

    address_id_map = {}

    for addr in legacy_address.objects.all():
        created = new_address.objects.create(
            number=addr.number,
            street=addr.street,
            city=addr.city,
            state=addr.state,
            zip_code=addr.zip_code,
            country_iso_code=addr.country_iso_code,
        )
        address_id_map[addr.id] = created.id

    for let in legacy_letting.objects.all():
        new_letting.objects.create(
            title=let.title,
            address_id=address_id_map[let.address_id],
        )


def backwards(apps, schema_editor):
    """
    Reverse the data migration by clearing new app tables.
    """
    apps.get_model("lettings", "Letting").objects.all().delete()
    apps.get_model("lettings", "Address").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("lettings", "0001_initial"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]