# Generated by Django 4.1.5 on 2023-02-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emanga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]