import flet as ft


def main(page: ft.Page):
    page.fonts = {
        "AlibabaPuHuiTi": "assets/fonts/Alibaba-PuHuiTi-Light.ttf",
        "SourceHanSansSC": "assets/fonts/SourceHanSansSC-VF.ttf",
        "Alibaba-PuHuiTi-Heavy": "assets/fonts/Alibaba-PuHuiTi-Heavy.ttf.ttf",
    }
    page.theme = ft.Theme(font_family="SourceHanSansSC")
    page.window_center()
    page.window_width = 600
    page.window_height = 400
    page.window_resizable = False
    
    

    def login(e):
        print("实现登录逻辑")
        print(page.theme.font_family)
        pass

    page.add(
        ft.Container(
            height=page.height,
            padding=30,
            expand=True,
            bgcolor=ft.colors.PINK_200,
            content=ft.Column(
                controls=[
                    ft.TextField(label="输入交换机IP地址"),
                    ft.TextField(label="输入交换机连接密码", password=True),
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.TextButton(
                                    text="点击连接", on_click=login, expand=True
                                ),
                                # margin=ft.margin.all(value=10),
                                expand=True,
                            ),
                        ],
                    ),
                ],
            ),
        )
    )


ft.app(main, assets_dir="assets")
