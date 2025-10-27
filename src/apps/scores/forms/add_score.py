from django import forms

from apps.participants.models import Participant


class ParticipantForm(forms.Form):
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
                "type": "number",
            }
        ),
    )
