from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    
    try:
        percent = (page_qs.count() / qs.count()) * 100.0
    except:
        percent = 0

    context = {
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent": percent
    }
    
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", context)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    try:
        percent = (page_qs.count() / qs.count()) * 100.0
    except:
        percent = 0

    context = {
        "page_visit_count": page_qs.count(),
        "total_visit_count": qs.count(),
        "percent": percent
    }
    
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", context)

VALID_CODE = "abc123"

def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get("protected_page_allowed") or 0
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed=1
            request.session["protected_page_allowed"] = is_allowed
    
    if is_allowed:
        return  render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})
