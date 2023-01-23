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
    int how_many_zeros = 6;
    clock_t start_time = clock();
    int count = 0;
    unsigned long long num = 0;
    char number[20];
    sprintf(number, "dark7void_%llu", num);
    unsigned char hashed_number[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    while(1) {
        sprintf(number + 10, "%llu", num);
        num++;
        SHA256_Update(&sha256, number, strlen(number));
        SHA256_Final(hashed_number, &sha256);
        SHA256_Init(&sha256);  // reset the context for the next hash
        if (hashed_number[0] == 0 && hashed_number[1] == 0 && hashed_number[2] == 0 /*&& hashed_number[3] == 0 && hashed_number[4] < 16*/) {
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
