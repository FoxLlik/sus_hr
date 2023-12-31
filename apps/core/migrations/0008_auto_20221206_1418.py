# Generated by Django 4.0.5 on 2022-12-06 14:18

from django.db import migrations, models

import colorama
from colorama import Fore, Back

from .helper.unit3 import unit3

colorama.init(autoreset=True)


class Migration(migrations.Migration):

    def insert_to_unit(apps, schema_editor):

        print("\n STARTING")
        Unit2 = apps.get_model('core', 'Unit2')
        Unit3 = apps.get_model('core', 'Unit3')

        unit2_qs = Unit2.objects.all()

        for unit2 in unit2_qs:
            unit3_data = unit3[unit2.code]
            for unit3_item in unit3_data:

                # bag horoo
                unit3_code = unit3_item['code_list_code']
                unit3_name = unit3_item['code_list_name']

                created_unit2 = Unit3.objects.create(
                    name=unit3_name,
                    code=unit3_code,
                    unit2=unit2
                )

        print(Back.GREEN + Fore.BLACK + "___DONE___")

    dependencies = [
        ('core', '0007_auto_20221206_1418'),
    ]

    operations = [
        migrations.RunPython(insert_to_unit),
    ]
