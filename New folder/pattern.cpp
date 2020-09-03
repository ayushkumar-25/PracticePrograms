#include<stdio.h>
#include<stdlib.h>
int main()
{
	int size = 5; int i,j;
	for(i=0;i<=size;i++)
	{
		for(j=0;j<=i;j++)
		{
			printf(" AK ");
		}
		printf("\n");
	}
	
	for(i=size-1;i>=0;i--)
	{
		for(j=i;j>=0;j--)
		{
			printf(" AK ");
		}
		printf("\n");
	}

}
