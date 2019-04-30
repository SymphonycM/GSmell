#define POT A0
int v;
void setup() {
  Serial.begin(9600);
}

void loop() {
  v=analogRead(POT);
  Serial.println(v);
}
