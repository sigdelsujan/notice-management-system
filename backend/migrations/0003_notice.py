# Generated by Django 4.1.5 on 2023-01-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_delete_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('desc', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
