# Generated by Django 4.0.5 on 2023-08-10 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_auto_20230810_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Нэр')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код')),
            ],
        ),
        migrations.AddField(
            model_name='orgposition',
            name='main_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.mainposition', verbose_name='Үндсэн албан тушаалын төрөлүүд'),
        ),
    ]
