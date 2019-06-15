# Generated by Django 2.2.2 on 2019-06-15 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('k2_domain', '0001_added_domain'),
        ('k2_app', '0002_added_application_domains'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationdomain',
            name='description',
        ),
        migrations.RemoveField(
            model_name='applicationdomain',
            name='name',
        ),
        migrations.RemoveField(
            model_name='applicationdomain',
            name='title',
        ),
        migrations.AddField(
            model_name='applicationdomain',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='k2_domain.Domain'),
            preserve_default=False,
        ),
    ]
