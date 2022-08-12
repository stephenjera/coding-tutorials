#include <stdio.h>
#include <stdlib.h>
//#include <pthread.h>


// Create new data type
typedef struct {
	int first[1][1];
	int second[1][1];
	int result[1][1];
	int r1, c1, r2, c2;
} matrixParty, * matrixPartys;

void fillMatrix(int first[][1], int second[][1], int r1, int c1, int r2, int c2);
//void multiply(int first[][1], int second[][1], int result[][1], int r1, int c1, int r2, int c2);
//void* multiply(void* first[][1], void* second[][1], void* result[][1], void* r1, void* c1, void* r2, void* c2);
void* multiply(void* arg);
void display(int matrix[][1], int r1, int c2);


int main() {

	matrixParty starting;
	starting.r1 = 1, starting.r2 = 1, starting.c1 = 1, starting.c2 = 1;

	printf(" Please insert the number of rows and columns for first matrix \n ");
	scanf_s("%d %d", &starting.r1, &starting.c1);

	printf(" Please insert the number of rows and columns for second matrix\n");
	scanf_s(" %d %d", &starting.r2, &starting.c2);

	printf("\n");
	printf("r1: %d\n", starting.r1);
	printf("c1: %d\n", starting.c1);
	printf("r2: %d\n", starting.r2);
	printf("c2: %d\n\n", starting.c2);


	// create matrices sizes
	int first[10][10], second[10][10], result[10][10];

	// check r1 and c2 match 
	if (starting.r1 == starting.c2) {
		fillMatrix(starting.first, starting.second, starting.r1, starting.c1, starting.r2, starting.c2);
	}
	else {
		printf("Rows first and columns second don't match\n\n");
		exit(1);
	}

	// print matrix 1
	printf("matrix 1 is:\n\n");
	display(starting.first, starting.r1, starting.c1);

	// print matrix 2
	printf("matrix 2 is:\n\n");
	display(starting.second, starting.r2, starting.c2);

	// matrix multiplication
	multiply(&starting);

	printf("result is:\n\n");
	display(starting.result, starting.r1, starting.c2);

	return 0;
}


void fillMatrix(int first[][1], int second[][1], int r1, int c1, int r2, int c2) {
	//populate matrix 1
	int i, j, k; // loop variables
	for (i = 0; i < r1; i++) {
		for (j = 0; j < c1; j++) {
			first[i][j] = 5;
		}
	}

	//populate matrix 2
	for (i = 0; i < r2; i++) {
		for (j = 0; j < c2; j++) {
			second[i][j] = 5;
		}
	}
}

void* multiply(void* arg) {
	matrixPartys s = (matrixPartys)arg;
	//bufferP buffer = (bufferP) args; 
	// matrix multiplication
	int i, j, k; // loop variables
	for (i = 0; i < s->r1; i++) {
		for (j = 0; j < s->c2; j++) {
			s->result[i][j] = 0;
			for (k = 0; k < s->r2; k++) {
				s->result[i][j] += s->first[i][k] * s->second[k][j];
			}
		}
	}
}

void display(int matrix[][1], int r1, int c1) {
	int i, j; // loop variables
	for (i = 0; i < r1; i++) {
		for (j = 0; j < c1; j++) {
			printf("%d \t", matrix[i][j]);
		}
		printf(" \n ");
	}
}
