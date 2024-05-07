import flet as ft
from componments.TrelloPage import TrelloApp  # 从组件中引入


def main(page: ft.Page):
    page.title = "Flet Trello clone"
    page.padding = 0
    page.bgcolor = ft.colors.BLUE_GREY_200
    TrelloApp(page)
    page.update()


ft.app(main)
