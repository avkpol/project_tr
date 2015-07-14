from django.contrib import admin

from src.project_tr.models.control import Control
from src.project_tr.models.control_type import ControlType
from src.project_tr.models.control_classification import ControlClassification


admin.site.register(Control)
admin.site.register(ControlType)
admin.site.register(ControlClassification)

# Register your models here.
