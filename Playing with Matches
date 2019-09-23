import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner scan = new Scanner(System.in);
	
	        int num = scan.nextInt();
	
        	int[] ar1 = new int[20];
    	    int[] ar2 = new int[20];
	        int[] sum = new int[20];
	        int[] dig = new int[20];
	        
	        for(int i = 0;i<num;i++ )
		        {
		            ar1[i] = scan.nextInt();
		            ar2[i] = scan.nextInt();
		    
		        }
	    scan.close();
	        
	        for(int j = 0;j<num;j++)
	        {
	            sum[j] = ar1[j] + ar2[j];
	       	        }
	        
	int i= 0;
	int x = 0;
	
	for(int k = 0;k<num;k++)
	{ int count = 0;
    	while(sum[k] != 0)
    	{  
    	    dig[i] = sum[k]%10;
    	    sum[k] = sum[k]/10;
    	
    	    
    	   if(dig[i] == 0)
    	    {
    	        count+=6;
    	    }
    	    else if(dig[i] == 1)
    	    {
    	        count+=2;
    	        
    	    }
    	     else if(dig[i] == 2)
    	    {
    	        count+=5;
    	        
    	        }
    	     else if(dig[i] == 3)
    	    {
    	        count+=5;
    	    }
    	     else if(dig[i] == 4)
    	    {
    	        count+=4;
    	        
    	    }
    	     else if(dig[i] == 5)
    	    {
    	        count+=5;
    	        
    	    }
    	     else if(dig[i] == 6)
    	    {
    	        count+=6;
    	        System.out.println("6");
    	    }
    	     else if(dig[i] == 7)
    	    {
    	        count+=3;
    	        
    	    }
    	     else if(dig[i] == 8)
    	    {
    	        count+=7;
    	    }
    	     else if(dig[i] == 9)
    	    {
    	        count+=6;
    	        System.out.println("6");
    	    }
    	    i++;}
    	    System.out.println(count);
    	}
    		}
}
		
			
