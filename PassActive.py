from fpdf import FPDF
from fpdf.enums import XPos, YPos

class QuestionnairePDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "Questionnaire : Profil de Competences & Orientation Metiers", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(5)

    def question(self, num, text, options=None):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, f"{num}. {text}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        if options:
            self.set_font("Helvetica", "", 11)
            for opt in options:
                self.cell(0, 8, f"   [ ] {opt}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

pdf = QuestionnairePDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Questions
pdf.question(1, "Quelles sont les taches que vous avez le plus souvent realisees dans vos precedentes experiences ?", [
    "Accueil du public / relation client",
    "Utilisation de machines / conduite d'engins",
    "Manipulation de chiffres / gestion administrative",
    "Vente / negociation",
    "Organisation / logistique / gestion des stocks",
    "Soin aux personnes / accompagnement",
    "Bricolage / reparation / entretien",
    "Animation / enseignement / formation",
    "Surveillance / securite",
    "Autre : __________"
])

pdf.question(2, "Dans quel(s) domaine(s) vous sentez-vous le plus a l'aise ?", [
    "Technique / manuel",
    "Relationnel / service a la personne",
    "Organisation / gestion",
    "Creation / art / esthetique",
    "Numerique / informatique",
    "Environnement / nature",
    "Aucune preference"
])

pdf.question(3, "Preferez-vous travailler :", [
    "De maniere autonome",
    "En equipe",
    "Peu importe"
])

pdf.question(4, "Quel rythme de travail vous convient le mieux ?", [
    "Calme, regulier",
    "Dynamique, rapide",
    "Variable, adaptable"
])

pdf.question(5, "Parmi ces competences transversales, lesquelles vous decrivent le mieux ?", [
    "Sens de l'organisation",
    "Capacite d'adaptation",
    "Sens de la communication",
    "Esprit d'analyse",
    "Resolution de problemes",
    "Esprit d'equipe",
    "Precision / rigueur"
])

pdf.question(6, "Quel(s) outil(s) ou environnement(s) vous sont familiers ?", [
    "Ordinateur / bureautique",
    "Outils manuels / machines",
    "Telephone / contact client",
    "Vehicules / conduite",
    "Aucun en particulier"
])

pdf.question(7, "Avez-vous un diplome ou une formation dans un domaine specifique ?", [
    "Oui -> Precisez : __________",
    "Non",
    "Formation en cours"
])

pdf.question(8, "Quelles sont vos preferences de conditions de travail ?", [
    "Travail en interieur",
    "Travail en exterieur",
    "Horaires fixes",
    "Horaires variables",
    "Station debout / activite physique",
    "Poste assis / calme"
])

pdf.question(9, "Quels metiers vous attirent, meme sans experience ?", [
    "1. _____________________",
    "2. _____________________",
    "3. _____________________"
])

pdf.question(10, "Etes-vous pret(e) a vous former pour changer de metier ?", [
    "Oui",
    "Peut-etre",
    "Non"
])

pdf.output("Questionnaire_Profil_Competences.pdf")