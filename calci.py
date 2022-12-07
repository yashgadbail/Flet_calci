import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.theme_mode = LIGHT


    txt_field = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=300)
    
    def button_click(e):
        pass
        
    
    page.add(
            ft.Column(
                [
                ft.Row(
                    [
                    txt_field,
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                    ft.Row(
                    [
                        ft.TextButton("7", on_click=button_click),
                        ft.TextButton("8", on_click=button_click),
                        ft.TextButton("9", on_click=button_click),
                        ft.TextButton("+", on_click=button_click),
                    ],alignment=ft.MainAxisAlignment.CENTER,
                           
                    ),
                    ft.Row(
                    [
                        ft.TextButton("4", on_click=button_click),
                        ft.TextButton("5", on_click=button_click),
                        ft.TextButton("6", on_click=button_click),
                        ft.TextButton("-", on_click=button_click),
                    ],alignment=ft.MainAxisAlignment.CENTER,
                           
                    ),
                    ft.Row(
                    [
                        ft.TextButton("1", on_click=button_click),
                        ft.TextButton("2", on_click=button_click),
                        ft.TextButton("3", on_click=button_click),
                        ft.TextButton("x", on_click=button_click),
                    ],alignment=ft.MainAxisAlignment.CENTER,
                           
                    ),
                    ft.Row(
                    [
                        ft.TextButton("C", on_click=button_click),
                        ft.TextButton("0", on_click=button_click),
                        ft.TextButton("=", on_click=button_click),
                        ft.TextButton("/", on_click=button_click),
                    ],alignment=ft.MainAxisAlignment.CENTER,
                           
                    ),
                ]
            )         
        )

ft.app(target=main)