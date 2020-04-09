#include<stdio.h>
int main()
{
	int i,j,n,k;
	scanf("%d",&n);
	for (i=0;i<n+1;i++)
	{
		for(k=(n-i); k>=0; k--)
		{
			printf(" ");
		}
		for(j=0;j<i;j++)
		{
			printf("#");
		}
		printf("\n");
	}
}
