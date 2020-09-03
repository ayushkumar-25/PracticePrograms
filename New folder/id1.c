#include<stdio.h>
int main()
{
	int id,intern,day,d,diff,k,i;
	printf("\nEnter ID: ");
	scanf("%d",&id);
	d=id%10;
	diff=d;
	day=0;
	for(i=0;i<=d;i++)
	{
		diff=diff-i;
		day++;
		if(diff==0)
		{
		break;
		}
	}
	k=(id/10);
	intern=(k*10-(5000*(day-1)))/5000;
	printf("Day: %d",day);
	printf("\nIntern: %d",intern);
	
}
