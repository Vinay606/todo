from django.forms import ModelForm
from . models import todo
class todoform(ModelForm):
    class Meta:
        model=todo
        fields='__all__'
