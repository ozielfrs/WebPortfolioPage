# Generated by Django 4.0.3 on 2022-03-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_mail', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('liurl', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=512)),
            ],
        ),
    ]
