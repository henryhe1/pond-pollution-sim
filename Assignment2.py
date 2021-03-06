"""
This Python program simulates the amount of pollutant in each of 3 ponds due to a chemical spill at each minute of time.
It takes user input (validated) and outputs hourly pollutant level reports, final pollutant reports and
a pollution line graph for each pond. Console reports can be used to test data and unrounded values. graphics and
plotpoints modules are used.

Author: Henry He
Student #: 250869172
Course: CS1026A, Assignment 2
Instructor: Jordan van Dyk
Language: Python 3.4
Date modified: October 28, 2015

"""

from graphics import GraphicsWindow
from plotpoints import createGrid
from plotpoints import drawDots

win = GraphicsWindow(1000, 500)
canvas = win.canvas()
createGrid(canvas, 1400, 1400)


#Test Data for Reference

# TIME = 1440 #minutes, or 24 hours
# POLLUTANT_RATE_INTOPOND1 = 0.125 # liters per minute
# MAX_POLLUTANT = 40 #liters

FLOW_RATE = 0.005 #liters per minute, Global Constant


def totalpollutant(pollutant, spillRate, t): #total totalpollutant spilled into Pond 1
    if t == 0:
        return 0
    else:
        pollutant += spillRate
        return pollutant

def pond1(x1, x3, spillRate, t): #pollution in pond 1 (L)
    if t == 0:
        return 0
    else:
        x1 = x1 + FLOW_RATE * x3 - FLOW_RATE * x1 + spillRate # x1t = x1t-1 + Inflow3t-1 – Outflow2t-1 + LeakRatet
        return x1

def pond2(x1, x2, t): # pollution in pond 2 (L)
    if t == 0 or t == 1:
        return 0
    else:
        x2 = x2 + FLOW_RATE * x1 - FLOW_RATE * x2
        return x2

def pond3(x2, x3, t): #pollution in pond 3 (L)
    if t == 0 or t == 1 or t == 2:
        return 0
    else:
        x3 = x3 + FLOW_RATE * x2 - FLOW_RATE * x3
        return x3

def stringRound(number):

    n = str(round(number, 2)) # round a number to two dec places and cast it to a string.

    return n

def hourlyreport(xHourly, yHourly, t, x1, x2, x3, pollutant, n):

    canvas.setColor("black")

    canvas.drawText(xHourly, yHourly + n, "time: " + str(t) + "min")
    n += 10 #next line canvas
    canvas.drawText(xHourly, yHourly + n, "  x1: " + stringRound(x1) + "L")
    n += 10
    canvas.drawText(xHourly, yHourly + n, "  x2: " + stringRound(x2) + "L")
    n += 10
    canvas.drawText(xHourly, yHourly + n, "  x3: " + stringRound(x3) + "L")
    n += 10
    canvas.drawText(xHourly, yHourly + n, "  pollutant: " + stringRound(pollutant) + "L")
    n += 10

    return n

