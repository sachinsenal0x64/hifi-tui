package components

import (
	"github.com/rivo/tview"
)

type PlayerComponets struct {
	Container     *tview.Flex
	BodyComponent *tview.TextArea
}

func CreatePlayer() *PlayerComponets {
	ct := tview.NewFlex()
	ct.SetDirection(tview.FlexRow).SetBorder(true).SetTitle("Player")
	// Add library component on its container

	return &PlayerComponets{
		Container: ct,
	}
}
