# Generated by Django 3.1.1 on 2020-09-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200924_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=255)),
                ('amount', models.CharField(default=0, max_length=255)),
                ('paymenton', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
