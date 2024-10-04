#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include "esp_timer.h"
#include "img_converters.h"
#include "Arduino.h"
#include "fb_gfx.h"
#include "soc/soc.h"
#include "soc/rtc_cntl_reg.h"
#include "esp_http_server.h"
#include "esp_wifi.h"
#include "driver/ledc.h"
#include "driver/gpio.h"
#include "camera_stream.h" //custom lib with startCameraServer() function


// Replace with your network credentials
const char* ssid = "<INSERT_SSID>";
const char* password = "<INSERT_PASS>";

//"http://192.168.1.65:5000/trigger"
const char* serverName = "INSERT_FLASK_SERVER_IP";

#define PART_BOUNDARY "123456789000000000000987654321"

// This project was tested with the AI Thinker Model, M5STACK PSRAM Model and M5STACK WITHOUT PSRAM
#define CAMERA_MODEL_AI_THINKER

// Antenna Selection
#define ANTENNA_GPIO GPIO_NUM_2

// Led
#define BUILTIN_LED 4
#define BUTTON_PIN 13

//PIR Sensor GPIO
#define PIR_SENSOR_GPIO 12

#if defined(CAMERA_MODEL_AI_THINKER)
  #define PWDN_GPIO_NUM     32
  #define RESET_GPIO_NUM    -1
  #define XCLK_GPIO_NUM      0
  #define SIOD_GPIO_NUM     26
  #define SIOC_GPIO_NUM     27
  
  #define Y9_GPIO_NUM       35
  #define Y8_GPIO_NUM       34
  #define Y7_GPIO_NUM       39
  #define Y6_GPIO_NUM       36
  #define Y5_GPIO_NUM       21
  #define Y4_GPIO_NUM       19
  #define Y3_GPIO_NUM       18
  #define Y2_GPIO_NUM        5
  #define VSYNC_GPIO_NUM    25
  #define HREF_GPIO_NUM     23
  #define PCLK_GPIO_NUM     22
#else
  #error "Camera model not selected"
#endif

void startCameraServer();

void setup() {
  // Enable external antenna
  gpio_pad_select_gpio(ANTENNA_GPIO);
  gpio_set_direction(ANTENNA_GPIO, GPIO_MODE_OUTPUT);
  gpio_set_level(ANTENNA_GPIO, 1); // Set to 1 to enable external antenna, set to 0 to use internal antenna

  // Configure the built-in LED pin as an output
  // Configure the LEDC PWM
  ledcSetup(0, 5000, 8); // Channel 0, 5 kHz frequency, 8-bit resolution
  ledcAttachPin(BUILTIN_LED, 0); // Attach the LED pin to the channel

  // Set initial brightness
  ledcWrite(0, 0); // 50% duty cycle (128 out of 255)
  
  // Initialize PIR sensor GPIO as input
  pinMode(PIR_SENSOR_GPIO, INPUT);
 
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG; 
  
  if(psramFound()){
    config.frame_size = FRAMESIZE_SVGA;
    config.jpeg_quality = 12;
    config.fb_count = 2;
  } else {
    config.frame_size = FRAMESIZE_CIF;
    config.jpeg_quality = 15;
    config.fb_count = 1;
  }
  
  // Camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.println("Camera init failed with");
  }

  // Rotate the image 180 degrees
  sensor_t *s = esp_camera_sensor_get();
  s->set_vflip(s, 1);    // Flip vertically
  s->set_hmirror(s, 1);  // Flip horizontally

  // Wi-Fi connection
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  Serial.print("Camera Stream Ready! Go to: http://");
  Serial.print(WiFi.localIP());

  // Start streaming web server
  startCameraServer();
}


void loop() {
  int pirState = digitalRead(PIR_SENSOR_GPIO);
  
  if (pirState == HIGH) {
    // PIR sensor is triggered, turn on the LED
    ledcWrite(0, 50); // 50% duty cycle

    // Send HTTP GET request to Flask server
    if (WiFi.status() == WL_CONNECTED) { // Check Wi-Fi connection status
      HTTPClient http;

      http.begin(serverName); // Specify destination for HTTP request
      int httpResponseCode = http.GET();  // Send the request

      // Check the response code
      if (httpResponseCode > 0) {
        String response = http.getString(); // Get the response to the request
        Serial.println(httpResponseCode);   // Print HTTP response code
        Serial.println(response);           // Print the server response
      }
      else {
        Serial.print("Error on sending request: ");
        Serial.println(httpResponseCode);
      }

      http.end();  // Free resources
    }
    delay(500); // Delay for 0.5 second


  } else {
    // PIR sensor not triggered, turn off the LED
    ledcWrite(0, 0);
  }

  delay(500);
}
