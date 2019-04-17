from django.shortcuts import render

# Create your views here.

def steg_base(request):
    return render(request,'audio_steg/base.html')

def steg_welcome(request):
    return render(request, 'audio_steg/welcome.html')

def steg_audio_input(request):
    return render(request, 'audio_steg/audio_input.html')

def steg_text_input(request):
    return render(request, 'audio_steg/text_input.html')

def steg_image_input(request):
    return render(request, 'audio_steg/image_input.html')
