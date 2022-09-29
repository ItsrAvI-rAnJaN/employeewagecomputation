import random
import logging


class Employee:
    """
    class Employee
    method: Calculate Daily Wage of Employee
    """

    def daily_wage(self):
        """
        Function to Calculate  Daily Wage or check Employee Working Full or Part time
        :return: Employee Daily Wages
        """
        try:
            is_part_time = 1
            is_full_time = 2
            emp_rate_per_hrs = 20
            emp_hrs = 0
            emp_check = random.randrange(0, 3)
            if emp_check == is_full_time:
                print("Employee is working Full TIme")
                emp_hrs = 8
            elif emp_check == is_part_time:
                print("Employee is working Part time")
                emp_hrs = 4
            else:
                print("Employee is Absent")

            emp_wage = emp_hrs*emp_rate_per_hrs
            print("Employee Wage : ", emp_wage)

        except Exception as err:
            print(err)
            logging.excption(err)


if __name__ == "__main__":
    obj_emp = Employee()
    obj_emp.daily_wage()
