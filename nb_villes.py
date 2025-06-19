import json

with open("cities.json", "r", encoding="utf-8") as f:
    cities = json.load(f)


def nb_ville():
    print(f"Nombre total de villes dans cities.json : {len(cities)}")


def info(ville: str):
    ville_info = [city for city in cities if ville in city.get("name", "")]
    if ville_info:
        print(f"Infos pour {ville} :")
        for info in ville_info:
            print(info)
    else:
        print(f"Aucune ville nommée {ville} trouvée.")


# info("Melle")
info("Lezay")
info("Vanzay")
