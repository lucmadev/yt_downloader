import flet as ft
import components.download as dl
import components.settings as settings


format = ""

def main(page: ft.Page):
    page.adaptive = True
    urls = ft.TextField(label="Ingresa la url a descargar", value="")
    def btnAudioClicked(e):
        global format
        format = "Audio"

    def btnVideoClicked(e):
        global format
        format = "Video"

    def btnDownloadClicked(e):
        if urls.value == "":
            page.add(
            ft.Text("FALTA URL A DESCARGAR", color=ft.Colors.RED)
            )
        elif format == "Audio":
            dl.descargarMusica(urls.value)
        elif format == "Video":
            dl.descargarVideos(urls.value)
        elif format == "":
            page.add(
            ft.Text("ERROR DE FORMATO", color=ft.Colors.RED)
            )


    def get_directory_result(e: ft.FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelled!"
        settings.setDir(directory_path.value)

    get_directory_dialog = ft.FilePicker(on_result=get_directory_result)
    directory_path = ft.Text


    btnFormat = ft.Row([
            ft.ElevatedButton(text="Audio", on_click=btnAudioClicked),
            ft.ElevatedButton(text="Video", on_click=btnVideoClicked),
        ]
        )
    def settingsTab(e):
        page.clean()
        settingsView = ft.SafeArea(
                        minimum_padding= 10,
                        content= ft.Column([
                                ft.Text("Configuracion", theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                ft.ElevatedButton("Cambiar lugar de descarga", icon=ft.Icons.FOLDER_OPEN, on_click=lambda _: get_directory_dialog.get_directory_path(), disabled=page.web)])
                                )
        page.add(settingsView)

    downloadView = ft.SafeArea(minimum_padding= 10, content=ft.Container(ft.Column([
                    urls,
                    btnFormat,
                    ft.IconButton(icon=ft.Icons.DOWNLOAD, on_click=btnDownloadClicked, hover_color= '#FFFFFF'),
                    ],
                    ),
            ))
    
    def downloadTab(e):
        page.clean()
        page.add(downloadView)


    page.overlay.extend([get_directory_dialog])
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.Colors.BLACK,
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.DOWNLOAD, icon_color=ft.Colors.WHITE, on_click=downloadTab),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.Icons.SETTINGS, icon_color=ft.Colors.WHITE, on_click=settingsTab),
            ]
        ),
    )

    page.add(page.bottom_appbar, downloadView)

ft.app(main)
