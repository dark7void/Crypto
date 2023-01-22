#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>
#include <time.h>

int main() {
    int how_many_zeros = 6;
    clock_t start_time = clock();
    int count = 0;
    unsigned long long num = 0;
    char number[20];
    sprintf(number, "dark7void%llu", num);
    unsigned char hashed_number[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    while(1) {
        sprintf(number + 9, "%llu", num);
        num++;
        SHA256_Update(&sha256, number, strlen(number));
        SHA256_Final(hashed_number, &sha256);
        SHA256_Init(&sha256);  // reset the context for the next hash
        if (hashed_number[0] == 0 && hashed_number[1] == 0 && hashed_number[2] == 0 /*&& hashed_number[3] == 0 && hashed_number[4] < 16*/) {
            clock_t end_time = clock();
            count++;
            printf("found: %s\n", number);
            printf("Hashes per second: %f\n", (double) count / ((double)(end_time - start_time) / CLOCKS_PER_SEC));
        }
    }
    return 0;
}
