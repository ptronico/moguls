from django import forms

from apps.participants.models import Participant


class EditScoreForm(forms.Form):
    """
    Form for cleaning user submited data for creating
    new score of a participant in an event.
    """

    participant = forms.ModelChoiceField(
        queryset=Participant.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-control"},
        ),
    )
    air_score = forms.FloatField(
        max_value=20.0,
        label="Air score",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "max": "20",
                "min": "0",
                "step": "0.1",
                "type": "number",
            }
        ),
    )
    turns_score = forms.FloatField(
        max_value=60.0,
        label="Turns score",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "max": "60",
                "min": "0",
                "step": "0.1",
                "type": "number",
            }
        ),
    )
    time_score = forms.FloatField(
        max_value=20.0,
        label="Time score",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "max": "20",
                "min": "0",
                "step": "0.1",
                "type": "number",
            }
        ),
    )
