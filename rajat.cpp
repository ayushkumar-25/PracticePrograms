#include<stdio.h>
int main()
{
	int i=0,x=0,sum=0,a[100];
	x = scanf("%d",&x);
	for (i=0;i<x;i++)
	scanf("%d",&a[i]);
	for (i=0;i<x;i++)
	sum = sum+a[i];
	printf("%d",sum);
}
