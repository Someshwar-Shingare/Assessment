# Generated by Django 4.0.3 on 2022-03-05 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=32)),
                ('error', models.CharField(max_length=150)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
