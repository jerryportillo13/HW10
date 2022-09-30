class Employee: 
    #initialize
    def __init__(self, name, ID, dept, jobtitle, salary):\
        
        #attributes
        self.__name = name
        self.__ID = ID
        self.__dept = dept
        self.__jobtitle = jobtitle
        self.__salary = salary

    #accessors
    def get_name(self):
        return self.__name
    
    def get_ID(self):
        return self.__ID

    def get_dept(self):
        return self.__dept

    def get_jobtitle(self):
        return self.__jobtitle

    def get_salary(self):
        return self.__salary

    


