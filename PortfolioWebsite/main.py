import flet
from flet import (
    Page,
    Column,
    Row,
    alignment,
    padding,
    ResponsiveRow,
    border,
    Text,
    Container,
    LinearGradient,
    MainAxisAlignment,
    Icon,
    icons,
    CrossAxisAlignment,
    colors,
    PopupMenuButton,
    PopupMenuItem,
    TextAlign,
)

"""Flet responisve Portfolio website"""


def main(page: Page):
    # title
    page.title = "Flet Portfolio"

    def on_resize(e):
        if page.width < page.height:
            _nav.controls[0].visible = False
            _nav.update()
            _mini_navbar.visible = True
            _mini_navbar.update()
        else:
            _nav.controls[0].visible = True
            _nav.update()
            _mini_navbar.visible = False
            _mini_navbar.update()

    def _change_text_color(e):
        if e.control.content.color == "black":
            e.control.content.color = "blue"
            e.control.content.update()
        else:
            e.control.content.color = "black"
            e.control.content.update()

    # navbar
    _nav = Row(
        alignment=MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            # Container(
            #     content=Icon(icons.FAVORITE)
            # ),
            Container(
                padding=padding.only(right=20),
                # bgcolor="pink",
                expand=True,
                height=64,
                content=Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        Container(
                            content=Text("关 于", weight="w600", color="black"),
                            on_hover=lambda e: _change_text_color(e),
                        ),
                        Container(
                            content=Text("联 系", weight="w600", color="black"),
                            on_hover=lambda e: _change_text_color(e),
                        ),
                        Container(
                            content=Text("服 务", weight="w600", color="black"),
                            on_hover=lambda e: _change_text_color(e),
                        ),
                    ],
                ),
            )
        ],
    )

    # minimized navbar
    _mini_navbar = Row(
        visible=False,
        controls=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(
                        content=Container(
                            content=Text(
                                "关 于", color="black", text_align=TextAlign.CENTER
                            ),
                            on_hover=lambda e: _change_text_color(e),
                        )
                    ),
                    PopupMenuItem(
                        content=Container(
                            content=Text(
                                "联 系", color="black", text_align=TextAlign.CENTER
                            ),
                            on_hover=lambda e: _change_text_color(e),
                        )
                    ),
                    PopupMenuItem(
                        content=Container(
                            content=Text(
                                "服 务", color="black", text_align=TextAlign.CENTER
                            ),
                            on_hover=lambda e: _change_text_color(e),
                        )
                    ),
                ]
            ),
        ],
    )
    _nav.controls.append(_mini_navbar)

    # titles
    _title = ResponsiveRow(
        vertical_alignment=CrossAxisAlignment.CENTER,
        controls=[
            Container(
                # col={"xs":6, "sm":8, "md":10, "lg":10, "xl":12},
                alignment=alignment.top_center,
                padding=padding.only(top=20),
                content=Text(
                    "Line Indent Portfolio & Projects",
                    size=40,
                    weight="w800",
                    color=colors.WHITE,
                    text_align="center",
                ),
            )
        ],
    )

    # title heading
    _sub_titile = ResponsiveRow(
        alignment=MainAxisAlignment.CENTER,
        controls=[
            Container(
                # col={"xs":12, "sm":10, "md":10, "lg":10, "xl":12},
                padding=20,
                alignment=alignment.top_center,
                content=Text(
                    "欢迎来到我的个人小站！\n 如果感兴趣请联系我！",
                    text_align=TextAlign.CENTER,
                    size=16,
                    weight="w500",
                    color="#bbbbbb",
                ),
            ),
        ],
    )

    # main column
    _main_col = Column(alignment=CrossAxisAlignment.CENTER)
    _main_col.controls.append(_nav)
    _main_col.controls.append(_title)
    _main_col.controls.append(_sub_titile)

    # bg container
    _background = Container(
        height=page.height,
        margin=-10,
        expand=True,
        gradient=LinearGradient(
            begin=alignment.bottom_left,
            end=alignment.top_right,
            colors=["#13547a", "#80d0c7"],
        ),
        content=_main_col,
    )

    page.add(_background)
    # resize
    page.on_resize = on_resize


if __name__ == "__main__":
    flet.app(target=main)
