Drone Side Stack


High Level: Arudpilot and PX4

Middle Level: flight controller hardware (pixhawk, raspberrypi)

Lower level: Drone hardware


The software in the loop runs a simulation and this simulation takes care of the middle level and lower level items

The same code you use in the SITL can be used in a real drone




-----------------------------

communication layer( middleware)

Mavlink - just standard collection of messages


-----------------------------

Ground control station

GCS software: APM planner( mission planner) Q ground control. pretty much gui that utilize the mavlink protocol. So there could be a

GCS Hardware: Telemetry module
