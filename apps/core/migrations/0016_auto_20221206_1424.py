# Generated by Django 4.0.5 on 2022-12-06 14:24

from django.db import migrations
from main.utils.consts import init_notif_types


class Migration(migrations.Migration):

    def _fix_data(apps, schema):
        NotificationType = apps.get_model("core", 'NotificationType')

        for ntype in init_notif_types:
            NotificationType.objects.update_or_create(
                name=ntype['name'],
                defaults={
                    "color": ntype['color'],
                    "level": ntype['level'],
                    "code": ntype['code'],
                }
            )

    dependencies = [
        ('core', '0015_auto_20221206_1423'),
    ]

    operations = [
        migrations.RunPython(_fix_data)
    ]