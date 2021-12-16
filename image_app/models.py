from django.db import models
from .validators import validate_file_extension, validate_image,validate_no
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_photo = models.ImageField(upload_to="images/",null=True,blank=True,
                              validators=[validate_file_extension,validate_image])
    email = models.EmailField(max_length=1000, null=False,default="")
    mobile_no = models.IntegerField(validators=[validate_no])

    def __str__(self):
        return self.name
