from django.urls import path

from mutation_analyzer import views

urlpatterns = [
    path("mutants/", views.MutationAnalyzerView.as_view(), name="mutants"),
    path("stats/", views.StatsView.as_view(), name="stats"),
]
