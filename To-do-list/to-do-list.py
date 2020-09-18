from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, String
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

class Task(Base):
    __tablename__ = 'task'
    id = Column("id", Integer, primary_key=True)
    task = Column("task", String, default='default_value')
    deadline = Column("deadline", Date, default=datetime.today())


def week_task():
    week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
            4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    today = datetime.today()
    for i in range(7):
        week_day = week[today.weekday()]
        day = today.day
        month = today.strftime('%b')
        print(f'{week_day} {day} {month}:')
        rows = session.query(Task).filter(Task.deadline == today.date()).all()
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for row in rows:
                print(f"%d. %s. {day} {month}" % (row.id, row.task))
        today += timedelta(days=1)
        print()


def all_task():
    print("All tasks:")
    rows = session.query(Task).all()
    if len(rows) == 0:
        print("Nothing to do!")
    else:
        rows = session.query(Task).order_by(Task.deadline).all()
        for row in rows:
            day = row.deadline.day
            month = row.deadline.strftime('%b')
            print(f"%d. %s. {day} {month}" % (row.id, row.task))


def missed_task():
    rows = session.query(Task).filter(Task.deadline < datetime.today().date()) \
        .order_by(Task.deadline).all()
    if len(rows) == 0:
        print("Nothing is missed!")
    else:
        for row in rows:
            day = row.deadline.day
            month = row.deadline.strftime('%b')
            print(f"%d. %s. {day} {month}" % (row.id, row.task))


def delete_task():
    rows = session.query(Task).all()
    if len(rows) == 0:
        print("Nothing to delete")
    else:
        print('Choose the number of the task you want to delete:')
        rows = session.query(Task).order_by(Task.deadline).all()
        for row in rows:
            day = row.deadline.day
            month = row.deadline.strftime('%b')
            print(f"%d. %s. {day} {month}" % (row.id, row.task))
        user_choice = int(input())
        specific_row = rows[user_choice - 1]
        session.delete(specific_row)
        session.commit()



while True:
    print()
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    choice = input()
    print()

    if choice == '0':
        # To exit
        print('Bye!')
        break

    elif choice == '1':
        # Today's task
        today = datetime.today()
        rows = session.query(Task).filter(Task.deadline == today.date()).all()
        day = today.day
        month = today.strftime('%b')
        print(f'Today {day} {month}:')
        if len(rows) == 0:
            print("Nothing to do!")
        for row in rows:
            print("%d. %s" % (row.id, row.task))

    elif choice == '2':
        # Week's Tasks
        week_task()

    elif choice == '3':
        # All tasks
        all_task()

    elif choice == '4':
        # Missed tasks
        missed_task()

    elif choice == '5':
        # adding task
        print('Enter task')
        user_task = input()
        print('Enter deadline')
        date_string = input()
        user_deadline = datetime.strptime(date_string, '%Y-%m-%d')
        new_row = Task(task=user_task, deadline=datetime.date(user_deadline))
        session.add(new_row)
        session.commit()
        print('The task has been added!')

    elif choice == '6':
        # For deleting task
        delete_task()

session.close()