# PROGRAMMER: Paul Gonzales
# DATE: month day, 2019
# ASSIGNMENT: Homework 06
# ALGORITHM: How the program works.  This should be structured using short, descriptive phrases that are indented appropriately.

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
    print("Length of Job: " + str(workhrs) + "hrs")
    print("Cost of Labor: $" + str(laborcost/100))
    print("Gallons of Paint: " + str(gallons))
    print("Cost of Paint: $" + str(paintcost/100))
    print("Project Total: $" + str(projectcost/100))

    return None

if __name__ == "__main__":
    main()