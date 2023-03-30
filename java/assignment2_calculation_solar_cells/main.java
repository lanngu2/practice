/* The two main math equations are 
  * 1) production (in kWh) = SOLAR_RADIATION * EFFICIENCY * PANEL_AREA * hours * NUM_OF_PANELS / 1000; //Note the equation in instruction is in Wh, so we divide by 1000 to get kWh as price is per kWh
  * 2) value = production * ELECTRIC_PRICe
        where,
        NUM_OF_PANELS = 26;
        PANEL_HEIGHT = 1; //Units is meters, so no conversion is needed as SOLAR_RADIATION is per m^2
        SOLAR_RADIATION = 166; //this is in Wh units, hence divide by 1000 in eq 1 above to convert to kWh
        PANEL_WIDTH = 1.7; //Units is meters, so no conversion is needed as SOLAR_RADIATION is per m^2
        PANEL_AREA = PANEL_WIDTH * PANEL_HEIGHT;
        EFFICIENCY = 0.2; //(instruction says 20 percent efficiency, so, 20/100 = 0.2)
        ELECTRIC_PRICE = 0.9; //this is per kWh, so we calculate production in kWh in eq 1 
*/
    
import java.util.Scanner;

class Main {
  //List and declare all the constant
  final static double NUM_OF_PANELS = 26;
  final static double PANEL_HEIGHT = 1;
  final static double PANEL_WIDTH = 1.7;
  final static double PANEL_AREA = 1.7; //PANEL_WIDTH * PANEL_HEIGHT=surface
  final static double ELECTRIC_PRICE = 0.9;//this is per kWh, 
  final static double SOLAR_RADIATION = 166;
  final static double EFFICIENCY = 0.2;
  final static int JUNE = 6;
  final static int JULY = 7;
  
  public static void main(String[] args) {
    //System.out.println("Hello World!");
    //Create an object/instance of scanner class to read user input
    //Use the new keyword to create an instance
    Scanner userInput = new Scanner(System.in);//System.in refers to standard input

    //Declare variable for Production(in kWh) and Value
    double production = 0.0;
    double value = 0.0;
    double sun_hours = 0.0;
    
    double hour_sunrise = 0.0;
    double minute_sunrise = 0.0;
    
    double hour_sunset = 0.0;
    double minute_sunset =0.0;
    
    int month = 0;
    int date = 0;

    //Validate month and date
    System.out.print("Enter today's date [mm-dd]: ");
    userInput.useDelimiter ("[-|:|\\s]+");
    month = userInput.nextInt();
    if (month != JUNE && month != JULY) {
      System.out.println("Wrong month, Month can be June or July");
      System.exit(0);
    }
    
    date = userInput.nextInt();
    
    if (month == JUNE) {
      if (date > 30 || date < 0) {
        System.out.println("Wrong date, date is positive and <= 30");
        System.exit(0);
      }  
    }
    
    
    if (month == JULY) {
      if (date > 31 || date < 0) {
        System.out.println("Wrong date, date is positive and <= 31");
        System.exit(0);
      }  
    }  
    
    //Validate hour_sunrise and minute_sunrise
    System.out.print("Enter the time of sunrise [hh: mm] ");
    userInput.useDelimiter ("[:|\\s]+");
    hour_sunrise = userInput.nextInt();
    if (hour_sunrise < 0 ) {
      System.out.println("Hour must be >0");
      System.exit(0);
    }
    if (hour_sunrise >23) {
      System.out.println("Hour must be <23");
      System.exit(0);
    }
    minute_sunrise = userInput.nextInt();
    //Validate minutes
    if (minute_sunrise < 0 ) {
      System.out.println("minute must be >0");
      System.exit(0);
    }
    if (minute_sunrise >59) {
      System.out.println("minute must be <59");
      System.exit(0);
    }

    //Validate hour_sunset and minute_sunset
    System.out.print("Enter the time of sunset [hh: mm] ");
    userInput.useDelimiter ("[:|\\s]+");
    hour_sunset = userInput.nextInt();
    if (hour_sunset < 0 ) {
      System.out.println("Hour must be >0");
      System.exit(0);
    }
    if (hour_sunset >23) {
      System.out.println("Hour must be <23");
      System.exit(0);
    }
    
    minute_sunset = userInput.nextInt();
    if (minute_sunset < 0 ) {
      System.out.println("minute must be >0");
      System.exit(0);
    }
    if (minute_sunset >59) {
      System.out.println("minute must be <59");
      System.exit(0);
    }
    
    //validare the time of sunrise and the time of sunset
    hour_sunrise = (hour_sunrise + minute_sunrise/60);
    hour_sunset = (hour_sunset+minute_sunset/60); 
    if (hour_sunrise > hour_sunset) {
      System.out.println("the time of sunrise is before the time of sunset! ");
      System.exit(0);
    }
    
    System.out.println("========================================== ");

    
    //caculation sun_hours:
    sun_hours = hour_sunset - hour_sunrise ;

    //caculation equations of Production(in kWh) and Value:
    production = SOLAR_RADIATION * EFFICIENCY * PANEL_AREA * sun_hours * NUM_OF_PANELS / 1000; //kWh
    value = production * ELECTRIC_PRICE ;
    
    //Roundling scale
    int noOfDecimals = 2;
    double scale = 0;
    scale = Math.pow(10,noOfDecimals);
    
    //newValue = Math.round(value*scale)/scale;
    production = Math.round(production*scale)/scale;
    value = Math.round(value*scale)/scale;
    sun_hours = Math.round(sun_hours*scale)/scale;


    
    System.out.println("Sun hours: " + sun_hours + " hours");
    System.out.println("The production on " + date +"/" +month +" is: " + production +" kWh to a value of: SEK "+ value);
  }
}
