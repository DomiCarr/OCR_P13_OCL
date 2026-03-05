# oc_lettings_site/migrations/0002_drop_legacy_models.py

"""Migration to remove legacy models from oc_lettings_site."""

# oc_lettings_site/migrations/0002_drop_legacy_models.py

"""
Schema migration to drop legacy tables after data has been migrated.
"""

from django.db import migrations


class Migration(migrations.Migration):
    """Database schema migration."""

    dependencies = [
        ("lettings", "0002_migrate_data_from_legacy"),
        ("profiles", "0002_migrate_data_from_legacy"),
        ("oc_lettings_site", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Letting"),
        migrations.DeleteModel(name="Address"),
        migrations.DeleteModel(name="Profile"),
    ]