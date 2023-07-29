package main

import (
	"fmt"
	"io/fs"
	"log"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	language := `en`
	paths := getPaths(`..\` + language)

	for _, path := range paths {
		newPath := strings.ReplaceAll(path, `\`, "_")
		newPath = fmt.Sprintf(`..\_build\%s\%s.html`, language, newPath)

		if err := os.MkdirAll(filepath.Dir(newPath), 0666); err != nil {
			log.Panicln(err)
		}

		if err := os.WriteFile(newPath, []byte{}, 0666); err != nil {
			log.Panic(err)
		}
	}
}

func getPaths(rootPath string) []string {
	var pathsToRedirect []string

	walkFunc := func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}

		if d.IsDir() {
			return nil
		}

		if strings.HasSuffix(path, ".md") {
			entry := strings.TrimSuffix(strings.TrimPrefix(path, rootPath+`\`), ".md")
			pathsToRedirect = append(pathsToRedirect, entry)
		}

		return nil
	}

	if err := filepath.WalkDir(rootPath, walkFunc); err != nil {
		log.Panicln(err)
	}

	return pathsToRedirect
}
