package main

import (
	"flag"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"

	"golang.org/x/net/html"
)

func main() {
	directory := flag.Arg(0)

	err := filepath.WalkDir(directory, func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}

		if d.IsDir() {
			return nil
		}

		var root *html.Node
		{
			file, err := os.Open(path)
			if err != nil {
				return err
			}
			defer file.Close()

			root, err = html.Parse(file)
			if err != nil {
				return err
			}
		}

		transformTree(root)

		file, err := os.OpenFile(path, os.O_WRONLY|os.O_TRUNC, 0666)
		if err != nil {
			return err
		}
		defer file.Close()

		if err := html.Render(file, root); err != nil {
			return err
		}

		fmt.Println(path)
		return filepath.SkipAll
	})
	if err != nil {
		panic(err)
	}
}

func transformTree(node *html.Node) {
	var childrenToRemove []*html.Node

	for child := node.FirstChild; child != nil; child = child.NextSibling {
		// Remove <a id="mode_toggle">
		if isModeToggle(child) {
			childrenToRemove = append(childrenToRemove, child)
		} else {
			transformTree(child)
		}
	}

	for _, child := range childrenToRemove {
		node.RemoveChild(child)
	}
}

func isModeToggle(node *html.Node) bool {
	if node.Type == html.ElementNode && node.Data == "a" {
		for _, attr := range node.Attr {
			if attr.Key == "id" && attr.Val == "mode_toggle" {
				return true
			}
		}
	}

	return false
}
