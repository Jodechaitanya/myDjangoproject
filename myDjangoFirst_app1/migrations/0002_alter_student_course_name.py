# Generated by Django 5.1.2 on 2024-10-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDjangoFirst_app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_name',
            field=models.CharField(default='Django training', max_length=50),
        ),
    ]
