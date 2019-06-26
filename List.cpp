#include<iostream>
using namespace std;

static int end=-1;
static int *p=new int[2];
static int length=2; 	
	 	
template <class T>
T Resize(T n1)
{
	cout<<"Older length: "<<length<<endl;
	int *p1=new int[2*length];
	//cout<<sizeof(p1);///here sizeof not working it is only showing the value 8 at every condition
	length=2*length;
	cout<<"New length"<<(length)<<endl;
	
	for(int temp=0;temp<length;temp++)
	{
		p1[temp]=0;
		//p1[temp]=p[temp];
	}
	for(int temp=0;temp<=end;temp++)
	{
		p1[temp]=p[temp];
	}
	//cout<<"New Array: ";
	/*for(int temp=0;temp<length;temp++)
	{
		cout<<" "<<p1[temp];
	}*/
	p=p1;
	//cout<<"New Array1: ";
	/*for(int temp=0;temp<length;temp++)
	{
		cout<<" "<<*(p+temp);
	}*/
}
template <class T0>
T0 Add(T0 n1)
{
	if((end+1)==length)
	{
		Resize(0);
	}	
	//int temp=end;
	p[end+1]=n1;
	end++;
	for(int temp1=0;temp1<length;temp1++)
	{
		cout<<p[temp1]<<" ";
	}
	cout<<endl;
	cout<<"value of end: "<<end<<endl;
	cout<<endl;
	cout<<"value of length: "<<length<<endl;
	
}
template <class T1 >
T1 Insert(T1 n1, T1 n2)
{
	if((end+1)==length)
	{
		Resize(0);
	}
	for(int temp=(length-1);temp>=n1;temp--)
	{
		p[temp]=p[temp-1];
	}
	p[n1]=n2;
	end++;
	for(int temp1=0;temp1<length;temp1++)
	{
		cout<<p[temp1]<<" ";
	}
	cout<<endl;
	cout<<"value of end: "<<end<<endl;
	cout<<endl;
	cout<<"value of length: "<<length<<endl;
	
}
template <class T2>
T2 Delete(T2 n1)
{
	for(int temp=n1;temp<(length-1);temp++)
	{
		p[temp]=p[temp+1];
	}
	p[end]=0;
	length--;
	for(int temp1=0;temp1<length;temp1++)
	{
		cout<<p[temp1]<<" ";
	}
	end--;
	cout<<endl;
	cout<<"value of end: "<<end<<endl;
	cout<<endl;
	cout<<"value of length: "<<length<<endl;
}
template <class T3>
T3 Read(T3 n1)
{
	cout<<"Element: "<<p[n1]<<endl;
	
}
int main()
{
	//int *p;
	//p=a;
	while(1)
	{
		//int a[]={5,6,7,8};
		//end=-1;
		int choice;
		cout<<"list implementation"<<endl;
		cout<<"1.Add elements to list"<<endl;
		cout<<"2.Insert elements to list"<<endl;
		cout<<"3.Delete elements to list"<<endl;
		cout<<"4.Read elements to list"<<endl;
		cout<<"5.Resize list"<<endl;
		cout<<"6.Read capacity to list"<<endl;
		cin>>choice;
		switch(choice)
		{
			case 1:
				int temp;
				cout<<"enter element"<<endl;
				cin>>temp;
				Add(temp);
				break;
			case 2:
				int temp1;
				cout<<"enter Index No";
				cin>>temp;
				cout<<"enter Element";
				cin>>temp1;
				Insert(temp,temp1);
				break;
			case 3:
				int temp2;
				cout<<"enter index to delete";
				cin>>temp2;
				Delete(temp2);		
				break;
			case 4:
				int temp3;
				cout<<"enter index to read";
				cin>>temp3;
				Read(temp3);
				break;
			case 5:
				Resize(0);
				break;
			case 6:
				cout<<"Capacity is: "<<length;
				break;
			
		}
		
	}
}
