# basic
A simple basic like compiler to c.

## Language syntax
```
PRINT "This is example program\n" ; 
LET max ;
LET i ;
PRINT "max loops: " ;
INPUT max ;
i = 0 ;
IF max > 20 THEN
    max = 20 ;
ENDIF
WHILE i < max DO
    PRINT "HELLO number: " ;
    PRINT i ;
    i = i + 1 ;
ENDWHILE
```
it's output:
```c
#include <stdlib.h>
#include <stdio.h>
int main () {
    printf("This is example program\n");
int max;
int i;
printf("max loops: ");
scanf("%d", &max);
i = 0;
if (max > 20) {
    max = 20;

}
while (i < max) {
    printf("HELLO number: ");
printf("%d\n", i);
i = (i + 1);

}

}
```


## Language features
- printing strings
- defining variabels (only numbers)
- taking inputs (only numbers)
- if statements
- while loops
- handling mathematical expressions