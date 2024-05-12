package main

import (
	"fmt"
	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

// Song struct to represent song information
type Song struct {
	Duration string
	Title    string
	Album    string
	Artist   string
}

func printSelectedSongInfo(song Song) {
	fmt.Printf("Selected Song:\nTitle: %s\nAlbum: %s\nArtist: %s\nDuration: %s\n",
		song.Title, song.Album, song.Artist, song.Duration)
}

func main() {
	theme := tview.Theme{
		PrimitiveBackgroundColor:    tcell.ColorDefault,
		ContrastBackgroundColor:     tcell.ColorDefault,
		MoreContrastBackgroundColor: tcell.ColorDefault,
		BorderColor:                 tcell.ColorDefault,
		TitleColor:                  tcell.ColorDefault,
		GraphicsColor:               tcell.ColorDefault,
		PrimaryTextColor:            tcell.ColorDefault,
		SecondaryTextColor:          tcell.ColorDefault,
		TertiaryTextColor:           tcell.ColorDefault,
		InverseTextColor:            tcell.ColorDefault,
		ContrastSecondaryTextColor:  tcell.ColorDefault,
	}
	tview.Styles = theme
	app := tview.NewApplication()
	table := tview.NewTable().SetBorders(false)
	// Sample song data
	songs := []Song{
		{Duration: "03:30", Title: "bubble-table alternatives", Album: "bubble-table alternatives and similar packages  bubble-table alternatives and similar packages", Artist: "Artist1"},
		{Duration: "04:15", Title: "Song2", Album: "Album2", Artist: "Artist2"},
		{Duration: "02:45", Title: "Song3", Album: "Album3", Artist: "Artist3"},
		{Duration: "05:00", Title: "Song4", Album: "Album4", Artist: "Artist4"},
		{Duration: "03:20", Title: "Song5", Album: "Album5", Artist: "Artist5"},
		{Duration: "03:30", Title: "Song1", Album: "Album1", Artist: "Artist1"},
		{Duration: "04:15", Title: "Song2", Album: "Album2", Artist: "Artist2"},
		{Duration: "02:45", Title: "Song3", Album: "Album3", Artist: "Artist3"},
		{Duration: "05:00", Title: "Song4", Album: "Album4", Artist: "Artist4"},
		{Duration: "03:20", Title: "Song5", Album: "Album5", Artist: "Artist5"},
		{Duration: "03:30", Title: "Song1", Album: "Album1", Artist: "Artist1"},
		{Duration: "04:15", Title: "Song2", Album: "Album2", Artist: "Artist2"},
		{Duration: "02:45", Title: "Song3", Album: "Album3", Artist: "Artist3"},
		{Duration: "05:00", Title: "Song4", Album: "Album4", Artist: "Artist4"},
		{Duration: "03:20", Title: "Song5", Album: "Album5", Artist: "Artist5"},
	}

	// Set up table headers
	headers := []string{"Duration", "Title", "Artist", "Album"}
	for c, header := range headers {
		color := tcell.ColorWhite
		if c > 0 {
			color = tcell.ColorWhite
		}
		table.SetCell(0, c,
			tview.NewTableCell(header).
				SetTextColor(color).
				SetAlign(tview.AlignLeft).SetExpansion(1).
				SetSelectable(false))

	}
	var selectedRow int

	// Populate the table with sample songs

	for r, song := range songs {
		// Ensure duration is aligned with time
		formattedDuration := fmt.Sprintf("[%2s:%02s]", song.Duration[:2], song.Duration[3:])

		table.SetCell(r+1, 0,
			tview.NewTableCell(formattedDuration).
				SetTextColor(tcell.ColorWhite).
				SetAlign(tview.AlignLeft))
		table.SetCell(r+1, 1,
			tview.NewTableCell(song.Title).
				SetTextColor(tcell.ColorWhite).
				SetAlign(tview.AlignLeft))
		table.SetCell(r+1, 2,
			tview.NewTableCell(song.Album).
				SetTextColor(tcell.ColorWhite).
				SetAlign(tview.AlignLeft))
		table.SetCell(r+1, 3,
			tview.NewTableCell(song.Artist).
				SetTextColor(tcell.ColorWhite).
				SetAlign(tview.AlignLeft))
	}

	// Set up hover effect for the entire row starting from row 1
	table.SetSelectable(true, false).
		SetSelectedFunc(func(row int, column int) {
			if row > 0 {
				// Reset text color for the previously selected row
				if selectedRow > 0 {
					for c := 0; c < len(headers); c++ {
						table.GetCell(selectedRow, c).SetTextColor(tcell.ColorWhite)
					}
					// Reset duration color for the previously selected row
					table.GetCell(selectedRow, 0).SetTextColor(tcell.ColorWhite)
				}

				// Set text color for the new selected row
				selectedRow = row
				//selectedColumn = column  // Commenting this line as it's not used
				for c := 0; c < len(headers); c++ {
					table.GetCell(row, c).SetTextColor(tcell.ColorRed)
				}
				// Highlight the duration for the new selected row
				table.GetCell(row, 0).SetTextColor(tcell.ColorRed)
				// printSelectedSongInfo(songs[row])
			}

		}).
		SetDoneFunc(func(key tcell.Key) {
			if key == tcell.KeyEscape {
				app.Stop()
			}
		})

	// Set the initial selection to the first data row
	table.Select(1, 0).SetFixed(1, 1).SetDoneFunc(func(key tcell.Key) {
		if key == tcell.KeyEscape {
			app.Stop()
		}
		if key == tcell.KeyEnter {
			table.SetSelectable(true, true)
		}
	})

	if err := app.SetRoot(table, true).SetFocus(table).Run(); err != nil {
		panic(err)
	}
}
