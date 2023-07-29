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
	for _, language := range []string{"en", "ja", "ko", "zh-cn", "zh-tw"} {
		paths := getPaths(`..\` + language)
		writeRedirects(language, paths)
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

func writeRedirects(language string, paths []string) {
	for _, path := range paths {
		newPath := strings.ReplaceAll(path, `\`, "_")
		newPath = fmt.Sprintf(`..\_build\%s\%s.html`, language, newPath)

		if err := os.MkdirAll(filepath.Dir(newPath), 0666); err != nil {
			log.Panicln(err)
		}

		const redirectFormat = `<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;url=https://emurasoft.github.io/emeditor-help/%s/%s.html"></head></html>`

		redirectText := fmt.Sprintf(redirectFormat, language, filepath.ToSlash(path))

		if err := os.WriteFile(newPath, []byte(redirectText), 0666); err != nil {
			log.Panic(err)
		}
	}
}
