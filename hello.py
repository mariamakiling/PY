import flet as ft

def main (page: ft.Page):
    page.add(ft.Text('Hello World'))

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
