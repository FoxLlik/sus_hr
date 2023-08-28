# Generated by Django 4.0.5 on 2023-08-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_auto_20230810_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='degree_type',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Дэд профессор'), (2, 'Профессор'), (3, 'Академич')], db_index=True, default=None, null=True, verbose_name='Эрдмийн зэрэг'),
        ),
        migrations.AddField(
            model_name='employee',
            name='education_level',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Дадлагажигч багш'), (2, 'Багш'), (3, 'Ахлах багш'), (4, 'Дэд профессор')], db_index=True, default=None, null=True, verbose_name='Боловсролын түвшин'),
        ),
        migrations.AddField(
            model_name='employee',
            name='teacher_rank_type',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Дадлагажигч багш'), (2, 'Багш'), (3, 'Ахлах багш'), (4, 'Дэд профессор'), (5, 'Профессор')], db_index=True, default=None, null=True, verbose_name='Албан тушаал'),
        ),
    ]