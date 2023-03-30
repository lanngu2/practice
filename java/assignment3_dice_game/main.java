import java.util.Scanner;
class Main {
  //List and declare all the constant
  public static void main(String[] args) {
    System.out.println("Welcome to dice game 12. You must roll 1-3 dice and try to get the sum of 12...");
    System.out.println(" ");
    //Create an object/instance of scanner class to read user input
    //Use the new keyword to create an instance
    Scanner Input = new Scanner(System.in);//System.in refers to standard input
    //Declare variable  
    boolean isRound = false; //controls when exit game     
    int win = 0;
    int loss = 0;
    
    while (isRound == false) {
      //Declare variable  
      int dice1 = 0;
      int dice2 = 0;
      int dice3 = 0;
      int sum = 0;
      int number = 0;
      String inString;
      
      //Validate the rolled
      while(dice1 == 0 || dice2 == 0 || dice3 == 0 ) {
        int countSum = 0;
        System.out.println(" ");
        System.out.print("Enter a number between 1 and 3 (or q to quit): ");
        if(Input.hasNextInt()) {
          number = Input.nextInt();
          if(number == 1 && dice1 == 0 ) {
            dice1 = (int)(Math.random() * 6+1);
            countSum = 1;
          }
          else if (number == 2 && dice2 == 0){
            dice2 = (int)(Math.random() * 6+1);
            countSum = 1;
          }
          else if (number == 3 && dice3 == 0){
            dice3 = (int)(Math.random() * 6+1); 
            countSum = 1;
          }
          else {
            System.out.println("Sorry, that is an invalid entry. Try again. Valid entries are 1, 2, 3, and q");
          }
          if (countSum == 1){
            sum = dice1 + dice2+ dice3 ;
            if (sum == 12){
              win = win + 1;
              loss = loss + 0;
              System.out.println(dice1 +" " + dice2 +" " + dice3 + " sum:" + sum +" #win:" + win+" #loss:" + loss);
              break ;
            }
            else if (sum <12){
              win = win + 0;
              loss = loss + 0;
            }
            else {
              win = win + 0;
              loss = loss + 1;
            }
            System.out.println(dice1 +" " + dice2 +" " + dice3 + " sum:" + sum +" #win:" + win+" #loss:" + loss);
          } 
        }
        else if(Input.hasNext()) {
          inString = Input.next();
          if(inString.equalsIgnoreCase("q")) {
            System.out.println("#win:" + win+" #loss:" + loss);
            System.out.println("Game Over!");
            System.exit(0);
          }
            else {
            System.out.println("Sorry, that is an invalid entry. Try again. Valid entries are 1, 2, 3, and q");  
          }
        }
      }
      if (sum == 12){
        System.out.println("You won!! ");
      }
      else if (sum <12){
        System.out.println("You neither won nor lost the game. ");
      }
      else {
        System.out.println("You lost!!");
      }
      System.out.println(" ") ;
      System.out.println("Next round");
    }
  }    
}