from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "npm": "2506617512", 
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik "
            "pada pengembangan produk, manajemen proyek, dan teknologi."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Hasya Azzahra Rangkuti",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)