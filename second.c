#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int getBinary(int x, int n){
    int binary = 0;
    int multiple = 1;
    int temp = x;
    while(temp>0){      
        int digit = temp%2;
        binary = binary + (digit*multiple);
        multiple = multiple*10;
        temp = temp/2;
    }
    printf("The binary value for %d is %d\n", x, binary);
    int hold = n;
    while(hold>0){
        binary = binary/10;
        hold--;
    }
    return binary%(10);
}

int complement(int x, int n){
    int array[30];
    int temp = x;
    int index = 0;
    while(temp>0){
        int digit = temp%2;
        array[index] = digit;
        index++;
        temp = temp/2;
    }
    if(array[n] == 0){
        array[n] = 1;
    }else if(array[n] == 1){
        array[n] = 0;
    }
    int finale = 0;
    index-=1;
    while(index>-1){
        int power = 2;
        if(index == 0){
            power = 1;
        }else{
            for(int i = 1; i<index; i++){
                power = power*2;
            }
        }
        finale = finale + array[index] * power;
        index--;
    }
    return finale;
}

int set(int x, int n, int v){
    int array[30];
    int temp = x;
    int index = 0;
    while(temp>0){
        int digit = temp%2;
        array[index] = digit;
        index++;
        temp = temp/2;
    }
    array[n] = v;
    index-=1;
    int finale = 0;
    while(index>-1){
        int power = 2;
        if(index == 0){
            power = 1;
        }else{
            for(int i = 1; i<index; i++){
                power = power*2;
            }
        }
        finale = finale + array[index] * power;
        index--;
    }
    return finale;
}

int main(int argc, char *filename[argc+1]){
    //OPEN FILE
    FILE *file = fopen(filename[1], "r");
    if(file == NULL){
        EXIT_FAILURE;
    }
    //GET MANIPULATED VALUE
    int value;
    fscanf(file, "%d", &value);
    //GET FIRST OPERATION
    char operation[28];
    while(fscanf(file, "%s", operation) != EOF){
        if(strcmp(operation, "get") == 0){
            int temp1;
            int temp2;
            fscanf(file, "%d", &temp1);
            printf("%d\n", getBinary(value, temp1));
        }else if(strcmp(operation, "comp") == 0){
            int temp1;
            int temp2;
            fscanf(file, "%d", &temp1);
            fscanf(file, "%d", &temp2);
            value = complement(value, temp1);
            printf("%d\n", value);
        }else if(strcmp(operation, "set") == 0){
            int temp1;
            int temp2;
            fscanf(file, "%d", &temp1);
            fscanf(file, "%d", &temp2);
            value = set(value, temp1, temp2);
            printf("%d\n", value);
        } 
    }    
    EXIT_SUCCESS;
}