#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import sys
import time
import wiringpi2 as wiringpi

# Set which GPIO pins the drive outputs are connected to
DRIVE_1 = 7     # GPIO 4
DRIVE_2 = 1     # GPIO 18
DRIVE_3 = 10    # GPIO 8
DRIVE_4 = 11    # GPIO 7


# Map of functions to drive pins
leftDrive = DRIVE_1                     # Drive number for left motor
rightDrive = DRIVE_4                    # Drive number for right motor
penDrive = DRIVE_3                      # Drive number for pen solenoid

# my adaptation based on forum post and leftward tracking!!!
# Set the drive power for both motors, 1 to 100
leftDriveLevel  = 100                    # PWM drive for the left motor when on
rightDriveLevel = 74                   # PWM drive for the right motor when on

# Setup the software PWMs for 0 to 100
wiringpi.wiringPiSetup()
wiringpi.softPwmCreate(leftDrive, 0, 100)
wiringpi.softPwmWrite(leftDrive, 0)
wiringpi.softPwmCreate(rightDrive, 0, 100)
wiringpi.softPwmWrite(rightDrive, 0)

# Setup the solenoid drive pin
wiringpi.pinMode(penDrive, 1)           # Set as an output pin

# Functions for the robot to perform
def MoveForward(n):
    """Move forward for 'n' seconds"""
    wiringpi.softPwmWrite(leftDrive, leftDriveLevel)
    wiringpi.softPwmWrite(rightDrive, rightDriveLevel)
    time.sleep(n)
    wiringpi.softPwmWrite(leftDrive, 0)
    wiringpi.softPwmWrite(rightDrive, 0)

def MoveLeft(n):
    """Move left for 'n' seconds"""
    wiringpi.softPwmWrite(leftDrive, leftDriveLevel)
    wiringpi.softPwmWrite(rightDrive, 0)
    time.sleep(n)
    wiringpi.softPwmWrite(leftDrive, 0)

def MoveRight(n):
    """Move right for 'n' seconds"""
    wiringpi.softPwmWrite(leftDrive, 0)
    wiringpi.softPwmWrite(rightDrive, rightDriveLevel)
    time.sleep(n)
    wiringpi.softPwmWrite(rightDrive, 0)

def PenUp(n):
    """Lift the pen up"""
    wiringpi.digitalWrite(penDrive, 0)

def PenDown(n):
    """Place the pen down"""
    wiringpi.digitalWrite(penDrive, 1)

def HelpMessage(n):
    """Display a list of available commands"""
    print ''
    print 'Available commands:'
    commands = dCommands.keys()
    commands.sort()
    for command in commands:
        print '% 10s - %s, %s' % (command, dCommands[command].func_name, dCommands[command].__doc__)
    print ''

# Map of command names to functions
dCommands = {
        'FORWARD':MoveForward,
        'FD':MoveForward,
        'LEFT':MoveLeft,
        'LT':MoveLeft,
        'RIGHT':MoveRight,
        'RT':MoveRight,
        'PENUP':PenUp,
        'PU':PenUp,
        'PENDOWN':PenDown,
        'PD':PenDown,
        'HELP':HelpMessage,
        '?':HelpMessage
        }

# If we have been run directly then look at command line
if __name__ == "__main__":
    # Process command
    if len(sys.argv) > 1:
        # Extract the command name and value (if there is any)
        command = sys.argv[1].upper()
        if len(sys.argv) > 2:
            sValue = sys.argv[2].upper()
        else:
            sValue = '0'
        try:
            fValue = float(sValue)
        except:
            fValue = 0.0
    
        # Select the appropriate function and call it
        if dCommands.has_key(command):
            dCommands[command](fValue)
        else:
            print 'Command "%s" not recognised' % (command)
            HelpMessage(fValue)
    else:
        # No command, display the help message
        print 'Usage: %s command [n]' % (sys.argv[0])
        HelpMessage(0)

    
