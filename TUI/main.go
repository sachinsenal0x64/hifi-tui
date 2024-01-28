package main

import (
	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
)

// song informations

type Songs struct {
	duration float64
	title    string
	artist   string
	album    string
}

func main() {
	app := tview.NewApplication()

	// 2x2

	flex := tview.NewFlex().
		AddItem(tview.NewFlex().SetDirection(tview.FlexRow).
			AddItem(tview.NewBox().SetBorder(true).SetTitle("Library"), 0, 1, false).
			AddItem(tview.NewBox().SetBorder(true).SetTitle("Lyrics"), 0, 1, false), 0, 1, false).

		// 2x2

		AddItem(tview.NewFlex().SetDirection(tview.FlexRow).
			AddItem(tview.NewBox().SetBorder(true).SetTitle("Songs"), 0, 10, false).
			AddItem(tview.NewBox().SetBorder(true).SetTitle("Player"), 0, 1, false), 0, 3, false)

	// Set up an event loop
	app.SetInputCapture(func(event *tcell.EventKey) *tcell.EventKey {
		// Check for the Escape key press
		if event.Rune() == 'q' {
			app.Stop()
		}
		switch event.Rune() {
		case 'k':
			app.Stop()
		case 'j':
			return nil
		}
		return event
	})

	// The application will run until app.Stop() is called (in response to the Escape key press)

	if err := app.SetRoot(flex, true).Run(); err != nil {
		panic(err)
	}

}
