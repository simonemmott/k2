# Generated by Django 2.2.2 on 2019-06-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k2_domain', '0010_Added_SubType'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtype',
            name='name',
            field=models.CharField(default='XXX', max_length=30, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
