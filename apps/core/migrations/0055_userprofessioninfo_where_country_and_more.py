# Generated by Django 4.0.5 on 2023-08-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_employee_degree_type_employee_education_level_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofessioninfo',
            name='where_country',
            field=models.PositiveBigIntegerField(blank=True, choices=[(1, 'Дотоодод'), (2, 'Гадаадад')], db_index=True, default=1, null=True, verbose_name='Мэргэжил дээшлүүлсэн байдал'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='education_level',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Дипломын'), (2, 'Бакалавр'), (3, 'Магистр'), (4, 'Доктор')], db_index=True, default=None, null=True, verbose_name='Боловсролын түвшин'),
        ),
    ]