from django.db import models
from k2_core.mixins.member import MemberMixin

class Member(models.Model, MemberMixin):
    class Type:
        FIELD = 'FLD'
        EXPRESSION = 'EXP'
        METHOD = 'MTH'
        LIST = 'LST'
        CLASS = 'CLS'
        CHOICES = [
            (FIELD, 'Field'),
            (EXPRESSION, 'Expression'),
            (METHOD, 'Method'),
            (LIST, 'List'),
            (CLASS, 'Class')
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
        
#    class RawDataType:
#        STRING = 'STR'
#        NUMBER = 'NUM'
#        BOOLEAN = 'BLN'
        
    name = models.CharField('Name', max_length=50, blank=False, null=True)
    title = models.CharField('Title', max_length=90, blank=False, null=True)
    description = models.TextField('Description', blank=True, null=True)
    member_type = models.CharField('Member Type', max_length=3, choices=Type.CHOICES, default=Type.FIELD, blank=False, null=True)
    data_type = models.ForeignKey('BaseType', verbose_name='Data Type', on_delete=models.PROTECT, related_name='members_with_data_type', blank=True, null=True)
    member_of_type = models.ForeignKey('BaseType', verbose_name='Member of Type', on_delete=models.CASCADE, related_name='members', blank=False, null=True)
    clazz = models.OneToOneField('Clazz', verbose_name='Class', on_delete=models.CASCADE, blank=True, null=True)
    
    