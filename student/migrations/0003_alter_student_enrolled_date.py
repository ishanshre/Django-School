# Generated by Django 4.1.7 on 2023-03-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_guardian_middle_name_alter_student_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrolled_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]