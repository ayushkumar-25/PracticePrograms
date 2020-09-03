#include<stdio.h>
#include<stdlib.h>
int main()
{
    //taking input in the array
    int n,arr[10][10],sum1=0,sum2=0,sum=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        for (int j=0;j<n;j++)
        {
            scanf("%d",&arr[i][j]);
        }
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
            if(i+j==2)         //here we can't use 'else if' because if will leave the middle number of the array which already came in 1st if statement.
            {
                sum2 += arr[i][j];
            }
        }
    }
    //printing the diagonal sum
    sum = abs(sum1-sum2);
    printf("%d",sum);
    //printf("%d",sum2);
}
