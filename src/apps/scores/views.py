from django.shortcuts import render

from .models import Score


def ranking(request):
    scores = Score.objects.filter().order_by("-total_score")
    return render(request, "ranking.html", context={"scores": scores})
