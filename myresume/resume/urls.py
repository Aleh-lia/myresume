from django.urls import path


from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('job/', job, name="job"),
    path('education/', education, name="education"),
    path('skills/', skills, name="skills"),
]