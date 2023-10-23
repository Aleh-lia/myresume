from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import logging
from django.db.models import Count
from resume.models import *

# Create your views here.


logger = logging.getLogger(__name__)

def index(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Главная страница",
        "content": "",
    }
    authors = Author.objects.all()
    context["authors"] = authors
    return render(request, template_name="resume/index.html", context=context)

def fullname(request: HttpRequest) -> HttpResponse:
    clients_with_order_counts = Author.objects.annotate(order_count=Count("orders"))
    return render(
        request, "resume/index.html", context={"clients": clients_with_order_counts}
    )

def job(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Опыт работы",
        "content": "",
    }
    jobs = Job.objects.all()
    context["jobs"] = jobs
    return render(request, template_name="resume/job.html", context=context)

def education(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Образование",
        "content": "",
    }
    educations = University.objects.all()
    context["educations"] = educations
    return render(request, template_name="resume/education.html", context=context)

def skills(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Навыки",
        "content": "",
    }
    skills = Skills.objects.all()
    context["skills"] = skills
    return render(request, template_name="resume/skills_geek.html", context=context)