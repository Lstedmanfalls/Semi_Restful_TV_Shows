from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Shows

def index(request): #GET REQUEST
    return redirect("/shows")

def shows(request): #GET REQUEST
    context = {
    "all_the_shows": Shows.objects.all(),
    }
    return render(request, "shows.html", context)

def add_show(request): #GET REQUEST
    context = {
    "all_the_shows": Shows.objects.all()
    }
    return render(request, "add_show.html", context)

def create_show(request): #POST Request
    errors = Shows.objects.create_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/new_show")
    elif request.method != "POST":
        return redirect("/")
    elif request.method == "POST":
        create = Shows.objects.create(title = request.POST["title"], network = request.POST["network"], release_date = request.POST["release_date"], description = request.POST["description"])
        show_id = create.id
        messages.success(request, "Show successfully created")
    return redirect(f"/shows/{show_id}")

def view_show(request, show_id): #GET REQUEST
    this_show = Shows.objects.get(id=show_id)
    context = {
    "a_show": this_show
    }
    return render(request, "view_show.html", context)

def edit_show(request, show_id): #GET REQUEST
    this_show = Shows.objects.get(id=show_id)
    context = {
    "a_show": this_show
    }
    return render(request, "edit_show.html", context)

def update_show(request, show_id): #POST Request
    errors = Shows.objects.update_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_id}/edit")
    elif request.method != "POST":
        return redirect("/")
    elif request.method == "POST":
        a_show = Shows.objects.get(id=show_id)
        a_show.title = request.POST["title"]
        a_show.network = request.POST["network"]
        a_show.release_date = request.POST["release_date"]
        a_show.description = request.POST["description"]
        a_show.save()
        messages.success(request, "Show successfully updated")
    return redirect(f"/shows/{show_id}")

def delete_show(request, show_id): #POST Request
    if request.method != "POST":
        return redirect("/")
    if request.method == "POST":
        a_show = Shows.objects.get(id=show_id)
        a_show.delete()
    return redirect("/shows")
