from django import forms
from .models import Product

PUBLISH_CHOICES = (
   # ('', ""),
    ('publish', "Publish"),
    ('draft', "Draft")
)

class ProductAddForm(forms.Form):
    title = forms.CharField(label="Your Title", widget=forms.TextInput(
        attrs={
            "class": "custom-class",
            "placeholder": "Title"
        }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "my-custo-class",
            "placeholder": "Description",
            "some-attr": "haha",
        }
    ))
    price = forms.DecimalField()
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=False)

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00 :
            raise forms.ValidationError("Price must be greater than 1")
        elif price >= 99.99:
            raise forms.ValidationError("Price must be less than 100")
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) >= 3:
            return title
        else:
            raise forms.ValidationError("Title must be greater than 3 characters long")

class ProductModelForm(forms.ModelForm):
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=False)

    title = forms.CharField(label="Your Title", widget=forms.TextInput(
        attrs={
            "class": "custom-class",
            "placeholder": "Title"
        }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "my-custo-class",
            "placeholder": "Description",
            "some-attr": "haha",
        }
    ))


    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
        ]
        # widgets = {
        #     "title": forms.TextInput(
        #         attrs={
        #             "placeholder": "Title"
        #         }
        #     )
        # }
    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00 :
            raise forms.ValidationError("Price must be greater than 1")
        elif price >= 100.00:
            raise forms.ValidationError("Price must be less than 100")
        else:
            return price

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) >= 3:
            return title
        else:
            raise forms.ValidationError("Title must be greater than 3 characters long")
