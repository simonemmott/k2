# Generated by Django 2.2.2 on 2019-07-06 17:18

from django.db import migrations, models
import django.db.models.deletion
import k2_core.mixins.base_type
import k2_core.mixins.domain
import k2_core.mixins.field
import k2_core.mixins.member
import k2_core.mixins.model
import k2_core.mixins.sub_type


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('title', models.CharField(max_length=90, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            bases=(models.Model, k2_core.mixins.domain.DomainMixin),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('title', models.CharField(max_length=90, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('type', models.CharField(choices=[('FLD', 'Field'), ('EXP', 'Expression'), ('MTH', 'Method'), ('LST', 'List')], default='FLD', max_length=3, null=True, verbose_name='Member Type')),
                ('data_type', models.CharField(choices=[('INT', 'Integer'), ('FLT', 'Float'), ('STR', 'String'), ('BLN', 'Boolean'), ('DTE', 'Date'), ('OBJ', 'Object')], default='STR', max_length=3, null=True, verbose_name='Data Type')),
                ('base_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='k2_domain.BaseType')),
            ],
            bases=(models.Model, k2_core.mixins.member.MemberMixin),
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('member_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='k2_domain.Member')),
                ('max_length', models.IntegerField(blank=True, default=0, null=True, verbose_name='Max Length')),
                ('required', models.NullBooleanField(default=False, verbose_name='Required')),
                ('default_value', models.CharField(blank=True, max_length=200, null=True, verbose_name='Default value')),
                ('field_type', models.CharField(choices=[('BLN', 'Boolean'), ('NBL', 'Null boolean'), ('STR', 'String'), ('DTE', 'Date'), ('DTM', 'Date time'), ('DEC', 'Decimal'), ('EML', 'Email'), ('IMG', 'Image'), ('INT', 'Integer'), ('PIN', 'Positive integer'), ('TXT', 'Memo'), ('TME', 'Time'), ('URL', 'URL'), ('LKD', 'Linked field'), ('SBT', 'Sub type')], default='STR', max_length=3, verbose_name='Field Type')),
                ('on_delete_type', models.CharField(blank=True, choices=[('CAS', 'Cascade'), ('PRO', 'Protect'), ('NUL', 'Blank')], default='CAS', max_length=3, null=True, verbose_name='On delete')),
            ],
            bases=('k2_domain.member', k2_core.mixins.field.FieldMixin),
        ),
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('value', models.CharField(max_length=3, verbose_name='Value')),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_types', to='k2_domain.Field')),
            ],
            bases=(models.Model, k2_core.mixins.sub_type.SubTypeMixin),
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('basetype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='k2_domain.BaseType')),
                ('title', models.CharField(max_length=90, verbose_name='Title')),
                ('p_title', models.CharField(blank=True, max_length=90, null=True, verbose_name='Plural title')),
                ('admin_model', models.BooleanField(blank=True, default=False, null=True, verbose_name='Admin Model')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='k2_domain.Domain')),
            ],
            bases=('k2_domain.basetype', k2_core.mixins.model.ModelMixin),
        ),
        migrations.AddField(
            model_name='member',
            name='object_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='members_with_data_type', to='k2_domain.Model'),
        ),
    ]
