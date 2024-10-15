# Hearbeat Sensor MESA ❤️

## Atholton's Wearable Tech: "Breath Catcher"

Using Adafruit's Circuit Playground Express as well as sublanguage CircuitPython, we've made a program to monitor respiratory and heartbeat rates from a model baby. 

Requirements for the design include: 

* **capable of displaying respiration rate (i.e., breaths per minute) in a way that is intuitive for parents, childcare providers, and health care professionals to understand.**
* suitable for use on an infant (i.e., would not cause discomfort or injury to an infant).
* easily placed on and removed from an infant.
* adjustable to allow appropriate fit on different sizes of infants.
* able to stay in place and continue monitoring respiration during normal infant movements like squirming, rolling, and being lifted by a caregiver.
* durable, reusable, and aesthetically pleasing.

With this in mind the software team hypothesized a solution to measure heart rate without causing discomfort and came to the conclusion that utilizing the circuits accelerometer would be the best solution. 

## How it works

The code utilizes the built in accelerometer on the CPX, specifically the z-axis to measure the vertical movement of the baby's chest as the respiration and cardiac cycle proceed.

There are 3 main distinctions in the code: 

* If the LEDs are red, that means the respiratory/cardiac rate are higher than the standard average.
* If the LEDS are green, that means the respiratory/cardiac rate are at normal levels.
* If the LEDs are yellow, that means the respiratory/cardiac rate are below the standard average.

