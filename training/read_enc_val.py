import serial

def listen_to_serial(port, baudrate=115200):
    try:
        # Open the serial port
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Listening to {port} at {baudrate} baudrate. Press Ctrl+C to stop.")

        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            # Print the received data
            print(str(line))

    except serial.SerialException as e:
        print(f"Error: {e}")

    finally:
        if ser.is_open:
            ser.close()
            print("Serial port closed.")

# Replace 'COM3' with the appropriate serial port on your system
# You can find the port in the Arduino IDE or your operating system's device manager.
listen_to_serial('COM4')
