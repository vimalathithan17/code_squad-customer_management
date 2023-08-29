from django.forms import ModelForm,DateField,DateInput
from .models import Customer,CustomerProfile,TravelHistory

class CustomerCreationForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class CustomerProfileForm(ModelForm):
    class Meta:
        model=CustomerProfile
        fields='__all__'

class TravelHistoryForm(ModelForm):
    class Meta:
        model=TravelHistory
        fields='__all__'