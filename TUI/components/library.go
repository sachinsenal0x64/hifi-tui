package components

import (
	"github.com/rivo/tview"
)

type LibraryComponets struct {
	Container     *tview.Flex
	BodyComponent *tview.TextArea
}

func CreateRequest() *LibraryComponets {
	ct := tview.NewFlex()
	ct.SetDirection(tview.FlexRow).SetBorder(true).SetTitle("Library")

	body := tview.NewTextArea()
	body.SetBorder(true)
	body.SetTitle("Body")
	body.SetText("", true)

	// Add requests component on its container
	ct.AddItem(body, 0, 1, false)

	return &LibraryComponets{
		Container:     ct,
		BodyComponent: body,
	}
}
