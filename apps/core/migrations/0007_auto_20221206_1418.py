# Generated by Django 4.0.5 on 2022-12-06 14:18

from django.db import migrations
from main.utils.consts import init_forTomilolt


class Migration(migrations.Migration):

    def insert_data(apps, schema):
        ForTomilolt = apps.get_model("core", 'ForTomilolt')
        Orgs = apps.get_model("core", 'Orgs')
        SubOrgs = apps.get_model("core", 'SubOrgs')
        Salbars = apps.get_model("core", 'Salbars')

        for kind in init_forTomilolt:
            for org in Orgs.objects.all():
                ForTomilolt \
                    .objects \
                    .create(
                        org=org,
                        name=kind['name'],
                    )

        for kind in init_forTomilolt:
            for suborg in SubOrgs.objects.all():
                ForTomilolt \
                    .objects \
                    .create(
                        org=suborg.org,
                        sub_org=suborg,
                        name=kind['name'],
                    )

        for kind in init_forTomilolt:
            for salbar in Salbars.objects.all():
                ForTomilolt \
                    .objects \
                    .create(
                        org=salbar.org,
                        sub_org=salbar.sub_orgs,
                        salbar=salbar,
                        name=kind['name'],
                    )

    dependencies = [
        ('core', '0006_auto_20221206_1417'),
    ]

    operations = [
        migrations.RunPython(insert_data)
    ]
