import java.util.InputMismatchException ;
import java.util.Scanner;

class Main{
  public static void main(String[] args){
    Scanner userInput = new Scanner(System.in) ;
    int[] randomArray;
    int randomCount = 0;

    int[]evenArray;
    int evenCount = 0;

    int[]oddArray;
    int oddCount = 0;

    while(true) {
      System.out.print("How many random numbers in the range 0 - 999 are desired?  ");
      try {
        String temp = userInput.nextLine(); //Process and read the entry
        //randomCount = userInput.nextInt();
        randomCount = Integer.parseInt(temp); //Get integer from the string
        
        randomArray = new int[randomCount];
        evenArray = new int[randomCount];
        oddArray = new int[randomCount];
        
        System.out.println("Number Accepter");
        break;
      }
      catch(OutOfMemoryError e) {
        System.out.println("OutOfMemoryError, I cannot handle that number, try again");
      }
      catch (InputMismatchException e){
        //userInput.nextLine(); // clear the input from System.in
        System.out.println("InputMismatchException, I can read only Integers, pleaser enter Integer") ;
      }
      catch (NumberFormatException e){
        //userInput.nextLine(); // clear the input from System.in
        System.out.println("NumberFormatException, I can read only Integers, pleaser enter Integer") ;
      }
    }

    //Generate Random numbers
    for(int i = 0; i < randomCount; i++) {
      //generate random numbers here
      randomArray[i] = (int)(Math.random()*1000);
      if(randomArray[i] % 2 == 0) {
        evenArray[evenCount] = randomArray[i] ;
        evenCount++ ;
      }
      else {
        oddArray[oddCount] = randomArray[i] ;
        oddCount++ ;
      }
    }
    System.out.println("\nHere are the random numbers:") ;
    for (int i = 0; i < randomCount; i++) {
      System.out.print(randomArray[i] + " ") ;
    }

    System.out.println(" ") ; //Astehics
    System.out.println("\n" + evenCount + "  -Even number") ; //Asthetics
 
    for (int i = 0; i < evenCount; i++) {
      System.out.print(evenArray[i] + " ") ;
    }  

    for (int k = 0; k < evenCount; k++){
    //iterate through the subarray and compare adjacent elements
      for (int j = 0; j < evenCount-1; j++) {
        if (evenArray[j]> evenArray[j+1]){
          int tempo = evenArray [j] ;
            evenArray[j]= evenArray [j+1] ;
            evenArray [j+1] = tempo;
        }
      }   
    }

    System.out.println(" ") ; //Asthetics
    System.out.println("\n" + oddCount + " -Odd number") ; //Asthetics
    for (int i = 0; i < oddCount; i++) {
      System.out.print(oddArray[i] + " ") ;
    }
    for (int k = 0; k < oddCount; k++){
    //iterate through the subarray and compare adjacent elements
      for (int j = 0; j < oddCount-1; j++) {
        if (oddArray[j]> oddArray[j+1]){
          int tempo = oddArray [j] ;
            oddArray[j]= oddArray [j+1] ;
            oddArray [j+1] = tempo;
        }
      }   
    }
    
    System.out.println(" ") ; //Asthetics
    System.out.println("\nHere are the random numbers arranged: ");
    if (evenCount != 0 ) {
      for (int k = 0 ; k <evenCount; k++){
      System.out.print(evenArray[k] + "  ") ;
      } 
    }
    else {
      System.out.println("No Even Numbers  ") ;
    }
    
    System.out.print(" - ");

    
    if (oddCount != 0 ) {
      for (int k = 0 ; k <oddCount; k++){
      System.out.print(oddArray[k] + "  ") ;
      } 
    }
    else {
      System.out.println("No Odd Numbers") ;
    }

    System.out.println(" ") ; //Asthetics    
    System.out.println("\nOf the above "+ randomCount+" numbers, "+ evenCount+" were even and "+ oddCount+ " odd") ; 
 
  }
}
