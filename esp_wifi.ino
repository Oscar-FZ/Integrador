#include <Arduino.h>
#include <WiFi.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <freertos/queue.h>

const char* ssid = "Familia _FZ_2.4";
const char* password = "gu6122411";

String strs[20]; //si algo falla eso era strs[20]
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

void receiverWiFi() { 
  while (1) {
    static WiFiClient client;
    static int16_t seqExpected = 0;
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
      String value;
      String str;

      if ((length = client.available()) > 0) {
        Serial.println("Received length: " + String(length));
        value = client.readString();
        Serial.println("[PRINT] " + value);
        Serial.println("[PRINT] Length: " + String(value.length()));  
      }
    }
  }
}

void setup() {
  Serial.begin(115200);
  connectWiFi();
}

void loop() {
  printWifiStatus();
  receiverWiFi();
  delay(1000);
}