# Generated by Django 2.2.2 on 2019-07-06 18:37

from django.db import migrations, models
import django.db.models.deletion
import k2_core.mixins.application
import k2_core.mixins.application_domain
import k2_core.mixins.base_type
import k2_core.mixins.member
import k2_core.mixins.module
import k2_core.mixins.package


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=90)),
                ('description', models.TextField()),
            ],
            bases=(models.Model, k2_core.mixins.application.ApplicationMixin),
        ),
        migrations.CreateModel(
            name='BaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('type', models.CharField(choices=[('MOD', 'Module'), ('CLS', 'Class'), ('MDL', 'Model'), ('VEW', 'View'), ('SZR', 'Serializer')], default='MOD', max_length=3, verbose_name='Type')),
            ],
            bases=(models.Model, k2_core.mixins.base_type.BaseTypeMixin),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True, unique=True, verbose_name='Name')),
                ('version', models.CharField(max_length=20, null=True, verbose_name='Version')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            bases=(models.Model, k2_core.mixins.package.PackageMixin),
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('basetype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='k2_app.BaseType')),
            ],
            bases=('k2_app.basetype', k2_core.mixins.module.ModuleMixin),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('title', models.CharField(max_length=90, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('member_type', models.CharField(choices=[('FLD', 'Field'), ('EXP', 'Expression'), ('MTH', 'Method'), ('LST', 'List')], default='FLD', max_length=3, null=True, verbose_name='Member Type')),
                ('data_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='members_with_data_type', to='k2_app.BaseType', verbose_name='Data Type')),
                ('member_of_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='k2_app.BaseType', verbose_name='Member of Type')),
            ],
            bases=(models.Model, k2_core.mixins.member.MemberMixin),
        ),
        migrations.CreateModel(
            name='ApplicationDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_domains', to='k2_app.Application')),
            ],
            bases=(models.Model, k2_core.mixins.application_domain.ApplicationDomainMixin),
        ),
    ]
