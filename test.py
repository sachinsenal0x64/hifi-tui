import csv
import io
import json  # Import the json module

from textual.app import App, ComposeResult
from textual.widgets import DataTable, Label

CSV = """lane,swimmer,country,time
4,Joseph Schooling,Singapore,50.39
2,Michael Phelps,United States,51.14
5,Chad le Clos,South Africa,51.14
6,László Cseh,Hungary,51.14
3,Li Zhuhao,China,51.26
8,Mehdy Metella,France,51.58
7,Tom Shields,United States,51.73
1,Aleksandr Sadovnikov,Russia,51.84"""


class TableApp(App[list]):
    def compose(self) -> ComposeResult:
        yield Label("Select a row and its key will appear here", id="selected")
        table = DataTable()
        table.focus()
        table.cursor_type = "row"
        table.fixed_columns = 1
        table.fixed_rows = 1
        yield table

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        rows = csv.reader(io.StringIO(CSV))
        table.add_columns(*next(rows))
        table.add_rows(rows)

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        selected_row = self.query_one(DataTable).get_row(event.row_key)
        selected_row_dict = {
            "lane": selected_row[0],
            "swimmer": selected_row[1],
            "country": selected_row[2],
            "time": selected_row[3]
        }  # Create a dictionary from the selected row

        self.query_one("#selected", Label).update(f"{selected_row_dict!r}")

        # Save the selected row as JSON in a file
        with open("selected_row.json", "w") as file:
            json.dump(selected_row_dict, file)


if __name__ == "__main__":
    TableApp().run()
