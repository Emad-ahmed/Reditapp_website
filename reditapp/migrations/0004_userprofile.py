# Generated by Django 3.2.6 on 2022-02-09 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reditapp', '0003_sharefile_semister'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reditapp.registration')),
            ],
        ),
    ]
