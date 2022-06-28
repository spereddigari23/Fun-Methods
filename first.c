#include <stdio.h>
#include <stdlib.h>
// CHECK TO SEE IF A VALUE IS PRIME
int isPrime(int value){
    if(value<=2){
        return 0;
    }else{
        for(int i = 2; i<(value/2); i++){
            if(value%i == 0){
                return 0;
            }
        }
        return 1;
    }
}
// READ INTS FROM A FILE AND FIND COUNT OF THE TIMES THE VALUE IS PRIME AS WELL AS IF VALUE-2 IS PRIME OR VALUE+2 IS PRIME
int main(int argc, char *filename[argc+1]){
    FILE *file = fopen(filename[1], "r");
    if(file == NULL){
        EXIT_FAILURE;
    }
    int value;
    int counter = 0;
    while(fscanf(file, "%d", &value) != EOF){
        int prime = isPrime(value);
        counter++;
        if(prime == 1){
            if(isPrime(value+2) == 1 || isPrime(value-2) == 1){
                printf("yes\n");
            }else{
                printf("no\n");
            }
        }else{
            printf("no\n");
        }
    }
    fclose(file);
    return EXIT_SUCCESS;
}
