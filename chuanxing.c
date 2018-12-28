#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double PI25DT = 3.141592653589793238462643;

int main()
{
	
	int n = 10000000;
	double h = 1.0 / (double)n;
	double s = 0.0;
	int i;
	double mypi;
	for (i = 0; i <= n; i++)
	{
		s += 4.0 / (1.0 + h * ((double)i - 0.5) * h * ((double)i - 0.5));
	}
	mypi = h * s;
	printf("%lf\n", mypi);
	fflush(stdout);
	
	return 0;
}
