from crewai import Task

import requests
class MeetingPrepTasks:
    def __init__(self, agent):
        self.agent = agent
        self.pokemon_description = ""

    def fetch_pokemon_data(self):
        api_url = "https://pokeapi.co/api/v2/pokemon/pikachu"
        response = requests.get(api_url)
        pokemon_data = response.json()
        pokemon_species_url = pokemon_data['species']['url']
        species_response = requests.get(pokemon_species_url)
        species_data = species_response.json()
        self.pokemon_description = species_data['flavor_text_entries'][0]['flavor_text']
        
    def develop_blog(self):
        self.fetch_pokemon_data()
        return Task(
            description="Describing listed Pokemon details",
            expected_output="Blog of 5 lines based on data provided on Pokemon",
            agent=self.agent,
            additional_data={"pokemon_description": self.pokemon_description}
        )

