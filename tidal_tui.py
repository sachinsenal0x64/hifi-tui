from textual.app import App, ComposeResult
from textual.widgets import Static


class SearchBox(App):
    def searchbox(self) -> ComposeResult:
        yield Static(classes="box", id="box")
        yield Static(classes="box2", id="box2")


if __name__ == "__main__":
    app = SearchBox()

    app.run()
