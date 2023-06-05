# TASK 1 :- Here is the SQL query that fetches the top 3 departments along with their names and 
# average monthly salaries:

    SELECT d.NAME AS DEPT_NAME, AVG(s.AMT) AS AVG_MONTHLY_SALARY
    FROM Departments d
    JOIN Employees e ON d.DepartmentID = e.`DEPT ID`
    JOIN Salaries s ON e.ID = s.EMP_ID
    GROUP BY d.DepartmentID, d.NAME
    ORDER BY AVG_MONTHLY_SALARY DESC
    LIMIT 3;

    #EXPLAINATION :- The query joins the three tables based on the appropriate foreign key relationships, calculate the 
    #average salary using the AVG() function, groups the result by department, and sorts it in descending order of 
    #average monthly salary. Finally, the LIMIT clause the result to the top 3 departments.


# TASK 2 :- PYTHON CODE for the same above output.

    import csv


    # Define the file paths for the CSV files
    departments_file = 'departments.csv'
    employees_file = 'employees.csv'
    salaries_file = 'salaries.csv'

    # Create dictionaries to store department names and total salaries
    department_salaries = {}




    # Read departments data
    with open(departments_file, 'r') as file:
        departments_reader = csv.reader(file)
        next(departments_reader)                                    # Skip header row
        for row in departments_reader:
            department_id = int(row[0])
            department_name = row[1]
            department_salaries[department_id] = [department_name, 0]



    # Read salaries data and calculate total salaries for each department
    with open(salaries_file, 'r') as file:
        salaries_reader = csv.reader(file)
        next(salaries_reader)                                       # Skip header row
        for row in salaries_reader:
            employee_id = int(row[0])
            month = int(row[1][4:])                                 # Extract the month from the YYYYMM format
            amount = int(row[2])
            department_id = None

            with open(employees_file, 'r') as emp_file:
                employees_reader = csv.reader(emp_file)
                next(employees_reader)                              # Skip header row
                for emp_row in employees_reader:
                    if int(emp_row[0]) == employee_id:
                        department_id = int(emp_row[2])
                        break

            if department_id is not None:
                if department_id in department_salaries:
                    department_salaries[department_id][1] += amount



    # Sort departments based on total salaries and fetch the top 3
    sorted_departments = sorted(department_salaries.items(), key=lambda x: x[1][1], reverse=True)
    top_departments = sorted_departments[:3]



    # Print the report
    print("DEPT_NAME")
    print("AVG_MONTHLY_SALARY (USD)")
    for dept_id, (dept_name, total_salary) in top_departments:
        avg_salary = total_salary // 12                               # Assuming salaries are given on a monthly basis
        print(dept_name)
        print(avg_salary)
        print()


    #Explaination :- Firstly, save the CSV files (departments.csv, employees.csv & salaries.csv ) in the same directory as 
    #the script. Script read the data from each CSV file, calculates the total salaries for each department, sorts the 
    #departments base on total salaries, and print the top 3 departments along with their average monthly salaries.


#TASK 3 :- Debugging in PYTHON SCRIPT

    def compute(n):
    if n < 10:
    out = n ** 2
    elif n < 20:
    out = 1
    for i in range(1, n-10+1): # Added +1 to include n-10 in the loop 
    range
    out *= i
    else:
    lim = n - 20 + 1 # Added +1 to the code 
    out = lim * lim
    out = out - lim
    out = int(out / 2) # Converted the result to an integer
    print(out)
    n = int(input("Enter an integer: "))
    compute(n)

    #Explaination :- The bug is fixed by adding +1 to the loop range in the elif block to include the value n-10, added +1 
    # to the lim value and converting the result to an integer in the else block to match the expected output