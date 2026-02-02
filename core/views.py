from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'core/home.html')
def projects(request):
    projets = [
        {'id': 1, 'titre': 'Blog Django', 'description': 'Blog avec posts et catégories, authentification utilisateurs.'},
        {'id': 2, 'titre': 'Gestion Station-Service', 'description': 'Application React pour gérer carburant, camions et approvisionnement.'},
        {'id': 3, 'titre': 'Calculatrice Python', 'description': 'Calculatrice Python avec Git et fonctionnalités avancées.'},
    ]
    return render(request, 'core/projects.html', {'projets': projets})
def project_detail(request, id):
    # Cherche le projet par id
    projet = get_object_or_404([p for p in projets if p['id'] == id], id=id)
    return render(request, 'core/project_detail.html', {'projet': projet})
def skills(request):
    # Liste des compétences
    competences = [
        'Python',
        'Django',
        'HTML',
        'CSS',
        'Git',
        'github',
        'MySQL',
        'Bootstrap'
    ]
    return render(request, 'core/skills.html', {'competences': competences})