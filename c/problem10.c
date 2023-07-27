//Summation of Primes 

/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes below two million
*/


// Holy fuck this is so much faster than Python



#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

int main(){

//start of clock
clock_t start, end;
double execution_time;
start = clock();

int n = 3;
long summation = 2;
while (n < 2000000) {
	bool isPrime = true;

	int i;
	for (i = 2; i < sqrt(n) + 1; i ++){
   		if (n % i == 0){

			isPrime = false;}
						}
	if (isPrime){
                //printf("%d \n", n);
		summation += n;
				}

		n += 1;

}

printf("\n%ld \n", summation);

//end of clock
end = clock();
execution_time = ((double)(end - start)) / CLOCKS_PER_SEC;
printf("Total run time: %f seconds\n\n", execution_time);

return 0;
}


