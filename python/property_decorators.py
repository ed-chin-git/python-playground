class Employee:
  def __init__(self, first, last):
    self.first = first
    self.last= last
    self.email= first.lower()+'.'+last.lower()+'@email.com'
    
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

def print_emp(emp):
  print('\n'+emp.first+' '+emp.last)
  print(emp.email)

def main():
  emp_names = set()
  employees = set()

  emp_names.add(('Jim','Smith'))
  emp_names.add(('Alice','Jones'))
  emp_names.add(('Frank','Wilson'))
  emp_names.add(('Mary','Todd'))

  for emp_name in emp_names:
    emp = Employee(emp_name[0], emp_name[1])
    employees.add(emp)


  for emp in employees:
      print_emp(emp)
  
if __name__ == '__main__':
    main()
