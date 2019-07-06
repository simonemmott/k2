from django.db import models
from k2_app.models.member import Member
import k2_util
from k2_core.mixins.field import FieldMixin

class Field(Member, FieldMixin):
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
    
