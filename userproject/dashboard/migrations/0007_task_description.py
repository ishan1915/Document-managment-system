# Generated by Django 5.0.7 on 2025-06-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_documentversion_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='d'),
            preserve_default=False,
        ),
    ]
