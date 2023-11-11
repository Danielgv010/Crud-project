def home_page():
    print('''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>master-project</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="wrapper">
        <div class="col-2">
            <h1>REGISTER</h1>
            <form action="register.py">
                <label for="name">Name</label>
                <input type="text" name="name">
                <label for="email">Email</label>
                <input type="text" name="email">
                <label for="password">Password</label>
                <input type="password" name="password">
                <input type="submit" value="SUBMIT">
            </form>
        </div>
        <div class="col-2">
            <h1>LOGIN</h1>
            <form action="login.py">
                <label for="email">Email</label>
                <input type="text" name="email">
                <label for="password">Password</label>
                <input type="password" name="password">
                <input type="submit" value="SUBMIT">
            </form>
        </div>
    </div>
</body>

</html>
''')

def message_page(type, message, redirect): # Permite mostrar páginas con un mensaje de info/error/success
    color = 'black'
    if type == 'error': # Si es de error aparecerá en rojo
        color = 'red'
    elif type == 'info': # Si es de info aparecerá en azul
        color = 'blue'
    elif type == 'success': # Si es de exito aparecerá en verde
        color = 'green'

    print(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="2;{redirect}"/>
        <title>Message</title>
    </head>
    <body>
        <h1 style="color:{color}">{type.upper()}</h1>
        <h2>{message}</h2>
    </body>
    </html>
    ''')

def crud(data_list):
    start = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="wrapper">
        <div class="col-2">
            <a href="crud.py">See All</a>
            <form action="filter.py">
                <label for="company">Company</label>
                <input type="text" name="company" id="company">
                <label for="theme">Theme</label>
                <input type="text" name="theme" id="theme">
                <label for="player-count">Player Count</label>
                <input type="text" name="player-count" id="player-count">
                <label for="from-year">From year</label>
                <input type="text" name="from-year" id="from-year">
                <label for="until">Until</label>
                <input type="text" name="until" id="until">
                <input type="submit" value="Filter">
            </form>
            <br/>
            <form action="insert.py">
                <label for="name">Name</label>
                <input type="text" name="name" id="name">
                <label for="company">Company</label>
                <input type="text" name="company" id="company">
                <label for="theme">Theme</label>
                <input type="text" name="theme" id="theme">
                <label for="player-count">Player Count</label>
                <input type="text" name="player-count" id="player-count">
                <label for="release-date">Release date</label>
                <input type="text" name="release-date" id="release-date">
                <input type="submit" value="Insert">
            </form>
            <form action="batchInsert.py" enctype="multipart/form-data" method="post">
                <input type="file" name="file-item">
                <input type="submit"/>
            </form>
            <a href="logout.py">Logout</a>
        </div>
        <div class="col-2">
            <table border="1">
                <thead>
                    <th>Name</th>
                    <th>Company</th>
                    <th>Theme</th>
                    <th>Player count</th>
                    <th>Release date</th>
                    <th></th>
                    <th></th>
                </thead>
                <tbody id="table-body">'''

    table=""
    for data in data_list:
        delete_button = f'<a href="delete.py?id={data[0]}">Delete</a>' 
        modify_button = f'<a href="modifyForm.py?id={data[0]}">Modify</a>'
        row = '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'
        table += row.format(data[1],data[2],data[3],data[4],data[5],delete_button,modify_button)

    end = '''
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
'''

    print(start)
    print(table)
    print(end)


def modify_window_crud(data_list):
    print(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="wrapper">
        <form action="modify.py">
            <input type="hidden" name="id" id="id" value="{data_list[0]}">
            <label for="name">Name</label>
            <input type="text" name="name" id="name" value="{data_list[1]}">
            <label for="company">Company</label>
            <input type="text" name="company" id="company" value="{data_list[2]}">
            <label for="theme">Theme</label>
            <input type="text" name="theme" id="theme" value="{data_list[3]}">
            <label for="player-count">Player Count</label>
            <input type="text" name="player-count" id="player-count" value="{data_list[4]}">
            <label for="release-date">Release date</label>
            <input type="text" name="release-date" id="release-date" value="{data_list[5]}">
            <input type="submit" value="Modify">
        </form>
    </div>
</body>
</html>
''')