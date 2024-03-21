import datetime
import random
import demjson
from flask import Flask, render_template, request, redirect, session


import os
from email.mime import image
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail   #pip install flask-mail --user

from db_connections import Db

app = Flask(__name__)

app.secret_key = "key"

pth=r"C:\Social Guide Project\Social_Guide\static\Photo\\"
apth=r"C:\Social Guide Project\Social_Guide\static\application\\"

mypassword="#Justinsaju66"


@app.route('/')
def start():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login_index.html")


@app.route('/login1', methods=['post'])
def login1():
    db = Db()
    username = request.form['username']
    password = request.form['password']
    qry = "select * from login where username='" + username + "' and password='" + password + "'"
    result = db.selectOne(qry)
    if result is not None:
        if result['type'] == "admin":
            session['ln'] = "kk"
            return redirect('/admin_home')
        elif result['type'] == "mayor":
            session['ln'] = "kk"
            session['L_id'] = result['L_id']
            return redirect('/mayor_home')
        elif result['type'] == "councillor":
            session['ln'] = "kk"
            session['L_id'] = result['L_id']
            return redirect('/councillor_home')
        elif result['type'] == "department":
            session['ln'] = "kk"
            session['L_id'] = result['L_id']
            return redirect('/Dept_home')
        elif result['type'] == "clerk":
            session['ln'] = "kk"
            session['L_id'] = result['L_id']
            return redirect('/clerk_home')
        elif result['type'] == "user":
            session['ln'] = "kk"
            session['L_id'] = result['L_id']
            return redirect('/user_home')
        else:
            return '''<script>alert("invalid");window.location="/"</script>'''
    else:
        return '''<script>alert("invalid");window.location="/"</script>'''


@app.route('/admin_home')
def admin_home():
    if session['ln'] == "kk":
        return render_template("Admin/adminheader.html")
    else:
        return  redirect('/')


@app.route('/logout')
def logout():
    session['ln'] = ""
    return redirect('/login')


@app.route('/mayor_management', methods=['get'])
def mayor_management():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from mayor,login where mayor.mayor_id=login.L_id and type='mayor'"
        result = db.select(qry)
        return render_template("Admin/Mayor_management.html", value=result)
    else:
        return  redirect('/')

@app.route('/add_mayor', methods=['post'])
def add_mayor():
    if session['ln'] == "kk":
        return render_template("Admin/Add_mayor.html")
    else:
        return redirect("/")


@app.route('/add_mayor1', methods=['post'])
def add_mayor1():
    if session['ln'] == "kk":
        db = Db()
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        place = request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        district = request.form['district']
        phone = request.form['phone']
        email = request.form['email']
        joining_date = request.form['joining_date']
        Photo = request.files['photo']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        Photo.save(pth + date + ".jpg")
        path = "/static/Photo/" + date + ".jpg"
        password = random.randint(0000, 9999)
        qry = "insert into login values('','" + email + "','" + str(password) + "','mayor')"
        L_id = db.insert(qry)
        qry = "insert into mayor values('" + str(
            L_id) + "','" + name + "','" + age + "','" + gender + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + phone + "','" + email + "','" + joining_date + "','" + str(
            path) + "')"
        db.insert(qry)
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            gmail.ehlo()

            gmail.starttls()

            gmail.login('justinsaju66@gmail.com', mypassword)  # mail that send password

        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your password is " + str(password))  # content

        msg['Subject'] = 'Verification'

        msg['To'] = email

        msg['From'] = 'justinsaju66@gmail.com'

        try:

            gmail.send_message(msg)

        except Exception as e:

            print("COULDN'T SEND EMAIL", str(e))
        return '''<script>alert("successfully registered");window.location="/mayor_management"</script>'''
    else:
        return redirect('/')

