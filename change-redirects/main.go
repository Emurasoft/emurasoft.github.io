package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"

	"golang.org/x/net/html"
)

func main() {
	for _, language := range []string{"en", "ja", "zh-cn", "zh-tw"} {
		file, err := os.Open(fmt.Sprintf("%s.txt", language))
		if err != nil {
			panic(err)
		}
		defer file.Close()

		entries, err := csv.NewReader(file).ReadAll()
		if err != nil {
			panic(err)
		}

		for _, entry := range entries {
			path := entry[0]
			targetPath := entry[1]

			path = strings.TrimPrefix(path, language+"/")
			path = strings.ReplaceAll(path, "/", "_")
			path = changeSuffix(path)

			targetPath = strings.TrimPrefix(targetPath, language+"/")
			targetPath = fmt.Sprintf("%s/%s", language, targetPath)
			targetPath = changeSuffix(targetPath)

			changeRedirect(path, targetPath, language)
		}
	}
}

func changeSuffix(path string) string {
	s, found := strings.CutSuffix(path, ".md")
	if !found {
		log.Panicf(".md not in path: %s", path)
	}

	return s + ".html"
}

func changeRedirect(path string, targetPath string, language string) {
	path = filepath.Join(`..\_add_to_build`, language, path)

	var tree *html.Node
	{
		file, err := os.Open(path)
		if err != nil {
			fmt.Printf("open error: %s\n", err)
			return
		}
		defer file.Close()

		tree, err = html.Parse(file)
		if err != nil {
			panic(err)
		}
	}

	var search func(node *html.Node)
	search = func(node *html.Node) {
		if node.Type == html.ElementNode && node.Data == "meta" {
			for i := range node.Attr {
				if node.Attr[i].Key == "content" {
					node.Attr[i].Val = fmt.Sprintf("0;url=https://www.emeditor.org/%s", targetPath)
				}
			}
		}

		for c := node.FirstChild; c != nil; c = c.NextSibling {
			search(c)
		}
	}
	search(tree)

	file, err := os.OpenFile(path, os.O_WRONLY|os.O_TRUNC, 0666)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	if err := html.Render(file, tree); err != nil {
		panic(err)
	}
}
