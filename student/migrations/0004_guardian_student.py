# Generated by Django 4.1.7 on 2023-03-28 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_enrolled_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardian',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='guardians', to='student.student'),
            preserve_default=False,
        ),
    ]
