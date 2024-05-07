import flet as ft


class TrelloApp:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.appbar_items = [
            ft.PopupMenuItem(text="登录"),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(text="设置"),
        ]
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text("Trollo", size=32, text_align=ft.TextAlign.START),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(items=self.appbar_items),
                    margin=ft.margin.only(left=50, right=25),
                )
            ],
        )

        self.page.appbar = self.appbar
        self.page.update()
