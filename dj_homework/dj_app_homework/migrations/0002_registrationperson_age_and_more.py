# Generated by Django 4.1.6 on 2023-02-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_app_homework', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationperson',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrationperson',
            name='password',
            field=models.CharField(max_length=15),
        ),
    ]