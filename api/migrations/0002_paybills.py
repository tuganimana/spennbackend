# Generated by Django 3.1.1 on 2020-09-24 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paybills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Payment Processed on', max_length=255)),
                ('paymenton', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
