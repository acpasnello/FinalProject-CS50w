# Generated by Django 4.1.3 on 2022-12-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PFS', 'Pending'), ('PSF', 'Pending'), ('F', 'Friends'), ('BFS', 'Blocked'), ('BSF', 'Blocked'), ('BB', 'Blocked')], max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lastupdated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
