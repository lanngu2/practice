class Main {

  //List and declare all the constant
    final static double VOLTAGE_400 = 400;
    final static double VOLTAGE_230 = 230;
    final static double BATTERY_CAPACITY = 35.8;
  

  public static void main(String[] args) {
    //System.out.println("Hello World!");
    //Declare variable for Charging power (5 such values)
    double chargingPower1 = 0.0;
    double chargingPower2 = 0.0;
    double chargingPower3 = 0.0; 
    double chargingPower4 = 0.0;
    double chargingPower5 = 0.0;
      
    //Declare variable for Charging time (5 such values)
    double chargingTime1 = 0.0;
    double chargingTime2 = 0.0;
    double chargingTime3 = 0.0;
    double chargingTime4 = 0.0;
    double chargingTime5 = 0.0;

    //Roundling scale
    int noOfDecimals = 2;
    double scale = 0;
    scale = Math.pow(10,noOfDecimals);
    //newValue = Math.round(value*scale)/scale;
    
    chargingPower1 = 10.0* VOLTAGE_230/1000;
    chargingPower2 = 16.0*VOLTAGE_230/1000;
    chargingPower3 = (10.0*VOLTAGE_400* Math.sqrt(3))/1000;
    chargingPower3 = Math.round(chargingPower3*scale)/scale;
    chargingPower4 = (16.0 * VOLTAGE_400*Math.sqrt(3)/1000);
    chargingPower4 = Math.round(chargingPower4*scale)/scale;
    chargingPower5 = (32.0 * VOLTAGE_400*Math.sqrt(3)/1000);
    chargingPower5 = Math.round(chargingPower5*scale)/scale;
    //chargingPower4 = Math.round((16.0 * VOLTAGE_400*Math.sqrt(3)/1000d)*100)/100d;
    //chargingPower5 = Math.round((32.0 * VOLTAGE_400*Math.sqrt(3)/1000d)*100)/100d;
    //System.out.println(chargingPower1);
    //System.out.printf("%.2f", chargingPower5);
    
    chargingTime1 = BATTERY_CAPACITY/chargingPower1;
    chargingTime1 = Math.round(chargingTime1*scale)/scale;
    chargingTime2 = BATTERY_CAPACITY/chargingPower2;
    chargingTime2 = Math.round(chargingTime2*scale)/scale;
    chargingTime3 = BATTERY_CAPACITY/chargingPower3;
    chargingTime3 = Math.round(chargingTime3*scale)/scale;
    chargingTime4 = BATTERY_CAPACITY/chargingPower4;
    chargingTime4 = Math.round(chargingTime4*scale)/scale;
    chargingTime5 = BATTERY_CAPACITY/chargingPower5;
    chargingTime5 = Math.round(chargingTime5*scale)/scale;  
      
    System.out.println("Battery: 35.8 (kwh)");
    System.out.printf("%-10s %-10s %-20s %-20s%n", "Current(A)", "Voltage(V)", "Charging Power(kW)","Charging Time(h)");
    System.out.printf("%-10s %-10s %-20s %-20s%n", "10", "230", chargingPower1, chargingTime1);
    System.out.printf("%-10s %-10s %-20s %-20s%n", "10", "230", chargingPower2, chargingTime2);
    System.out.printf("%-10s %-10s %-20s %-20s%n", "10", "400", chargingPower3, chargingTime3);
    System.out.printf("%-10s %-10s %-20s %-20s%n", "16", "400", chargingPower4, chargingTime4);
    System.out.printf("%-10s %-10s %-20s %-20s%n", "32", "400", chargingPower5, chargingTime5);
  }
}