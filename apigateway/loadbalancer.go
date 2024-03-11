package main

import (
	"fmt"
	"math"
	"time"
)

type Servers struct {
	Node string
	CON  float64
}

func minserver(servers []Servers) {
	for {

		Highcon := math.Inf(1)

		// Find the current minimum and maximum CON values
		for _, b := range servers {
			Mincon := b.CON
			if Mincon < Highcon {
				Highcon = Mincon
			}
		}

		for i := range servers {
			b := &servers[i]
			if b.CON == Highcon {
				time.Sleep(1 * time.Second)
				b.CON++
				fmt.Println(b.CON, b.Node)
			}
		}

	}
}

func main() {

	songs := []Servers{
		{Node: "https://google.com", CON: 1},
		{Node: "https://youtube.com", CON: 10},
		{Node: "https://example.com", CON: 15},
	}

	minserver(songs)
}
