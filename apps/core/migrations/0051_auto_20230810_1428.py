# Generated by Django 4.0.5 on 2023-08-10 14:28

import colorama
from colorama import Fore, Back

from django.db import migrations

colorama.init(autoreset=True)


class Migration(migrations.Migration):

    def insert_property_and_education_institution(apps, schema_editor):

        print("\n PropertyType, EducationInstitutionCategory моделийн утгууд хадгалах процесс эхлэж байна.")

        property_types = [
            {
                'name' : 'Өмчийн (Төрийн)',
            },
            {
                'name' : 'Өмчийн оролцоотой, % (Төрийн)',
            },
            {
                'name' : 'Хамтарсан (Төрийн)',
            },
            {
                'name' : 'Монгол Улсын иргэний (Хувийн)',
            },
            {
                'name' : 'Гадаадтай хамтарсан, % (Хувийн)',
            },
            {
                'name' : 'Гадаад улсын (Хувийн)',
            },
            {
                'name' : 'Өмчийн (Орон нутгийн)',
            },
            {
                'name' : 'Өмчийн оролцоотой, % (Орон нутгийн)',
            },
            {
                'name' : 'Хамтарсан (Орон нутгийн)',
            },
            {
                'name': 'Олон нийтийн /шашны'
            },
            {
                'name': 'Гадаадын салбар сургууль'
            }
        ]

        education_institute_types = [
            {
                'name' : 'Их сургууль',
            },
            {
                'name' : 'Дээд сургууль',
            },
            {
                'name' : 'Коллеж',
            },
            {
                'name' : 'Технологийн коллеж',
            },
        ]

        PropertyType = apps.get_model('core', 'PropertyType')
        EducationalInstitutionCategory = apps.get_model('core', 'EducationalInstitutionCategory')

        PropertyType.objects.all().delete()
        EducationalInstitutionCategory.objects.all().delete()

        for property_type_item in property_types:
            PropertyType.objects.create(name=property_type_item['name'])

        for education_institute_type_item in education_institute_types:
            EducationalInstitutionCategory.objects.create(name=education_institute_type_item['name'])

        print(Back.GREEN + Fore.BLACK + "PropertyType, EducationalInstitutionCategory үүсж дууслаа!")

    dependencies = [
        ('core', '0050_educationalinstitutioncategory_propertytype_and_more'),
    ]

    operations = [
        migrations.RunPython(insert_property_and_education_institution),
    ]