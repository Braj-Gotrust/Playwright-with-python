class Employee:
    def __init__(self,eid, ename, esalary):
        self.eid = eid
        self.ename = ename
        self.esalary = esalary
    def displayEmp(self):
        print("empid:{} empname:{} empsalary:{}".format(self.eid, self.ename, self.esalary))