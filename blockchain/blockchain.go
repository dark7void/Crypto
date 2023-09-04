package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"golang.org/x/crypto/sha3"
)

const (
	output_file_name = "output.txt"
	input_str        = "treel0ver"
)

func main() {

	output_file, err := os.OpenFile(output_file_name, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer output_file.Close()

	number := 0
	number_str := strconv.Itoa(number)

	last_hash := sha3.Sum256([]byte(input_str))
	// in case you want to continue another chain, input the string of the last block:
	last_hash = sha3.Sum256([]byte(get_last_hash_from_file()))
	// also remember to change the chain position
	last_hash_parts := strings.Split(get_last_hash_from_file(), ":")
	first_value, err := strconv.Atoi(last_hash_parts[0])
	chain_position := first_value + 1
	chain_position_str := strconv.Itoa(chain_position)

	for {

		str_last_hash := fmt.Sprintf("%x", last_hash)
		combined_str := chain_position_str + ":" + number_str + ":" + str_last_hash + ":" + input_str
		hash := sha3.Sum256([]byte(combined_str))

		if has_six_leading_zeroes(hash) {
			//RANDOM_STUFF := strconv.Itoa((number ^ 4500) % 256)
			//input_str = "treel0ver" + RANDOM_STUFF
			number = 0
			chain_position++
			chain_position_str = strconv.Itoa(chain_position)
			last_hash = hash
			hash_string := fmt.Sprintf("%s\t\t%x\n", combined_str, hash)
			fmt.Print(hash_string)
			if _, err := output_file.WriteString(hash_string); err != nil {
				fmt.Println("Error writing to file:", err)
			}
			//break
		}
		number++
		number_str = strconv.Itoa(number)
	}
}

func has_six_leading_zeroes(hash [32]byte) bool {
	//return hash[0] == 0 && hash[1] == 0 && (hash[2]&0xf0) == 0
	return hash[0] == 0 && hash[1] == 0 && hash[2] == 0
}

func get_last_hash_from_file() string {
	filePath := output_file_name

	file, _ := os.Open(filePath)

	defer file.Close()

	// Create a scanner to read lines from the file
	scanner := bufio.NewScanner(file)

	// Initialize a variable to store the last line
	var lastLine string

	// Read lines from the file
	for scanner.Scan() {
		lastLine = scanner.Text()
	}

	// Split the last line by tab character
	parts := strings.SplitN(lastLine, "\t", 2)

	// Check if there's at least one tab in the last line
	if len(parts) >= 2 {
		firstValue := parts[0]
		return firstValue
	} else {
		return input_str
	}

}
