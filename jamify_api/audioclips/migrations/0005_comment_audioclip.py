# Generated by Django 4.1.1 on 2022-09-13 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audioclips', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='audioclip',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='audioclips.audioclip'),
            preserve_default=False,
        ),
    ]
