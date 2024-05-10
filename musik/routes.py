from musik import app, db
from flask import render_template, request, flash, url_for, redirect,make_response,session
from sqlalchemy import text

@app.route('/')
def home_page():
    userid = session.get('user')
    if (session.get('user') != None):
        return render_template('home.html',name = userid,loged_in = True)
    return render_template('home.html', loged_in = False)

@app.route('/login', methods=['GET', 'POST'])
def login_pages():
    print("login was called")
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        print("Here the Data!!!")
        print(username)
        print(password)

        if (username is None or
                isinstance(username, str) is False or
                len(username) < 3):
            print("not valid")
            # flash(f"Username is not valid", category='warning')
            return render_template('login.html')

        if (password is None or
                isinstance(password, str) is False or
                len(password) < 3):
            print("something with password")
            # flash(f"Password is not valid", category='warning')
            return render_template('login.html')

        query_stmt = f"select username from user where username = '{username}' and password = '{password}'"
        print(query_stmt)
        result = db.session.execute(text(query_stmt))
        print(result)
        user = result.fetchall()
        # print("debug1")
        if not user:
            # flash(f"Try again", category='warning')
            # print("debug2")
            return render_template('login.html')
        # print("debug3")
        flash(f"'{user[0]}', you are logged in ", category='success')
        # print("debug4")
        query_stmt = f"select id from user where username = '{username}'"
        result = db.session.execute(text(query_stmt))
        userid = result.fetchall()
        print(userid[0][0])
        session['user'] = userid[0][0]
        return redirect(url_for('home_page'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def  register_pages():
    if request.method == 'POST':
        print('Post')

        username = request.form.get('Username')
        email = request.form.get('Email')
        password1 = request.form.get('Password1')
        password2 = request.form.get('Password2')

        print(username)
        print(email)
        print(password1)
        print(password2)

        if(username is None or
                isinstance(username, str) is False or
                len(username) < 3):
            print("username not valid")
            #flash("Username not valid", category='danger')
            return render_template('register.html')

        if(email is None or
                isinstance(email, str) is False or
                len(email) < 3):
            print("email not valid")
            #flash("Email not valid", category='danger')
            return render_template('register.html')

        if(password1 is None or
                isinstance(password1, str) is False or
                len(password1) < 3 or
                password1 != password2):
            print("password1 not valid")
            #flash("Password1 not valid", category='danger')
            return render_template('register.html')

        query_stmt = f"select * from user where username = '{username}'"
        print(query_stmt)
        result = db.session.execute(text(query_stmt))
        item = result.fetchone()
        print(item)

        if item is not None:
            #flash("Username exists, try again")
            print("Username exists")
            return render_template('register.html')

        query_insert = f"insert into user (username, email_address, password) values ('{username}', '{email}', '{password1}')"
        print(query_insert)
        db.session.execute(text(query_insert))
        db.session.commit()
        #flash("You are registered", category='success')
        query_stmt = f"select id from user where username = '{username}'"
        result = db.session.execute(text(query_stmt))
        userid = result.fetchall()
        print(userid[0][0])
        session['user'] = userid[0][0]
        return redirect(url_for('home_page'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', default=None)
    return redirect(url_for('home_page'))

@app.route('/artists',methods=['GET', 'POST'])
def artists_page():
    query_stmt = f"select * from artists"
    result = db.session.execute(text(query_stmt))
    itemsquery = result.fetchall()

    print(itemsquery)
    if (session.get('user') != None):
        return render_template('artists.html',items=itemsquery,loged_in = True)
    return render_template('artists.html',items=itemsquery,loged_in = False)

@app.route('/add_artist', methods=['GET', 'POST'])
def add_artists_page():
    if request.method == 'POST':
        name = request.form.get('Name')
        image = request.form.get('Image')
        description = request.form.get('Description')
        print(name,image,description)
        query_insert = f"insert into artists (name, picture, infoText) values ('{name}', '{image}', '{description}');"# user3',(select username from user where id = 3),(select password from user where id = 3)); --
        print(query_insert)
        db.session.execute(text(query_insert))
        db.session.commit()
    if (session.get('user') != None):
        return render_template('add_artist.html',loged_in = True)
    return redirect(url_for('home_page'))