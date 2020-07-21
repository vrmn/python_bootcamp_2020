stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100) ]

for item in stock_prices:

      print(item)

Output
('APPL', 200)
('GOOG', 400)
('MSFT', 100)


for ticker, price in stock_prices:

      print(ticker)

output
APPL
GOOG
MSF


-------------------

work_hours = [('abby', 100), ('Billy', 400), ('cassie', 800)]


def employee_check(work_hours):

      current_max = 0                   #ask yourself what you intend to return. In this case its a tuple with employee_of_month and current_max
      employee_of_month = ''

      for employee, hours in work_hours:
              if hours > current_max:
                    current_max = hours
                    employee_of_month = employee
              else:
                    pass



      return(employee_of_month, current_max)

result = employee_check(work_hours)    you can store as a tuple
result
output ('cassie', 800)


name, hours = employee_check(work_hours)     or you can do tuple unpacking

name
output cassie

hours
output 800
