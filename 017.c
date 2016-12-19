#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* get_prefix(int number) {
  char* text;
  int tmpI;
  switch (number) {
    case 20:
      text = "twenty ";
      break;
    case 30:
      text = "thirty ";
      break;
    case 40:
      text = "forty ";
      break;
    case 50:
      text = "fifty ";
      break;
    case 60:
      text = "sixty ";
      break;
    case 70:
      text = "seventy ";
      break;
    case 80:
      text = "eighty ";
      break;
    case 90:
      text = "ninety ";
      break;
    default:
      text = "";
  }
  return text;
}

int strlenNoSpaces(char* str) {
  int cont = 0;
  for (int i = 0; str[i] != '\0'; i++) {
    if (str[i] != ' ') cont++;
  }
  return cont;
}

char* get_number_spelled(int number) {
  char* text;
  char* tmpS1;
  char* tmpS2;
  char* tmpS3;
  int tmpI;
  if (number < 1)
    text = "";
  else if (number == 1)
    text = "one";
  else if (number == 2)
    text = "two";
  else if (number == 3)
    text = "three";
  else if (number == 4)
    text = "four";
  else if (number == 5)
    text = "five";
  else if (number == 6)
    text = "six";
  else if (number == 7)
    text = "seven";
  else if (number == 8)
    text = "eight";
  else if (number == 9)
    text = "nine";
  else if (number == 10)
    text = "ten";
  else if (number == 11)
    text = "eleven";
  else if (number == 12)
    text = "twelve";
  else if (number == 13)
    text = "thirteen";
  else if (number == 14)
    text = "fourteen";
  else if (number == 15)
    text = "fifteen";
  else if (number == 16)
    text = "sixteen";
  else if (number == 17)
    text = "seventeen";
  else if (number == 18)
    text = "eighteen";
  else if (number == 19)
    text = "nineteen";
  else if (number >= 20 && number < 100 ) {
    tmpI = 10 * (number / 10);
    tmpS1 = get_prefix(tmpI);
    tmpS2 = get_number_spelled(number - tmpI);
    text = malloc((sizeof(char) * strlen(tmpS1) + 1) +
                  (sizeof(char) * strlen(tmpS2) + 1));
    strcpy(text, tmpS1);
    strcat(text, tmpS2);
  } else if (number >= 100 && number < 1000 ) {
    tmpI = number / 100;
    tmpS1 = get_number_spelled(tmpI);
    tmpS2 = number == 100 * tmpI ? " hundred " : " hundred and ";
    tmpS3 = get_number_spelled(number - tmpI * 100);
    text = malloc((sizeof(char) * strlen(tmpS1) + 1) +
                  (sizeof(char) * strlen(tmpS2) + 1) +
                  (sizeof(char) * strlen(tmpS3) + 1));
    strcpy(text, tmpS1);
    strcat(text, tmpS2);
    strcat(text, tmpS3);
  } else if (number >= 1000 && number < 10000) {
    tmpI = number / 1000;
    tmpS1 = get_number_spelled(tmpI);
    tmpS2 = " thousand ";
    tmpS3 = get_number_spelled(number - tmpI * 1000);
    text = malloc((sizeof(char) * strlen(tmpS1) + 1) +
                  (sizeof(char) * strlen(tmpS2) + 1) +
                  (sizeof(char) * strlen(tmpS3) + 1));
    strcpy(text, tmpS1);
    strcat(text, tmpS2);
    strcat(text, tmpS3);
  }
  return text;
}

int main() {
  char* text;
  long cont = 0L;
  for (int i = 1; i < 1001; i++) {
    text = get_number_spelled(i);
    //printf("%d => %s, chars: %d\n", i, text, strlenNoSpaces(text));
    cont += strlenNoSpaces(text);
  }
  printf("%ld chars\n", cont);
  return 0;
}
