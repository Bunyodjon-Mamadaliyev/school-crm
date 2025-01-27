# Generated by Django 5.1.5 on 2025-01-27 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('work_experience', models.PositiveIntegerField(default=0)),
                ('images', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='subjects.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
