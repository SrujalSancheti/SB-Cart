# Generated by Django 3.0.7 on 2020-07-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200703_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=500)),
                ('phone', models.CharField(default='', max_length=10)),
            ],
        ),
    ]