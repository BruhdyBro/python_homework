import csv
import traceback
import os
import custom_module
from datetime import datetime


# Task 2
def read_employees():
    employees = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            employees['fields'] = next(reader)
            while True:
                try:
                    rows.append(next(reader))
                except StopIteration:
                    break
            
            
            employees['rows'] = rows

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}") 

    return employees

employees = read_employees()


# Task 3
def column_index(input):
    
    try:
        return employees["fields"].index(input)
    except AttributeError:
        return -1
    
employee_id_column = column_index("employee_id")


# Task 4
def first_name(rowNum):
    index = column_index("first_name")

    try:
        return employees["rows"][rowNum][index]
    except KeyError:
        return "Name not in list."
    


# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    return list(filter(employee_match, employees["rows"]))


# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches


# Task 7
def sort_by_last_name():
    
    index = column_index("last_name")
    employees["rows"].sort(key= lambda row: row[index])

    return employees["rows"]

employees["rows"] = sort_by_last_name()


# Task 8
def employee_dict(row):
    employee = {}
    i = 0
    for header in employees["fields"]:
        employee[header] = row[i]
        i += 1
    employee.pop("employee_id", None)

    return employee
    

# Task 9
def all_employees_dict():

    all_employees = {}

    tEmployees = read_employees()
    for employee in tEmployees["rows"]:
        all_employees[employee[0]] = employee_dict(employee)

    return all_employees


# Task 10
#Create env variable in terminal: $env:THISVALUE = "ABC"
def get_this_value():
    return os.getenv("THISVALUE")


# Task 11
def set_that_secret(secret_to_set):
    custom_module.set_secret(secret_to_set)

set_that_secret("Testing123")


# Task 12
def read_minutes():

    def reader(minutesNum):
        minutes = {}
        rows = []
        try:
            with open(f'../csv/minutes{minutesNum}.csv', 'r') as file:
                reader = csv.reader(file)
                minutes['fields'] = tuple(next(reader))
                while True:
                    try:
                        rows.append(tuple(next(reader)))
                    except StopIteration:
                        break
                
                
                minutes['rows'] = rows

        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}") 

        return minutes
    
    v1 = reader(1)
    v2 = reader(2)

    return v1, v2
global minutes1, minutes2 
minutes1, minutes2 = read_minutes()


# Task 13
def create_minutes_set():
    
    v3 = set(minutes1["rows"])
    v4 = set(minutes2["rows"])

    v5 = v3.union(v4)
    return v5

global minutes_set
minutes_set = create_minutes_set()


# Task 14
def create_minutes_list():
    
    minutes_to_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))

    return minutes_to_list 

global minutes_list
minutes_list = create_minutes_list()


# Task 15
def write_sorted_list():
    minutes_list.sort(key= lambda x: x[1])
    minutes_to_map = map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list)
    back_to_list = []
    try:
        with open('minutes.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            for data in minutes_to_map:
                try:
                    back_to_list.append(data)
                    writer.writerow(data)
                except StopIteration:
                    break
        
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    return back_to_list

write_sorted_list()