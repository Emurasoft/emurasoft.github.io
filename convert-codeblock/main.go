package main

import (
	"fmt"
	"io"
	"io/fs"
	"log"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	langIDs := []string{"en", "ja", "ko", "zh-cn", "zh-tw"}

	for _, langID := range langIDs {
		err := filepath.WalkDir(
			fmt.Sprintf(`C:\Users\MakotoEmura\Documents\emeditor-help\%s\plugin\message`, langID),
			walkFunc,
		)
		if err != nil {
			log.Panic(err)
		}
	}
}

func walkFunc(path string, d fs.DirEntry, err error) error {
	if err != nil {
		return err
	}

	if d.Type().IsDir() || d.Name() == "index.md" {
		return nil
	}

	text := ""
	{
		file, err := os.Open(path)
		if err != nil {
			return err
		}
		defer file.Close()

		bytes, err := io.ReadAll(file)
		if err != nil {
			return err
		}
		text = string(bytes)
	}

	split := splitText(text)

	split.Codeblock = strings.NewReplacer(
		// Double newline
		"\r\n\r\n", "\r\n",
		// Unneeded escape character
		`\`, ``,
	).Replace(split.Codeblock)

	resultText := split.Head + "```\r\n" + split.Codeblock + "```\r\n" + split.End

	file, err := os.OpenFile(path, os.O_WRONLY|os.O_TRUNC, 0666)
	if err != nil {
		return err
	}
	defer file.Close()

	_, err = file.WriteString(resultText)
	return err
}

type SplitText struct {
	Head      string
	Codeblock string
	End       string
}

func splitText(text string) *SplitText {
	title, body := splitTitle(text)

	// Find second instance of title - Beginning of codeblock
	titleIndex := strings.Index(body, title)
	if titleIndex < 0 {
		log.Panicf("title not found: %s", title)
	}

	afterTitle := body[titleIndex:]

	parametersIndex := strings.Index(afterTitle, "\r\n## Parameters")
	if parametersIndex < 0 {
		log.Panicf("parameters not found: %s", afterTitle)
	}

	return &SplitText{
		Head:      "# " + title + body[:titleIndex],
		Codeblock: afterTitle[:parametersIndex],
		End:       afterTitle[parametersIndex:],
	}
}

func splitTitle(text string) (title string, body string) {
	text = strings.TrimLeft(text, "# ")
	i := strings.Index(text, "\r\n")
	if i < 0 {
		log.Panicf("separator not found: %s", text)
	}
	return text[:i], text[i:]
}
