package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/zeebo/blake3"
)

const (
	output_file_name = "output.txt"
	input_str        = "tree text here"
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

	last_hash := blake3.Sum256([]byte(input_str))
	// in case you want to continue another chain, input the string of the last block:
	last_hash = blake3.Sum256([]byte(get_last_hash_from_file()))
	// also remember to change the chain position
	last_hash_parts := strings.Split(get_last_hash_from_file(), ":")
	first_value, err := strconv.Atoi(last_hash_parts[0])
	chain_position := first_value + 1
	chain_position_str := strconv.Itoa(chain_position)

	for {

		str_last_hash := fmt.Sprintf("%x", last_hash)
		combined_str := chain_position_str + ":" + number_str + ":" + str_last_hash + ":" + input_str
		hash := blake3.Sum256([]byte(combined_str))

		if has_four_leading_zeroes(hash) {
			current_time := time.Now().UTC().Format("02/01/2006 15:04:05")
			//RANDOM_STUFF := strconv.Itoa((number ^ 4500) % 256)
			//input_str = "treel0ver" + RANDOM_STUFF
			chain_position++
			chain_position_str = strconv.Itoa(chain_position)
			number = 0
			last_hash = hash
			hash_string := fmt.Sprintf("%s\t\t%x %s\n", combined_str, hash, current_time)
			fmt.Print(hash_string)
			if _, err := output_file.WriteString(hash_string); err != nil {
				fmt.Println("Error writing to file:", err)
			}
		}
		number++
		number_str = strconv.Itoa(number)
	}
}

func has_four_leading_zeroes(hash [32]byte) bool {
	return hash[0] == 0 && hash[1] == 0 && hash[2] == 0
}

func get_last_hash_from_file() string {
	filePath := output_file_name

	file, _ := os.Open(filePath)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	var lastLine string

	for scanner.Scan() {
		lastLine = scanner.Text()
	}

	parts := strings.SplitN(lastLine, "\t", 2)

	if len(parts) >= 2 {
		firstValue := parts[0]
		return firstValue
	} else {
		return input_str
	}

}
