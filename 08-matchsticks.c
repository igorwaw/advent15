/*  
The only escape sequences used are:
 \\ (which represents a single backslash), 
 \" (which represents a lone double-quote character), 
 \x plus two hexadecimal characters (which represents a single character

For example, given the four strings above, the total number 
of characters of string code (2 + 5 + 10 + 6 = 23) minus the total 
number of characters in memory for string values 
(0 + 3 + 7 + 1 = 11) is 23 - 11 = 12. */

#include <stdio.h>
#include <stdbool.h>

const char* FILENAME="08-small.txt";
const int MAXSTR=200; // max line length

int main() {
    FILE* fileptr;
    int byte_counter=0;
    int char_counter=0;
    int line_counter=0;
    char line[MAXSTR];
    fileptr = fopen(FILENAME, "r");
    if (!fileptr) {
        printf("file: %s can't be opened\n", FILENAME);
        return 1;
    }
    // read file line by line
    bool saw_first_quotation=false;
    
    while ( fgets(line, MAXSTR, fileptr) != NULL ) {
        ++line_counter;
        int byte_current=0;
        int char_current=0;
        //printf("Parsing line %d: %s",line_counter, line);
        for (int i=0;i<MAXSTR;++i) { // parse characters of the line
            ++byte_current;
            //putchar('.');
            if (line[i]=='"') {
                if (saw_first_quotation)  { 
                    // this must me end-quote, reset the quation flag and go to next line
                    saw_first_quotation=false;
                    break;
                }
                else
                    saw_first_quotation=true;
            }
            else if (line[i]=='\\') {
                //putchar('\\'); // need to check the next character
                ++i;
                ++byte_current;
                if (line[i]=='\\' || line[i]=='"')
                    ++char_current;
                else if (line[i]=='x') {
                    // 2-digit hex code, need to skip 2 more bytes
                    byte_current+=2;
                    i+=2;
                    ++char_current;
                }
                
            }
            else // ordinary character
                ++char_current;
        } // end for / parse characters of the line
        //printf ("bytes: %d, characters: %d \n", byte_current, char_current);
        byte_counter+=byte_current;
        char_counter+=char_current;
    } // end while / parse file
    printf("Number of lines: %d\n",line_counter);
    printf("Number of bytes: %d\n",byte_counter);
    printf("Number of characters: %d\n",char_counter);
    printf("Part 1: difference: %d\n", byte_counter-char_counter);
}
