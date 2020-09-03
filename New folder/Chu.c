#include<stdio.h>
int main()
{
	int arr1[3],arr2[3],score[1],i,aliceScore=0,BobScore=0;
	
	for(i=0;i<3;i++)
		scanf("%d",&arr1[i]);
		
	
	for(i=0;i<3;i++)
		scanf("%d",&arr2[i]);
		
	for(i=0;i<3;i++)
	{
		if(arr1[i]>arr2[i])
			aliceScore++;
			
		else if(arr1[i]<arr2[i])
			BobScore++;
	}
	score[0]=aliceScore;
	score[1]=BobScore;
	printf("%d %d",score[0],score[1]);
}
