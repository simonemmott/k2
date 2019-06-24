from django.db import models
from .member import Member

class Field(Member):
    class FieldType:
        BOOLEAN = 'BLN'
        NULL_BOOLEAN = 'NBL'
        STRING = 'STR'
        DATE = 'DTE'
        DATE_TIME = 'DTM'
        DECIMAL = 'DEC'
        EMAIL = 'EML'
        FILE = 'FIL'
        IMAGE = 'IMG'
        INTEGER = 'INT'
        POSITIVE_INTEGER = 'PIN'
        TEXT = 'TXT'
        TIME = 'TME'
        URL = 'URL'
        CHOICES = [
            (BOOLEAN, 'Boolean'),
            (NULL_BOOLEAN, 'Null boolean'),
            (STRING, 'String'),
            (DATE, 'Date'),
            (DATE_TIME, 'Date time'),
            (DECIMAL, 'Decimal'),
            (EMAIL, 'Email'),
            (IMAGE, 'Image'),
            (INTEGER, 'Integer'),
            (POSITIVE_INTEGER, 'Positive integer'),
            (TEXT, 'Memo'),
            (TIME, 'Time'),
            (URL, 'URL'),
        ]
    max_length = models.IntegerField('Max Length', default=0, blank=True, null=True)
    required = models.NullBooleanField('Required', default=False, blank=True, null=True)
    default_value = models.CharField('Default value', max_length=200, blank=True, null=True)
    field_type = models.CharField('Field Type', max_length=3, choices=FieldType.CHOICES, default=FieldType.STRING, blank=False, null=False)
    
    def __init__(self, *args, **kw):
        super(Field, self).__init__(*args, **kw)
        self.type = Member.Type.FIELD
        
    def save(self, *args, **kw):
        self.type = Member.Type.FIELD
        return super(Member, self).save(*args, **kw)
    
    def field_class_name(self):
        if self.field_type == Field.FieldType.BOOLEAN:
            return 'BooleanField'
        if self.field_type == Field.FieldType.NULL_BOOLEAN:
            return 'NullBooleanField'
        if self.field_type == Field.FieldType.STRING:
            return 'CharField'
        if self.field_type == Field.FieldType.DATE:
            return 'DateField'
        if self.field_type == Field.FieldType.DATE_TIME:
            return 'DateTimeField'
        if self.field_type == Field.FieldType.DECIMAL:
            return 'DecimalField'
        if self.field_type == Field.FieldType.EMAIL:
            return 'EmailField'
        if self.field_type == Field.FieldType.FILE:
            return 'FileField'
        if self.field_type == Field.FieldType.IMAGE:
            return 'ImageField'
        if self.field_type == Field.FieldType.INTEGER:
            return 'IntegerField'
        if self.field_type == Field.FieldType.POSITIVE_INTEGER:
            return 'PositiveIntegerField'
        if self.field_type == Field.FieldType.TEXT:
            return 'TextField'
        if self.field_type == Field.FieldType.TIME:
            return 'TimeField'
        if self.field_type == Field.FieldType.URL:
            return 'UrlField'
        
        raise ValueError('No field class defined for field of {type} - ({disp})'.format(type=self.field_type, disp=self.get_field_type_display()))
    
    def max_length_clause(self):
        if self.max_length and self.max_length > 0:
            return ', max_length={v}'.format(v=self.max_length)
        return ''
    
    def blank_clause(self):
        if self.required != None and self.required == True:
            return ', blank=False'
        return ', blank=True'
    
    def null_clause(self):
        return ', null=True'
    
    def default_clause(self):
        if not self.default_value:
            return ''
        if self.data_type == Member.DataType.BOOLEAN:
            if self.default_value.upper() in ['', '0', 'FALSE', 'NO']:
                return ', default=False'
            return ', default=True'
        if self.data_type in [Member.DataType.INTEGER, Member.DataType.FLOAT]:
            return ', default={v}'.format(v=self.default_value)  
        if self.data_type in [Member.DataType.STRING, Member.DataType.DATE]:
            return ", default='{v}'".format(v=self.default_value)  
        return ''
    
