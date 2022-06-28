import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
// FUNCTION TO CHECK IF INTEGER VALUE IS PRIME
public class first{
    public static boolean isPrime(int val){
        if(val == 3){
            return true;
        }else{
            for(int i = 2; i<val/2; i++){
                if(val%i == 0){
                    return false;
                }
            }
        }
        return true;
    }
    // OPEN AND READ INTS FROM FILE TO FIND IF VALUE IS PRIME AS WELL AS IF VALUE-2 IS PRIME OR VALUE+2 IS PRIME
    public static void main(String[] args) {
        try{
            File read = new File("first.txt");
            Scanner input = new Scanner(read);
            while(input.hasNext()){
                String[] list = input.nextLine().split(" ");
                int temp = Integer.parseInt(list[0]);
                if(isPrime(temp) == false){
                    System.out.println("no");
                }else if(isPrime(temp-2) == true || isPrime(temp+2) == true){
                    System.out.println("yes");
                }else{
                    System.out.println("no");
                }
            }
            input.close();
        } catch (FileNotFoundException f){
            System.out.println("Error, the file is not found");
            f.printStackTrace();
        }
        
    }
}