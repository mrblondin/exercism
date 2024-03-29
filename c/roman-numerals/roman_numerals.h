#ifndef ROMAN_NUMERALS_H
#define ROMAN_NUMERALS_H

typedef struct {
  int decimal;
  char * roman; 
} roman_form_t;

char *to_roman_numeral(unsigned int number);

#endif
