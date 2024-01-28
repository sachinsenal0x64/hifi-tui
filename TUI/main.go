package main

import (
	"github.com/rivo/tview"
)

func main() {
	app := tview.NewApplication()

	flex := tview.NewFlex().
		AddItem(tview.NewFlex().SetDirection(tview.FlexRow).
			AddItem(tview.NewBox().SetBorder(true).SetTitle("Library"), 0, 1, false).
			AddItem(tview.NewBox().SetBorder(true).SetTitle("Lyrics"), 0, 1, false), 0, 1, false).
		AddItem(tview.NewFlex().SetDirection(tview.FlexRow).
			AddItem(tview.NewBox().SetBorder(true).SetTitle("Songs"), 0, 10, false).
			AddItem(tview.NewBox().SetBorder(true).SetTitle("Player"), 0, 1, false), 0, 3, false)
	if err := app.SetRoot(flex, true).Run(); err != nil {
		panic(err)
	}
}
