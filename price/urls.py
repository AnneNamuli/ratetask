from django.urls import path
from price import views

path(
        "rates/<\d{4}-\d{2}-\d{2}:date_from>/<str:date_to>/<str:origin>/<str:destination>",
        views.AverageDailyPrice.as_view(),
        name="rates",
    ),
