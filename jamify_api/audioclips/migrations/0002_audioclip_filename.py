# Generated by Django 4.1.1 on 2022-09-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioclips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audioclip',
            name='filename',
            field=models.CharField(default='test', max_length=150),
            preserve_default=False,
        ),
    ]
