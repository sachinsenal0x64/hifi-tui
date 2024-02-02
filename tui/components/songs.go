package components

import (
	"github.com/rivo/tview"
)

type SongComponets struct {
	Container     *tview.Flex
	BodyComponent *tview.TextArea
}

func CreateSong() *SongComponets {
	ct := tview.NewFlex()
	ct.SetDirection(tview.FlexRow).SetBorder(true).SetTitle("Songs")

	// Add library component on its container

	return &SongComponets{
		Container: ct,
	}
}
