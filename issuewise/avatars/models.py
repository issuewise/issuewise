from uuid import uuid4
from unipath import Path

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.files import File
from django.core.exceptions import ValidationError

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def get_directory_from_model(app_label, model):
    joined = '.'.join([app_label, model])
    model_directory_path = settings.MODEL_AVATAR_DIR[joined]
    components = Path(model_directory_path).components()
    return components

def get_directory(instance,filename):
    media_root = settings.MEDIA_ROOT
    avatar_root = media_root.child('avatars')

    content_type = instance.content_type
    instance_app_label= content_type.app_label
    instance_model = content_type.model
    model_directory_components = get_directory_from_model(instance_app_label,instance_model)
    model_directory_path=Path(model_directory_components)
    object_id = instance.object_id

    directory = Path(avatar_root, model_directory_path, unicode(object_id))

    return directory

def avatar_upload_path(instance, filename):
    directory = get_directory(instance,filename)

    ext = Path(filename).ext
    unique_file_name = unicode(uuid4())
    unique_filename_with_ext = ''.join([unique_file_name, ext])

    path = directory.child(unique_filename_with_ext)

    return path

def thumbnail_upload_path(instance, filename):
    directory = get_directory(instance,filename)

    ext = Path(filename).ext
    unique_file_name = unicode(uuid4())
    unique_filename_with_ext = ''.join([unique_file_name, u'-thumbnail', ext])

    path = directory.child(unique_filename_with_ext)

    return path
    
    
class BaseAvatar(models.Model):
    
    avatar = models.ImageField(_('avatar'), max_length = 300,
        upload_to = avatar_upload_path) 
    content_type = models.ForeignKey(ContentType,
        verbose_name = _('model type'))
    object_id = models.PositiveIntegerField(_('model primary key'))
    content_object = GenericForeignKey('content_type', 'object_id')
    is_primary = models.BooleanField(_('is this the primary avatar?'),
        default = True)
    uploaded_at = models.DateTimeField(_('uploaded at'), auto_now_add = True)


    class Meta:
        abstract = True


class WiseAvatar(BaseAvatar):

    THUMBNAIL_HEIGHT = settings.THUMBNAIL_HEIGHT
    THUMBNAIL_WIDTH = settings.THUMBNAIL_WIDTH

    thumbnail = ProcessedImageField(max_length = 300, 
                                    upload_to=thumbnail_upload_path,
                                    processors=[ResizeToFill(THUMBNAIL_HEIGHT,
                                                             THUMBNAIL_WIDTH)],
                                    options={'quality': 60},
                                    blank = True, null = True) 

    def clean(self):
        filestream = self.avatar.file
        file_object = File(filestream)
        self.thumbnail = file_object

    def save(self, *args, **kwargs):
        WiseAvatar.full_clean(self)
        super(WiseAvatar,self).save(*args, **kwargs)
        
        
            
            
            
    


