import flet as ft

def main(page: ft.Page):
    page.title = "Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 400
    page.window_width = 400

    txt_field = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=300,read_only=True,label="Calculator")
    
    def button_click(e):
        txt_field.value += str(e.control.data)
        page.update()
        
    def optr_click(e):
        txt_field.value += str(e.control.data)
        page.update()
    
    def clear_click(e):
        txt_field.value = ""
        page.update()

    def equl_click(e):
        txt_field.value = str(eval(txt_field.value.replace("x","*")))
        page.update()

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
                        ft.TextButton("7", on_click=button_click,data=7),
                        ft.TextButton("8", on_click=button_click,data=8),
                        ft.TextButton("9", on_click=button_click,data=9),
                        ft.TextButton("+", on_click=optr_click,data="+"),
                    ],alignment=ft.MainAxisAlignment.CENTER,
                           
                    ),
                    ft.Row(
                    [
                        ft.TextButton("4", on_click=button_click,data=4),
                        ft.TextButton("5", on_click=button_click,data=5),
                        ft.TextButton("6", on_click=button_click,data=6),
                        ft.TextButton("-", on_click=optr_click,data="-"),
                    ],alignment=ft.MainAxisAlignment.CENTER,
                           
                    ),
                    ft.Row(
                    [
                        ft.TextButton("1", on_click=button_click,data=1),
                        ft.TextButton("2", on_click=button_click,data=2),
                        ft.TextButton("3", on_click=button_click,data=3),
                        ft.TextButton("x", on_click=optr_click,data="x"),
                    ],alignment=ft.MainAxisAlignment.CENTER,
                           
                    ),
                    ft.Row(
                    [
                        ft.TextButton("C", on_click=clear_click),
                        ft.TextButton("0", on_click=button_click,data=0),
                        ft.TextButton("=", on_click=equl_click),
                        ft.TextButton("/", on_click=optr_click,data="/"),
                    ],alignment=ft.MainAxisAlignment.CENTER,
                           
                ),
            ]
        )         
    )
ft.app(target=main)
