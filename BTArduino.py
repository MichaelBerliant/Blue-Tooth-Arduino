import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

arduino_port = '/dev/cu.HC-05'  # Modify this according to your system
baud_rate = 115200  # Must match the baud rate in your Arduino code
ser = serial.Serial(arduino_port, baud_rate)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x, y)

z = np.abs(x)

ax.plot_surface(x, y, z, color='blue')

ax.axis('off')

elev = 0
azim = 90
roll = 90

ax.view_init(elev, azim, roll)
plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))

plt.draw()
plt.pause(0.001)

while True:
    if ser.in_waiting > 0:
        _x = ser.readline().decode().rstrip()
        _y = ser.readline().decode().rstrip()
        _z = ser.readline().decode().rstrip()

        x_value = float(_x)
        y_value = float(_y)
        z_value = float(_z)

        elev = x_value
        azim = y_value
        roll = z_value

        ax.view_init(elev, azim, roll)
        plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))

        plt.draw()
        plt.pause(0.001)

ser.close()
