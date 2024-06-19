from flet import *
from flet_route import Params, Basket
from middleware.checklogin import check_login


def login(page: Page, params: Params, basket: Basket):
    # 获取session
    session = page.session.get("session_login")
    print(session)
    check = check_login(session)

    def login_out(e):
        page.session.clear()
        page.go("/")
        page.update()

    login_page = Column(
        [
            Text("欢迎登录", size=30, weight="bold"),
            ElevatedButton("logout", on_click=login_out),
        ]
    )

    # 如果session校验失败
    wrong_login = Column(
        [
            ElevatedButton(
                "wrong login", bgcolor="red", color="white", on_click=login_out
            )
        ]
    )

    return View("/login", controls=[login_page] if check else [wrong_login])
