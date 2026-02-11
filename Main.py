import flet as ft

def main(page: ft.Page):
    # د اپلیکیشن سرلیک او تنظیمات
    page.title = "زما لومړی Flet اپلیکیشن"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT  # یا DARK انتخابولی شئ

    # د شمېر ښودلو لپاره یو ټیسټ بکس
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    # د کمولو د بټن فنکشن
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    # د زیاتولو د بټن فنکشن
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    # په سکرین د شیانو اضافه کول
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# اپلیکیشن رن کول
ft.app(target=main)
