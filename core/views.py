from django.http import HttpResponse

# ======================
# DONNÉES EN DUR
# ======================
PROJETS = [
    {
        'id': 1,
        'titre': 'Blog Django',
        'description': 'Blog avec posts et catégories, authentification utilisateurs.',
        'techno': ['Python', 'Django', 'HTML', 'CSS', 'Git']
    },
    {
        'id': 2,
        'titre': 'Gestion Station-Service',
        'description': 'Application React pour gérer carburant, camions et approvisionnement.',
        'techno': ['React', 'JavaScript', 'Git']
    },
    {
        'id': 3,
        'titre': 'Calculatrice Python',
        'description': 'Calculatrice Python avec Git et fonctionnalités avancées.',
        'techno': ['Python', 'Git']
    },
]

# ======================
# PAGE ACCUEIL
# ======================
def home(request):
    return HttpResponse("""
        <h1>Bienvenue sur mon portfolio personnel.</h1>
        <h2>Djenabou Balde</h2>
        <h4 class="text-muted">Diplômée en MIAGE – Analyse & Développement</h4>
        <p class="mt-3">
            Développeuse passionnée par la conception d’applications web modernes,
            performantes et bien structurées.
        </p>
        <a href="/projects/">Mes Projets</a> |
        <a href="/skills/">Compétences</a> |
        <a href="/contact/">Contact</a>
    """)

# ======================
# PAGE MES PROJETS
# ======================
def projects(request):
    html = "<h1>Mes Projets</h1><ul>"

    for p in PROJETS:
        html += f"""
            <li>
                <strong>{p['titre']}</strong><br>
                {p['description']}<br>
                <a href="/project/{p['id']}/">Voir détails</a>
            </li><br>
        """

    html += "</ul><a href='/'>Retour Accueil</a>"
    return HttpResponse(html)

# ======================
# PAGE DÉTAIL PROJET
# ======================
def project_detail(request, id):
    projet = None
    for p in PROJETS:
        if p['id'] == id:
            projet = p
            break

    if projet is None:
        return HttpResponse("<h2>Projet non trouvé</h2>", status=404)

    html = f"""
        <h1>{projet['titre']}</h1>
        <p>{projet['description']}</p>

        <h4>Technologies utilisées :</h4>
        <ul>
    """

    for tech in projet['techno']:
        html += f"<li>{tech}</li>"

    html += """
        </ul>
        <a href="/projects/">Retour aux projets</a>
    """

    return HttpResponse(html)

# ======================
# PAGE COMPÉTENCES
# ======================
def skills(request):
    competences = [
        'Python', 'Django', 'HTML', 'CSS',
        'Git', 'GitHub', 'MySQL', 'Bootstrap'
    ]

    html = "<h1>Mes Compétences</h1><ul>"
    for c in competences:
        html += f"<li>{c}</li>"
    html += "</ul><a href='/'>Retour Accueil</a>"

    return HttpResponse(html)

# ======================
# PAGE CONTACT (GET)
# ======================
def contact(request):
    nom = request.GET.get('nom', '')
    email = request.GET.get('email', '')
    message = request.GET.get('message', '')

    html = """
        <h1>Contact</h1>

        <form method="get">
            Nom : <input type="text" name="nom"><br><br>
            Email : <input type="email" name="email"><br><br>
            Message : <textarea name="message"></textarea><br><br>
            <button type="submit">Envoyer</button>
        </form>
    """

    if nom and email and message:
        html += f"""
            <hr>
            <h3>Message reçu :</h3>
            <p><strong>Nom :</strong> {nom}</p>
            <p><strong>Email :</strong> {email}</p>
            <p><strong>Message :</strong> {message}</p>
        """

    html += "<br><a href='/'>Retour Accueil</a>"

    return HttpResponse(html)
