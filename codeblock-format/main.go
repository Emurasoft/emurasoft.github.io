package main

import (
	"fmt"
	"io/fs"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

func getWalkFunc() fs.WalkDirFunc {
	return func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}

		if d.IsDir() || d.Name() == "index.md" {
			return nil
		}

		b, err := os.ReadFile(path)
		if err != nil {
			return err
		}
		text := string(b)

		startIndex := strings.Index(text, "typedef")
		if startIndex < 0 {
			panic("not found")
		}

		endIndex := strings.Index(text, ";\r\n\r\n##")
		if endIndex < 0 {
			panic("not found")
		}
		endIndex += 1

		codeBlock := text[startIndex:endIndex]
		codeBlock = strings.NewReplacer(
			"\\", "",
			"\r\n\r\n", "\n",
			"\u00a0", " ",
		).Replace(codeBlock)

		command := exec.Command("clang-format", "--style={BasedOnStyle: LLVM, UseTab: ForIndentation, IndentWidth: 4, TabWidth: 4, AlignTrailingComments: false}")
		command.Stdin = strings.NewReader(codeBlock)
		formatted, err := command.Output()
		if err != nil {
			return err
		}

		parts := []string{text[:startIndex], "```\n", string(formatted), "\n```", text[endIndex:]}
		newText := strings.Join(parts, "")

		return os.WriteFile(path, []byte(newText), 0666)
	}
}

func main() {
	for _, language := range []string{"en", "ja", "ko", "zh-cn", "zh-tw"} {
		path := fmt.Sprintf(`C:\Users\MakotoEmura\Documents\emeditor-help\%s\plugin\structure`, language)
		if err := filepath.WalkDir(path, getWalkFunc()); err != nil {
			panic(err)
		}
	}
}
