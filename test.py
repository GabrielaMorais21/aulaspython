import math 
signal_power = noise_power = 5
ratio = signal_power / noise_power
decibels = 10 * math.sin(ratio)
radians = 0.7
heigth = math.sin(radians)