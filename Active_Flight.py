import numpy as np
import matplotlib.pyplot as plt


# Payload
PayloadWeight = 24.0 # in grams
PayloadConsumptionRate = 0.08 # Rate per g
PayloadConsumption = (PayloadWeight * PayloadConsumptionRate)/100 + 1 # Percentage increase of total power consumption
print(PayloadConsumption)
# Sensors

VN_300 = 1.25 #W INS
HC_SR04 = 0.075 * 2 #W  UltraSonic
Ellipse = 0.4 #W INS
Maxbotix = 0.0242 * 2 #W Ultrasonic
TFmini_S_I2C = 0.7 * 2#W Lidar
Garmin_LIDAR_Lite_v4 = 0.425 * 2 #W Lidar
LightWare_SF45_B = 1.5 * 2 #W Lidar
AHRS_M2 = 0.06 #W INS
Inertial_Labs_INS_B = 2.5 #W INS 

SensorsUsed = AHRS_M2 + HC_SR04
print(SensorsUsed)

#Mini 3

energy_Mini3 = 28.4 # Wh, max energy
SafetyMargin = 0.8 # 
HoveringTime_Mini3 = 40 # Min
FlightTime_Mini3 = 47 # Min
ActiveHovering_Mini3 = np.arange(0, 20, 0.5) # Min

HoveringPower_Mini3 = energy_Mini3/(HoveringTime_Mini3/60) # Watts
FlightPower_Mini3 = energy_Mini3/(FlightTime_Mini3/60) # Watts
print(FlightPower_Mini3)
HoveringConsumptiontest = HoveringPower_Mini3 * (10 / 60) # Wh
print(HoveringConsumptiontest)

ActiveFlight_Mini3 = []
for t in ActiveHovering_Mini3:
    HoveringConsumption = HoveringPower_Mini3 * (t / 60) # Wh
    ActualEnergy = energy_Mini3 * SafetyMargin - HoveringConsumption*PayloadConsumption

    FlightConsumption = 0
    SensorConsumption = 0
    flight_time = 0
    while (FlightConsumption*PayloadConsumption + SensorConsumption) < ActualEnergy:
        FlightConsumption = FlightPower_Mini3 * (flight_time/60)
        SensorConsumption = SensorsUsed * ((flight_time + t)/60)
        flight_time += 0.01
    
    ActiveFlight_Mini3.append(flight_time)

# Mavic 3
energy_Mavic3 = 77 # Wh, max energy
HoveringTime_Mavic3 = 40 # Min
FlightTime_Mavic3 = 46 # Min
ActiveHovering_Mavic3 = np.arange(0, 20, 0.5) # Min

HoveringPower_Mavic3 = energy_Mavic3/(HoveringTime_Mavic3/60) # Watts
FlightPower_Mavic3 = energy_Mavic3/(FlightTime_Mavic3/60) # Watts


ActiveFlight_Mavic3 = []
for t in ActiveHovering_Mavic3:
    HoveringConsumption = HoveringPower_Mavic3 * (t / 60) # Wh
    ActualEnergy = energy_Mavic3 * SafetyMargin - HoveringConsumption*PayloadConsumption

    FlightConsumption = 0
    SensorConsumption = 0
    flight_time = 0
    while (FlightConsumption*PayloadConsumption + SensorConsumption) < ActualEnergy:
        FlightConsumption = FlightPower_Mavic3 * (flight_time/60)
        SensorConsumption = SensorsUsed * ((flight_time + t)/60)
        flight_time += 0.01
    
    ActiveFlight_Mavic3.append(flight_time)

# Autel lite+

energy_Autel = 68.7 # Wh, max energy
HoveringTime_Autel = 38 # Min
FlightTime_Autel = 40 # Min
ActiveHovering_Autel = np.arange(0, 20, 0.5) # Min

HoveringPower_Autel = energy_Autel/(HoveringTime_Autel/60) # Watts
FlightPower_Autel = energy_Autel/(FlightTime_Autel/60) # Watts

ActiveFlight_Autel = []
for t in ActiveHovering_Autel:
    HoveringConsumption = HoveringPower_Autel * (t / 60) # Wh
    ActualEnergy = energy_Autel * SafetyMargin - HoveringConsumption*PayloadConsumption

    FlightConsumption = 0
    SensorConsumption = 0
    flight_time = 0
    while (FlightConsumption*PayloadConsumption + SensorConsumption) < ActualEnergy:
        FlightConsumption = FlightPower_Autel * (flight_time/60)
        SensorConsumption = SensorsUsed * ((flight_time + t)/60)
        flight_time += 0.01
    
    ActiveFlight_Autel.append(flight_time)

