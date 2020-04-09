#include<stdio.h>
int main()
{
	int i=0,n=0,j=0,b[100],c[100];
	
	printf("Enter N: ");
	scanf("%d",&n);
	
	printf("Enter number of Buses from each stop: ");
	for (i=0;i<=n;i++)
	{
		scanf("%d",&b[i]);
	}
	
	c[1]=b[1];
	
	for (i=0;i<=n;i++)
	{
		for(j=i+1;j<=n;j++)
		{
			if (j%i==0)
			{
				c[j]=b[j]-b[i];
			}
		}
	}
	printf("Number of unique bus are: ");
	for(i=0;i<=n;i++);
	printf("%d",c[i]);
}
