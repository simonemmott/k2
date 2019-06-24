from django.db import models
import k2_core.model

class Member(models.Model):
    class Type:
        FIELD = 'FLD'
        EXPRESSION = 'EXP'
        METHOD = 'MTH'
        LIST = 'LST'
        CHOICES = [
            (FIELD, 'Field'),
            (EXPRESSION, 'Expression'),
            (METHOD, 'Method'),
            (LIST, 'List'),
        ]
    class DataType:
        INTEGER = 'INT'
        FLOAT = 'FLT'
        STRING = 'STR'
        BOOLEAN = 'BLN'
        DATE = 'DTE'
        OBJECT = 'OBJ'
        CHOICES = [
            (INTEGER, 'Integer'),
            (FLOAT, 'Float'),
            (STRING, 'String'),
            (BOOLEAN, 'Boolean'),
            (DATE, 'Date'),
            (OBJECT, 'Object'),
        ]
    name = models.CharField('Name', max_length=50, blank=False, null=False)
    title = models.CharField('Title', max_length=90, blank=False, null=False)
    description = models.TextField('Description', blank=True, null=True)
    type = models.CharField('Member Type', max_length=3, choices=Type.CHOICES, default=Type.FIELD, blank=False, null=False)
    data_type = models.CharField('Data Type', max_length=3, choices=DataType.CHOICES, default=DataType.STRING, blank=False, null=False)
    object_type = models.ForeignKey('Model', on_delete=models.PROTECT, related_name='members_with_data_type', blank=True, null=True)
    model = models.ForeignKey('Model', on_delete=models.CASCADE, related_name='members', blank=False, null=False)
    
    def __str__(self):
        return '{type}: {cls}::{field}({title})'.format(
            type=k2_core.model.get_choice_display(Member.Type.CHOICES, self.type),
            cls=self.model.class_name(),
            field=self.name,
            title=self.title
        )
    