# Generated by Django 4.0.5 on 2023-05-26 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_orgs_sign_zahiral'),
    ]

    operations = [
        migrations.AddField(
            model_name='salbars',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Хөтөлбөрийн багийн ахлагч'),
        ),
    ]