# chatbotapp/chatbot.py - Version améliorée avec toutes les questions
class ChatbotGestionProjet:
    def __init__(self):
        self.knowledge_base = self._initialize_knowledge_base()

    def _initialize_knowledge_base(self):
        """Base de connaissances complète avec matching intelligent"""
        return {
            # Définitions fondamentales - Priorité haute
            "chef_projet": {
                "primary_keywords": ["chef de projet", "project manager", "responsable projet", "role chef"],
                "secondary_keywords": ["fonction", "mission", "responsabilite", "quoi", "qui est"],
                "exclude_keywords": ["projet", "definition projet", "c'est quoi un projet"],
                "priority": 10,
                "reponse": "Le Chef de Projet (Project Manager) est la personne responsable de la planification, l'execution et la cloture d'un projet. Il assure la coordination entre les parties prenantes et garantit la livraison dans les delais et le budget."
            },
            "definition_projet": {
                "primary_keywords": ["projet", "definition projet", "c'est quoi un projet", "qu'est-ce qu'un projet"],
                "secondary_keywords": ["definir", "concept", "notion"],
                "exclude_keywords": ["chef de projet", "project manager", "responsable projet"],
                "priority": 9,
                "reponse": "Un projet est un ensemble d'activites a realiser en vue d'un objectif defini, en temps et budget maitrises. Il possede un caractere innovant et unique, avec un debut et une fin definis."
            },
            "gestion_projet": {
                "primary_keywords": ["gestion de projet", "management de projet", "conduite de projet"],
                "secondary_keywords": ["processus", "methodologie"],
                "priority": 8,
                "reponse": "La gestion de projet est l'ensemble des processus et outils qui permettent de conduire et gerer un projet dans le respect des dispositions initiales. C'est un equilibre entre les contraintes du produit, des couts et des delais."
            },

            # Phases et processus
            "phases_projet": {
                "primary_keywords": ["phases", "etapes projet", "phases d'un projet", "cycle de vie"],
                "secondary_keywords": ["etape", "phase", "cycle"],
                "reponse": "Pour un petit projet d'ingenierie : 1) Recueil des besoins, 2) Developpement du produit, 3) Validation, 4) Restitution. Pour un projet spatial : Phase 0 (analyse de mission) a Phase F (retrait de service)."
            },
            "processus_gestion": {
                "primary_keywords": ["processus", "groupes de processus", "processus gestion"],
                "secondary_keywords": ["groupe", "etape", "sequence"],
                "reponse": "Les 5 groupes de processus sont : 1) Demarrage - Autoriser le projet, 2) Planification - Definir les objectifs, 3) Execution - Realiser le travail, 4) Surveillance - Suivre et controler, 5) Cloture - Finaliser le projet."
            },

            # Acteurs et parties prenantes
            "acteurs_projet": {
                "primary_keywords": ["acteurs", "parties prenantes", "stakeholders", "qui sont les acteurs"],
                "secondary_keywords": ["personnes", "intervenants", "participants"],
                "reponse": "Les acteurs principaux sont : le client (maitre d'ouvrage MOA) qui exprime le besoin, et le fournisseur (maitre d'oeuvre MOE) qui satisfait le besoin. L'ensemble des acteurs impliques sont les parties prenantes."
            },
            "moa_moe": {
                "primary_keywords": ["moa", "moe", "maitre d'ouvrage", "maitre d'oeuvre"],
                "secondary_keywords": ["client", "fournisseur", "difference"],
                "reponse": "MOA (Maitre d'Ouvrage) : le client qui exprime le besoin. MOE (Maitre d'Oeuvre) : le fournisseur qui realise la solution. Le MOA valide, le MOE execute."
            },

            # Concepts de base
            "tache": {
                "primary_keywords": ["tache", "lot de travail", "work package", "wp"],
                "secondary_keywords": ["activite", "travail", "lot"],
                "reponse": "Une tache ou lot de travail (Work Package) est une charge de travail qui definit une entite du projet. Les taches presentent des dependances entre elles et sont attribuees a des acteurs specifiques."
            },
            "jalon": {
                "primary_keywords": ["jalon", "milestone", "evenement projet"],
                "secondary_keywords": ["date", "evenement", "repere"],
                "reponse": "Un jalon est un evenement particulier qui marque le debut ou la fin d'une partie bien identifiee du projet. Il est associe a une date precise et sert de repere significatif."
            },
            "livrables": {
                "primary_keywords": ["livrable", "deliverable", "produit livrable"],
                "secondary_keywords": ["resultat", "produit", "delivrable"],
                "reponse": "Les livrables sont les attendus du projet. Il existe : livrables 'produit' (produit, manuels, notices techniques) et livrables 'projet' (documents relatifs au projet lui-meme)."
            },
            "dependances": {
                "primary_keywords": ["dependance", "dependances", "articulation taches"],
                "secondary_keywords": ["relation", "lien", "ordre"],
                "reponse": "Les dependances sont les articulations necessaires entre les taches. Elles definissent les relations de precedence (taches qui doivent etre realisees avant ou apres une tache donnee)."
            },

            # Méthodologies et outils
            "pbs": {
                "primary_keywords": ["pbs", "product breakdown structure", "decomposition produit"],
                "secondary_keywords": ["produit", "structure", "arborescence"],
                "reponse": "Le PBS (Product Breakdown Structure) est la decomposition arborescente du produit en elements. Il repond a la question 'quoi?' et permet une vision modulaire et hierarchique du produit."
            },
            "wbs": {
                "primary_keywords": ["wbs", "work breakdown structure", "decomposition taches"],
                "secondary_keywords": ["travail", "structure", "arborescence"],
                "reponse": "Le WBS (Work Breakdown Structure) est la decomposition arborescente des taches a effectuer. Il repond a 'quoi-faire?' et met en evidence toutes les taches et lots de travail a accomplir."
            },
            "obs": {
                "primary_keywords": ["obs", "organization breakdown structure", "organisation projet"],
                "secondary_keywords": ["organisation", "structure", "responsable"],
                "reponse": "L'OBS (Organization Breakdown Structure) definit 'qui-est-responsable-de-quoi?'. En pratique, on utilise souvent une matrice taches/personnes ou la methode RACI (Responsible, Accountable, Consulted, Informed)."
            },
            "cbs": {
                "primary_keywords": ["cbs", "cost breakdown structure", "decomposition couts"],
                "secondary_keywords": ["cout", "budget", "structure"],
                "reponse": "Le CBS (Cost Breakdown Structure) est la decomposition arborescente des couts du projet. Il permet d'associer a chaque element du projet un cout specifique."
            },
            "sow": {
                "primary_keywords": ["sow", "statement of work", "cahier des charges"],
                "secondary_keywords": ["document", "specification", "cahier"],
                "reponse": "Le Statement of Work (SoW) integre toutes les donnees d'une tache : description, budget, duree, responsable, livrables, risques, protocoles de validation, etc."
            },
            "gantt": {
                "primary_keywords": ["gantt", "diagramme de gantt", "planning"],
                "secondary_keywords": ["diagramme", "calendrier", "temps"],
                "reponse": "Le diagramme de Gantt est une representation visuelle du calendrier projet. Il associe a chaque tache une duree, des jalons et des dependances sur un axe temporel."
            },
            "cqqcoqp": {
                "primary_keywords": ["cqqcoqp", "qui quoi quand", "methode question"],
                "secondary_keywords": ["methode", "question", "analyse"],
                "reponse": "Le CQQCOQP est une methode qui repond aux questions : Qui, Quoi, Quand, Comment, Combien, Pourquoi, et Ou? C'est le fondement de l'analyse projet."
            },

            # Gestion des risques
            "risque": {
                "primary_keywords": ["risque", "gestion des risques", "risk management"],
                "secondary_keywords": ["danger", "incertitude", "probleme"],
                "reponse": "Un risque est un evenement interne ou externe pouvant entrainer un changement dans le deroulement initial du projet. La gestion des risques comprend identification, evaluation, plans de recouvrement et controles."
            },
            "etapes_risques": {
                "primary_keywords": ["etapes gestion risques", "processus risques", "gestion risques"],
                "secondary_keywords": ["etape", "processus", "methode"],
                "reponse": "4 etapes : 1) Definition et identification des risques, 2) Evaluation et classement (impact/probabilite), 3) Elaboration de plans de recouvrement, 4) Controles et alertes."
            },
            "matrice_risques": {
                "primary_keywords": ["matrice risques", "evaluation risques", "impact probabilite"],
                "secondary_keywords": ["matrice", "evaluation", "classement"],
                "reponse": "La matrice impact/probabilite d'occurrence permet de classer les risques. Chaque risque est positionne selon son impact sur le projet et sa probabilite de survenue."
            },

            # Planification et suivi
            "calendrier": {
                "primary_keywords": ["calendrier", "planning", "echeancier"],
                "secondary_keywords": ["temps", "date", "programmation"],
                "reponse": "Le calendrier regroupe l'ensemble des taches sur un axe temporel. Il permet de programmer les activites et de visualiser l'avancement du projet."
            },
            "plan_projet": {
                "primary_keywords": ["plan projet", "project plan", "documentation projet"],
                "secondary_keywords": ["plan", "document", "organisation"],
                "reponse": "Pour les grands projets, le plan-projet articule les differents aspects : plan de demarrage, plan de travail, plan de suivi, gestion des risques, plan qualite, gestion de configuration, etc."
            },

            # Qualité et validation
            "validation": {
                "primary_keywords": ["validation", "protocole validation", "acceptation"],
                "secondary_keywords": ["verification", "test", "acceptation"],
                "reponse": "La validation assure que le produit repond aux exigences du client. Des protocoles de validation sont definis dans le Statement of Work pour chaque tache."
            },

            # Outils logiciels
            "logiciels": {
                "primary_keywords": ["logiciel", "outil gestion", "software", "ganttproject"],
                "secondary_keywords": ["outil", "application", "programme"],
                "reponse": "Pour petits projets : Ganttproject (gratuit). Autres outils : OpenProj, XMind. Pour projets industriels : MS Project. Solutions SaaS : ClockingTT, Collabtive, ProjectPier."
            },

            # Méthodes spécifiques
            "raci": {
                "primary_keywords": ["raci", "matrice raci", "responsabilites"],
                "secondary_keywords": ["matrice", "role", "responsabilite"],
                "reponse": "La methode RACI definit les roles : R (Responsible - execute), A (Accountable - valide), C (Consulted - consulte), I (Informed - informe). Utilisee dans la matrice des responsabilites."
            },
            "complexite": {
                "primary_keywords": ["complexite", "projet complexe", "grand projet"],
                "secondary_keywords": ["difficile", "complique", "ampleur"],
                "reponse": "La complexite d'un projet augmente avec : la complexite technique, le nombre d'acteurs, les differences culturelles, les legislations, etc. Cela demande une organisation structuree."
            },
            "objectif_projet": {
                "primary_keywords": ["objectif", "but projet", "finalite"],
                "secondary_keywords": ["but", "finalite", "destination"],
                "reponse": "L'objectif du projet doit etre bien defini prealablement, avec des livrables fournis a dates definies, dans des delais et budget maitrises."
            },
            "contraintes": {
                "primary_keywords": ["contrainte", "triple contrainte", "delai cout qualite"],
                "secondary_keywords": ["limitation", "restriction", "equilibre"],
                "reponse": "La triple contrainte en gestion de projet : equilibre entre les contraintes du produit (qualite, exigences techniques), les couts et les delais. Modifier une variable affecte les autres."
            }
        }

    def get_response(self, user_input):
        """Réponse avec matching intelligent et différenciation"""
        user_input_lower = user_input.lower().strip()

        # Nettoyage de la question
        cleaned_input = self._clean_input(user_input_lower)

        # Recherche de la meilleure correspondance
        best_match = self._find_best_match(cleaned_input)

        if best_match:
            return best_match["reponse"]

        # Si pas de correspondance claire, donner des suggestions contextuelles
        return self._get_contextual_suggestion(cleaned_input)

    def _clean_input(self, text):
        """Nettoie et normalise le texte d'entrée"""
        import re
        # Supprimer la ponctuation excessive
        text = re.sub(r'[^\w\s]', ' ', text)
        # Normaliser les espaces
        text = ' '.join(text.split())
        return text

    def _find_best_match(self, question):
        """Trouve la meilleure correspondance avec scoring avancé"""
        best_match = None
        best_score = 0

        for key, data in self.knowledge_base.items():
            score = self._calculate_match_score(question, data)

            # Appliquer la priorité
            priority = data.get("priority", 1)
            score *= priority

            if score > best_score:
                best_score = score
                best_match = data

        # Seuil minimum pour éviter les mauvaises correspondances
        if best_score >= 2:
            return best_match

        return None

    def _calculate_match_score(self, question, data):
        """Calcule un score de matching intelligent"""
        score = 0

        # Points pour les mots-clés primaires (forte pondération)
        for keyword in data["primary_keywords"]:
            if self._contains_word(question, keyword):
                score += 3

        # Points pour les mots-clés secondaires
        for keyword in data.get("secondary_keywords", []):
            if keyword in question:
                score += 1

        # Pénalités pour les mots exclus
        for exclude_word in data.get("exclude_keywords", []):
            if self._contains_word(question, exclude_word):
                score -= 4  # Forte pénalité

        # Bonus pour les questions commençant par des mots interrogatifs
        question_starters = ["qu'est", "c'est", "quoi", "comment", "qui", "quand", "ou", "pourquoi"]
        if any(question.startswith(starter) for starter in question_starters):
            score += 1

        return score

    def _contains_word(self, text, word):
        """Vérifie si le mot est présent dans le texte (match partiel intelligent)"""
        return word in text

    def _get_contextual_suggestion(self, question):
        """Donne des suggestions basées sur le contexte de la question"""
        if "projet" in question:
            if any(word in question for word in ["chef", "manager", "responsable"]):
                return "Je pense que vous demandez sur le CHEF DE PROJET. Pour une reponse precise, essayez : 'Quel est le role du chef de projet ?'"
            else:
                return "Voulez-vous savoir sur le PROJET lui-meme ou sur le CHEF DE PROJET ? Essayez : 'Definition d un projet' ou 'Role du chef de projet'"

        elif any(word in question for word in ["risque", "danger", "probleme"]):
            return "Si vous parlez de gestion des RISQUES, essayez : 'gestion des risques' ou 'etapes gestion risques'"

        elif any(word in question for word in ["planning", "calendrier", "temps"]):
            return "Pour les questions de PLANIFICATION, essayez : 'diagramme de gantt' ou 'calendrier projet'"

        else:
            suggestions = [
                "chef de projet", "definition projet", "gestion de projet",
                "processus", "risques", "gantt", "livrables"
            ]
            return f"Je n'ai pas compris. Suggestions : {', '.join(suggestions[:5])}..."


# Instance globale
chatbot = ChatbotGestionProjet()