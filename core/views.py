from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')
def projects(request):
    projets = [
        {'id': 1, 'titre': 'Blog Django', 'description': 'Blog avec posts et catégories, authentification utilisateurs.'},
        {'id': 2, 'titre': 'Gestion Station-Service', 'description': 'Application React pour gérer carburant, camions et approvisionnement.'},
        {'id': 3, 'titre': 'Calculatrice Python', 'description': 'Calculatrice Python avec Git et fonctionnalités avancées.'},
    ]
    return render(request, 'core/projects.html', {'projets': projets})