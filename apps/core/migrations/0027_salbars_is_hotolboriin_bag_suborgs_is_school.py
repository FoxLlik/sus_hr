# Generated by Django 4.0.5 on 2023-01-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_employee_register_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='salbars',
            name='is_hotolboriin_bag',
            field=models.BooleanField(default=False, null=True, verbose_name='Хөтөлбөрийн баг эсэх'),
        ),
        migrations.AddField(
            model_name='suborgs',
            name='is_school',
            field=models.BooleanField(default=False, null=True, verbose_name='Сургууль эсэх'),
        ),
    ]
