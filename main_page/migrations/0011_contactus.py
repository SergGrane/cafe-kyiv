# Generated by Django 4.0.2 on 2022-02-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0010_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.TextField(blank=True, max_length=400)),
                ('map', models.URLField(blank=True, max_length=800)),
                ('location', models.TextField(blank=True, max_length=400)),
                ('open', models.TextField(blank=True, max_length=300)),
                ('call', models.TextField(blank=True, max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
