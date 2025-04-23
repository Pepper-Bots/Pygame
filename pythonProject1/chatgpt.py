# Recréation après réinitialisation de l'état
import pandas as pd

# Plan d'entraînement
training_plan = {
    "Semaine": ["1-2", "1-2", "3-4", "3-4", "5-6", "5-6", "7-8", "7-8"],
    "Jour": ["Lundi, Mercredi, Vendredi", "Samedi ou Dimanche",
             "Lundi, Mercredi, Vendredi", "Samedi ou Dimanche",
             "Lundi, Mercredi, Vendredi", "Samedi ou Dimanche",
             "Lundi, Mercredi, Vendredi", "Samedi ou Dimanche"],
    "Entraînement": [
        "30 min : 5 min marche rapide, alterner 1 min course / 2 min marche (x6), 5 min marche lente",
        "20-30 min de course libre (optionnel)",
        "35 min : 5 min marche rapide, alterner 2 min course / 1 min marche (x6), 5 min marche lente",
        "20 min de course continue (rythme libre)",
        "40 min : 5 min marche rapide, alterner 3 min course / 1 min marche (x6), 5 min marche lente",
        "30 min de course continue",
        "45 min : 5 min marche rapide, alterner 4 min course / 1 min marche (x6), 5 min marche lente",
        "40 min de course continue"
    ]
}
df_training = pd.DataFrame(training_plan)

# Plan alimentaire
meal_plan = {
    "Repas": ["Petit-déjeuner", "Collation matin", "Déjeuner",
              "Collation pré-course", "Dîner", "Collation après-dîner"],
    "Aliments": [
        "1 œuf entier + 2 blancs d’œuf, 40 g flocons d’avoine + graines de chia, 1 fruit frais, café/thé sans sucre",
        "10 amandes/noisettes, 1 yaourt nature ou végétal",
        "100 g poulet/poisson maigre/tofu, 150 g légumes vapeur, 50 g quinoa/riz complet, 1 c. à soupe huile olive/colza",
        "1 banane ou poignée de fruits secs, 1 carré chocolat noir",
        "150 g poisson gras/poulet, légumes grillés/vapeur, 1 petite patate douce ou 2 tranches pain complet",
        "Infusion, poignée de noix du Brésil ou 1 carré chocolat noir"
    ]
}
df_meal = pd.DataFrame(meal_plan)

# Idées de recettes
recipes = {
    "Recette": [
        "Buddha Bowl au poulet",
        "Curry de lentilles corail et légumes",
        "Saumon grillé aux légumes rôtis",
        "Wraps de dinde et avocat",
        "Salade quinoa-avocat-grenade",
        "Chili végétarien",
        "Soupe thaï au poulet et lait de coco"
    ],
    "Ingrédients": [
        "Poulet grillé, quinoa, carottes râpées, épinards, avocat, sauce tahini",
        "Lentilles corail, carottes, courgettes, lait de coco, curry en poudre",
        "Filet de saumon, patates douces, brocolis, huile d'olive, citron",
        "Galettes de blé complet, dinde fumée, avocat, tomates, salade verte",
        "Quinoa, avocat, grenade, noix, huile de noix, jus de citron",
        "Haricots rouges, poivrons, tomates, épices chili, maïs",
        "Poulet, lait de coco, champignons, carottes, gingembre, citronnelle"
    ],
    "Préparation": [
        "Cuire le quinoa, griller le poulet, assembler avec les légumes et la sauce.",
        "Faire revenir les légumes, ajouter les lentilles et le lait de coco, mijoter.",
        "Griller le saumon au four, rôtir les légumes à l'huile d'olive et au citron.",
        "Assembler tous les ingrédients dans une galette, rouler et servir.",
        "Cuire le quinoa, ajouter l'avocat, la grenade, les noix, et l'assaisonnement.",
        "Faire mijoter tous les ingrédients ensemble, servir chaud.",
        "Cuire les légumes avec le poulet, ajouter le lait de coco et les épices."
    ],
    "Conservation": [
        "3 jours au frigo dans une boîte hermétique",
        "4 jours au frigo dans une boîte hermétique",
        "2 jours au frigo dans une boîte hermétique",
        "1 jour au frigo dans une boîte hermétique",
        "3 jours au frigo dans une boîte hermétique",
        "4 jours au frigo dans une boîte hermétique",
        "2 jours au frigo dans une boîte hermétique"
    ]
}
df_recipes = pd.DataFrame(recipes)

# Sauvegarder les tableaux dans des fichiers Excel
file_path_training_meal = "/mnt/data/Plan_Entrainement_Alimentaire.xlsx"
recipes_file_path = "/mnt/data/Recettes_Sportives.xlsx"

with pd.ExcelWriter(file_path_training_meal) as writer:
    df_training.to_excel(writer, sheet_name="Entraînement", index=False)
    df_meal.to_excel(writer, sheet_name="Alimentaire", index=False)

df_recipes.to_excel(recipes_file_path, sheet_name="Recettes", index=False)

file_path_training_meal, recipes_file_path
