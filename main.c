#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>
#include <time.h>
#include <stdlib.h>

int main() {
    srand(time(0));
    int count = 0;
    time_t start = time(NULL);
    while (1) {
        char data[20];
        for (int i = 0; i < 20; i++) {
            data[i] = rand() % 26 + 'a';
        }
        data[19] = '\0';

        unsigned char hash[SHA256_DIGEST_LENGTH];
        SHA256_CTX sha256;
        SHA256_Init(&sha256);
        SHA256_Update(&sha256, data, strlen(data));
        SHA256_Final(hash, &sha256);

        if (hash[0] == 0 && hash[1] == 0 && hash[2] == 0 && hash[3] == 0) {
            count++;
            time_t end = time(NULL);
            double rate = (double) count / difftime(end, start);
            printf("Found another! rate: %f\n", rate);
            printf("%s\n", data);
        }
        if (count == 100) {
            break;
        }
    }
    printf("Found %d hashes with 6 leading zeros!\n", count);
    
    return 0;
}
