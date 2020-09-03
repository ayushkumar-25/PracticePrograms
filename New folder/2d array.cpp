#include<stdio.h>
#include<stdlib.h>
int main()
{
	//taking input in the array
	int n,arr[10][10],sum1=0,sum2=0,a=0;
	printf("Enter size of the Matrix: ");
	scanf("%d",&n);
	printf("\n");
	a=n-1;
	for(int i=0;i<n;i++)
	{
		for (int j=0;j<n;j++)
		{
			printf("Enter element for (%d,%d): ",i+1,j+1);
			scanf("%d",&arr[i][j]);
		}
	}
	printf("\nEntered Matrix:- \n");
	
	//displaying the 2D array
	for(int i=0;i<n;i++)
	{
		for (int j=0;j<n;j++)
		{
			printf(" %d ",arr[i][j]);
		}
		printf("\n");
	}
	
	//finding sum of diagonals
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if (i==j)
			{
				sum1 += arr[i][j];
			}
			if(i+j==a) 		//here we can't use 'else if' because if will leave the middle number of the array which already came in 1st if statement.
			{
				sum2 += arr[i][j];
			}
		}
	}

	//printing the diagonal sum
	
	int sum = abs(sum1-sum2);
	printf("\n\nAbsolute difference of the diagonals = %d",sum);
	printf("\n\n");
}
