import random
import logging


class Employee:
    """
    class Employee
    method: Calculate Daily Wage of Employee
    """

    def daily_wage(self):
        """
        Function to Calculate Employee Daily Wage
        :return: Employee Daily Wages
        """
        try:
            is_present = 1
            emp_rate_per_hrs = 20
            emp_hrs = 0
            emp_check = random.randrange(0, 2)
            if emp_check == is_present:
                print("Employee is Present")
                emp_hrs = 8
            else:
                print("Employee is Absent")
                emp_hrs = 0
            emp_wage = emp_hrs*emp_rate_per_hrs
            print("Employee Wage : ", emp_wage)
        except Exception as err:
            print(err)
            logging.excption(err)


if __name__ == "__main__":
    obj_emp = Employee()
    obj_emp.daily_wage()
