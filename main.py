import flet as ft

def main(page: ft.Page):
    # د اپلیکیشن سرلیک
    page.title = "Zama App"
    
    # د پاڼې تنظیمات (هرڅه په منځ کې راوړل)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # یو متن او یو ایکن جوړول
    my_text = ft.Text(value="سلام! دا زما اپلیکیشن دی", size=30, color="blue")
    my_icon = ft.Icon(name=ft.icons.ANDROID, size=50, color="green")

    # په سکرین د شیانو ښودل
    page.add(
        my_icon,
        my_text
    )

# د اپلیکیشن رن کول
ft.app(target=main)
