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
            (TEXT, 'Memo'),
            (TIME, 'Time'),
            (URL, 'URL'),
        ]
    field_type = models.CharField('Field Type', max_length=3, choices=FieldType.CHOICES, default=FieldType.STRING, blank=False, null=False)
    
    def __init__(self, *args, **kw):
        super(Field, self).__init__(*args, **kw)
        self.type = Member.Type.FIELD
        
    def save(self, *args, **kw):
        self.type = Member.Type.FIELD
        return super(Member, self).save(*args, **kw)