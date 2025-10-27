from django import forms

from apps.scores.models import Score


class EditScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ["air_score", "turns_score", "time_score"]
        widgets = {
            "air_score": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "max": "20",
                    "min": "0",
                    "step": "0.1",
                    "type": "number",
                }
            ),
            "turns_score": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "max": "60",
                    "min": "0",
                    "step": "0.1",
                    "type": "number",
                }
            ),
            "time_score": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "max": "20",
                    "min": "0",
                    "step": "0.1",
                    "type": "number",
                }
            ),
        }
