from import_export import resources
from .models import uploadModel

class uploadResource(resources.ModelResource):
    class Meta:
        model = uploadModel
