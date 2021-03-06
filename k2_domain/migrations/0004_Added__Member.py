# Generated by Django 2.2.2 on 2019-06-24 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('k2_domain', '0003_Added__Domain_admin_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('title', models.CharField(max_length=90, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('type', models.CharField(choices=[('FLD', 'Field'), ('EXP', 'Expression'), ('MTH', 'Method'), ('LST', 'List')], default='FLD', max_length=3, verbose_name='Member Type')),
                ('data_type', models.CharField(choices=[('INT', 'Integer'), ('FLT', 'Integer'), ('STR', 'Integer'), ('BLN', 'Integer'), ('DTE', 'Integer'), ('OBJ', 'Object')], default='STR', max_length=3, verbose_name='Data Type')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='k2_domain.Model')),
                ('object_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='members_with_data_type', to='k2_domain.Model')),
            ],
        ),
    ]
