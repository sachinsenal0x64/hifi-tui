package components

import (
	"github.com/rivo/tview"
)

type LibraryComponets struct {
	Container     *tview.Flex
	BodyComponent *tview.TextArea
}

func CreateLibrary() *LibraryComponets {
	ct := tview.NewFlex()
	ct.SetDirection(tview.FlexRow).SetBorder(true).SetTitle("Library")

	// Add library component on its container

	return &LibraryComponets{
		Container: ct,
	}
}
