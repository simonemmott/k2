# Generated by Django 2.2.2 on 2019-07-06 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('k2_app', '0001_initial'),
        ('k2_domain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationdomain',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='k2_domain.Domain'),
        ),
        migrations.AddField(
            model_name='module',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='k2_app.Package'),
        ),
    ]
