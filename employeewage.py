import random
import logging


class Employee:
    """
    class Employee
    method: Check Attedance of Employee
    """

    def attendance(self):
        """
        Function to Check attedance of Employee
        :return: employee present or absent
        """
        try:
            is_present = 1
            emp_check = random.randrange(0, 2)
            if emp_check == is_present:
                print("Employee is Present")
            else:
                print("Employee is Absent")
        except Exception as err:
            print(err)
            logging.excption(err)


if __name__ == "__main__":
    obj_emp = Employee()
    obj_emp.attendance()
