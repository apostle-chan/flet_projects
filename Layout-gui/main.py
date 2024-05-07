import flet as ft


def main(page: ft.Page):

    page.padding = 0
    page.bgcolor = ft.colors.BLUE

    main_body_ = ft.Container(
        expand=True,
        content=ft.Row(
            controls=[
                ft.Container(
                    width=page.width / 5,
                    bgcolor=ft.colors.GREEN,
                    content=ft.Column(controls=[ft.Text("2")]),
                ),
                ft.Container(
                    expand=True,
                    bgcolor=ft.colors.YELLOW,
                    content=ft.Column(controls=[ft.Text("3")]),
                ),
            ],
        ),
    )
    main_ = ft.Container(
        tooltip="外部容器",
        height=page.height,
        bgcolor=ft.colors.PINK,
        border=ft.border.all(width=1, color=ft.colors.BLACK),
        content=ft.Column(
            controls=[
                ft.Container(
                    height=100,
                    bgcolor=ft.colors.GREEN_ACCENT_400,
                    content=ft.Row(controls=[ft.Text("1")]),
                ),
                main_body_,
            ],
        ),
    )

    def on_resize(e):
        main_.height = page.height
        main_body_.content.controls[0].width = page.width / 5
        main_.update()
        main_body_.update()

    page.on_resize = on_resize
    page.add(main_)


ft.app(main)