# Autel Robotics Evo ll Pro  

energy_Autel_Pro = 82 # Wh, max energy
HoveringTime_Autel_Pro = 35 # Min
FlightTime_Autel_Pro = 40 # Min
ActiveHovering_Autel_Pro = np.arange(0, 20, 0.5) # Min

HoveringPower_Autel_Pro = energy_Autel_Pro/(HoveringTime_Autel_Pro/60) # Watts
FlightPower_Autel_Pro = energy_Autel_Pro/(FlightTime_Autel_Pro/60) # Watts

ActiveFlight_Autel_Pro = []
for t in ActiveHovering_Autel_Pro:
    HoveringConsumption = HoveringPower_Autel_Pro * (t / 60) # Wh
    ActualEnergy = energy_Autel_Pro * SafetyMargin - HoveringConsumption*PayloadConsumption

    FlightConsumption = 0
    SensorConsumption = 0
    flight_time = 0
    while (FlightConsumption*PayloadConsumption + SensorConsumption) < ActualEnergy: #Wh
        FlightConsumption = FlightPower_Autel_Pro * (flight_time/60) #Wh
        SensorConsumption = SensorsUsed * ((flight_time + t)/60) #Wh
        flight_time += 0.01
    
    ActiveFlight_Autel_Pro.append(flight_time)




# Air 2S 

energy_Air2S = 41.4 # Wh, max energy
HoveringTime_Air2S = 30 # Min
FlightTime_Air2S = 31 # Min
ActiveHovering_Air2S = np.arange(0, 20, 0.5) # Min

HoveringPower_Air2S = energy_Air2S/(HoveringTime_Air2S/60) # Watts
FlightPower_Air2S = energy_Air2S/(FlightTime_Air2S/60) # Watts

ActiveFlight_Air2S = []
for t in ActiveHovering_Air2S:
    HoveringConsumption = HoveringPower_Air2S * (t / 60) # Wh
    ActualEnergy = energy_Air2S * SafetyMargin - HoveringConsumption*PayloadConsumption

    FlightConsumption = 0
    SensorConsumption = 0
    flight_time = 0
    while (FlightConsumption*PayloadConsumption + SensorConsumption) < ActualEnergy: #Wh
        FlightConsumption = FlightPower_Air2S * (flight_time/60) #Wh
        SensorConsumption = SensorsUsed * ((flight_time + t)/60) #Wh
        flight_time += 0.01
        
    ActiveFlight_Air2S.append(flight_time)
    
x_value = 10
index = (np.abs(ActiveHovering_Mini3 - x_value)).argmin()
y_value_Mini = np.interp(x_value, ActiveHovering_Mini3, ActiveFlight_Mini3 )
y_value_Mavic = np.interp(x_value, ActiveHovering_Mavic3, ActiveFlight_Mavic3 )
y_value_Air = np.interp(x_value, ActiveHovering_Air2S, ActiveFlight_Air2S )
y_value_AutelLite = np.interp(x_value, ActiveHovering_Autel, ActiveFlight_Autel )
y_value_AutelEvo = np.interp(x_value, ActiveHovering_Autel_Pro, ActiveFlight_Autel_Pro )

# Plot the relationship between ActiveHovering and ActiveFlight
plt.plot(ActiveHovering_Mini3, ActiveFlight_Mini3, linestyle="-", label='Mini 3')
plt.plot(ActiveHovering_Mavic3, ActiveFlight_Mavic3, linestyle="--", label='Mavic 3')
plt.plot(ActiveHovering_Autel, ActiveFlight_Autel, linestyle=":", label='Autel Lite+')
plt.plot(ActiveHovering_Autel_Pro, ActiveFlight_Autel_Pro, linestyle="-.", label="Autel Evo Pro")
plt.plot(ActiveHovering_Air2S, ActiveFlight_Air2S, linestyle="--", marker='o',label="Air2S")
plt.xlabel('Active Hovering Time (min)')
plt.ylabel('Active Flight Time (min)')
print("Hovering for Mini3 for X =", x_value, "is Active flight =", y_value_Mini)
print("Hovering for Mini3 for X =", x_value, "is Active flight =", y_value_Mavic)
print("Hovering for Mini3 for X =", x_value, "is Active flight =", y_value_Air)
print("Hovering for Mini3 for X =", x_value, "is Active flight =", y_value_AutelLite)
print("Hovering for Mini3 for X =", x_value, "is Active flight =", y_value_AutelEvo)
plt.legend()
plt.grid(True)
#plt.savefig('C:/Users/mariu/BachelorOppgave\FlightTime_VN300Rugged_Garmin.png', dpi=500)
plt.show()
