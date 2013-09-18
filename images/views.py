# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect

from models import Image
from forms import ImageForm


def image_list(request):
    images = Image.objects.all()
    return render(request, "images/image_list.html", {'images': images})


def image_upload(request, image_id=None):
    instance = None
    if image_id:
        instance = Image.objects.get(pk=image_id)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.image = ""
            new_instance.save()
            return redirect("image_list")
    else:
        form = ImageForm(instance=instance)

    return render(request, "images/image_upload.html", {'instance': instance, 'form': form})
