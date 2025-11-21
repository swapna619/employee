#test employee.py
import pytest
from employee import get_employee_info
def test_get_employee_info():
    #sample data
    name = "Alice Smith"
    emp_id = "E202"
    department = "HR"
    salary = 60000
    #expected result
    expected_output = (
        "Employee Name:Alice Smith\n"
        "Employee ID:E202\n"
        "Department:HR\n"
        "Salary:60000"
    )
 #Assertion
    assert get_employee_info(name, emp_id, department, salary) == expected_output