def finalcanvas(xHourly, yHourly, x1, x2, x3, pollutant, t, max, spillRate, fulltime):

    canvas.setColor("Black")
    canvas.setTextFont("helvetica", 30, "normal")

    canvas.drawText(xHourly-310, yHourly - 40, "POND POLLUTANT SIMULATOR 2000")
    canvas.drawText(xHourly-330, yHourly - 30, "a visual of how pollutant in each pond over time")
    canvas.drawText(xHourly-315, yHourly - 20, "blue=pond1, green=pond2, red=pond3")

    #Final Results Console Display

    print("final results")
    print("time: ", t)
    print("  x1: ", x1)
    print("  x2: ", x2)
    print("  x3: ", x3)
    print("  pollutant: ", pollutant)

    #Final Results Canvas Display

    xFinal = xHourly + 100

    canvas.drawText(xFinal, yHourly, "Final Report")
    canvas.drawText(xFinal, yHourly + 20, "time: " + str(t) + "min")
    canvas.drawText(xFinal, yHourly + 30, "  x1: " + stringRound(x1) + "L")
    canvas.drawText(xFinal, yHourly + 40, "  x2: " + stringRound(x2) + "L")
    canvas.drawText(xFinal, yHourly + 50, "  x3: " + stringRound(x3) + "L")
    canvas.drawText(xFinal, yHourly + 60, "  pollutant: " + stringRound(pollutant) + "L")

    #Inputs Canvas Display
    canvas.setFill()
    canvas.setOutline("black")
    canvas.drawRect(xFinal - 5, yHourly + 95, 120, 90)
    canvas.drawText(xFinal, yHourly + 100, "Inputs and Constants")
    canvas.drawText(xFinal, yHourly + 120, "  max pollutant: " + str(max) + "L")
    canvas.drawText(xFinal, yHourly + 130, "  leak rate: " + str(spillRate) + "L/min")
    canvas.drawText(xFinal, yHourly + 140, "  sim time: " + str(fulltime) + "min")
    canvas.drawText(xFinal, yHourly + 150, "  interpond flow rate: ")
    canvas.drawText(xFinal, yHourly + 160, "    " + str(FLOW_RATE) + "L/min")

def getMax():

    while True:
        try:
            max = float(input("Please enter the maximum amount of pollutant (L): ").strip())
            while max <= 0:
                print("Positive values only for max pollutant please")
                max = float(input("Please enter the maximum amount of pollutant (L): ").strip())
            return max
            break

        except ValueError:
            print("Numbers only please.")

def getSpillRate():

    while True:
        try:
            spillRate = float(input("Please enter the rate at which the pollutant is leaking (L/min): ").strip())
            while spillRate <= 0:
                print("Positive values only for spill rate please")
                spillRate = float(input("Please enter the rate at which the pollutant is leaking (L/min): ").strip())
            return spillRate
            break

        except ValueError:
                print("Numbers only please.")

def getFulltime():

    while True:
        try:
            fulltime = float(input("Please enter the number of minutes to run the sim: ").strip())
            while fulltime <= 0:
                print("Positive numbers only for time please")
                fulltime = float(input("Please enter the number of minutes to run the sim: ").strip())
            return fulltime
            break

        except ValueError:
                print("Numbers only please.")

def main():

    # User Input
    max = getMax()
    spillRate = getSpillRate()
    fulltime = getFulltime()

    #initial values at t=0
    t = 0
    x1 = 0
    x2 = 0
    x3 = 0
    pollutant = 0

    xHourly = 470 # coordinates of hourly report, upon which all other coordinates are based. Change these to shift the whole canvas
    yHourly = 50
    n = 20 # counter for while loop canvas hourly report

    canvas.drawText(xHourly, yHourly, "Hourly Report") #need to do this outside of while loop

    while t <= fulltime: # while stop conditions are not satisfied

        #calling indiv pond functions
        x1 = pond1(x1, x3, spillRate, t)
        x2 = pond2(x1, x2, t)
        x3 = pond3(x2, x3, t)
        pollutant = totalpollutant(pollutant, spillRate, t)

        #Plot functions
        drawDots(canvas, t, 1500, x1, 25, "blue")
        drawDots(canvas, t, 1500, x2, 25, "green")
        drawDots(canvas, t, 1500, x3, 25, "red")

        if t % 60 == 0: # controls number of minutes per hourly report

            #Hourly Report Console
            print("time: ", t)
            print("  x1: ", x1)
            print("  x2: ", x2)
            print("  x3: ", x3)
            print("  pollutant: ", pollutant)

            #Hourly Report Canvas

            if n >= 400: #canvas shift over one column
                n = 0
                xHourly += 100

            n = hourlyreport(xHourly, yHourly, t, x1, x2, x3, pollutant, n) #update n as it prints down the canvas

        if pollutant >= max:
            spillRate = 0

        t += 1 # calculates values for each minute

    t -= 1 # undo final result t value

    finalcanvas(xHourly, yHourly, x1, x2, x3, pollutant, t, max, spillRate, fulltime) # canvas function

main()

win.wait()
