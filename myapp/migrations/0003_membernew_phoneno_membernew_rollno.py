# Generated by Django 5.0 on 2024-01-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_member_membernew'),
    ]

    operations = [
        migrations.AddField(
            model_name='membernew',
            name='phoneno',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='membernew',
            name='rollno',
            field=models.IntegerField(null=True),
        ),
    ]
