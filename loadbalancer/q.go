package main

import (
	"fmt"
	"time"
)

// Queue represents a simple queue data structure for songs
type Queue struct {
	items []string
}

// Enqueue adds a song to the end of the queue
func (q *Queue) Enqueue(song string) {
	q.items = append(q.items, song)
}

// Dequeue removes and returns the song at the front of the queue
func (q *Queue) Dequeue() string {
	if len(q.items) == 0 {
		return ""
	}
	dequeuedItem := q.items[0]
	q.items = q.items[1:]
	return dequeuedItem
}

// Peek returns the song at the front of the queue without removing it
func (q *Queue) Peek() string {
	if len(q.items) == 0 {
		return ""
	}
	return q.items[0]
}

// PrintQueue prints the current queue
func (q *Queue) PrintQueue() {
	fmt.Println("Queue:", q.items)
}

func main() {
	queue := Queue{}

	// Adding 5 songs to the queue
	queue.Enqueue("Song1")
	queue.Enqueue("Song2")
	queue.Enqueue("Song3")
	queue.Enqueue("Song4")
	queue.Enqueue("Song5")

	// Printing the initial queue
	queue.PrintQueue()

	// Simulating playing songs and dequeueing
	for i := 0; i < 5; i++ {
		currentSong := queue.Peek()
		fmt.Println("Playing:", currentSong)
		time.Sleep(time.Second * 10)
		queue.Dequeue()
		fmt.Println("Song finished. Dequeued:", currentSong)
		queue.PrintQueue()
	}
}
