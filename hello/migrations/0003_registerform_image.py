# Generated by Django 3.1.2 on 2021-04-09 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_teacher_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerform',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
