# Generated by Django 5.0.6 on 2024-06-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filemanager", "0003_alter_file_parent"),
    ]

    operations = [
        migrations.AddField(
            model_name="folder",
            name="favorite",
            field=models.BooleanField(default=False),
        ),
    ]