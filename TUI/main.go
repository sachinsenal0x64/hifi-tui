package main

import (
	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
	"github.com/sachinsenal0x64/Hifi-Tui/TUI/components"
)

// Song informations

type Track struct {
	duration float64
	title    string
	artist   string
	album    string
}

type App struct {
	tview         *tview.Application
	rootContainer *tview.Flex
	library       *components.LibraryComponets
	song          *components.SongComponets
	lyrics        *components.LyricsComponets
	player        *components.PlayerComponets
}

func CreateApp() *App {
	lib := components.CreateLibrary()
	song := components.CreateSong()
	lyrics := components.CreateLyrics()
	player := components.CreatePlayer()

	a := App{
		tview:         tview.NewApplication(),
		rootContainer: tview.NewFlex(),
		library:       lib,
		song:          song,
		lyrics:        lyrics,
		player:        player,
	}

	a.rootContainer.AddItem(tview.NewFlex().SetDirection(tview.FlexRow).
		AddItem(a.library.Container, 0, 1, false).
		AddItem(a.lyrics.Container, 0, 1, false), 0, 1, false)

	a.rootContainer.AddItem(tview.NewFlex().SetDirection(tview.FlexRow).
		AddItem(a.song.Container, 0, 10, false).
		AddItem(a.player.Container, 0, 1, false), 0, 3, false)

	a.tview.SetRoot(a.rootContainer, true)

	a.SetInputHandlers()

	return &a
}

func (a App) Start() error {
	return a.tview.Run()
}

func (a *App) SetInputHandlers() {
	a.rootContainer.SetInputCapture(func(event *tcell.EventKey) *tcell.EventKey {
		// focus := a.tview.GetFocus()
		switch event.Rune() {
		case 'k':
			a.tview.SetFocus(a.library.Container)

		case 'j':
			a.tview.SetFocus(a.lyrics.Container)

		}

		// Check for the q key press
		if event.Rune() == 'q' {
			a.tview.Stop()
			return nil

		}
		return event

	})

}

func main() {
	// app := tview.NewApplication()

	// // 2x2

	// flex := tview.NewFlex().
	// 	AddItem(tview.NewFlex().SetDirection(tview.FlexRow).
	// 		AddItem(tview.NewBox().SetBorder(true).SetTitle("Library"), 0, 1, false).
	// 		AddItem(tview.NewBox().SetBorder(true).SetTitle("Lyrics"), 0, 1, false), 0, 1, false).

	// 	// 2x2

	// 	AddItem(tview.NewFlex().SetDirection(tview.FlexRow).
	// 		AddItem(tview.NewBox().SetBorder(true).SetTitle("Songs"), 0, 10, false).
	// 		AddItem(tview.NewBox().SetBorder(true).SetTitle("Player"), 0, 1, false), 0, 3, false)

	// // Set up an event loop
	// app.SetInputCapture(func(event *tcell.EventKey) *tcell.EventKey {

	// 	switch event.Rune() {
	// 	case 'k':
	// 		flex.SetBorder(true)

	// 	case 'j':
	// 		flex.SetBorder(false)
	// 	}

	// 	// Check for the q key press
	// 	if event.Rune() == 'q' {
	// 		app.Stop()
	// 		return nil
	// 	}

	// 	return event

	// })

	// // The application will run until app.Stop() is called (in response to the Escape key press)

	// if err := app.SetRoot(flex, true).Run(); err != nil {
	// 	panic(err)
	// }

	app := CreateApp()
	if err := app.Start(); err != nil {
		panic(err)
	}

}
