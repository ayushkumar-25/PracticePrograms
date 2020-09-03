#include<stdio.h>
int main()
{
	int x=0,sum=0,a[100];
	scanf("%d",&x);
	for (int i=0;i<x;i++)
	{
		scanf("%d",&a[i]);
		sum = sum + a[i];
	}
	printf("%d",sum);
}
