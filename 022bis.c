#include <stdio.h>
#include <string.h>

#define MAXLENGHT 2951125
#define NWORDS 234371

void swap(char *v[], int i, int j) {
    char *temp;
    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}

void myqsort(char *v[], int left, int right) {
    int i, last;
    if (left >= right) return;
    swap(v, left, (left + right)/2);
    last = left;
    for (i = left + 1; i <= right; i++) 
        if (strcmp(v[i], v[left]) < 0)
            swap(v, ++last, i);
    swap(v, left, last);
    myqsort(v, left, last - 1);
    myqsort(v, last + 1, right);
}

int evaluate_word(char *word) {
    int len = strlen(word);
    int value = 0;
    for (int i = 0; i < len; i++) 
        value += (word[i] - 'A' + 1);
    return value;
}

int main() {
    FILE *fp;
    char line[MAXLENGHT];
    char *words[NWORDS];
    char delimiter[] = "\",\"";
    char *word;
    double sum = 0.0;

    fp = fopen("p022_words.txt", "r");
    int cont = 0;
    if (fp != NULL && fgets(line, MAXLENGHT, fp) != NULL) {
        word = strtok(line, delimiter);
        while (word != NULL) {
            words[cont] = word;
            word = strtok(NULL, delimiter);
            cont++;
        }
    }
    fclose(fp);

    myqsort(words, 0, NWORDS-1);

    for (int i = 1; i <= NWORDS; i++) {
       sum += i * evaluate_word(words[i-1]);
    }

    printf("%.0f\n", sum);
    return 0;
}
