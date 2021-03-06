# Generated by Django 3.2.4 on 2021-07-10 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210710_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='my_image')),
                ('job', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('user_uuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Tag_UserProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
