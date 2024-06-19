from flet import *
from flet_route import Params, Basket


def home(page: Page, params: Params, basket: Basket):
    input_login = TextField(label="input password")

    def login_btn(e):
        # 添加登录逻辑
        page.session.set("session_login", input_login.value)
        page.go("/login")
        page.update()

    return View(
        "/",
        [
            Column(
                [
                    Text("Home", size=30),
                    input_login,
                    ElevatedButton("login", on_click=login_btn),
                ]
            )
        ],
        appbar=None,
    )
