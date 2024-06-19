import flet as ft
from flet import Page, Column, Text, TextField, ElevatedButton

import requests
import json


def main(page: Page):
    page.title = "Web scraper"

    url_field = TextField(value="", hint_text="URL", text_align="left", autofocus=True)
    result_txt = Text(value="", text_align="left")

    def scrape(e):
        url = url_field.value
        url_field.value = ""

        response = requests.get(url)
        json_data = json.loads(response.text)

        names = [item["name"] for item in json_data]

        result_txt.value = "\n".join(names)

    page.add(
        Column(
            [
                url_field,
                ElevatedButton(text="Scrape", on_click=scrape),
                ft.Divider(),
                result_txt,
            ]
        )
    )


ft.app(target=main)
