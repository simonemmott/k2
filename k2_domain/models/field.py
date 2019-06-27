from django.db import models
from .member import Member
import k2_util

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
        LINKED = 'LKD'
        SUB_TYPE = 'SBT'
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
            (LINKED, 'Linked field'),
            (SUB_TYPE, 'Sub type')
        ]
    class OnDeleteType:
        CASCADE = 'CAS'
        PROTECT = 'PRO'
        SET_NULL = 'NUL'
        CHOICES = [
            (CASCADE, 'Cascade'),
            (PROTECT, 'Protect'),
            (SET_NULL, 'Blank'),
        ]
        
    max_length = models.IntegerField('Max Length', default=0, blank=True, null=True)
    required = models.NullBooleanField('Required', default=False, blank=True, null=True)
    default_value = models.CharField('Default value', max_length=200, blank=True, null=True)
    field_type = models.CharField('Field Type', max_length=3, choices=FieldType.CHOICES, default=FieldType.STRING, blank=False, null=False)
    on_delete_type = models.CharField('On delete', max_length=3, choices=OnDeleteType.CHOICES, default=OnDeleteType.CASCADE, blank=True, null=True)
    
    # sub_types -> list of SubType values for this field if it is a SUB_TYPE
    
    def __init__(self, *args, **kw):
        super(Field, self).__init__(*args, **kw)
        self.type = Member.Type.FIELD
        
    def save(self, *args, **kw):
        self.type = Member.Type.FIELD
        return super(Member, self).save(*args, **kw)
    
    def types_name(self):
        return '{name}Type'.format(name=k2_util.to_class_case(self.name))
    
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
        if self.field_type == Field.FieldType.LINKED:
            return 'ForeignKey'
        if self.field_type == Field.FieldType.SUB_TYPE:
            return 'CharField'
        
        raise ValueError('No field class defined for field of {type} - ({disp})'.format(type=self.field_type, disp=self.get_field_type_display()))
    
    def title_or_link_type(self):
        if self.field_type in [Field.FieldType.LINKED]:
            if self.object_type.domain == self.model.domain:
                return self.object_type.class_name()
            return '{domain}.{model}'.format(domain=self.object_type.domain.name, model=self.object_type.class_name())
        return self.title
    
    def model_field_options(self):
        return  self._on_delete_clause()+\
                self._verbose_name_clause()+\
                self._default_clause()+\
                self._max_length_clause()+\
                self._choices_clause()+\
                self._null_clause()+\
                self._blank_clause()+\
                self._help_text_clause()
                   
    def _on_delete_clause(self):
        if self.field_type in _related_types:
            return ', on_delete=models.{v}'.format(v=_on_delete_names.get(self.on_delete_type, '__ERR__'))
        return ''
        
                
    def _verbose_name_clause(self):
        if self.field_type in _related_types:
            return ', verbose_name="{v}"'.format(v=self.title.replace('"', "'"))
        return ''
    
    def _help_text_clause(self):
        if len(self.description) > 0 and len(self.description) < 100:
            return ', help_text="{v}"'.format(v=self.description.replace('"', "'"))
        return ''
    
    def _max_length_clause(self):
        if self.max_length and self.max_length > 0:
            return ', max_length={v}'.format(v=self.max_length)
        return ''
    
    def _choices_clause(self):
        if self.field_type == Field.FieldType.SUB_TYPE:
            return ', choices={v}.CHOICES'.format(v=self.types_name())
        return ''
    
    def _blank_clause(self):
        if self.required != None and self.required == True:
            return ', blank=False'
        return ', blank=True'
    
    def _null_clause(self):
        return ', null=True'
    
    def _default_clause(self):
        if not self.default_value:
            return ''
        if self.data_type == Member.DataType.BOOLEAN:
            if self.default_value.upper() in ['', '0', 'FALSE', 'NO']:
                return ', default=False'
            return ', default=True'
        if self.data_type in [Member.DataType.INTEGER, Member.DataType.FLOAT]:
            return ', default={v}'.format(v=self.default_value)  
        if self.data_type in [Member.DataType.STRING, Member.DataType.DATE]:
            return ', default="{v}"'.format(v=self.default_value.replace('"', "'"))  
        return ''
    
_related_types = [Field.FieldType.LINKED]

_on_delete_names = {
    Field.OnDeleteType.CASCADE: 'CASCADE',
    Field.OnDeleteType.PROTECT: 'PROTECT',
    Field.OnDeleteType.SET_NULL: 'SET_NULL'
}

