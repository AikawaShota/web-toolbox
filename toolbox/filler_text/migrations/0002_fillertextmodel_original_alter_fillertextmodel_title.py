# Generated by Django 4.1.5 on 2023-01-21 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filler_text', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fillertextmodel',
            name='original',
            field=models.CharField(default='abc', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fillertextmodel',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
