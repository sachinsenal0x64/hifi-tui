package components

import (
	"github.com/rivo/tview"
)

type LyricsComponets struct {
	Container     *tview.Flex
	BodyComponent *tview.TextArea
}

func CreateLyrics() *LyricsComponets {
	ct := tview.NewFlex()
	ct.SetDirection(tview.FlexRow).SetBorder(true).SetTitle("Lyrics")

	// Add library component on its container

	return &LyricsComponets{
		Container: ct,
	}
}
