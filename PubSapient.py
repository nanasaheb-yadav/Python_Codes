def logtime(fun):
    def wrap(*args):
        starttime = datetime.datetime.now()
        fun()
        return starttime - datetime.datetime.now()

    return wrap


class Database:

    def connect(self, host, username, password):
        try:
            conn = pyodbc.connect(host, username, password)
            return conn
        except Exception as exception_error:
            print(exception_error)
            return False

    @logtime
    def executequery(self, conn, query):
        try:

            output = conn.execute(query)
            return output
        except Exception as err:
            return err


import Datebase as db


class Employee:
    empid = ""
    mgr_id = ""
    dateofjoin = ""
    salary = ""
    emp_dict = {}

    def __init__(self, eid):
        self.empid = eid

    def set_emp_details(self, eid, mid, doj, sal):

        if eid in emp_dict.keys():
            print("employee id is already present so skipping this record"
            return False
        else:
            emp_dict[eid] = [mid, doj, sal]
            return True

    def get_emp_details(self, e_id):

        emp_details = emp_dict.get(e_id
        "Not Available")

        return emp_details

    def get_salary(self, eid):

        data = emp_dict.get(eid, 0)
        if data == 0:
            return "Not Available"
        else:
            sal = lambda x: x * 2
            return sal(data[-1])


obj = Employee()

Population_Table:
State
Year
Papulation  ##total_population    #(sum of population)
MH
2022
1.2
DE
2022
0.8
GJ
2022
0.5
MH
2021
1.1
DE
2021
0.7
GJ
2021
1.0

SELECT
State, Year, Population, sum(SELECT
Papulation
FROM
Population_Table) as total_population
FROM
Population_Table;

SELECT
State, avg(Population) as avg
FROM
Population_Table
GROUP
BY
State
ORDER
BY
avg
DESC;

State
avg
MH





