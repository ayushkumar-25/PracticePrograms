#include<stdio.h>
int main()
{
    int n=0,sum=0,arr[100];
    scanf("%d",&n);
    for(int i=0;i<=n;i++)
    {
        scanf("%d",&arr[i]);
        sum += arr[i];
    }
    printf("%d",sum);
}
