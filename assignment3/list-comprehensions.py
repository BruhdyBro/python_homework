import csv
import traceback

def read_employees():
    employees = list()
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                employees.append(f"{row[1]} {row[2]}")

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
print(employees)
sorted = list(filter((lambda x: "e" in x), employees))
print(sorted)