# Generated by Django 2.2.1 on 2019-06-02 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sociat', '0004_register_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
        migrations.RemoveField(
            model_name='register',
            name='profile_pic',
        ),
    ]