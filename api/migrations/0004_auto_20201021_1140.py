# Generated by Django 3.1.1 on 2020-10-21 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201018_2248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['date'], 'verbose_name': 'Post'},
        ),
        migrations.AlterModelOptions(
            name='replies',
            options={'ordering': ['date'], 'verbose_name': 'Replie'},
        ),
    ]
