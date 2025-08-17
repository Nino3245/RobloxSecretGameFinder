import requests
import sys

def list_places_in_universe(universe_id):
    url = f"https://develop.roblox.com/v1/universes/{universe_id}/places"
    cursor = None
    places = []

    while True:
        params = {"limit": 100}
        if cursor:
            params["cursor"] = cursor

        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} - {response.text}")

        data = response.json()
        for place in data.get("data", []):
            places.append({
                "id": place["id"],
                "name": place["name"]
            })

        cursor = data.get("nextPageCursor")
        if not cursor:
            break

    return places

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <UniverseID>")
        sys.exit(1)

    universe_id = sys.argv[1]
    places = list_places_in_universe(universe_id)

    print("Places in universe:", universe_id)
    for p in places:
        print(f"- {p['name']} (ID: {p['id']})")
