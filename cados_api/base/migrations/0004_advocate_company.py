# Generated by Django 4.1.1 on 2022-10-23 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.company'),
        ),
    ]
