package main

import (
	"fmt"
	"os"
	"strconv"

	"golang.org/x/crypto/sha3"
)

func main() {
	output_file_name := "output.txt"

	output_file, err := os.OpenFile(output_file_name, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer output_file.Close()

	input_str := "treel0ver"

	chain_position := 0
	chain_position_str := strconv.Itoa(chain_position)
	number := 0
	number_str := strconv.Itoa(number)

	last_hash := sha3.Sum256([]byte(input_str))
	// in case you want to continue another chain, input the string of the last block:
	last_hash = sha3.Sum256([]byte("586013:00000457558c9e60a9fa41ae34d3d86d5c8d1be92cec76deccc6e9da9551a791:YourStringHere"))

	for {

		str_last_hash := fmt.Sprintf("%x", last_hash)
		combined_str := chain_position_str + ":" + number_str + ":" + str_last_hash + ":" + input_str
		hash := sha3.Sum256([]byte(combined_str))

		if has_four_leading_zeroes(hash) {
			RANDOM_STUFF := strconv.Itoa((number ^ 4500) % 256)
			input_str = "treel0ver" + RANDOM_STUFF
			number = 0
			chain_position++
			chain_position_str = strconv.Itoa(chain_position)
			last_hash = hash
			hash_string := fmt.Sprintf("%s\t%x\n", combined_str, hash)
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

func has_four_leading_zeroes(hash [32]byte) bool {
	return hash[0] == 0 && hash[1] == 0 && (hash[2]&0xf0) == 0
}
