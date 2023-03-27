//c_implementation
int add(int n1,int n2)
{
	return n1+n2;
}
int product(int n1,int n2)
{
	return n1*n2;
}	
int main()
{
	int n1=1;
	int n2=2;
	int n3=3;
	int n4=4;
	int n5=5;
	int n6=6;
	int n7=7;
	int n8=8;
	int n9=9;
	int n10=10;
	int n11=11;
	int n12=12;
	int n13=13;
	int n14=14;
	int n15=15;
	int n16=16;
	int n17=17;
	int n18=18;
	int n19=19;
	int product1=product(n1,n2);
	product1+=product(product1,n3);
	product1+=product(product1,n4);
	product1+=product(product1,n5);
	product1+=product(product1,n6);
	product1+=product(product1,n7);
	product1+=product(product1,n8);
	product1+=product(product1,n9);
	product1+=product(product1,n10);
	product1+=product(product1,n11);
	product1+=product(product1,n12);
	product1+=product(product1,n13);
	product1+=product(product1,n14);
	product1+=product(product1,n15);
	product1+=product(product1,n16);
	product1+=product(product1,n17);
	product1+=product(product1,n18);
	product1+=product(product1,n19);
    int sum1=add(n1,n2);
	sum1+=add(sum1,n3);
	sum1+=add(sum1,n4);
	sum1+=add(sum1,n5);
	sum1+=add(sum1,n6);
	sum1+=add(sum1,n7);
	sum1+=add(sum1,n8);
	sum1+=add(sum1,n9);
	sum1+=add(sum1,n10);
	sum1+=add(sum1,n11);
	sum1+=add(sum1,n12);
	sum1+=add(sum1,n13);
	sum1+=add(sum1,n14);
	sum1+=add(sum1,n15);
	sum1+=add(sum1,n16);
	sum1+=add(sum1,n17);
	sum1+=add(sum1,n18);
	sum1+=add(sum1,n19);
	printf("%d %d",sum1,product1);
}
	