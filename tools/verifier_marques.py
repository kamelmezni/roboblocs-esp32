#!/usr/bin/env python3
# verifier_marques.py : contrôle la présence des marques d'auteur RoboBlocs
# dans un ou plusieurs fichiers (page HTML, main.py, bibliothèques, projet .json...).
# Usage :  python verifier_marques.py fichier1 [fichier2 ...]   (ou un dossier)
#          python verifier_marques.py            (sans argument : une fenêtre permet de choisir le fichier)
#          python verifier_marques.py --strict fichier   (code de sortie 1 si l'empreinte est absente : utile en CI)
# © 2026 Prof. MEZNI Kamel - Lycée Liberté Jendouba - Club Internet des Objets et IA
import os
import sys

MARQUES = ["MEZNI-LLJ-2026", "Prof. MEZNI Kamel", "Lycée Liberté Jendouba",
           "Club Internet des Objets et IA", "RoboBlocs ESP32"]
ZERO, UN, CADRE = "\u200b", "\u200c", "\u2060"


def empreintes(texte):
    """Retrouve les empreintes invisibles (caractères de largeur nulle) et les décode."""
    trouvees = []
    for morceau in texte.split(CADRE)[1::2]:          # texte entre deux repères U+2060
        bits = "".join("0" if c == ZERO else "1" for c in morceau if c in (ZERO, UN))
        if len(bits) >= 8 and len(bits) % 8 == 0:
            try:
                trouvees.append(bytes(int(bits[i:i + 8], 2) for i in range(0, len(bits), 8)).decode("ascii"))
            except ValueError:
                pass
    return trouvees


def analyser(chemin):
    """Affiche le bilan d'un fichier et renvoie True si l'empreinte d'auteur est retrouvée."""
    with open(chemin, encoding="utf-8", errors="ignore") as f:
        texte = f.read()
    print("\n=== " + chemin)
    for m in MARQUES:
        print("  %-34s %3d fois" % (m, texte.count(m)))
    emp = empreintes(texte)
    print("  empreintes invisibles : %d  %s" % (len(emp), sorted(set(emp)) if emp else ""))
    ok = "MEZNI-LLJ" in emp
    if ok:
        print("  -> EMPREINTE D'AUTEUR RETROUVÉE : ce fichier provient de RoboBlocs (Prof. MEZNI Kamel).")
    elif texte.count("MEZNI") or texte.count("RoboBlocs"):
        print("  -> marques visibles présentes, empreinte invisible absente (supprimée ou altérée ?).")
    else:
        print("  -> aucune marque trouvée.")
    return ok


def choisir_fichiers():
    """Ouvre une fenêtre de sélection (utile quand on lance le script depuis Thonny)."""
    try:
        import tkinter
        from tkinter import filedialog
        racine = tkinter.Tk()
        racine.withdraw()
        return list(filedialog.askopenfilenames(title="Choisir le(s) fichier(s) à vérifier"))
    except Exception:
        return []


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    args = [a for a in args if a != "--strict"]
    if not args:
        args = choisir_fichiers()
    if not args:
        print("Usage : python verifier_marques.py [--strict] fichier_ou_dossier ...")
        return 0
    tous_ok = True
    for arg in args:
        if os.path.isdir(arg):
            for racine, _, noms in os.walk(arg):
                for n in sorted(noms):
                    if n.lower().endswith((".html", ".htm", ".js", ".py", ".json", ".txt", ".md")):
                        tous_ok &= analyser(os.path.join(racine, n))
        else:
            tous_ok &= analyser(arg)
    return 1 if (strict and not tous_ok) else 0


if __name__ == "__main__":
    sys.exit(main())
