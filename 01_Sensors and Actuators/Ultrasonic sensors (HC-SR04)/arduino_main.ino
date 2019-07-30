/*
Developer: M.Sc. Shiva Agrawal
Place: Germany
Version: 1.0
Date: 13.06.2019

Description: Driver code for Arduino ATmega2560 for reading 10 Ultrasonic sensors and calculate the distance from eah in cm.In every cycle, all the 10 sensors are read but one after other to avoid interference of waves and hence to avoid noise in measurement.
*/

// constants and initialization of pins where each Ultrasonic sensor is connected to arduino ATmega22560
// NOTE: here pin numbers are hard coded because the Interface is fixed and is not expected to change in future revisions.
const int totalUltrasonicSensors = 10;
int trigPin[totalUltrasonicSensors] = {31,33,35,37,39,41,43,45,47,49};
int echoPin[totalUltrasonicSensors] = {30,32,34,36,38,40,42,44,46,48};
float measurementValues[totalUltrasonicSensors];
    
/*
function to calculate distance in cm from the obstacle.
@param: triPin: pin number where trigger pin of Ultrasonic sensor is connected.
@param: echoPin: pin number where echo pin of Ultrasonic sensor is connected.
@return: value of calculated distance in float
*/
float calculateDistanceInCm(int trigPin, int echoPin)
   {
      float distance;
      long duration;
      // Clears the trigPin
      digitalWrite(trigPin, LOW);
      delayMicroseconds(2);
      
      // Sets the trigPin on HIGH state for 10 micro seconds
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);
      
      // Reads the echoPin, returns the sound wave travel time in microseconds
      duration = pulseIn(echoPin, HIGH);
      
      // Calculating the distance in cm
      distance= duration*0.034/2;
      return (distance);
   }

/*
Function to initiliaze the configuration.
It sets the trig pins to output and echo pins to input for all the sensors.
It also begins the serial communication with 9600 baud rate
*/
    
void setup() 
    {
      for(byte count = 0; count < totalUltrasonicSensors; count++)
      {
         pinMode(trigPin[count], OUTPUT); // Sets the trigPin as an Output
         pinMode(echoPin[count], INPUT); // Sets the echoPin as an Input
      }
      Serial.begin(9600); // Starts the serial communication
    }

/*
This function is like main() function with built in while(True) loop to do the work indefinately.
It does the measurement process of each sensor and then collect the values along with sensorID together
of all the 10 sensors, convert it into one string and send it serially. 
*/ 
void loop() 
   {
     String completeData;
     for(byte count = 0; count < totalUltrasonicSensors; count++)
      {
        delay(5);
        measurementValues[count] = calculateDistanceInCm(trigPin[count], echoPin[count]);
        if (measurementValues[count] > 400) // for invalid values
        {
          measurementValues[count] = 0; // assign 0 whch means value is invalid
        }
      
        //create one string to concatenate data from all sensors
        // Format: sensorID1:value1,sensorID2:value2,...... 
        completeData = completeData + String(count+1) + ":" + String(measurementValues[count]) + ":";
      }
     delay(50);
     Serial.print(completeData + "\n");
   }
