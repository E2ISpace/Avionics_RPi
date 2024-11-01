void setup() {
    Serial.begin(9600);  // 시리얼 통신을 9600 baud로 시작
}

void loop() {
    if (Serial.available() > 0) {
        String receivedMessage = Serial.readString();  // 메시지를 읽습니다.
        
        if (receivedMessage == "RESET") {
            // 리셋 관련 동작
            Serial.println("Received RESET command");
            // 추가 동작
        }
    }
}

