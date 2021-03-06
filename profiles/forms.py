"""
Models for form in user profile and adding a review
"""
from django import forms
from .models import Review, UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form to update or maintain the user profile
    """
    class Meta:
        """
        The form inherits from the UserProfile model,
        except for the 'user' field since that one is unique
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-secondary rounded-pill profile-form-input')
            self.fields[field].label = False


RATING_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]


class ReviewForm(forms.ModelForm):
    """
    Model for the review form
    """
    rating = forms.DecimalField(
            max_digits=2, decimal_places=1,
            widget=forms.Select(choices=RATING_CHOICES))
    review = forms.CharField(widget=forms.Textarea)

    class Meta:
        """
        It uses two specific fields of the Review model
        """
        model = Review
        fields = ['rating', 'review']
