#include<iostream>
using namespace std;
int main()
{
	int n,d,k,i,diff,c,x;
	c=0;
	diff=0;
	cout<<"\n enter id";
	cin>>n;
	d=n%10;
	for(i=0;i<=d;i++)
	{
		diff=d-i;
		c++;
		if(diff==0)
		break;
	}
	k=n/10;
	x=(k-(5000*c)/5000);
	cout<<c<<"\n"<<x;
	return 0;
}
