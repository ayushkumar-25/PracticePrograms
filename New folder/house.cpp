#include<stdio.h>
int main()
{
	int N=0,Y=0,X=0,arr[100],sum=0,i,sumsalary=0,sumHouse=0;
	printf("Enter no of house: ");
	scanf("%d",&N);
	printf("Enter Current salary: ");
	scanf("%d",&X);
	printf("Enter years of working: ");
	scanf("%d",&Y);
	printf("Enter house rent: ");
	for(i=0;i<N;i++)
	{
	
		scanf("%d",&arr[i]);
		sum=sum+arr[i];
	}
	if(sum>X)
	{
		for(i=0;i<Y;i++)
			sumsalary=2*sumsalary+X;
		printf("%d",sumsalary);
	}
	else
	{
		for(i=0;i<Y;i++)
			sumHouse=2*sumHouse+sum;
		printf("%d",sumHouse);
	}
}
