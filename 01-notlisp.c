#include <stdio.h>
#include <stdbool.h>

const char* FILENAME="01-input.txt";

int main() {
    FILE* fileptr;
    char direction;
    int current_floor=0;
    int instr_counter=0;
    fileptr = fopen(FILENAME, "r");
    if (!fileptr) {
        printf("file: %s can't be opened\n", FILENAME);
        return 1;
    }

    bool above_ground=true;
    while ( (direction=getc(fileptr)) != EOF ) {
        ++instr_counter;
        if (direction=='(')
            ++current_floor;
        else if (direction==')')
            --current_floor;
        else {
            printf("Wrong direction: %c\n",direction);
            return 2;
        }
        if (above_ground && current_floor<0) { // entering basement first time
            above_ground=false;
            printf("Answer for part 2 (step when basement entered): %d\n", instr_counter);
        }
    }
    printf("Answer for part 1 (last floor): %d\n", current_floor);
}