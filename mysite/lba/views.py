from django.shortcuts import render
from .models import mode_list


def mode_choise(request):
    modes = ''
    for i in range(len(mode_list)):
        modes += f"<tr><td><a href='{i}/'><strong>{mode_list[i]['name']}</strong></a></td>" \
                 f"<td> - &nbsp;&nbsp;{mode_list[i]['description']}</td>"
    context = {
        'modes': modes,
    }
    return render(request, 'lba/mode-list.html', context)


def mode_run(request, id):
    name = mode_list[id]['name']
    description = modes_list[id]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'lba/mode-detail.html', context)
