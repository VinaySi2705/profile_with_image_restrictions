from django.core.exceptions import ValidationError
import os



def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg' , '.png' ,'.jpg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')



def validate_image(self):
    filesize = self.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

def validate_no(value):
    if len(str(value)) !=10:
        raise ValidationError('no.should be in length 10')