@app.route('/delete_mayor/<id>', methods=['get'])
def delete_mayor(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "update login set type='deleted' where L_id='" + id + "'"
        db.delete(qry)
        return '''<script>alert("Deleted");window.location="/mayor_management"</script>'''
    else:
        return redirect("/")


@app.route('/edit_mayor/<id>', methods=['get'])
def edit_mayor(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from mayor,login where mayor.mayor_id=login.L_id and login.type='mayor' and mayor.mayor_id='" + id + "'"
        result = db.selectOne(qry)
        return render_template("Admin/Edit_mayor.html", value=result)
    else:
        return redirect("/")


@app.route('/edit_mayor1/<id>', methods=['post'])
def edit_mayor1(id):
    if session['ln'] == "kk":
        db = Db()
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        place = request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        district = request.form['district']
        phone = request.form['phone']
        email = request.form['email']
        joining_date = request.form['joining_date']
        Photo = request.files['photo']
        if request.files is not None:
            if Photo.filename != "":
                date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
                Photo.save(pth + date + ".jpg")
                path = "/static/Photo/" + date + ".jpg"
                qry = "update mayor set M_name='" + name + "',age='" + age + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',joining_date='" + joining_date + "',photo='" + str(
                    path) + "' where mayor_id='" + id + "'"
                db.update(qry)
                return '''<script>alert("updated successfully");window.location="/mayor_management"</script>'''
            else:
                qry = "update mayor set M_name='" + name + "',age='" + age + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',joining_date='" + joining_date + "' where mayor_id='" + id + "'"
                db.update(qry)
                return '''<script>alert("updated successfully");window.location="/mayor_management"</script>'''
        else:
            qry = "update mayor set M_name='" + name + "',age='" + age + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',joining_date='" + joining_date + "' where mayor_id='" + id + "'"
            db.update(qry)
            return '''<script>alert("updated successfully");window.location="/mayor_management"</script>'''
    else:
        return redirect("/")


@app.route('/councillor_management')
def councillor_management():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor,login where councillor.co_id=login.L_id and type='councillor'"
        result = db.select(qry)
        return render_template("Admin/Councillor_management.html", value=result)
    else:
        return redirect("/")


@app.route('/add_councillor', methods=['post'])
def add_councillor():
    if session['ln'] == "kk":
        return render_template("Admin/add_councillor.html")
    else:
        return redirect("/")


@app.route('/add_councillor1', methods=['post'])
def add_councillor1():
    if session['ln'] == "kk":
        db = Db()
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        place = request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        district = request.form['district']
        phone = request.form['phone']
        email = request.form['email']
        qualification = request.form['qualification']
        photo = request.files['photo']
        ward = request.form['ward']
        password = random.randint(0000, 9999)
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(pth + date + ".jpg")
        path = "/static/Photo/" + date + ".jpg"
        qry = "insert into login values('','" + email + "','" + str(password) + "','councillor')"
        L_id = db.insert(qry)
        qry = "insert into councillor values('" + str(
            L_id) + "','" + name + "','" + age + "','" + gender + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + phone + "','" + email + "','" + qualification + "','" + str(
            path) + "','" + ward + "')"
        db.insert(qry)
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            gmail.ehlo()

            gmail.starttls()

            gmail.login('justinsaju66@gmail.com', mypassword)  # mail that send password

        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your password is " + str(password))  # content

        msg['Subject'] = 'Verification'

        msg['To'] = email

        msg['From'] = 'justinsaju66@gmail.com'

        try:

            gmail.send_message(msg)

        except Exception as e:

            print("COULDN'T SEND EMAIL", str(e))
        return '''<script>alert("successfully registered");window.location="/councillor_management"</script>'''
    else:
        return redirect("/")


@app.route('/edit_councillor/<id>', methods=['get'])
def edit_councillor(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor,login where councillor.co_id=login.L_id and login.type='councillor' and councillor.co_id='" + id + "'"
        result = db.selectOne(qry)
        return render_template("Admin/Edit_councillor.html", value=result)
    else:
        return redirect("/")


@app.route('/edit_councillor1/<id>', methods=['post'])
def edit_councillor1(id):
    if session['ln'] == "kk":
        db = Db()
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        place = request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        district = request.form['district']
        phone = request.form['phone']
        email = request.form['email']
        qualification = request.form['qualification']
        photo = request.files['photo']
        ward = request.form['ward']
        if request.files is not None:
            if photo.filename != "":
                date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
                photo.save(pth + date + ".jpg")
                path = "/static/Photo/" + date + ".jpg"
                qry = "update councillor set c_name='" + name + "',age='" + age + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',qualification='" + qualification + "',photo='" + str(
                    path) + "',ward='" + ward + "' where co_id='" + id + "'"
                db.update(qry)
                return '''<script>alert(" updated successfully");window.location="/councillor_management"</script>'''
            else:
                qry = "update councillor set c_name='" + name + "',age='" + age + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',qualification='" + qualification + "',ward='" + ward + "' where co_id='" + id + "'"
                db.update(qry)
                return '''<script>alert(" updated successfully");window.location="/councillor_management"</script>'''
        else:
            qry = "update councillor set c_name='" + name + "',age='" + age + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',qualification='" + qualification + "',ward='" + ward + "' where co_id='" + id + "'"
            db.update(qry)
            return '''<script>alert(" updated successfully");window.location="/councillor_management"</script>'''
    else:
        return redirect("/")


@app.route('/delete_councillor/<id>', methods=['get'])
def delete_councillor(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "update login set type='deleted' where L_id='" + id + "'"
        db.delete(qry)
        return '''<script>alert("Deleted");window.location="/councillor_management"</script>'''
    else:
        return redirect("/")


@app.route('/department_management')
def department_management():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from department,login where department.D_id=login.L_id and login.type='department'"
        result = db.select(qry)
        return render_template("Admin/Dept_management.html", value=result)
    else:
        return redirect("/")


@app.route('/add_dept', methods=['post'])
def add_dept():
    if session['ln'] == "kk":
        return render_template("Admin/add_department.html")
    else:
        return redirect("/")


@app.route('/add_dept1', methods=['post'])
def add_dept1():
    if session['ln'] == "kk":
        db = Db()
        department = request.form['department']
        password = random.randint(0000, 9999)
        qry = "insert into login values('','" + department + "','" + str(password) + "','department')"
        res = db.insert(qry)
        qry = "insert into department values('" + str(res) + "','" + department + "')"
        db.insert(qry)
        return '''<script>alert("successfully added");window.location="/department_management"</script>'''
    else:
        return redirect("/")


@app.route('/edit_dept/<id>', methods=['get'])
def edit_dept(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from department where D_id='" + id + "'"
        result = db.selectOne(qry)
        return render_template("Admin/Edit_department.html", value=result)
    else:
        return redirect("/")


@app.route('/edit_dept1/<id>', methods=['post'])
def edit_dept1(id):
    if session['ln'] == "kk":
        db = Db()
        department = request.form['department']
        qry = "update department set department='" + department + "' where D_id='" + id + "'"
        db.update(qry)
        return '''<script>alert("updated successfully");window.location="/department_management"</script>'''
    else:
        return redirect("/")


@app.route('/delete_dept/<id>', methods=['get'])
def delete_dept(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "update login set type='deleted' where L_id='" + id + "'"
        db.delete(qry)
        return '''<script>alert("Deleted");window.location="/department_management"</script>'''
    else:
        return redirect("/")


@app.route('/clerk_management')
def clerk_management():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from clerk,login,department where clerk.clerk_id=login.L_id and department.D_id=clerk.D_id and type='clerk'"
        result = db.select(qry)
        return render_template("Admin/Clerk_management.html", value=result)
    else:
        return redirect("/")


@app.route('/add_clerk', methods=['post'])
def add_clerk():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from department"
        res = db.select(qry)
        return render_template("Admin/add_clerk.html", val=res)
    else:
        return redirect("/")


@app.route('/add_clerk1', methods=['post'])
def add_clerk1():
    if session['ln'] == "kk":
        db = Db()
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        place = request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        district = request.form['district']
        phone = request.form['phone']
        email = request.form['email']
        qualification = request.form['qualification']
        photo = request.files['photo']
        department = request.form['department']
        password = random.randint(0000, 9999)
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(pth + date + ".jpg")
        path = "/static/Photo/" + date + ".jpg"
        qry = "insert into login values('','" + email + "','" + str(password) + "','clerk')"
        L_id = db.insert(qry)
        qry = "insert into clerk values('" + str(
            L_id) + "','" + name + "','" + age + "','" + gender + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + phone + "','" + email + "','" + qualification + "','" + str(path) + "','" + department + "')"
        db.insert(qry)
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            gmail.ehlo()

            gmail.starttls()

            gmail.login('justinsaju66@gmail.com', mypassword)  # mail that send password

        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your password is " + str(password))  # content

        msg['Subject'] = 'Verification'

        msg['To'] = email

        msg['From'] = 'justinsaju66@gmail.com'

        try:

            gmail.send_message(msg)

        except Exception as e:

            print("COULDN'T SEND EMAIL", str(e))
        return '''<script>alert("successfully registered");window.location="/clerk_management"</script>'''
    else:
        return redirect("/")


@app.route('/edit_clerk/<id>', methods=['get'])
def edit_clerk(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from department,login where department.D_id=login.L_id"
        res = db.select(qry)
        qry = "select * from clerk,login where clerk.clerk_id=login.L_id and clerk.clerk_id='" + id + "'"
        result = db.selectOne(qry)
        return render_template("Admin/Edit_clerk.html", val=res, value=result)
    else:
        return redirect("/")


@app.route('/edit_clerk1/<id>', methods=['post'])
def edit_clerk1(id):
    if session['ln'] == "kk":
        db = Db()
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        place = request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        district = request.form['district']
        phone = request.form['phone']
        email = request.form['email']
        qualification = request.form['qualification']
        photo = request.files['photo']
        department = request.form['department']
        if request.files is not None:
            if photo.filename != "":
                date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
                photo.save(pth + date + ".jpg")
                path = "/static/Photo/" + date + ".jpg"
                qry = "update clerk set name='" + name + "',age='" + age + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',qualification='" + qualification + "',photo='" + str(
                    path) + "',D_id='" + department + "' where clerk_id='" + id + "'"
                db.update(qry)
                return '''<script>alert("successfully updated");window.location="/clerk_management"</script>'''
            else:
                qry = "update clerk set name='" + name + "',age='" + age + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',qualification='" + qualification + "',D_id='" + department + "' where clerk_id='" + id + "'"
                db.update(qry)
                return '''<script>alert("successfully updated");window.location="/clerk_management"</script>'''
        else:
            qry = "update clerk set name='" + name + "',age='" + age + "',gender='" + gender + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',qualification='" + qualification + "',D_id='" + department + "' where clerk_id='" + id + "'"
            db.update(qry)
            return '''<script>alert("successfully updated");window.location="/clerk_management"</script>'''
    else:
        return redirect("/")


@app.route('/delete_clerk/<id>', methods=['get'])
def delete_clerk(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "update login set type='deleted' where L_id='" + id + "'"
        db.delete(qry)
        return '''<script>alert("Deleted");window.location="/clerk_management"</script>'''
    else:
        return redirect("/")


@app.route('/previous_mayor_details')
def previous_mayor_details():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from mayor,login where mayor.mayor_id=login.L_id and login.type='deleted'"
        result = db.select(qry)
        return render_template("Admin/Previous_mayor_details.html", value=result)
    else:
        return redirect("/")


@app.route('/corporation_management')
def corporation_management():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from corporation"
        result = db.select(qry)
        return render_template("Admin/Corporation_management.html", value=result)
    else:
        return redirect("/")


@app.route('/add_corporation', methods=['post'])
def add_corporation():
    if session['ln'] == "kk":
        return render_template("Admin/add_corporation.html")
    else:
        return redirect("/")


@app.route('/add_corporation1', methods=['post'])
def add_corporation1():
    if session['ln'] == "kk":
        db = Db()
        name = request.form['name']
        place = request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        district = request.form['district']
        phone = request.form['phone']
        email = request.form['email']
        photo = request.files['photo']
        no_of_wards = request.form['no_of_wards']
        password = random.randint(0000, 9999)
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(pth+ date + ".jpg")
        path = "/static/Photo/" + date + ".jpg"
        qry = "insert into corporation values('','" + name + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + phone + "','" + email + "','" + str(
            path) + "','" + no_of_wards + "')"
        db.insert(qry)
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)

            gmail.ehlo()

            gmail.starttls()

            gmail.login('justinsaju66@gmail.com', mypassword)  # mail that send password

        except Exception as e:
            print("Couldn't setup email!!" + str(e))

        msg = MIMEText("Your password is " + str(password))  # content

        msg['Subject'] = 'Verification'

        msg['To'] = email

        msg['From'] = 'justinsaju66@gmail.com'

        try:

            gmail.send_message(msg)

        except Exception as e:

            print("COULDN'T SEND EMAIL", str(e))
        return '''<script>alert("successfully registered");window.location="/corporation_management"</script>'''
    else:
        return redirect("/")


@app.route('/edit_corporation/<id>', methods=['get'])
def edit_corporation(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from corporation,login where corporation.corp_id=login.L_id and login.type='corporation' and corporation.corp_id='" + id + "'"
        result = db.selectOne(qry)
        return render_template("Admin/Edit_corporation.html", value=result)
    else:
        return redirect("/")


@app.route('/edit_corporation1/<id>', methods=['post'])
def edit_corporation1(id):
    if session['ln'] == "kk":
        db = Db()
        name = request.form['name']
        place = request.form['place']
        post = request.form['post']
        pin = request.form['pin']
        district = request.form['district']
        phone = request.form['phone']
        email = request.form['email']
        photo = request.files['photo']
        no_of_wards = request.form['no_of_wards']
        if request.files is not None:
            if photo.filename != "":
                date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
                photo.save(pth+ date + ".jpg")
                path = "/static/Photo/" + date + ".jpg"
                qry = "update corporation set name='" + name + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',photo='" + str(
                    path) + "',no_of_wards='" + no_of_wards + "' where corp_id='" + id + "'"
                db.update(qry)
                return '''<script>alert("updated successfully");window.location="/corporation_management"</script>'''
            else:
                qry = "update corporation set name='" + name + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',no_of_wards='" + no_of_wards + "' where corp_id='" + id + "'"
                db.update(qry)
                return '''<script>alert("updated successfully");window.location="/corporation_management"</script>'''
        else:
            qry = "update corporation set name='" + name + "',place='" + place + "',post='" + post + "',pin='" + pin + "',district='" + district + "',phone='" + phone + "',email='" + email + "',no_of_wards='" + no_of_wards + "' where corp_id='" + id + "'"
            db.update(qry)
            return '''<script>alert("updated successfully");window.location="/corporation_management"</script>'''
    else:
        return redirect("/")


@app.route('/delete_corporation/<id>', methods=['get'])
def delete_corporation(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "update login set type='rejected' where L_id='" + id + "'"
        db.delete(qry)
        return '''<script>alert("Deleted");window.location="/corporation_management"</script>'''
    else:
        return redirect("/")







#################################     MAYOR   ######################################





@app.route('/mayor_home')
def mayor_home():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from mayor where mayor_id='" + str(session['L_id']) + "'"
        res = db.selectOne(qry)
        return render_template("Mayor/mayor_header.html", value=res)
    else:
        return redirect("/")


@app.route('/view_profile')
def view_profile():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from mayor,login where mayor.mayor_id=login.L_id and login.type='mayor' and mayor_id='" + str(session['L_id']) + "' "
        res = db.selectOne(qry)
        return render_template("Mayor/view_profile.html", value=res)
    else:
        return redirect("/")


@app.route('/mc_interaction')
def mc_interaction():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from mayor,chat_mc,councillor where mayor.mayor_id=chat_mc.to_id and councillor.co_id=chat_mc.from_id"
        res = db.select(qry)
        return render_template("Mayor/m_c chat.html", value=res)
    else:
        return redirect("/")


@app.route('/chat_mc/<a>')
def chat_mc(a):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor,chat_mc where councillor.co_id=chat_mc.to_id"
        res = db.selectOne(qry)
        return render_template("Mayor/m_c reply.html", value=res)
    else:
        return redirect("/")


@app.route('/chat_mc1/<a>', methods=['post'])
def chat_mc1(a):
    if session['ln'] == "kk":
        db = Db()
        chat = request.form['textfield']
        qry = "insert into chat_mc values('','" + str(session['L_id']) + "','" + a + "','" + chat + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/mc_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/msg_councillor', methods=['post'])
def msg_councillor():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor"
        res = db.select(qry)
        return render_template("Mayor/mayor_chat.html", value=res)
    else:
        return redirect("/")


@app.route('/msg_councillor1', methods=['post'])
def msg_councillor1():
    if session['ln'] == "kk":
        db = Db()
        councillor = request.form['select']
        message = request.form['textfield']
        qry = "insert into chat_mc values('','" + str(session['L_id']) + "','" + councillor + "','" + message + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/mc_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/view_notification')
def view_notification():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from notification n,clerk c where n.clerk_id=c.clerk_id"
        res = db.select(qry)
        return render_template("Mayor/view_notification.html", value=res)
    else:
        return redirect("/")


@app.route('/view_feedback')
def view_feedback():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from feedback ,user  where feedback.user_id=user.user_id"
        res = db.select(qry)
        return render_template("Mayor/view_feedback.html", value=res)
    else:
        return redirect("/")


@app.route('/view_suggestion')
def view_suggestion():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from suggestion ,councillor  where suggestion.councillor_id=councillor.co_id"
        res = db.select(qry)
        return render_template("Mayor/view_suggestion.html", value=res)
    else:
        return redirect("/")


@app.route('/project_approve')
def project_approve():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from project,councillor where project.councillor_id=councillor.co_id and project.status='pending'"
        result = db.select(qry)
        return render_template("Mayor/project_approve.html", value=result)
    else:
        return redirect("/")


@app.route('/accept_project/<id>', methods=['get', 'post'])
def accept_project(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "UPDATE project SET  status='approved' where  project_id='" + id + "'"
        db.update(qry)
        return '''<script> alert("Approved"); window.location="/project_approve"</script>'''
    else:
        return redirect("/")


@app.route('/reject_project/<id>', methods=['get', 'post'])
def reject_project(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "UPDATE project SET  status='rejected' where  project_id='" + id + "'"
        db.update(qry)
        return '''<script> alert("Rejected"); window.location="/project_approve"</script>'''
    else:
        return redirect("/")


@app.route('/view_issue')
def view_issue():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from issues,user where issues.user_id=user.user_id "
        res = db.select(qry)
        return render_template("Mayor/view_issue.html", value=res)
    else:
        return redirect("/")


@app.route('/view_complaint')
def view_complaint():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor c,councillor_complaint t  where c.co_id=t.councillor_id"
        res = db.select(qry)
        return render_template("Mayor/view_complaint.html", value=res)
    else:
        return redirect("/")


@app.route('/send_reply/<a>', methods=['get'])
def send_reply(a):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor_complaint where c_id='" + a + "'"
        result = db.selectOne(qry)
        return render_template('Mayor/complaint_reply.html', value=result)
    else:
        return redirect("/")


@app.route('/send_reply1/<a>', methods=['post'])
def send_reply1(a):
    if session['ln'] == "kk":
        db = Db()
        reply = request.form['textarea']
        qry = "update councillor_complaint set reply='" + reply + "',reply_date=curdate() where   c_id='" + a + "'"
        db.update(qry)
        return '''<script>alert("Send successfully");window.location="/view_complaint"</script>'''
    else:
        return redirect("/")


##############################       Councillor        #################################






@app.route('/councillor_home')
def councillor_home():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor where co_id='" + str(session['L_id']) + "'"
        res = db.selectOne(qry)
        return render_template("councillor/councillorheader.html", value=res)
    else:
        return redirect("/")


@app.route('/councillor_profile', methods=['get'])
def councillor_profile():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor,login where councillor.co_id=login.L_id and login.type='councillor' and co_id='" + str(session['L_id']) + "' "
        res = db.selectOne(qry)
        return render_template("councillor/view_profile.html", value=res)
    else:
        return redirect("/")


@app.route('/user_interaction')
def user_interaction():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from user,chat_uc,councillor where councillor.co_id=chat_uc.to_id and user.user_id=chat_uc.from_id"
        res = db.select(qry)
        return render_template("councillor/uc_chat.html", value=res)
    else:
        return redirect("/")


@app.route('/user_interaction1/<a>')
def user_interaction1(a):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from user,chat_uc where user.user_id=chat_uc.to_id"
        res = db.selectOne(qry)
        return render_template("councillor/uc_reply.html", value=res)
    else:
        return redirect("/")


@app.route('/user_interaction2/<a>', methods=['post'])
def user_interaction2(a):
    if session['ln'] == "kk":
        db = Db()
        chat = request.form['textfield']
        qry = "insert into chat_uc values('','" + str(session['L_id']) + "','" + a + "','" + chat + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/user_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/chat_user', methods=['post'])
def chat_user():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from user"
        res = db.select(qry)
        return render_template("councillor/user_chat.html", value=res)
    else:
        return redirect("/")


@app.route('/chat_user1', methods=['post'])
def chat_user1():
    if session['ln'] == "kk":
        db = Db()
        user = request.form['select']
        message = request.form['textfield']
        qry = "insert into chat_uc values('','" + str(session['L_id']) + "','" + user + "','" + message + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/user_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/councillor_feedback')
def councillor_feedback():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from feedback ,user  where feedback.user_id=user.user_id"
        res = db.select(qry)
        return render_template("councillor/view_feedback.html", value=res)
    else:
        return redirect("/")


@app.route('/cc_interaction')
def cc_interaction():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor,chat_cc where councillor.co_id=chat_cc.to_id and co_id='" + str(
            session['L_id']) + "'"
        res = db.select(qry)
        return render_template("councillor/cc_chat.html", value=res)
    else:
        return redirect("/")


@app.route('/cc_reply/<a>')
def uc_reply(a):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor,chat_cc where councillor.co_id=chat_cc.to_id"
        res = db.selectOne(qry)
        return render_template("councillor/cc_chat_reply.html", value=res)
    else:
        return redirect("/")


@app.route('/cc_reply1/<a>', methods=['post'])
def uc_reply1(a):
    if session['ln'] == "kk":
        db = Db()
        chat = request.form['textfield']
        qry = "insert into chat_cc values('','" + str(session['L_id']) + "','" + a + "','" + chat + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/cc_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/chat_cc', methods=['post'])
def chat_cc():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor"
        res = db.select(qry)
        return render_template("councillor/councillor_chat.html", value=res)
    else:
        return redirect("/")


@app.route('/chat_cc1', methods=['post'])
def chat_cc1():
    if session['ln'] == "kk":
        db = Db()
        councillor = request.form['select']
        message = request.form['textfield']
        qry = "insert into chat_cc values('','" + str(session['L_id']) + "','" + councillor + "','" + message + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/cc_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/send_complaint')
def send_complaint():
    if session['ln'] == "kk":
        return render_template("councillor/send_complaint.html")
    else:
        return redirect("/")


@app.route('/send_complaint1', methods=['post'])
def send_complaint1():
    if session['ln'] == "kk":
        db = Db()
        complaint = request.form['complaint']
        qry = "insert into councillor_complaint values('','" + str(session['L_id']) + "','" + complaint + "',curdate(),'pending','pending')"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/councillor_home"</script>'''
    else:
        return redirect("/")


@app.route('/c_view_reply')
def c_view_reply():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor_complaint,councillor where councillor.co_id=councillor_complaint.councillor_id and councillor_id='" + str(
            session['L_id']) + "'"
        res = db.select(qry)
        return render_template("councillor/view_reply.html", value=res)
    else:
        return redirect("/")


@app.route('/add_project')
def add_project():
    if session['ln'] == "kk":
        return render_template("councillor/add_project.html")
    else:
        return redirect("/")


@app.route('/add_project1', methods=['post'])
def add_project1():
    if session['ln'] == "kk":
        db = Db()
        project = request.form['project']
        qry = "insert into project values('','" + str(session['L_id']) + "','" + project + "',curdate(),'pending')"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/councillor_home"</script>'''
    else:
        return redirect("/")


@app.route('/send_suggestion')
def send_suggestion():
    if session['ln'] == "kk":
        return render_template("councillor/send_suggestion.html")
    else:
        return redirect("/")


@app.route('/send_suggestion1', methods=['post'])
def send_suggestion1():
    if session['ln'] == "kk":
        db = Db()
        suggestion = request.form['suggestion']
        qry = "insert into suggestion values('','" + str(session['L_id']) + "','" + suggestion + "',curdate())"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/councillor_home"</script>'''
    else:
        return redirect("/")


@app.route('/mayor_interaction')
def mayor_interaction():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from mayor,chat_mc where mayor.mayor_id=chat_mc.to_id and chat_mc.to_id='" + str(
            session['L_id']) + "'"
        res = db.select(qry)
        return render_template("councillor/mc_chat.html", value=res)
    else:
        return redirect("/")


@app.route('/chat_mayor/<a>', methods=['get'])
def chat_mayor(a):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from mayor,chat_mc where mayor.mayor_id=chat_mc.to_id"
        res = db.selectOne(qry)
        return render_template("councillor/mc_chat_reply.html", value=res)
    else:
        return redirect("/")


@app.route('/chat_mayor1/<a>', methods=['post'])
def chat_mayor1(a):
    if session['ln'] == "kk":
        db = Db()
        chat = request.form['textfield']
        qry = "insert into chat_mc values('','" + str(session['L_id']) + "','" + a + "','" + chat + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/mayor_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/msg_mayor', methods=['post'])
def msg_mayor():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from mayor,login where login.L_id=mayor.mayor_id and login.type='mayor'"
        res = db.select(qry)
        return render_template("councillor/chat_mayor.html", value=res)
    else:
        return redirect("/")


@app.route('/msg_mayor1', methods=['post'])
def msg_mayor1():
    if session['ln'] == "kk":
        db = Db()
        mayor = request.form['select']
        message = request.form['textfield']
        qry = "insert into chat_mc values('','" + str(session['L_id']) + "','" + mayor + "','" + message + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/mayor_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/view_frequent_issues')
def view_frequent_issues():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from issues,user where issues.user_id=user.user_id "
        res = db.select(qry)
        # print(res)

        #frequent pattern finding using FPgrowth Algm

        import pandas as pd
        from mlxtend.preprocessing import TransactionEncoder

        from nltk.stem import PorterStemmer
        from nltk.tokenize import word_tokenize

        ps = PorterStemmer()

        if len(res)>0:
            dataset = []
            for rows in res:
                words = word_tokenize(rows['issues'])
                dataset.append(words)
            # print(dataset)
            te = TransactionEncoder()
            te_ary = te.fit(dataset).transform(dataset)
            df = pd.DataFrame(te_ary, columns=te.columns_)

            from mlxtend.frequent_patterns import fpgrowth

            k = fpgrowth(df, min_support=0.6, use_colnames=True)
            freq_words = []
            freq_issues = []
            fqwrd=""
            print("output")
            for index, row in k.iterrows():
                # print(row)
                if row['support'] >= 0.50:
                    for k in row['itemsets']:
                        if k not in freq_words:
                            freq_words.append(k)
                            fqwrd=fqwrd+k+", "
                            for rows in res:
                                if k in rows['issues']:
                                    if rows['issues']  not in freq_issues:
                                        freq_issues.append(rows['issues'])
                                    # print(freq_issues)


        return render_template("councillor/verify_issues.html", value=res, fqw=fqwrd, fqi=freq_issues)
    else:
        return redirect("/")


@app.route('/assign_p_time')
def assign_p_time():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from project where status='approved'"
        res = db.select(qry)
        return render_template("councillor/project_timeperiod.html", value=res)
    else:
        return redirect("/")


@app.route('/add_project_time/<a>', methods=['get'])
def add_project_time(a):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from project where project_id='" + a + "'"
        res = db.selectOne(qry)
        return render_template("councillor/assign_time.html", value=res)
    else:
        return redirect("/")


@app.route('/add_project_time1/<a>', methods=['post'])
def add_project_time1(a):
    if session['ln'] == "kk":
        db = Db()
        timeperiod = request.form['textfield']
        qry = "insert into project_timing values('','" + a + "','" + timeperiod + "')"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/councillor_home"</script>'''
    else:
        return redirect("/")


###############################################               Department                #########################################3






@app.route('/Dept_home')
def Dept_home():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from department where D_id='" + str(session['L_id']) + "'"
        res = db.selectOne(qry)
        return render_template("Department/dept_header.html", value=res)
    else:
        return redirect("/")


@app.route('/view_staff')
def view_staff():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from clerk,login,department where clerk.clerk_id=login.L_id and department.D_id=clerk.D_id and  login.type='clerk' and department.D_id='" + str(
            session['L_id']) + "'"
        res = db.select(qry)
        return render_template("Department/view_clerk.html", value=res)
    else:
        return redirect("/")


@app.route('/attendance_details', methods=['get'])
def attendance_details():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from clerk,department,login where clerk.D_id=department.D_id and clerk.clerk_id=login.L_id and login.type='clerk' and department.D_id='" + str(
            session['L_id']) + "'"
        result = db.select(qry)
        return render_template("Department/attendance.html", value=result)
    else:
        return redirect("/")


@app.route('/attendance_details1/<id>', methods=['get'])
def attendance_details1(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from clerk,login where clerk.clerk_id=login.L_id and login.type='clerk' and clerk_id='" + id + "'"
        result = db.selectOne(qry)
        return render_template("Department/send_attendance.html", value=result)
    else:
        return redirect("/")


@app.route('/send_attendance/<id>', methods=['post'])
def send_attendance(id):
    if session['ln'] == "kk":
        db = Db()
        attendance = request.form['attendance']
        qry = "insert into attendance values('','" + str(session['L_id']) + "','" + id + "',curdate(),'" + attendance + "')"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/attendance_details"</script>'''
    else:
        return redirect("/")


@app.route('/dept_view_complaint')
def dept_view_complaint():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from user ,user_complaint,department  where user.user_id=user_complaint.user_id and department.D_id=user_complaint.D_id and user_complaint.D_id='" + str(
            session['L_id']) + "'"
        res = db.select(qry)
        return render_template("Department/complaint_mngment.html", value=res)
    else:
        return redirect("/")


@app.route('/dept_send_reply/<a>', methods=['get'])
def dept_send_reply(a):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from user_complaint where comp_id='" + a + "'"
        result = db.selectOne(qry)
        return render_template('Department/complaint_reply.html', value=result)
    else:
        return redirect("/")


@app.route('/dept_send_reply1/<a>', methods=['post'])
def dept_send_reply1(a):
    if session['ln'] == "kk":
        db = Db()
        reply = request.form['textarea']
        qry = "update user_complaint set reply='" + reply + "',reply_date=curdate() where   comp_id='" + a + "'"
        db.update(qry)
        return '''<script>alert("Send successfully");window.location="/dept_view_complaint"</script>'''
    else:
        return redirect("/")


@app.route('/assign_work', methods=['get'])
def assign_work():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from clerk where D_id='" + str(session['L_id']) + "'"
        result = db.select(qry)
        return render_template('Department/assign_work.html', value=result)
    else:
        return redirect("/")


@app.route('/assign_works/<a>', methods=['get'])
def assign_works(a):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from clerk"
        result = db.selectOne(qry)
        return render_template('Department/assign_works.html', value=result)
    else:
        return redirect("/")


@app.route('/assign_works1/<i>', methods=['post'])
def assign_works1(i):
    if session['ln'] == "kk":
        db = Db()
        work = request.form['work']
        date = request.form['date']
        qry = "insert into assign_work values('','" + i + "','" + work + "','" + date + "')"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/assign_work"</script>'''
    else:
        return redirect("/")


@app.route('/application_management')
def application_management():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from project,application where project.project_id=application.project_id and application.status='forwarded'"
        res = db.select(qry)
        return render_template("Department/application_mngmnt.html", value=res)
    else:
        return redirect("/")


@app.route('/dpt_approve_application/<id>', methods=['get', 'post'])
def dpt_approve_application(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "UPDATE application SET  status='accepted' where  app_id='" + id + "'"
        db.update(qry)
        return '''<script> alert("Approved"); window.location="/application_management"</script>'''
    else:
        return redirect("/")


@app.route('/dpt_reject_application/<id>', methods=['get', 'post'])
def dpt_reject_application(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "UPDATE application SET  status='rejected' where  app_id='" + id + "'"
        db.update(qry)
        return '''<script> alert("Rejected"); window.location="/application_management"</script>'''
    else:
        return redirect("/")


@app.route('/dept_view_report')
def dept_view_report():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from clerk,report where clerk.clerk_id=report.clerk_id and clerk.D_id='" + str(
            session['L_id']) + "'"
        res = db.select(qry)
        return render_template("Department/view_report.html", value=res)
    else:
        return redirect("/")


@app.route('/dept_view_rating')
def dept_view_rating():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from user,department,rating where user.user_id=rating.user_id and department.D_id=rating.dept_id"
        res = db.select(qry)
        return render_template("Department/view_rating.html", value=res)
    else:
        return redirect("/")


@app.route('/verify_issues')
def verify_issues():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from user,issues where user.user_id=issues.user_id"
        res = db.select(qry)
        return render_template("Department/view_issues.html", value=res)
    else:
        return redirect("/")


##############################          clerk           ####################################





@app.route('/clerk_home')
def clerk_home():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from clerk where clerk_id='" + str(session['L_id']) + "'"
        res = db.selectOne(qry)
        return render_template("clerk/clerkheader.html", value=res)
    else:
        return redirect("/")


@app.route('/clerk_profile', methods=['get'])
def clerk_profile():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from clerk,login,department where clerk.clerk_id=login.L_id and clerk.D_id=department.D_id and login.type='clerk' and clerk_id='" + str(
            session['L_id']) + "'"
        res = db.selectOne(qry)
        return render_template("clerk/view_profile.html", value=res)
    else:
        return redirect("/")


@app.route('/clerk_view_application', methods=['get'])
def clerk_view_application():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from application,user where application.user_id=user.user_id and application.status='pending'"
        res = db.select(qry)
        return render_template("clerk/view_application.html", value=res)
    else:
        return redirect("/")


@app.route('/approve_application/<id>', methods=['get', 'post'])
def approve_application(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "UPDATE application SET  status='forwarded' where  app_id='" + id + "'"
        db.update(qry)
        return '''<script> alert("Forwarded"); window.location="/clerk_view_application"</script>'''
    else:
        return redirect("/")


@app.route('/reject_application/<id>', methods=['get', 'post'])
def reject_application(id):
    if session['ln'] == "kk":
        db = Db()
        qry = "UPDATE application SET  status='rejected' where  app_id='" + id + "'"
        db.update(qry)
        return '''<script> alert("Rejected"); window.location="/clerk_view_application"</script>'''
    else:
        return redirect("/")


@app.route('/send_user_notification', methods=['get'])
def send_user_notification():
    if session['ln'] == "kk":
        return render_template('clerk/send_notification.html')
    else:
        return redirect("/")


@app.route('/send_user_notification1', methods=['post'])
def send_user_notification1():
    if session['ln'] == "kk":
        db = Db()
        notification = request.form['textarea']
        qry = "insert into notification values('','" + str(session['L_id']) + "','" + notification + "',curdate())"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/clerk_home"</script>'''
    else:
        return redirect("/")


@app.route('/send_report', methods=['get'])
def send_report():
    if session['ln'] == "kk":
        return render_template('clerk/submit_report.html')
    else:
        return redirect("/")


@app.route('/send_report1', methods=['post'])
def send_report1():
    if session['ln'] == "kk":
        db = Db()
        report = request.form['textarea']
        qry = "insert into report values('','" + str(session['L_id']) + "','" + report + "',curdate())"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/clerk_home"</script>'''
    else:
        return redirect("/")


@app.route('/view_assign_work', methods=['get'])
def view_assign_work():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from assign_work,clerk where assign_work.clerk_id=clerk.clerk_id and clerk.clerk_id='" + str(
            session['L_id']) + "'"
        res = db.select(qry)
        return render_template("clerk/view_assign_work.html", value=res)
    else:
        return redirect("/")


##################################               user                      ##################################





@app.route('/user_home')
def user_home():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from user where user_id='" + str(session['L_id']) + "'"
        res = db.selectOne(qry)
        return render_template("User/user_header.html", value=res)
    else:
        return redirect("/")


@app.route('/user_reg')
def user_reg():
    return render_template("Registration.html")


@app.route('/user_registration', methods=['post'])
def user_registration():
    db = Db()
    name = request.form['textfield']
    age = request.form['textfield2']
    gender = request.form['radio']
    place = request.form['textfield3']
    post = request.form['textfield4']
    pin = request.form['textfield5']
    district = request.form['select']
    phone = request.form['textfield6']
    email = request.form['textfield7']
    ward = request.form['textfield8']
    username = request.form['textfield9']
    password = request.form['textfield10']
    qry = "insert into login values('','" + username + "','" + password + "','user')"
    res = db.insert(qry)
    qry1 = "insert into user values('" + str(
        res) + "','" + name + "','" + age + "','" + gender + "','" + place + "','" + post + "','" + pin + "','" + district + "','" + phone + "','" + email + "','" + ward + "')"
    db.insert(qry1)
    return '''<script>alert("Send successfully");window.location="/"</script>'''


@app.route('/send_application', methods=['get'])
def send_application():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from project where status='approved'"
        res = db.select(qry)
        return render_template("User/application.html", value=res)
    else:
        return redirect("/")


@app.route('/send_application1', methods=['post'])
def send_application1():
    if session['ln'] == "kk":
        db = Db()
        project = request.form['select']
        application = request.files['fileField']
        date = datetime.datetime.now().strftime("%d%m%y-%H%M%S")
        application.save(apth + date + ".pdf")
        path = "/static/application/" + date + ".pdf"
        qry = "insert into application values('','" + str(session['L_id']) + "','" + str(
            path) + "',curdate(),'pending','" + project + "')"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/user_home"</script>'''
    else:
        return redirect("/")


@app.route('/view_application_status', methods=['get'])
def view_application_status():
    if session['ln'] == "kk":
        db = Db()
        qry = "select application.application,project.project,application.date,application.status from application,project where application.project_id=project.project_id  and user_id='" + str(session['L_id']) + "'"
        res = db.select(qry)
        return render_template("User/view_status.html", value=res)
    else:
        return redirect("/")


@app.route('/send_feedback', methods=['get'])
def send_feedback():
    if session['ln'] == "kk":
        return render_template("User/send_feedback.html")
    else:
        return redirect("/")


@app.route('/send_feeback1', methods=['post'])
def send_feedback1():
    if session['ln'] == "kk":
        db = Db()
        feedback = request.form['textarea']
        qry = "insert into feedback values('','" + str(session['L_id']) + "','" + feedback + "',curdate())"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/user_home"</script>'''
    else:
        return redirect("/")


@app.route('/user_councillor_interaction')
def user_councillor_interaction():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor,chat_uc where councillor.co_id=chat_uc.from_id and chat_uc.to_id='" + str(session['L_id']) + "'"
        res = db.select(qry)
        return render_template("User/counsilor_interact.html", value=res)
    else:
        return redirect("/")


@app.route('/user_c_reply/<a>')
def user_c_reply(a):
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor,chat_uc where councillor.co_id=chat_uc.to_id"
        res = db.selectOne(qry)
        return render_template("User/uc_reply.html", value=res)
    else:
        return redirect("/")


@app.route('/user_c_reply1/<a>', methods=['post'])
def user_c_reply1(a):
    if session['ln'] == "kk":
        db = Db()
        chat = request.form['textfield']
        qry = "insert into chat_uc values('','" + str(session['L_id']) + "','" + a + "','" + chat + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/user_councillor_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/chat_councillor', methods=['post'])
def chat_councillor():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from councillor "
        res = db.select(qry)
        return render_template("User/chat_councillor.html", value=res)
    else:
        return redirect("/")


@app.route('/chat_councillor1', methods=['post'])
def chat_councillor1():
    if session['ln'] == "kk":
        db = Db()
        councillor = request.form['select']
        message = request.form['textfield']
        qry = "insert into chat_uc values('','" + str(session['L_id']) + "','" + councillor + "','" + message + "',curdate())"
        db.insert(qry)
        return '''<script>alert("send successfully");window.location="/user_councillor_interaction"</script>'''
    else:
        return redirect("/")


@app.route('/user_send_complaint', methods=['get'])
def user_send_complaint():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from department"
        res = db.select(qry)
        return render_template("User/send_complaint.html", value=res)
    else:
        return redirect("/")


@app.route('/user_send_complaint1', methods=['post'])
def user_send_complaint1():
    if session['ln'] == "kk":
        db = Db()
        complaint = request.form['textarea']
        department = request.form['select']
        qry = "insert into user_complaint values('','" + str(
            session['L_id']) + "','" + complaint + "',curdate(),'pending','pending','" + department + "')"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/user_home"</script>'''
    else:
        return redirect("/")


@app.route('/view_complaint_reply')
def view_complaint_reply():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from user_complaint,department where user_complaint.D_id=department.D_id and  user_complaint.user_id='" + str(session['L_id']) + "'"
        res = db.select(qry)
        return render_template("User/view_reply.html", value=res)
    else:
        return redirect("/")


@app.route('/rating_dept', methods=['get'])
def rating_dept():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from department"
        res = db.select(qry)
        return render_template("User/rating_dpt.html", value=res)
    else:
        return redirect("/")


@app.route('/rating_dept1', methods=['post'])
def rating_dept1():
    if session['ln'] == "kk":
        db = Db()
        department = request.form['select']
        rating = request.form['RadioGroup1']
        qry = "insert into rating values('','" + str(session['L_id']) + "','" + department + "','" + rating + "',curdate())"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/user_home"</script>'''
    else:
        return redirect("/")


@app.route('/diff_issues')
def diff_issues():
    if session['ln'] == "kk":
        return render_template("User/send_issue.html")
    else:
        return redirect("/")


@app.route('/send_issue', methods=['post'])
def send_issue():
    if session['ln'] == "kk":
        db = Db()
        issue = request.form['textarea']
        qry = "insert into issues values('','" + str(session['L_id']) + "','" + issue + "',curdate())"
        db.insert(qry)
        return '''<script>alert("Send successfully");window.location="/user_home"</script>'''
    else:
        return redirect("/")


@app.route('/user_view_notification')
def user_view_notification():
    if session['ln'] == "kk":
        db = Db()
        qry = "select * from notification"
        res = db.select(qry)
        return render_template("User/view_notification.html", value=res)
    else:
        return redirect("/")


########################################## Mayor  chat with Councillor ################################################



@app.route('/chat_with_councillor')
def chat_with_councillor():
    if session['ln'] == "kk":
        return render_template("Mayor/chat.html")
    else:
        return redirect("/")

@app.route('/mayor_mayor_councillor_chat',methods=['post'])
def mayor_mayor_councillor_chat():
    if session['ln'] == "kk":
        db=Db()
        a=session['L_id']
        q1 = "select * from councillor"

        res = db.select(q1)
        v={}
        if len(res)>0:
            v["status"]="ok"
            v['data']=res
        else:
            v["status"]="error"

        rw=demjson.encode(v)
        print(rw)
        return rw
    else:
        return redirect("/")

@app.route('/chatsnd',methods=['post'])
def chatsnd():
    if session['ln'] == "kk":
        db = Db()
        c = session['L_id']
        b=request.form['n']
        print(b)
        m=request.form['m']

        q2="insert into chat_mc(from_id,to_id,message,date) values('"+str(c)+"','"+str(b)+"','"+m+"',curdate())"
        res=db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    else:
        return redirect("/")

@app.route('/chatrply',methods=['post'])
def chatrply():
    if session['ln'] == "kk":
        print("...........................")
        c = session['L_id']
        b=request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from chat_mc ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id']=c
        else:
            v["status"] = "error"
        rw = demjson.encode(v)
        return rw
    else:
        return redirect("/")


######################################### councillor chat with mayor ################################################



@app.route('/chat_with_mayor')
def chat_with_mayor():
    if session['ln'] == "kk":
        return render_template("councillor/mayor_chat.html")
    else:
        return redirect("/")

@app.route('/mayor_mayor_councillor_chat1',methods=['post'])
def mayor_mayor_councillor_chat1():
    if session['ln'] == "kk":
        db=Db()
        a=session['L_id']
        q1 = "select * from mayor"
        res = db.select(q1)
        v={}
        if len(res)>0:
            v["status"]="ok"
            v['data']=res
        else:
            v["status"]="error"

        rw=demjson.encode(v)
        print(rw)
        return rw
    else:
        return redirect("/")

@app.route('/chatsnd1',methods=['post'])
def chatsnd1():
    if session['ln'] == "kk":
        db = Db()
        c = session['L_id']
        b=request.form['n']
        print(b)
        m=request.form['m']

        q2="insert into chat_mc(from_id,to_id,message,date) values('"+str(c)+"','"+str(b)+"','"+m+"',curdate())"
        res=db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    else:
        return redirect("/")

@app.route('/chatrply1',methods=['post'])
def chatrply1():
    if session['ln'] == "kk":
        print("...........................")
        c = session['L_id']
        b=request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from chat_mc ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id']=c
        else:
            v["status"] = "error"
        rw = demjson.encode(v)
        return rw
    else:
        return redirect("/")


######################################### councillor chat with councillor ################################################



@app.route('/c_chat_with_councillor')
def c_chat_with_councillor():
    if session['ln'] == "kk":
        return render_template("councillor/councillor_chat.html")
    else:
        return redirect("/")


@app.route('/mayor_mayor_councillor_chat2', methods=['post'])
def mayor_mayor_councillor_chat2():
    if session['ln'] == "kk":
        db = Db()
        a = session['L_id']
        q1 = "select * from councillor"
        res = db.select(q1)
        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        print(rw)
        return rw
    else:
        return redirect("/")


@app.route('/chatsnd2', methods=['post'])
def chatsnd2():
    if session['ln'] == "kk":
        db = Db()
        c = session['L_id']
        b = request.form['n']
        print(b)
        m = request.form['m']

        q2 = "insert into chat_mc(from_id,to_id,message,date) values('" + str(c) + "','" + str(
            b) + "','" + m + "',curdate())"
        res = db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    else:
        return redirect("/")


@app.route('/chatrply2', methods=['post'])
def chatrply2():
    if session['ln'] == "kk":
        print("...........................")
        c = session['L_id']
        b = request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from chat_mc ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id'] = c
        else:
            v["status"] = "error"
        rw = demjson.encode(v)
        return rw
    else:
        return redirect("/")


######################################### councillor chat with user ################################################



@app.route('/c_chat_with_user')
def c_chat_with_user():
    if session['ln'] == "kk":
        return render_template("councillor/user_chat.html")
    else:
        return redirect("/")


@app.route('/mayor_mayor_councillor_chat3', methods=['post'])
def mayor_mayor_councillor_chat3():
    if session['ln'] == "kk":
        db = Db()
        a = session['L_id']
        q1 = "select * from user"
        res = db.select(q1)
        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        print(rw)
        return rw
    else:
        return redirect("/")


@app.route('/chatsnd3', methods=['post'])
def chatsnd3():
    if session['ln'] == "kk":
        db = Db()
        c = session['L_id']
        b = request.form['n']
        print(b)
        m = request.form['m']

        q2 = "insert into chat_mc(from_id,to_id,message,date) values('" + str(c) + "','" + str(
            b) + "','" + m + "',curdate())"
        res = db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    else:
        return redirect("/")


@app.route('/chatrply3', methods=['post'])
def chatrply3():
    if session['ln'] == "kk":
        print("...........................")
        c = session['L_id']
        b = request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from chat_mc ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id'] = c
        else:
            v["status"] = "error"
        rw = demjson.encode(v)
        return rw
    else:
        return redirect("/")

######################################### user chat with councillor ################################################



@app.route('/user_chat_with_councillor')
def user_chat_with_councillor():
    if session['ln'] == "kk":
        return render_template("User/user_chat_councillor.html")
    else:
        return redirect("/")


@app.route('/mayor_mayor_councillor_chat4', methods=['post'])
def mayor_mayor_councillor_chat4():
    if session['ln'] == "kk":
        db = Db()
        a = session['L_id']
        q1 = "select * from councillor"
        res = db.select(q1)
        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
        else:
            v["status"] = "error"

        rw = demjson.encode(v)
        print(rw)
        return rw
    else:
        return redirect("/")


@app.route('/chatsnd4', methods=['post'])
def chatsnd4():
    if session['ln'] == "kk":
        db = Db()
        c = session['L_id']
        b = request.form['n']
        print(b)
        m = request.form['m']

        q2 = "insert into chat_mc(from_id,to_id,message,date) values('" + str(c) + "','" + str(
            b) + "','" + m + "',curdate())"
        res = db.insert(q2)
        v = {}
        if int(res) > 0:
            v["status"] = "ok"

        else:
            v["status"] = "error"

        r = demjson.encode(v)

        return r
    else:
        return redirect("/")


@app.route('/chatrply4', methods=['post'])
def chatrply4():
    if session['ln'] == "kk":
        print("...........................")
        c = session['L_id']
        b = request.form['n']
        print("<<<<<<<<<<<<<<<<<<<<<<<<")
        print(b)
        t = Db()
        qry2 = "select * from chat_mc ORDER BY chat_id ASC ";
        res = t.select(qry2)
        print(res)

        v = {}
        if len(res) > 0:
            v["status"] = "ok"
            v['data'] = res
            v['id'] = c
        else:
            v["status"] = "error"
        rw = demjson.encode(v)
        return rw
    else:
        return redirect("/")


if __name__ == '__main__':
    app.run()
