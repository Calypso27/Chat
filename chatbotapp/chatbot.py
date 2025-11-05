import re
import unicodedata


class ChatbotGestionProjet:
    def __init__(self):
        self.knowledge_base = self._initialize_knowledge_base()

    def _initialize_knowledge_base(self):
        """Base de connaissances avec keywords précis"""
        return {
            "chef_projet": {
                "exact_phrases": ["chef de projet", "project manager", "responsable projet"],
                "keywords": ["chef", "manager", "pm", "responsable"],
                "context_words": ["role", "mission", "fonction", "qui"],
                "exclude_exact": ["gestion de projet", "management de projet"],
                "reponse": "Le Chef de Projet (Project Manager) est la personne responsable de la planification, l'exécution et la clôture d'un projet. Il assure la coordination entre les parties prenantes et garantit la livraison dans les délais et le budget."
            },
            "definition_projet": {
                "exact_phrases": ["c'est quoi un projet", "qu'est-ce qu'un projet", "définition projet"],
                "keywords": ["projet"],
                "context_words": ["définition", "définir", "concept", "qu'est", "c'est quoi"],
                "exclude_exact": ["chef de projet", "gestion de projet", "project manager"],
                "reponse": "Un projet est un ensemble d'activités à réaliser en vue d'un objectif défini, en temps et budget maîtrisés. Il possède un caractère innovant et unique, avec un début et une fin définis."
            },
            "gestion_projet": {
                "exact_phrases": ["gestion de projet", "management de projet", "conduite de projet"],
                "keywords": ["gestion", "management", "conduite"],
                "context_words": ["processus", "méthodologie", "comment gérer"],
                "exclude_exact": ["chef de projet"],
                "reponse": "La gestion de projet est l'ensemble des processus et outils qui permettent de conduire et gérer un projet dans le respect des dispositions initiales. C'est un équilibre entre les contraintes du produit, des coûts et des délais."
            },
            "phases_projet": {
                "exact_phrases": ["phases projet", "étapes projet", "cycle de vie"],
                "keywords": ["phases", "étapes", "cycle"],
                "context_words": ["déroulement", "processus"],
                "reponse": "Pour un petit projet d'ingénierie : 1) Recueil des besoins, 2) Développement du produit, 3) Validation, 4) Restitution. Pour un projet spatial : Phase 0 (analyse de mission) à Phase F (retrait de service)."
            },
            "processus_gestion": {
                "exact_phrases": ["processus gestion", "groupes de processus"],
                "keywords": ["processus"],
                "context_words": ["groupe", "étape", "séquence"],
                "reponse": "Les 5 groupes de processus sont : 1) Démarrage - Autoriser le projet, 2) Planification - Définir les objectifs, 3) Exécution - Réaliser le travail, 4) Surveillance - Suivre et contrôler, 5) Clôture - Finaliser le projet."
            },
            "acteurs_projet": {
                "exact_phrases": ["acteurs projet", "parties prenantes"],
                "keywords": ["acteurs", "stakeholders", "parties prenantes"],
                "context_words": ["qui", "personnes", "intervenants"],
                "reponse": "Les acteurs principaux sont : le client (maître d'ouvrage MOA) qui exprime le besoin, et le fournisseur (maître d'œuvre MOE) qui satisfait le besoin. L'ensemble des acteurs impliqués sont les parties prenantes."
            },
            "moa_moe": {
                "exact_phrases": ["moa moe", "maitre ouvrage oeuvre"],
                "keywords": ["moa", "moe", "maître", "ouvrage", "oeuvre"],
                "context_words": ["différence", "client", "fournisseur"],
                "reponse": "MOA (Maître d'Ouvrage) : le client qui exprime le besoin. MOE (Maître d'Œuvre) : le fournisseur qui réalise la solution. Le MOA valide, le MOE exécute."
            },
            "tache": {
                "exact_phrases": ["tâche", "lot de travail", "work package"],
                "keywords": ["tache", "tâche", "lot", "wp"],
                "context_words": ["activité", "travail"],
                "reponse": "Une tâche ou lot de travail (Work Package) est une charge de travail qui définit une entité du projet. Les tâches présentent des dépendances entre elles et sont attribuées à des acteurs spécifiques."
            },
            "jalon": {
                "exact_phrases": ["jalon", "milestone"],
                "keywords": ["jalon", "milestone"],
                "context_words": ["événement", "date", "repère"],
                "reponse": "Un jalon est un événement particulier qui marque le début ou la fin d'une partie bien identifiée du projet. Il est associé à une date précise et sert de repère significatif."
            },
            "livrables": {
                "exact_phrases": ["livrable", "deliverable"],
                "keywords": ["livrable", "deliverable"],
                "context_words": ["résultat", "produit", "attendu"],
                "reponse": "Les livrables sont les attendus du projet. Il existe : livrables 'produit' (produit, manuels, notices techniques) et livrables 'projet' (documents relatifs au projet lui-même)."
            },
            "dependances": {
                "exact_phrases": ["dépendance", "dépendances tâches"],
                "keywords": ["dépendance", "dépendances"],
                "context_words": ["relation", "lien", "ordre", "articulation"],
                "reponse": "Les dépendances sont les articulations nécessaires entre les tâches. Elles définissent les relations de précédence (tâches qui doivent être réalisées avant ou après une tâche donnée)."
            },
            "pbs": {
                "exact_phrases": ["pbs", "product breakdown structure"],
                "keywords": ["pbs"],
                "context_words": ["produit", "décomposition"],
                "reponse": "Le PBS (Product Breakdown Structure) est la décomposition arborescente du produit en éléments. Il répond à la question 'quoi?' et permet une vision modulaire et hiérarchique du produit."
            },
            "wbs": {
                "exact_phrases": ["wbs", "work breakdown structure"],
                "keywords": ["wbs"],
                "context_words": ["tâches", "décomposition", "travail"],
                "reponse": "Le WBS (Work Breakdown Structure) est la décomposition arborescente des tâches à effectuer. Il répond à 'quoi-faire?' et met en évidence toutes les tâches et lots de travail à accomplir."
            },
            "obs": {
                "exact_phrases": ["obs", "organization breakdown structure"],
                "keywords": ["obs"],
                "context_words": ["organisation", "responsable"],
                "reponse": "L'OBS (Organization Breakdown Structure) définit 'qui-est-responsable-de-quoi?'. En pratique, on utilise souvent une matrice tâches/personnes ou la méthode RACI."
            },
            "cbs": {
                "exact_phrases": ["cbs", "cost breakdown structure"],
                "keywords": ["cbs"],
                "context_words": ["coût", "budget"],
                "reponse": "Le CBS (Cost Breakdown Structure) est la décomposition arborescente des coûts du projet. Il permet d'associer à chaque élément du projet un coût spécifique."
            },
            "sow": {
                "exact_phrases": ["sow", "statement of work", "cahier des charges"],
                "keywords": ["sow", "cahier"],
                "context_words": ["spécification", "charges"],
                "reponse": "Le Statement of Work (SoW) intègre toutes les données d'une tâche : description, budget, durée, responsable, livrables, risques, protocoles de validation, etc."
            },
            "gantt": {
                "exact_phrases": ["gantt", "diagramme de gantt"],
                "keywords": ["gantt"],
                "context_words": ["diagramme", "planning", "calendrier"],
                "reponse": "Le diagramme de Gantt est une représentation visuelle du calendrier projet. Il associe à chaque tâche une durée, des jalons et des dépendances sur un axe temporel."
            },
            "cqqcoqp": {
                "exact_phrases": ["cqqcoqp"],
                "keywords": ["cqqcoqp"],
                "context_words": ["qui quoi quand", "méthode"],
                "reponse": "Le CQQCOQP est une méthode qui répond aux questions : Qui, Quoi, Quand, Comment, Combien, Pourquoi, et Où? C'est le fondement de l'analyse projet."
            },
            "risque": {
                "exact_phrases": ["risque", "gestion des risques"],
                "keywords": ["risque", "risques"],
                "context_words": ["danger", "incertitude"],
                "reponse": "Un risque est un événement interne ou externe pouvant entraîner un changement dans le déroulement initial du projet. La gestion des risques comprend identification, évaluation, plans de recouvrement et contrôles."
            },
            "etapes_risques": {
                "exact_phrases": ["étapes gestion risques", "processus risques"],
                "keywords": ["étapes"],
                "context_words": ["risques", "processus"],
                "reponse": "4 étapes : 1) Définition et identification des risques, 2) Évaluation et classement (impact/probabilité), 3) Élaboration de plans de recouvrement, 4) Contrôles et alertes."
            },
            "matrice_risques": {
                "exact_phrases": ["matrice risques", "impact probabilité"],
                "keywords": ["matrice"],
                "context_words": ["risques", "évaluation"],
                "reponse": "La matrice impact/probabilité d'occurrence permet de classer les risques. Chaque risque est positionné selon son impact sur le projet et sa probabilité de survenue."
            },
            "calendrier": {
                "exact_phrases": ["calendrier", "planning"],
                "keywords": ["calendrier", "planning"],
                "context_words": ["temps", "échéancier"],
                "reponse": "Le calendrier regroupe l'ensemble des tâches sur un axe temporel. Il permet de programmer les activités et de visualiser l'avancement du projet."
            },
            "plan_projet": {
                "exact_phrases": ["plan projet", "project plan"],
                "keywords": ["plan"],
                "context_words": ["projet", "documentation"],
                "reponse": "Pour les grands projets, le plan-projet articule les différents aspects : plan de démarrage, plan de travail, plan de suivi, gestion des risques, plan qualité, gestion de configuration, etc."
            },
            "validation": {
                "exact_phrases": ["validation", "protocole validation"],
                "keywords": ["validation"],
                "context_words": ["vérification", "test", "acceptation"],
                "reponse": "La validation assure que le produit répond aux exigences du client. Des protocoles de validation sont définis dans le Statement of Work pour chaque tâche."
            },
            "logiciels": {
                "exact_phrases": ["logiciel gestion", "outil gestion"],
                "keywords": ["logiciel", "outil", "software"],
                "context_words": ["application", "programme"],
                "reponse": "Pour petits projets : Ganttproject (gratuit). Autres outils : OpenProj, XMind. Pour projets industriels : MS Project. Solutions SaaS : ClockingTT, Collabtive, ProjectPier."
            },
            "raci": {
                "exact_phrases": ["raci", "matrice raci"],
                "keywords": ["raci"],
                "context_words": ["responsabilités", "matrice"],
                "reponse": "La méthode RACI définit les rôles : R (Responsible - exécute), A (Accountable - valide), C (Consulted - consulté), I (Informed - informé). Utilisée dans la matrice des responsabilités."
            },
            "complexite": {
                "exact_phrases": ["complexité projet", "projet complexe"],
                "keywords": ["complexité", "complexe"],
                "context_words": ["difficile", "compliqué"],
                "reponse": "La complexité d'un projet augmente avec : la complexité technique, le nombre d'acteurs, les différences culturelles, les législations, etc. Cela demande une organisation structurée."
            },
            "objectif_projet": {
                "exact_phrases": ["objectif projet", "but projet"],
                "keywords": ["objectif", "but"],
                "context_words": ["finalité", "destination"],
                "reponse": "L'objectif du projet doit être bien défini préalablement, avec des livrables fournis à dates définies, dans des délais et budget maîtrisés."
            },
            "contraintes": {
                "exact_phrases": ["contrainte", "triple contrainte"],
                "keywords": ["contrainte", "contraintes"],
                "context_words": ["délai", "coût", "qualité"],
                "reponse": "La triple contrainte en gestion de projet : équilibre entre les contraintes du produit (qualité, exigences techniques), les coûts et les délais. Modifier une variable affecte les autres."
            }
        }

    def _normalize_text(self, text):
        """Normalise le texte (accents, casse)"""
        # Convertir en minuscules
        text = text.lower()
        # Retirer les accents
        text = ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )
        return text

    def _clean_input(self, text):
        """Nettoie le texte d'entrée"""
        # Normaliser
        text = self._normalize_text(text)
        # Supprimer ponctuation excessive mais garder apostrophes
        text = re.sub(r'[^\w\s\']', ' ', text)
        # Normaliser espaces
        text = ' '.join(text.split())
        return text

    def get_response(self, user_input):
        """Trouve la meilleure réponse avec discrimination intelligente"""
        cleaned = self._clean_input(user_input)

        # Recherche avec scoring amélioré
        best_match = self._find_best_match(cleaned)

        if best_match:
            return best_match["reponse"]

        return self._get_contextual_suggestion(cleaned)

    def _find_best_match(self, question):
        """Trouve la meilleure correspondance avec scoring discriminant"""
        scores = {}

        for key, data in self.knowledge_base.items():
            score = self._calculate_smart_score(question, data)
            scores[key] = (score, data)

        # Trier par score
        sorted_matches = sorted(scores.items(), key=lambda x: x[1][0], reverse=True)

        if sorted_matches and sorted_matches[0][1][0] > 0:
            return sorted_matches[0][1][1]

        return None

    def _calculate_smart_score(self, question, data):
        """Calcul de score intelligent avec discrimination"""
        score = 0

        # 1. Phrases exactes (priorité maximale)
        for phrase in data.get("exact_phrases", []):
            phrase_norm = self._normalize_text(phrase)
            if phrase_norm in question:
                score += 50  # Très fort

        # 2. Exclure si phrases d'exclusion présentes
        for exclude in data.get("exclude_exact", []):
            exclude_norm = self._normalize_text(exclude)
            if exclude_norm in question:
                return -100  # Disqualifié

        # 3. Mots-clés avec matching exact de mot
        for keyword in data.get("keywords", []):
            keyword_norm = self._normalize_text(keyword)
            if self._exact_word_match(question, keyword_norm):
                score += 10

        # 4. Mots de contexte (bonus léger)
        for ctx_word in data.get("context_words", []):
            ctx_norm = self._normalize_text(ctx_word)
            if ctx_norm in question:
                score += 3

        return score

    def _exact_word_match(self, text, word):
        """Vérifie si le mot est présent comme mot entier"""
        pattern = r'\b' + re.escape(word) + r'\b'
        return bool(re.search(pattern, text))

    def _get_contextual_suggestion(self, question):
        """Suggestions contextuelles"""
        suggestions = []

        # Analyser le contexte
        if any(w in question for w in ["chef", "manager", "responsable"]):
            suggestions.append("chef de projet")

        if any(w in question for w in ["definition", "c'est quoi", "qu'est"]):
            if "projet" in question and "chef" not in question:
                suggestions.append("définition projet")

        if any(w in question for w in ["gestion", "management", "gerer"]):
            suggestions.append("gestion de projet")

        if any(w in question for w in ["risque", "danger"]):
            suggestions.append("gestion des risques")

        if any(w in question for w in ["planning", "calendrier", "gantt"]):
            suggestions.append("diagramme de gantt")

        if suggestions:
            return f"Je n'ai pas trouvé de réponse exacte. Vouliez-vous demander : {', '.join(suggestions)} ?"

        return "Je n'ai pas compris votre question. Essayez : 'Qu'est-ce qu'un projet ?', 'Rôle du chef de projet', 'Gestion des risques', etc."



chatbot = ChatbotGestionProjet()
