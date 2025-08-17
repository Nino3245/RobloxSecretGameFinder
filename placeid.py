import requests
import sys

def get_universe_id(place_id):
    url = f"https://apis.roblox.com/universes/v1/places/{place_id}/universe"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code} - {response.text}")
    
    data = response.json()
    return data.get("universeId")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_universe_id.py <PlaceID>")
        sys.exit(1)

    place_id = sys.argv[1]
    universe_id = get_universe_id(place_id)

    if universe_id:
        print(f"Universe ID for Place {place_id}: {universe_id}")
    else:
        print(f"Could not find Universe ID for Place {place_id}")
