# Generated by Django 5.1.3 on 2024-12-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_batch_end_date_remove_batch_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='name',
            field=models.CharField(default=2023, max_length=255),
            preserve_default=False,
        ),
    ]
