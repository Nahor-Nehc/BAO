import math

time1, time2 = map(float, input(">> ").split()) # in x10^-9
cam1, pos1, cam2, pos2 = input(">> ").split()
cam1 = int(cam1) # type:ignore
cam2 = int(cam2) # type:ignore

radius = 0.45
camera_degrees = 360/32

def angle_from_normal(camera, position):
  return camera * camera_degrees - ( (4 - (ord(position)-64)) * camera_degrees/4)

# distance of cam1 to point
d1 = 3 * 0.1 * time1

# distance of cam2 to point
d2 = 3 * 0.1 * time2

theta1 = angle_from_normal(cam1, pos1)
theta2 = angle_from_normal(cam2, pos2)

gamma = abs(theta1 - theta2)

beta = (180 - gamma)/2

smaller_dist = d2 if theta2 < theta1 else d1

distance = ((smaller_dist**2  +  radius ** 2  -  2 * smaller_dist * radius * math.cos(math.radians(beta))) ** 0.5)

try:
  alpha = math.degrees(math.asin((smaller_dist * math.sin(math.radians(beta))) / distance))
except:
  alpha = -1 * theta1

print(round(alpha + theta1, 2), round(100 * distance, 2))

# 4 2.109622594 0.3 
# 29 C 7 A 62.23 38.15 (4)
# 5 1.303263793 1.3425 
# 22 B 11 B 181.59 21.22 (4)
# 6 0.0433505397