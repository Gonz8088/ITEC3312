# PROGRAMMER: Paul Gonzales
# DATE: March 6, 2019
# ASSIGNMENT: Homework 06
# ALGORITHM: The user is prompted to enter the number of square feet of wall.
# The user is then prompted to enter the cost of a gallon of paint. The estimated
# hours of work, paint needed, cost of paint, cost of labor, and project
# are calculated with their respective functions.

def labor_hrs(sqft):
    """Current estimate of time needed is:
    7 hours / per 112 sqft
    """
    hours, area = 7, 112
    return (sqft/area) * hours

def gallons_paint(sqft):
    """Returns
    Current estimate of paint needed is:
    1 gallon / per 112 sqft
    """
    gallons, area = 1, 112
    return (sqft/area) * gallons

def paint_cost(gallons, cost_per):
    """Returns cost of paint"""
    return (gallons * cost_per)

def labor_cost(work_hours):
    """Returns cost of labor"""
    labor_rate = 4000 # unit is in 1 hundreths of dollar
    return work_hours * labor_rate

def project_cost(paint, labor):
    """Returns cost of project"""
    return paint + labor

def main():
    squareft = int(input("Enter Square Feet of Wall: "))
    # unit cost is in 1 hundreths of dollar
    unit_cost = (int(input("Enter Cost of Paint Can: "))) * 100

    workhrs = labor_hrs(squareft)
    gallons = gallons_paint(squareft)

    paintcost = paint_cost(gallons, unit_cost)
    laborcost = labor_cost(workhrs)
    projectcost = project_cost(paintcost, laborcost)

    print("\n --- Work/Cost Estimate --- \n \n")
    print("Length of Job: " + str(format(workhrs, '.2f')) + "hrs")
    print("Cost of Labor: $" + str(format(laborcost/100, '.2f')))
    print("Gallons of Paint: " + str(format(gallons, '.2f')))
    print("Cost of Paint: $" + str(format(paintcost/100, '.2f')))
    print("Project Total: $" + str(format(projectcost/100, '.2f')))

    return

if __name__ == "__main__":
    main()
