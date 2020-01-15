print('=========================================================')
print('Generate Involute.')
print('Author:Liu Baishuo QQ:465942953 MAIL:liubaishuo@live.com')
print('=========================================================')

class Point():
    x, y, z = 0, 0, 0

    def plane_select(self, plane_number):
        if plane_number == 2:
            self.y, self.z = self.x, self.y
            self.x = 0
        if plane_number == 3:
            self.z, self.x = self.x, self.y
            self.y = 0

import catia_operation
import math

rb = float(input('Input the Base circle Radius:'))
n = int(input('Input the point number:'))
plane_number = float(input('Input the plane you want to draw the curve, XY input 1, YZ input 2, ZX input 3:'))
Rmin = float(input('Input the R min:'))
Rmax = float(input('Input the R max:'))
roll_angle_min = math.sqrt((Rmin * Rmin - rb * rb))/rb
roll_angle_max = math.sqrt((Rmax * Rmax - rb * rb))/rb




point_list = []
for i in range(0, n):
    point = Point()
    point_list.append(point)



for i in range(0, n):
    roll_angle = roll_angle_min + i/(n-1) * (roll_angle_max - roll_angle_min)
    point_list[i].y = rb * math.sin(roll_angle) - rb * roll_angle * math.cos(roll_angle)
    point_list[i].x = rb * math.cos(roll_angle) + rb * roll_angle * math.sin(roll_angle)
    point_list[i].plane_select(plane_number)


print('Generating...')
catia_operation.creat_spline(point_list)

#for i in point_list:
    #print(i.x, i.y, i.z)
print('OK.')
input('press enter to exit.')
