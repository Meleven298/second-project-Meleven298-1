from backend.classes.Company import Company
from backend.classes.Employee import Employee

class StaffOperations:
    '''Класс операций над персоналом.'''

    def fire_employee(self, employee: Employee, employee_list: list[Employee]) -> Employee:
        '''Уволить сотрудника.
        
        Args:
            employee: Рабочий.
            employee_list: Список рабочих.

        Returns:
            fired_employee: Уволенный сотрудник.
        '''

        for i, emplo in enumerate(employee_list):
            if employee.id == emplo.id:
                fired_employee = employee_list.pop(i)
                
        return fired_employee

    def hire_employee(self, employee: Employee, employee_list: list[Employee]) -> None:
        '''Уволить сотрудника.
        
        Args:
            employee: Рабочий.
            employee_list: Список рабочих.
        '''

        position = input('Должность нового сотрудника? ')
        
        employee = Employee(position)
        employee_list.append(employee)

    def change_header(self, company: Company, new_header: str) -> None:
        '''Функция смены ответственного лица.
        
        Args:
            company: Компания.
            new_header: Имя нового ответственного лица.
        '''

        company.set_header(new_header)

        print('Ответственное лицо сменено')
    