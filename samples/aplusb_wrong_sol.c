#include <stdio.h>

int main() {
	int N;
	scanf("%d\n", &N);

	for (int i = 0; i < N; i++) {
////////////////////////////////////////////////CODE AREA
		int a, b;
		scanf("%d %d\n", &a, &b);
		printf("%d\n", a + b + 1);
////////////////////////////////////////////////END CODE AREA
	}
}
