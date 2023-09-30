package main

import (
	"fmt"
	"math/rand"
	"time"
)

func encrypt(text string) string {
	encryptedText := ""
	for _, char := range text {
		rand.Seed(time.Now().UnixNano())
		key := rand.Intn(91) + 10
		charCode := int(char)
		encryptedCharCode := (charCode * key) + key - 2
		encryptedText += fmt.Sprintf("%d%d", encryptedCharCode, key)
	}

	return encryptedText
}

func main() {
	var plaintext string
	fmt.Print("Введите текст для шифрования: ")
	_, _ = fmt.Scanln(&plaintext)
	encryptedText := encrypt(plaintext)
	fmt.Printf("Зашифрованный текст: %s\n", encryptedText)
}
