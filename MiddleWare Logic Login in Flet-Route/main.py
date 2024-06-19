from flet import *
from flet_route import Routing, path

from Home import home
from Login import login


def main(page: Page):
    page.window.width = 300

    # 定义路由
    define_routes = [
        path(url="/", view=home, clear=True),
        path(url="/login", view=login, clear=True),
    ]

    Routing(page=page, app_routes=define_routes)

    page.go("/")


app(target=main)
