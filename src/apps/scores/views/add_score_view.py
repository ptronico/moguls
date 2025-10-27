from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from apps.events.models import Event
from apps.scores.forms.add_score import ParticipantForm
from apps.scores.services.add_participant_score import AddParticipantScoreService


class AddScoreView(View):
    def get(self, request, event_id: int):
        context = {
            "event": Event.objects.get(id=event_id),
            "participant_form": ParticipantForm(),
        }
        return render(request, "add_score.html", context=context)

    def post(self, request, event_id: int):
        event = Event.objects.get(id=event_id)
        participant_form = ParticipantForm(request.POST)
        if participant_form.is_valid():
            add_participant_score_service = AddParticipantScoreService()
            add_participant_score_service.execute(
                event_id=event.id,
                participant_id=participant_form.cleaned_data["participant"].id,
                air_score=participant_form.cleaned_data["air_score"],
                turns_score=participant_form.cleaned_data["turns_score"],
                time_score=participant_form.cleaned_data["time_score"],
            )
            return redirect(reverse("ranking", args=[event_id]))
        context = {
            "event": event,
            "participant_form": participant_form,
        }
        return render(request, "add_score.html", context=context)
