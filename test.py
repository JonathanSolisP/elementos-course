import flet as ft
import requests

API_KEY = 'IoHiDsq59vVzdV0benC0Az6w6CPmlqxZ3db1xpnI'
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_animal(name: str):
    response = requests.get(BASE_URL, params={"name": name}, headers={"X-Api-Key": API_KEY})
    response.raise_for_status()
    return response.json()


def main(page: ft.Page):
    page.title = "Animal Lookup"
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    search_field = ft.TextField(label="Animal name", hint_text="e.g. cheetah", expand=True)
    results_column = ft.Column(spacing=10)

    def on_search(_):
        name = search_field.value.strip()
        if not name:
            return
        results_column.controls.clear()
        try:
            data = fetch_animal(name)
            if not data:
                results_column.controls.append(ft.Text("No results found.", italic=True))
            for animal in data:
                chars = animal.get("characteristics", {})
                taxonomy = animal.get("taxonomy", {})
                card = ft.Card(
                    content=ft.Container(
                        padding=15,
                        content=ft.Column([
                            ft.Text(animal.get("name", "Unknown"), size=20, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Scientific name: {taxonomy.get('scientific_name', '-')}", italic=True),
                            ft.Divider(),
                            ft.Text(f"Locations: {', '.join(animal.get('locations', []))}"),
                            ft.Text(f"Diet: {chars.get('diet', '-')}"),
                            ft.Text(f"Habitat: {chars.get('habitat', '-')}"),
                            ft.Text(f"Top speed: {chars.get('top_speed', '-')}"),
                            ft.Text(f"Lifespan: {chars.get('lifespan', '-')}"),
                            ft.Text(f"Weight: {chars.get('weight', '-')}"),
                            ft.Text(f"Biggest threat: {chars.get('biggest_threat', '-')}"),
                            ft.Text(f"Population: {chars.get('estimated_population_size', '-')}"),
                        ])
                    )
                )
                results_column.controls.append(card)
        except Exception as ex:
            results_column.controls.append(ft.Text(f"Error: {ex}", color=ft.Colors.RED))
        page.update()

    search_field.on_submit = on_search

    page.add(
        ft.Row([search_field, ft.Button(ft.Text("Search"), on_click=on_search)]),
        ft.Divider(),
        results_column,
    )


ft.app(target=main)
