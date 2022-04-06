from django.forms import ModelForm
from .models import Product


class ProductUpdateForm(ModelForm):

    class Meta:
        model = Product
        # fields = ['name', 'description', 'image', 'language', 'time', 'max_players', 'min_players', 'min_age_player',
        #       'type']
        fields = "__all__"