//Programa: Conectando Sensor Ultrassonico HC-SR04 ao Arduino
//Carrega a biblioteca do sensor ultrassonico
#include <Ultrasonic.h>
 
//Define os pinos para o trigger e echo
#define pino_trigger 25
#define pino_echo 24
#define pino_trigger_1 28
#define pino_echo_1 29
 
//Inicializa o sensor nos pinos definidos acima
Ultrasonic ultrasonic(pino_trigger, pino_echo);
Ultrasonic ultrasonic2(pino_trigger_1, pino_echo_1);
bool sensor1 = false;
bool sensor2 = false;

void setup()
{
  Serial.begin(9600);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
}
 
void loop()
{
  //Le as informacoes do sensor, em cm e pol
  float cmMsec, cmMsec2;
  long microsec = ultrasonic.timing();
  long microsec2 = ultrasonic2.timing();
  cmMsec = ultrasonic.convert(microsec, Ultrasonic::CM);
  cmMsec2 = ultrasonic2.convert(microsec2, Ultrasonic::CM);
  //Exibe informacoes no serial monitor
  //Serial.print("A2:");
  //Serial.println(cmMsec);
  //Serial.print("A3:");
  //Serial.println(cmMsec2);
  //Sensor 1
  if(cmMsec < 10 && sensor1 == false){
    digitalWrite(10,HIGH);
    sensor1 = true;
    Serial.print("A2:");
    Serial.println(sensor1);
    Serial.print("A3:");
    Serial.println(sensor2);
  }
  else if(sensor1 == true && cmMsec > 10){
    digitalWrite(10,LOW);
    sensor1 = false;
    Serial.print("A2:");
    Serial.println(sensor1);
    Serial.print("A3:");
    Serial.println(sensor2);
  }
  //Sensor2
  if(cmMsec2 < 10 && sensor2 == false){
    digitalWrite(11,HIGH);
    sensor2 = true;
    Serial.print("A2:");
    Serial.println(sensor1);
    Serial.print("A3:");
    Serial.println(sensor2);
  }
  else if(sensor2 == true && cmMsec2 > 10){
    digitalWrite(11,LOW);
    sensor2 = false;
    Serial.print("A2:");
    Serial.println(sensor1);
    Serial.print("A3:");
    Serial.println(sensor2);
  }
  
  delay(1000);
}
