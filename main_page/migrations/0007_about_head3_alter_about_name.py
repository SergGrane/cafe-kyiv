# Generated by Django 4.0.2 on 2022-02-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_about_about_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='head3',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
