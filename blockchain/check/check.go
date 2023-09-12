package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/zeebo/blake3"
)

func main() {
	file, err := os.Open("output.txt")
	if err != nil {
		fmt.Println("Error opening the file:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	lineNum := 0
	for scanner.Scan() {
		line := scanner.Text()
		lineNum++

		parts := strings.Split(line, "\t\t")

		if len(parts) != 2 {
			fmt.Printf("Line %d: Invalid format\n", lineNum)
			os.Exit(1)
		}

		hashParts := strings.Fields(parts[1])
		if len(hashParts) == 0 {
			fmt.Printf("Line %d: Invalid hash format\n", lineNum)
			os.Exit(1)
		}
		providedHash := hashParts[0]

		calculatedHash := blake3.Sum256([]byte(parts[0]))

		if fmt.Sprintf("%x", calculatedHash) != providedHash {
			fmt.Printf("Line %d: Hash mismatch\n", lineNum)
			os.Exit(1)
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading the file:", err)
		os.Exit(1)
	}

	fmt.Println("All lines verified successfully")
}
