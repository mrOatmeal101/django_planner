from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Room
from django.forms import modelform_factory

# Create your views here.
def detail(request, id):
    # meeting = Meeting.objects.get(pk=id) # pk means primary key
    meeting = get_object_or_404(Meeting, pk=id) # another way to do the above but send to 404 if try to got to page not found
    return render(request, "meetings/detail.html", {"meeting": meeting})

def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {'rooms': Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {"form": form})