# Generated by Django 4.0.6 on 2022-07-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appId', models.CharField(max_length=600)),
                ('appSertificate', models.CharField(max_length=1000)),
            ],
        ),
    ]
