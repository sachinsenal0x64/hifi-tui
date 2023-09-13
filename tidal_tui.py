from textual.app import App, ComposeResult
from textual.widgets import Static


class VerticalLayoutExample(App):
    CSS_PATH = "tidal_tui.css"

    def compose(self) -> ComposeResult:
        yield Static(classes="box")


class SearchBox(VerticalLayoutExample):
    def searchbox(self, App) -> ComposeResult:
        super().__init__(App)
        yield Static(classes="s_box")


if __name__ == "__main__":
    app = SearchBox()

    app.compose()

    app.run()
