# Generated by Django 5.0.6 on 2024-07-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('achievements', models.TextField(blank=True, null=True)),
                ('aboutUs', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='student_images/')),
            ],
        ),
    ]
