# Generated by Django 5.2 on 2025-04-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('input_text', models.TextField()),
                ('output_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
