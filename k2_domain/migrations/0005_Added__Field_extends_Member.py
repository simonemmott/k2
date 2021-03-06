# Generated by Django 2.2.2 on 2019-06-24 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('k2_domain', '0004_Added__Member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('member_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='k2_domain.Member')),
                ('field_type', models.CharField(choices=[('BLN', 'Boolean'), ('NBL', 'Null boolean'), ('STR', 'String'), ('DTE', 'Date'), ('DTM', 'Date time'), ('DEC', 'Decimal'), ('EML', 'Email'), ('IMG', 'Image'), ('INT', 'Integer'), ('TXT', 'Memo'), ('TME', 'Time'), ('URL', 'URL')], default='STR', max_length=3, verbose_name='Field Type')),
            ],
            bases=('k2_domain.member',),
        ),
    ]
