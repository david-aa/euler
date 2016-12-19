#include <stdio.h>

long double fact(long double n) {
	if (n <= 1) return 1;
	return n * fact(n - 1);
}

int main() {
	printf("%.0LF\n", fact(100));
}