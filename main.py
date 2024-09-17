# Used SQLite Library
import sqlite3
import time
# Used Rich Library
from rich.console import Console
from rich.markdown import Markdown
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()

pk = 0

table = Table() # Saved in this tabel function

connection = sqlite3.connect("index.db") # Connected with Data Base

cursor = connection.cursor()

# Created Tabel in DataBase
cursor.execute("CREATE TABLE IF NOT EXISTS task ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "title TEXT,"
               "body TEXT,"
               "end_task INTEGER"
               ")")

# Select Function
def select(end_task):
    global pk
    global table
    cursor.execute(f"SELECT * FROM task")
    model = cursor.fetchall()
    task = list(model)
    print(task)
    print(model)

    # Make Select Tabel with 2 rows and 4 columns
    table = Table(title="Selected")
    table.add_column("Id" , justify="center", style="blue")
    table.add_column("Title", justify="center", style="cyan", no_wrap=True)
    table.add_column("Body" , justify="center", style="magenta")
    table.add_column("End task" , justify="center", style="red")
    
    for task in task:
        
        table.add_row(str(task[0]) , task[1] , task[2], str(task[3]))
        table.add_row('  ' , '  ' , '  ', " ")
        
    console.print(table)
    connection.commit()
# Add Function
def add(title, body):
    cursor.execute("INSERT INTO task (title, body, end_task) VALUES (? , ? , ? )", (title, body, 0))
    print(cursor.fetchall())
    connection.commit()

# Delete Function
def delete(pk):
    cursor.execute(f"DELETE FROM task WHERE id = {pk}")
    connection.commit()

# Update Function
def update(pk):
    cursor.execute("UPDATE task SET end_task = ? WHERE id = ?", (1, pk))
    connection.commit()
   
while 1:
# nab todo list is first markdown
    MARKDOWN = """
# Nab Todo List
"""
    md = Markdown(MARKDOWN) # markdown saved in md variable
    console.print(md)

    x = input()

    # called add function every time , it adds task
    if x == "add":
    
        # Twe inputs for add function
        title = input("Title:")
        body = input("body :")
        add(title, body)

        # progressbar for add
        with Progress() as progress:

            task1 = (progress.add_task("[blue]Adding...", total=1000))

            while not progress.finished:
                progress.update(task1, advance=22)
                time.sleep(0.02)

    # called select function every time , it selects tasks
    elif x == "select":

        # progressbar for select
        with Progress() as progress:
        
            task2 = (progress.add_task("[green]Selecting...", total=1000))

            while not progress.finished:
                progress.update(task2, advance=22)
                time.sleep(0.002)
                
        select(0)

    # called delete function every time , it deletes task
    elif x == "delete":
        delete(int(input('id :')))

        # progressbar for delete
        with Progress() as progress:
        
            task3 = (progress.add_task("[red]Deleting", total=1000))

            while not progress.finished:
                progress.update(task3, advance=22)
                time.sleep(0.002)

    # called update function every time , it updates task
    elif x == "update":
        update(int(input('id :')))

        # progressbar for update
        with Progress() as progress:
        
            task4 = (progress.add_task("[blue]Updating...", total=1000))

            while not progress.finished:
                progress.update(task4, advance=22)
                time.sleep(0.002)

    # called help function every time , it's helping to users
    elif x == "help":

        # progressbar for help
        with Progress() as progress:
        
            task5 = (progress.add_task("[cyan]Helping...", total=1000))

            while not progress.finished:
                progress.update(task5, advance=22)
                time.sleep(0.002)

        console.print("""
        [blue underline]-add == add task 
        ------------------------
        [blue underline]-sel == select task
        ------------------------
        [blue underline]-del == delete task
        ------------------------
        [blue underline]-up == update task
        """)

    # called exit function every time , it's exiting in input
    elif x == "exit":
        
        # progressbar for add
        with Progress() as progress:
        
            task6 = (progress.add_task("[red]Exiting", total=1000))

            while not progress.finished:
                progress.update(task6, advance=22)
                time.sleep(0.002)
        break

    else:
    # 'Erorr' is second markdown
        MARKDOWN_2 = """
# Error
""" 
        md2 = Markdown(MARKDOWN_2)
        console.print(md2)
       

    

