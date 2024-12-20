# Generated by Django 5.1.3 on 2024-11-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('check_task', models.BooleanField(default=False)),
            ],
        ),
    ]
