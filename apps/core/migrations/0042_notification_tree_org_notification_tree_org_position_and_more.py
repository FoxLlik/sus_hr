# Generated by Django 4.0.5 on 2023-05-29 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_alter_employee_time_register_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='tree_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tree_org', to='core.orgs'),
        ),
        migrations.AddField(
            model_name='notification',
            name='tree_org_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tree_pos', to='core.orgposition'),
        ),
        migrations.AddField(
            model_name='notification',
            name='tree_salbar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tree_salbar', to='core.salbars', verbose_name='Салбар'),
        ),
        migrations.AddField(
            model_name='notification',
            name='tree_sub_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tree_sub_org', to='core.suborgs', verbose_name='Харьяалагдах алба нэгж'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='from_kind',
            field=models.IntegerField(choices=[(1, 'Байгууллага'), (2, 'Дэд байгууллага'), (3, 'Салбар'), (4, 'Албан тушаал'), (5, 'Алба хаагч'), (6, 'Хэрэглэгч'), (7, 'Оюутан')]),
        ),
        migrations.AlterField(
            model_name='notification',
            name='scope_kind',
            field=models.IntegerField(choices=[(1, 'Байгууллага'), (2, 'Дэд байгууллага'), (3, 'Салбар'), (4, 'Албан тушаал'), (5, 'Алба хаагч'), (6, 'Хэрэглэгч'), (7, 'Бүгд'), (8, 'Оюутан'), (10, 'Мэргэжил'), (11, 'Курс'), (12, 'Анги')]),
        ),
    ]