# Generated by Django 3.2.4 on 2021-07-12 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_alter_product_description'),
        ('account', '0008_userprofile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.company'),
        ),
    ]
