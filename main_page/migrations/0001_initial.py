# Generated by Django 4.0.2 on 2022-02-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=40, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
