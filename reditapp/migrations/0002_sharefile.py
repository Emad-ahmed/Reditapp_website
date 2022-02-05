# Generated by Django 3.2.6 on 2022-02-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reditapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=120)),
                ('subject_code', models.CharField(max_length=120)),
                ('departMent', models.CharField(choices=[('CSE', 'CSE'), ('ENGLISH', 'ENGLISH'), ('BBA', 'BBA'), ('BANGLA', 'BANGLA'), ('ISLAMIC STUDIES', 'ISLAMIC STUDIES'), ('EEE', 'EEE')], default='CSE', max_length=200)),
                ('question_photo', models.ImageField(blank=True, upload_to='images/')),
                ('question_file', models.FileField(blank=True, upload_to='documents/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
