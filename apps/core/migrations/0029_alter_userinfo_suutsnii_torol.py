# Generated by Django 4.0.5 on 2023-01-31 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_userinfo_experience_mnun_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='suutsnii_torol',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'гэр'), (2, 'байшин'), (3, 'орон сууц')], db_index=True, default=None, null=True, verbose_name='Сууцны төрөл'),
        ),
    ]