import application.salary as sal
import application.db.people as p
import datetime as dt

if __name__ == '__main__':
    print(dt.date.today())
    sal.calculate_salary()
    p.get_employees()
