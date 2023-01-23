#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>
#include <time.h>

int main() {

	double last_rate;
	double average_rate;
	double last_50_rates[50];
    for (int i = 0; i < 49; i++) {
        last_50_rates[i] = 0;
    }
	int found_num;
	int last_found_num;
	unsigned long long last_5000_nums[5000];
    for (int i = 0; i < 4999; i++) {
        last_5000_nums[i] = 0;
    }    
    int count = 0;
    unsigned long long num = 0;
    char number[20];
    sprintf(number, "dark7void_%llu", num);
    unsigned char hashed_number[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    clock_t start_time = clock();
    while(1) {
        sprintf(number + 10, "%llu", num);
        num++;
        SHA256_Update(&sha256, number, strlen(number));
        SHA256_Final(hashed_number, &sha256);
        SHA256_Init(&sha256);  // reset the context for the next hash
        if (hashed_number[0] == 0 && hashed_number[1] == 0 && hashed_number[2] < 16/* && hashed_number[3] == 0 && hashed_number[4] < 16*/) {
		    for (int i = 0; i < 5000; i++) {
		        last_5000_nums[i] = last_5000_nums[i + 1];
		    }

		    last_5000_nums[4999] = num-found_num;
		    double non2 = 0;
		    for (int i = 0; i < 5000; i++) {
		        if (last_5000_nums[i] == 0) {
		        	non2++;
		        }
		    }
		    double sum2 = 0;
			for (int i = 0; i < 5000; i++) {
			    sum2 += last_5000_nums[i];
			}
			
		    double average2 = sum2 / (5000-non2);
            printf("  (last 50 average of nums++: %.3f)", average2);
			printf("diff last number: %llu\n\n", num-found_num);
			found_num = num;
            clock_t end_time = clock();
            count++;
            printf("found: %s\n", number);
            double rate = (double) count / ((double)(end_time - start_time) / CLOCKS_PER_SEC);
		    for (int i = 0; i < 49; i++) {
		        last_50_rates[i] = last_50_rates[i + 1];
		    }
		    double non = 0;
		    for (int i = 0; i < 49; i++) {
		        if (last_50_rates[i] == 0) {
		        	non++;
		        }
		    }
		    last_50_rates[49] = rate;

            printf("hashes per second: %.3f", rate);

		    double sum = 0;
		    for (int i = 0; i < 50; i++) {
		        sum += last_50_rates[i];
		    }
		    double average = sum / (50-non);
            printf("  (last 50 average: %.3f)", average);
            double change = rate-last_rate;
            printf("  (change: %.3f", change);
            last_rate = (double) count / ((double)(end_time - start_time) / CLOCKS_PER_SEC);

            if (change < 0) {
            	printf(" 🔻)\n");
            } else if (change == 0) {
            	printf(" --)\n");
            } else {
            	printf(" ↑)\n");
            }
        }
    }
    return 0;
}
