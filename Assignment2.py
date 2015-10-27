"""
This Python program computes the amount of pollutant in each of 3 ponds due to a chemical spill at each minute of the
simulation. It takes user input and outputs hourly pollutant level reports, and final pollutant reports and
percent pollutant per pond via shade in a GUI. Console reports can be used to test data and unrounded values.

Author: Henry He
Student #: 250869172
Course: CS1026A, Assignment 2
Instructor: Jordan van Dyk
Language: Python 3.4

"""

from graphics import GraphicsWindow

win = GraphicsWindow(500, 1000)
canvas = win.canvas()


#Test Data for Reference

# TIME = 1440 #minutes, or 24 hours
# POLLUTANT_RATE_INTOPOND1 = 0.125 # liters per minute
# MAX_POLLUTANT = 40 #liters

FLOW_RATE = 0.005 #liters per minute, Global Constant


def totalpollutant(t, spillRate): #total totalpollutant spilled into Pond 1
    pollutant = spillRate * t
    return pollutant

def pond1(x1, x3, spillRate): #pollution in pond 1 (L)
    x1 = x1 + spillRate + x3 * FLOW_RATE - x1 * FLOW_RATE
    return x1

def pond2(x1, x2): # pollution in pond 2 (L)
    x2 = x2 + x1 * FLOW_RATE - x2 * FLOW_RATE
    return x2

def pond3(x2, x3): #pollution in pond 3 (L)
    x3 = x3 + x2 * FLOW_RATE - x3 * FLOW_RATE
    return x3

def stringRound(number):

    n = str(round(number, 2))

    return n

def hourlyreport(xHourly, yHourly, t, x1, x2, x3, pollutant, n):

    canvas.drawText(xHourly, yHourly + n, "time: " + str(t) + "min")
    n += 10
    canvas.drawText(xHourly, yHourly + n, "  x1: " + stringRound(x1) + "L")
    n += 10
    canvas.drawText(xHourly, yHourly + n, "  x2: " + stringRound(x2) + "L")
    n += 10
    canvas.drawText(xHourly, yHourly + n, "  x3: " + stringRound(x3) + "L")
    n += 10
    canvas.drawText(xHourly, yHourly + n, "  pollutant: " + stringRound(pollutant) + "L")
    n += 10

    return n

def finalcanvas(xHourly, yHourly, x1, x2, x3, pollutant, r, t, max, spillRate, fulltime):


    #Percentage calculations for each pond

    perA = x1 / pollutant * 100
    perB = x2 / pollutant * 100
    perC = x3 / pollutant * 100


    #Pondinating shade of pond with percentage
    a = int(255 - ((x1 / pollutant) * 255))
    b = int(255 - ((x2 / pollutant) * 255))
    c = int(255 - ((x3 / pollutant) * 255))

    #Pond Headers Canvas

    xPond = xHourly - 80
    yPond = yHourly - 300


    canvas.drawText(xPond, yPond - 70, "POND POLLUTANT SIMULATOR 2000")
    canvas.drawText(xPond, yPond - 50, "a visual of how much pollutant spilled flows to each pond")
    canvas.drawText(xPond, yPond - 40, "and the effect of human disturbance on an ecosystem over time")

    canvas.drawText(xPond, yPond, "Pond 1 (x1): " + stringRound(x1) + "L")
    canvas.drawText(xPond, yPond + 10, stringRound(perA) + "%")

    canvas.drawText(xPond + 150, yPond + 230, "Pond 2 (x2): " + stringRound(x2) + "L")
    canvas.drawText(xPond + 150, yPond + 240, stringRound(perB) + "%")

    canvas.drawText(xPond + 300, yPond, "Pond 3 (x3): " + stringRound(x3) + "L")
    canvas.drawText(xPond + 300, yPond + 10, stringRound(perC) + "%")

    #PondCirlces and Arrows Canvas

    canvas.setColor(a, a, a)
    canvas.drawOval(xPond, yPond + 20, r, r)
    canvas.drawArrow(xPond + r, yPond + 20 + (r/2), xPond + 150, yPond + 120 + (r/2))

    canvas.setColor(b, b, b)
    canvas.drawOval(xPond + 150, yPond + 120, r, r)
    canvas.drawArrow(xPond + 150 + r, yPond + 120 + (r/2), xPond + 300, yPond + 20 + (r/2))

    canvas.setColor(c, c, c)
    canvas.drawOval(xPond + 300, yPond + 20, r, r)
    canvas.drawArrow(xPond + 300, yPond + 20 + (r/2), xPond + r, yPond + 20 + (r/2))

    canvas.setColor("yellow")
    canvas.drawPolygon(xPond + 10, yPond + 60, xPond + 20, yPond + 50, xPond + 30, yPond + 60, xPond + 20, yPond + 70)
    canvas.setColor("black")
    canvas.drawArrow(xPond - 20, yPond + 60, xPond + 20, yPond + 60)

    # canvas.setTextFont("helvetica", 30, "normal")

    #Final Results Console Display

    print("final results")
    print("time: ", t)
    print("  x1: ", x1)
    print("  x2: ", x2)
    print("  x3: ", x3)
    print("  pollutant: ", pollutant)

    #Final Results Canvas Display

    xFinal = xHourly + 150

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
    max = input("Please enter the maximum amount of pollutant (L): ").strip()
    while not max.isdigit() or int(max) > 0:
        print("Positive values only for max pollutant please")
        max = input("Please enter the maximum amount of pollutant (L): ").strip()

    return float(max)

def getSpillRate():
    spillRate = input("Please enter the rate at which the pollutant is leaking (L/min): ").strip()
    while not spillRate.isdigit() or int(spillRate) > 0:
        print("Positive values only for spill rate please")
        spillRate = input("Please enter the rate at which the pollutant is leaking (L/min): ").strip()

    return float(spillRate)

def getFulltime():
    fulltime = input("Please enter the number of minutes to run the sim: ").strip()
    while not fulltime().isdigit() or int(fulltime()) > 0:
        print("Positive numbers only for time please")
        fulltime = input("Please enter the number of minutes to run the sim: ").strip()

    return float(fulltime)

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
    print("time: ", t)
    print("  x1: ", x1)
    print("  x2: ", x2)
    print("  x3: ", x3)
    print("  pollutant: ", pollutant)
    t += 1


    xHourly = 130 # coordinates of hourly report, upon which all other coordinates are based. Change these to shift the whole canvas
    yHourly = 400
    r = 100 # diameter of pond circles canvas
    n = 20 #counter for while loop canvas


    canvas.drawText(xHourly, yHourly, "Hourly Report") #need to do this outside of while loop

    while t <= fulltime and pollutant < max: # while stop conditions are satisfied

        #calling indiv pond functions
        x1 = pond1(x1, x3, spillRate)
        x2 = pond2(x1, x2)
        x3 = pond3(x2, x3)
        pollutant = totalpollutant(t, spillRate)

        if t % 60 == 0: # controls number of minutes per hourly report

            #Hourly Report Console
            print("time: ", t)
            print("  x1: ", x1)
            print("  x2: ", x2)
            print("  x3: ", x3)
            print("  pollutant: ", pollutant)

            #Hourly Report Canvas

            n = hourlyreport(xHourly, yHourly, t, x1, x2, x3, pollutant, n) #update n as it prints down the canvas

        t += 1 # calculates values for each minute

    t -= 1 # undo final result t value

    finalcanvas(xHourly, yHourly, x1, x2, x3, pollutant, r, t, max, spillRate, fulltime) # canvas function

main()

win.wait()
