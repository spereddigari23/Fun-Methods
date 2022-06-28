import java.io.FileNotFoundException;
import java.io.File;
import java.util.Scanner;

public class second {
    public static int set(int manipulatedValue, int n, int v){
        int[] array = new int[30];
        int temp = manipulatedValue;
        int index = 0;
        while(temp>0){
            int digit = temp%2;
            array[index] = digit;
            index++;
            temp = temp/2;
        }
        array[n] = v;
        for(int val : array){
            System.out.println(val);
        }
        int numOfDigits = index;
        int finale = 0;
        int nIndex = 0;
        while(numOfDigits != 0){
            finale = finale + array[nIndex]*(int)(Math.pow(2, index));
        }
        for(int i = 0; i==numOfDigits; i++){
            finale = finale + array[i]*(int)Math.pow(2, index);
            index--;
        }
        return finale;
    }
    public static int getBinary(int manipulatedValue, int n){
        int binary = 0;
        int multiple = 1;
        int temp = manipulatedValue;
        while(temp>0){
            int digit = temp%2;
            binary = binary + (digit*multiple);
            multiple = multiple*10;
            temp = temp/2;
        }
        System.out.println("The binary value is: "+binary);
        int hold = n;
        while(hold>0){
            binary = binary/10;
            hold--;
        }
        System.out.println("The correct digit is: "+binary%10);
        return binary%(10);
    }
    public static int comp(int manipulatedValue, int n){
        int[] array = new int[30];
        int temp = manipulatedValue;
        int index = 0;
        while(temp>0){
            int digit = temp%2;
            array[index] = digit;
            index++;
            temp = temp/2;
        }
        //NOW CHANGING THE VALUE TO COMPLEMENT
        if(array[n] == 0){
            array[n] = 1;
        }else if(array[n] == 1){
            array[n] = 0;
        }
        int finale = 0;
        index-=1;
        while(index>=0){
            finale = array[index]*(int)(Math.pow(2, index));
            index--;
        }
        return finale;
    }
    public static void main(String[] args) {
         try{
            File read = new File("second.txt");
            Scanner input = new Scanner(read);
            int manipulatedValue = input.nextInt();
            String[] line = input.nextLine().split(" ");
            if(line[0].equals("get")){
                get(manipulatedValue, Integer.parseInt(line[1]));
            }else if(line[0].equals("set")){
                set(manipulatedValue, line[1], line[2]);
            }
            input.close();
        } catch (FileNotFoundException f){
            System.out.println("Error the file has not been found.");
            f.printStackTrace();
        }
        System.out.println(get(72, 6));
        System.out.println(set(5, 1, 1));
        System.out.println(comp(4, 1));
    }
}
