import logging

from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from apps.events.models import Event
from apps.scores.models import Score
from apps.scores.forms.edit_score import EditScoreForm
from apps.scores.services.edit_participant_score import EditParticipantScoreService

logger = logging.getLogger(__name__)


class EditScoreView(View):
    template_name = "edit_score.html"

    def get(self, request, event_id: int, score_id: int):
        """
        Presents the score form for creating a new score.
        """
        score = Score.objects.get(id=score_id)
        context = {
            "event": Event.objects.get(id=event_id),
            "edit_score_form": EditScoreForm(instance=score),
        }
        return render(request, self.template_name, context=context)

    def post(self, request, event_id: int, score_id: int):
        """
        Creates a new score entry for a given participant and event.
        User sent data is validated before any write operation.
        """
        event = Event.objects.get(id=event_id)
        edit_score_form = EditScoreForm(request.POST)
        if edit_score_form.is_valid():
            print(edit_score_form.cleaned_data)
            edit_participant_score_service = EditParticipantScoreService()
            edit_participant_score_service.execute(
                score_id=score_id,
                air_score=edit_score_form.cleaned_data["air_score"],
                turns_score=edit_score_form.cleaned_data["turns_score"],
                time_score=edit_score_form.cleaned_data["time_score"],
            )
            return redirect(reverse("ranking", args=[event_id]))
        context = {
            "event": event,
            "edit_score_form": edit_score_form,
        }
        return render(request, self.template_name, context=context)
