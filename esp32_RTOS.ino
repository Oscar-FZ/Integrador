#include <Arduino.h>
#include <WiFi.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <freertos/queue.h>
#include <typeinfo>


TaskHandle_t RECEIVERWIFI;
TaskHandle_t MENU;

xQueueHandle options;

const char* ssid = "estudiantes.ie";
const char* password = "Estudiantes2024";

char* strs[20]; //si algo falla eso era strs[20]
char* menu_strs[20];
int StringCount = 0;

boolean alreadyConnected = false;  // whether or not the client was connected previously
WiFiServer server(10000);  // server port to listen on

void connectWiFi(void) {
  Serial.printf("Connecting to %s\n", ssid);
  Serial.printf("\nattempting to connect to WiFi network SSID '%s' password '%s' \n", ssid, password);
  // attempt to connect to Wifi network:
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(500);
  }
  server.begin();
  // you're connected now, so print out the status:
  printWifiStatus();
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);
  Serial.println(" listening on port 10000");
}

void printWifiStatus(void) {
  // print the SSID of the network you're attached to:
  Serial.print("\nSSID: ");
  Serial.println(WiFi.SSID());

  // print your WiFi shield's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}

void receiverWiFi(void *parameter) { 
  while (1) {
    static WiFiClient client;
    if (!client)
      client = server.available();  // Listen for incoming clients
    if (client) {                   // if client connected
      if (!alreadyConnected) {
        // clead out the input buffer:
        client.flush();
        Serial.println("We have a new client");
        alreadyConnected = true;
      }

      int length;
      char value;

      if ((length = client.available()) > 0) {
        Serial.println("Received length: " + String(length));
        value = client.read();
        xQueueSend(options, (void *) &value, (TickType_t) 10);
        Serial.println("[PRINT] " + String(value));
        //Serial.println("[PRINT] Length: " + String(value.length()));  
      }
    }
  }
}


void menu(void *parameter) {
  char menu_strs;
  while (1) {
    while (xQueueReceive(options, &(menu_strs), (TickType_t) 1) != pdPASS) {
      digitalWrite(18, LOW);
      digitalWrite(32, LOW);
      digitalWrite(33, LOW);
      digitalWrite(25, LOW);
    }
    Serial.println("[PRINT] Dato recibido");
    //Serial.println(typeid(menu_strs).name());
    if (String(menu_strs) == "a") {
      Serial.println("[PRINT] A");
      digitalWrite(18, HIGH);
      delay(1000);
    }

    else if (String(menu_strs)== "b") {
      Serial.println("[PRINT] B");
      digitalWrite(32, HIGH);
      delay(1000);
    }

    else if (String(menu_strs) == "c") {
      Serial.println("[PRINT] C");
      digitalWrite(33, HIGH);
      delay(1000);
    }

    else if (String(menu_strs) == "d") {
      Serial.println("[PRINT] D");
      digitalWrite(25, HIGH);
      delay(1000);
    }
  }
  

}

void setup() {
  Serial.begin(115200);
  
  options = xQueueCreate(10, sizeof(strs));
  connectWiFi();

  xTaskCreatePinnedToCore(receiverWiFi, "RECEIVERWIFI", 5000, NULL, 1, &RECEIVERWIFI, 1);
  xTaskCreatePinnedToCore(menu, "MENU", 5000, NULL, 2, &MENU, 0);

  pinMode(18, OUTPUT); // 
  pinMode(32, OUTPUT); // 
  pinMode(33, OUTPUT); // 
  pinMode(25, OUTPUT); // 
}

void loop() {}
