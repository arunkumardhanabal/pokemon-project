import requests
import json
import sys

BASE_URL = "https://pokeapi.co/api/v2/"


def fetch_pokemon_data(pokemon_name):
    """Fetches Pokémon data (name, base experience, height, weight, abilities)
    from the PokéAPI.
    """
    url = f"{BASE_URL}pokemon/{pokemon_name.lower()}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()

        pokemon_details = {
            "name": data["name"],
            "base_experience": data["base_experience"],
            "height": data["height"],
            "weight": data["weight"],
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]]
        }
        return json.dumps(pokemon_details, indent=4)

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": f"Error fetching data for {pokemon_name}: {e}"}, indent=4)
    except KeyError:
        return json.dumps({"error": f"Pokémon '{pokemon_name}' not found."}, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:  # Check if there are exactly 2 command-line arguments
        print("Usage: python pokemon_details.py <pokemon_name>")
        print("Example: python pokemon_details.py pikachu")
        sys.exit(1)

    pokemon_name = sys.argv[1]  # Get Pokémon name from command line
    output_json = fetch_pokemon_data(pokemon_name)
    print(output_json)
