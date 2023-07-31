package main

import (
	"bytes"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"strings"
)

func getWalkFunc(language string) fs.WalkDirFunc {
	return func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}

		if d.IsDir() {
			return nil
		}

		if strings.HasSuffix(path, fmt.Sprintf(`\%s\macro\index.md`, language)) {
			return nil
		}

		text, err := os.ReadFile(path)
		if err != nil {
			return err
		}

		text = bytes.ReplaceAll(text, []byte("```{toctree}"), []byte("```{toctree}\r\n:hidden:"))
		return os.WriteFile(path, text, 0666)
	}
}

func main() {
	for _, language := range []string{"en", "ja", "ko", "zh-cn", "zh-tw"} {
		path := fmt.Sprintf(`C:\Users\MakotoEmura\Documents\emeditor-help\%s\macro`, language)
		if err := filepath.WalkDir(path, getWalkFunc(language)); err != nil {
			panic(err)
		}
	}
}
