'''Records measurments to a given file. Usage example:

$ ./record_measurments.py out.txt'''
import sys
from rplidar import RPLidar


PORT_NAME = 'com4'


def run(path='output.txt'):
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    outfile = open(path, 'w')
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for measurment in lidar.iter_measures():
        #     line = '\t'.join(str(v) for v in measurment)
        #     outfile.write(line + '\n')
            boolean, quality, angle, distance = measurment  # Unpack values here
            if distance!=0.0 and 240 < int(angle) < 300:
                print(distance)
    except KeyboardInterrupt:
        print('Stopping.')
    lidar.stop()
    lidar.disconnect()
    outfile.close()

if __name__ == '__main__':
    run('output.txt')