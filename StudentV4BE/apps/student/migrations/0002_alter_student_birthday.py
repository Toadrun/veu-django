# Generated by Django 5.0 on 2024-05-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.CharField(db_column='Birthday', max_length=100),
        ),
    ]
