package main

import (
	"hifi-tui/tui/components"

	"github.com/gdamore/tcell/v2"
	"github.com/rivo/tview"
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
	var keySequence []rune
	a.rootContainer.SetInputCapture(func(event *tcell.EventKey) *tcell.EventKey {

		focus := a.tview.GetFocus()

		switch event.Rune() {

		case 'j':
			if focus == a.library.Container {
				a.tview.SetFocus(a.lyrics.Container)
			} else if focus == a.song.Container {
				a.tview.SetFocus(a.player.Container)
			}

		case 'k':
			if focus == a.lyrics.Container {
				a.tview.SetFocus(a.library.Container)
			} else if focus == a.player.Container {
				a.tview.SetFocus(a.song.Container)
			}

		case 'h':
			if focus == a.song.Container {
				a.tview.SetFocus(a.library.Container)
			} else if focus == a.player.Container {
				a.tview.SetFocus(a.lyrics.Container)
			}

		case 'l':
			if focus == a.lyrics.Container || focus == a.player.Container {
				a.tview.SetFocus(a.player.Container)
			} else {
				a.tview.SetFocus(a.song.Container)
			}

		case 'w':
			keySequence = append(keySequence, 'w')

		case 'q': // Check for the wq key press
			keySequence = append(keySequence, 'q')
			// Check for both 'wq' and 'q' key presses
			if len(keySequence) >= 2 && keySequence[len(keySequence)-2] == 'w' && keySequence[len(keySequence)-1] == 'q' {
				// 'wq' sequence detected, stop tview
				a.tview.Stop()
				keySequence = nil // Reset the sequence for the next input
				return nil
			}
		}
		if event.Key() == tcell.KeyEsc {
			a.tview.SetFocus(a.rootContainer)
		}
		return event
	})

}

func init() {
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
	app := CreateApp()

	if err := app.Start(); err != nil {
		panic(err)
	}

}
