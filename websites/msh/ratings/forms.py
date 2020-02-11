from django import forms
from .models import Rating
from crispy_forms.helper import FormHelper


def get_client_ip(request):
    try:
        # ip addresses: 'client,proxy1,proxy2'
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ''
    return ip


class Text:
    """text for rating fields in forms"""
    info = ("The availability of information about "
            "your city's or town's services")
    housing = 'Your satisfaction with the cost of housing'
    schools = 'The quality of public schools'
    police = 'Your trust in the local police'
    streets = 'The maintenance of streets and sidewalks'
    events = 'The availability of social community events'


def set_rating_choice_field(widget=None):
    """In form classes, this helps set rating fields to forms.ChoiceField."""
    def make_choice(choice_text):
        CHOICES = [(5, f'5: {choice_text} is high.'), (4, '4'), (3, '3'),
                   (2, '2'), (1, f'1: {choice_text} is low.')]
        if widget:
            choice_field = forms.ChoiceField(widget=widget, choices=CHOICES)
        else:
            choice_field = forms.ChoiceField(choices=CHOICES)
        return choice_field
    return make_choice


class Survey_Form(forms.ModelForm):
    """for submitting happiness surveys"""
    happy = forms.ChoiceField(widget=forms.RadioSelect, choices=[
                              (1, "1: You're happy."),
                              (0, "0: You're not happy.")])

    __choice_field = set_rating_choice_field(widget=forms.RadioSelect)
    info = __choice_field(choice_text=Text.info)
    housing = __choice_field(Text.housing)
    schools = __choice_field(Text.schools)
    police = __choice_field(Text.police)
    streets = __choice_field(Text.streets)
    events = __choice_field(Text.events)

    class Meta:
        model = Rating
        # fields = '__all__'
        fields = [
            'happy',
            'info',
            'housing',
            'schools',
            'police',
            'streets',
            'events',
        ]


class Predict_Survey_Form(forms.Form):
    """for happiness predictions"""
    __choice_field = set_rating_choice_field()
    info = __choice_field(choice_text=Text.info)
    housing = __choice_field(Text.housing)
    schools = __choice_field(Text.schools)
    police = __choice_field(Text.police)
    streets = __choice_field(Text.streets)
    events = __choice_field(Text.events)
