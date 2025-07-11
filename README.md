Pulsar is a rather simple (its my first ever hardware project) macropad which I made for [highway.hackclub.com](highway.hackclub.com). It features a 3x3 electrical matrix arranged into a 2x4 key grid and a rotary encoder. There's also an OLED display and two NeoPixels! Rather simple design but I'll probably come back and improve it sometime.

# Images
<img width="1116" height="637" alt="pulsar_full" src="https://github.com/user-attachments/assets/5c63273b-d402-480d-805e-96b012449057" />
<img width="1292" height="882" alt="pcb" src="https://github.com/user-attachments/assets/256c1fba-1cf0-4d6f-94f8-dfd0f7b95ba0" />
<img width="954" height="897" alt="schematic" src="https://github.com/user-attachments/assets/0d271e85-3898-406d-a972-515d40d2ac51" />

# BOM
I will 3d print the case myself.

Here's the BOM that KiCad generated:

|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|**Reference**|**Qty**|**Value**|**DNP**|**Exclude from BOM**|**Exclude from Board**|**Footprint**|**Datasheet**|
|**D1,D2**|2|SK6812MINI||||LED_SMD:LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm|[https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf](https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf)|
|**D3,D4,D5,D6,D7,D8,D9,D10,D11**|9|1N4148||||Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal|[https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf](https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf)|
|**J1**|1|Conn_01x04_Pin||||hackpad:SSD1306-0.91-OLED-4pin-128x32|~|
|**SW1,SW2,SW3,SW4,SW5,SW7,SW8,SW9**|8|SW_Push||||Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB|~|
|**SW6**|1|RotaryEncoder_Switch||||Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm|~|
|**U1**|1|XIAO-RP2040-DIP||||OPL:XIAO-RP2040-DIP||

I will also need 4 m3.5 screws
