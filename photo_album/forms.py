from django.forms import ModelForm
from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField
from cloudinary.compat import to_bytes
import cloudinary, hashlib
from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo

class PhotoDirectForm(PhotoForm):
    image = CloudinaryJsFileField()

class PhotoUnsignedDirectForm(PhotoForm):
    upload_preset_name = "yv8jbwvl"
    image = CloudinaryUnsignedJsFileField(upload_preset_name)
