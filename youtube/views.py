from django.shortcuts import render, redirect
from pytube import YouTube
# Create your views here.
def main(request):
    if request.method=="POST":
        link = request.POST.get('link')
        yt = YouTube(link)
        yt.streams.filter(mime_type="video/mp4",progressive=True).order_by('resolution').desc().first().download("D:/")
        return render(request,"appreciate.html")
    return render(request,"main.html")