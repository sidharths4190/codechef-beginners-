import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class first
{
    public static void main(String[] args)throws IOException {
        BufferedReader bufferedReader=new BufferedReader(new InputStreamReader(System.in));
        long num = Long.parseLong(bufferedReader.readLine());
        Map<Character,Integer> map=new HashMap<>();
        map.put('0',6);
        map.put('1',2);
        map.put('2',5);
        map.put('3',5);
        map.put('4',4);
        map.put('5',5);
        map.put('6',6);
        map.put('7',3);
        map.put('8',7);
        map.put('9',6);
        for(int k = 0;k<num;k++)
        {
            String[] s = bufferedReader.readLine().split(" ");
            Integer sum = Integer.parseInt(s[0])+Integer.parseInt(s[1]);
            String s1 = String.valueOf(sum);
            int count = 0;
            for(int i=0;i<s1.length();i++)
            {
                count+=map.get(s1.charAt(i));
            }
            System.out.println(count);
        }
    }
}
