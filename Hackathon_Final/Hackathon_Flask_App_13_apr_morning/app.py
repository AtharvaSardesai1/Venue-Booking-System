import bcrypt

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import re
import bcrypt

from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import re
from datetime import datetime, timedelta
app = Flask(__name__)

app.secret_key = 'Guitar'


# MySQL configuration
mysql_config = {
    'host': 'localhost',
    'user': 'arnav-rppoop1',
    'password': 'Guitar@123',
    'database': 'db_2'
}

# Initialize MySQL connection
mysql_connection = mysql.connector.connect(**mysql_config)
print("helll")
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    # if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    #     username = request.form['username']
    #     password = request.form['password']
    #     cursor = mysql_connection.cursor(dictionary=True)
    #     # cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
    #     cursor.execute('SELECT password FROM accounts WHERE username = %s', (username,))
    #     hashed_password = cursor.fetchone()
    #     account = cursor.fetchone()

    #     if account:
    #         session['loggedin'] = True
    #         session['id'] = account['id']
    #         session['username'] = account['username']
    #         session['du'] = 'Arnav Prasad'
    #         print(session)
    #         msg = 'Logged in successfully!'
    #         return render_template('index.html', msg=msg)
    #     else:
    #         msg = 'Incorrect username / password!'
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account:
            hashed_password = account['password']
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                # Passwords match, log in the user
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                session['du'] = 'Arnav Prasad'
                session['email'] = account['email']
                session['incharge'] = account['incharge']
                msg = 'Logged in successfully!'
                print(session)
                return render_template('user_venue_booking_page.html', msg=msg)
            else:
                # Passwords do not match
                msg = 'Incorrect username / password!'
        else:
            # No account found for the given username
            msg = 'Incorrect username / password!'

    return render_template('login2.html', msg=msg)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email, venue, date, time,flag,name):      
    # Email configuration
    sender_email = "rppoop@outlook.com"
    sender_password = "Aaditya@Anish#Bhargav"
    receiver_email = email
    smtp_server = "smtp.office365.com"
    smtp_port = 587  # Outlook.com SMTP port

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "BOOKING STATUS"

    # Email body
    if flag=="student":
        body = f"Your booking in {venue} on {date} at {time} has been confirmed.\n"
    elif flag=="realloc":
        body = f"{name},\nI wanted to inform you that your event has been rescheduled to {venue} at {time} on {date}.\nWe apologize for any inconvenience this may cause and appreciate your understanding.\nYour request is pending, you will receive a mail on confirmation."
    else:
        body = f"A request has been made for {venue} on {date} at {time}.\n" 
    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Email sent successfully!")

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Hash a password
            # password = b"mysecretpassword"
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # cursor.execute('INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)', (username, hashed_password, email))
            cursor.execute('INSERT INTO accounts (role,username, password, email) VALUES (%s , %s, %s, %s)', ('USER',username, hashed_password, email))
            mysql_connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register2.html', msg=msg)

#outsider login
@app.route('/outsider_login', methods=['GET', 'POST'])
def outsider_login():
    msg = ''
    # if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    #     username = request.form['username']
    #     password = request.form['password']
    #     cursor = mysql_connection.cursor(dictionary=True)
    #     # cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
    #     cursor.execute('SELECT password FROM accounts WHERE username = %s', (username,))
    #     hashed_password = cursor.fetchone()
    #     account = cursor.fetchone()

    #     if account:
    #         session['loggedin'] = True
    #         session['id'] = account['id']
    #         session['username'] = account['username']
    #         session['du'] = 'Arnav Prasad'
    #         print(session)
    #         msg = 'Logged in successfully!'
    #         return render_template('index.html', msg=msg)
    #     else:
    #         msg = 'Incorrect username / password!'
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account:
            hashed_password = account['password']
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')) and account['role']=='OUT':
                # Passwords match, log in the user
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
                session['du'] = 'Arnav Prasad'
                session['email'] = account['email']
                session['incharge'] = account['incharge']
                msg = 'Logged in successfully!'
                print(session)
                return render_template('outsider_venue_booking_page.html', msg=msg)
            else:
                # Passwords do not match
                msg = 'Incorrect username / password!'
        else:
            # No account found for the given username
            msg = 'Incorrect username / password!'

    return render_template('outsider_login.html', msg=msg)

@app.route('/outsider_register', methods=['GET', 'POST'])
def outsider_register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Hash a password
            # password = b"mysecretpassword"
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # cursor.execute('INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)', (username, hashed_password, email))
            cursor.execute('INSERT INTO accounts (role,username, password, email) VALUES (%s , %s, %s, %s)', ('OUT',username, hashed_password, email))
            mysql_connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('outsider_register.html', msg=msg)


#admin login and register functions: 

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'admin_password' in request.form:
        username = request.form['username']
        password = request.form['password']
        admin_password = request.form['admin_password']
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()

        if account:
            hashed_password = account['password']
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                # Passwords match, now check admin password
                if admin_password == 'hackathon' and account['role']=='ADMIN':
                    # Admin login successful
                    session['admin_loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    session['loggedin'] = True
                    session['du'] = 'Arnav Prasad'
                    session['email'] = account['email']
                    session['incharge'] = account['incharge']
                    msg = 'Admin logged in successfully!'
                    return render_template('admin_dashboard.html', msg=msg)
                else:
                    msg = 'Incorrect admin password!'
            else:
                # User password incorrect
                msg = 'Incorrect username / password!'
        else:
            # No account found for the given username
            msg = 'Incorrect username / password!'

    return render_template('admin_login.html', msg=msg)

@app.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'admin_password' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        admin_password = request.form['admin_password']
        incharge=request.form['incharge']
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email or not admin_password:
            msg = 'Please fill out the form!'
        elif admin_password != 'hackathon':
            msg = 'Incorrect admin password!'
        else:
            # Hash a password
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            # cursor.execute('INSERT INTO accounts (username, password, email) VALUES (%s, %s, %s)', (username, hashed_password, email))
            cursor.execute('INSERT INTO accounts (incharge, role,username, password, email) VALUES (%s, %s , %s, %s, %s)', (incharge, 'ADMIN',username, hashed_password, email))
            mysql_connection.commit()
            msg = 'Admin registered successfully!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('admin_register.html', msg=msg)


#ending of admin login and register functions.

# @app.route('/')
# def index():
#     return render_template('cards2.html')

# @app.route('/display_request_form')
# def requestform():
#     return render_template('user_venue_request_form.html')

@app.route('/display_outsider_request_form')
def outsider_requestform():
    return render_template('outsider_venue_request_form.html')

# @app.route('/process_venue_booking_request')
# def process_venue_booking_request():
#     index = request.args.get('index')
#     print(index)
#     # print(encodeURIComponent(index))
#     print("yessssssssss i ammmmmmmmmmm hereeeeeeeeeeeeee")
#     return redirect(url_for('display_venue_request_admin'))
#     # return render_template('venue_request_admin.html')


#ending of admin login and register functions.

# @app.route('/')
# def index():
#     return render_template('cards2.html')

import pandas as pd
import os

def process_booking(response_file_path):
    # Read CSV file into a DataFrame
    response_df = pd.read_csv(response_file_path)

    # Check if the response DataFrame is empty
    if response_df.empty:
        print("Response DataFrame is empty. No bookings to process.")
        return

    # Get the last row of the response DataFrame
    response_last_row = response_df.iloc[-1]

    # Construct file path for booking based on venue selection
    file_path_booking = f"{response_last_row['Venue_Selection']}_booking.csv"

    # Check if the booking file exists and is not empty
    if os.path.exists(file_path_booking) and os.path.getsize(file_path_booking) > 0:
        # Read existing booking DataFrame
        booking_df = pd.read_csv(file_path_booking)
    else:
        # Create an empty booking DataFrame if the file doesn't exist or is empty
        booking_df = pd.DataFrame()

        # print(booking_df['Event Date'])
        # print(response_last_row['Event Date'])

    if ((booking_df['Name'] == response_last_row['Name']) & (booking_df['Event_Date'] == response_last_row['Event_Date'])).any():
        print("Booking with the same Name and Date already exists. Skipping...")
        return

    new_row_data = response_last_row

    # Append the new row to the booking DataFrame
    booking_df = booking_df._append(new_row_data, ignore_index=True)

    # Drop duplicate rows if any
    booking_df = booking_df.drop_duplicates()
    print(booking_df)

    # Save the booking DataFrame to CSV file
    booking_df.to_csv(file_path_booking, index=False)
    send_email(response_last_row['College_Email'], new_row_data['Venue_Selection'], new_row_data['Event_Date'], new_row_data['Event_Time'],"student","")

    print("Booking processed and saved successfully.")

# Example usage:
# response_file_path = 'response_mine_1.csv'  # Replace with the actual path to your response file
# process_booking(response_file_path)


def process_booking_realloc(response_file_path):
    # Read CSV file into a DataFrame
    response_df = pd.read_csv(response_file_path)

    # Check if the response DataFrame is empty
    if response_df.empty:
        print("Response DataFrame is empty. No bookings to process.")
        return

    # Get the last row of the response DataFrame
    response_last_row = response_df.iloc[-1]

    # Construct file path for booking based on venue selection
    file_path_booking = f"{response_last_row['2nd_Choice']}_booking.csv"

    # Check if the booking file exists and is not empty
    if os.path.exists(file_path_booking) and os.path.getsize(file_path_booking) > 0:
        # Read existing booking DataFrame
        booking_df = pd.read_csv(file_path_booking)
    else:
        # Create an empty booking DataFrame if the file doesn't exist or is empty
        booking_df = pd.DataFrame()

        # print(booking_df['Event Date'])
        # print(response_last_row['Event Date'])

    if ((booking_df['Name'] == response_last_row['Name']) & (booking_df['Event_Date'] == response_last_row['Event_Date'])).any():
        print("Booking with the same Name and Date already exists. Skipping...")
        return

    new_row_data = response_last_row

    # Append the new row to the booking DataFrame
    booking_df = booking_df._append(new_row_data, ignore_index=True)

    # Drop duplicate rows if any
    booking_df = booking_df.drop_duplicates()
    print(booking_df)

    import mysql.connector

    # Connect to your MySQL server
    conn = mysql.connector.connect(
        host="localhost",
        user="arnav-rppoop1",
        password="Guitar@123",
        database="db_2"
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Define your SQL query
    # Define your SQL query with a WHERE condition
    incharge_name =  new_row_data['Venue_Selection']# Specify the incharge name here
    query = "SELECT email FROM accounts WHERE incharge = %s"

    # Execute the query
    cursor.execute(query, (incharge_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Extract the email addresses from the rows
    emails = [row[0] for row in rows]

    # Print the email addresses
    for email in emails:
        print(email)

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    # Save the booking DataFrame to CSV file
    booking_df.to_csv(file_path_booking, index=False)
    send_email(email, new_row_data['Venue_Selection'], new_row_data['Event_Date'], new_row_data['Event_Time'],"admin","")
    send_email(new_row_data['College_Email'], new_row_data['Venue_Selection'], new_row_data['Event_Date'],new_row_data['Event_Time'],"realloc",new_row_data['Name'])

    print("Booking processed and saved successfully.")


import numpy as np
def handleCollision(CSVfileName, input_row):

    # get data from csv file
    df=pd.read_csv(CSVfileName)

    print('heyyy')
    # pendingReq=df ['Status']
    event_date = input_row['Event_Date']
    pendingReq = df[df['Event_Date'] == event_date]['Status']
    print('fffffffffffffffffffff')

    # pendingReq=df[df['Event_Date'] == input_row['Event_Date'].item()]['Status']
    print("hhhhhhhhh")
    print("*")
    print(pendingReq)
    # print(any(status == 'Approved' for status in pendingReq))
    print('here')

    # check if someone has been already approved or not on that DATE
    if not any(status == 'Approved' for status in pendingReq):
        print('yayyyyyyyyyyyyyyy')
        # Find the index of the row where the 'Name' column has the value 'Charlie'
            # row_index = df.loc[df['Name'] == name].index[0]
        print(df)
        print(type(df))
        print(input_row)
        print(type(input_row))
        relevant_columns = ['Name', 'Event_Time', 'Event_Date', 'Venue_Selection']
        df_relevant = df[relevant_columns]

        input_row_relevant = input_row[relevant_columns]

        row_index = df_relevant[df_relevant.eq(input_row_relevant).all(axis=1)].index[0]

            # Update the 'Status' column of the found row to 'Approved'
        df.at[row_index, 'Status'] = 'Approved'

        # input_row['Event_Time'] = pd.to_datetime('08:00:00').time()
        # input_row['E'] = pd.to_datetime('17:00:00').time()
        start_time = input_row['Event_Time']
        duration = input_row['Event_Duration']

        # start_time_str = '11:00:00'
        start_time = datetime.strptime(start_time, '%H:%M:%S').time()

        duration = np.int64(3)  # Example value of duration

        # Convert duration to a regular Python integer
        duration_hours = int(duration)

        # Define the duration
        duration = timedelta(hours=duration_hours)

        # Combine the current date with the start time
        combined_datetime = datetime.combine(datetime.today(), start_time)

        # Calculate the end time by adding the duration
        end_time = (combined_datetime + duration).time()


        for index, row in df.iterrows():
            # event_time = pd.to_datetime(row['Event_Time']).time()
            event_time_str = row['Event_Time']
            event_time = datetime.strptime(event_time_str, '%H:%M:%S').time()
            # event_time = datetime.strptime(row['Event_Time'], '%H:%M:%S').time()

            duration_hours = int(row['Event_Duration'])
            
            duration_row = timedelta(hours=duration_hours)

            combined_datetime = datetime.combine(datetime.today(), event_time)
        # Calculate the end time
            # end_time_row = (datetime.datetime.combine(datetime.date.today(), event_time) + duration_row).time()
            end_time_row = (combined_datetime + duration_row).time()

            if (start_time <= event_time <= end_time) or (start_time <= end_time_row<=end_time):
                df.drop(index, inplace=True)
        send_email(input_row['College_Email'], input_row['Venue_Selection'], input_row['Event_Date'], input_row['Event_Time'],"student",str(session.get('username','unknown')))
        df.to_csv(CSVfileName,index=False)

    else:
        print("in else block")
        str_status = "Approved"
        specific_row = df[df['Status'] == str_status]


        new_choice_file = str((specific_row['2nd_Choice']).item()) + "_booking.csv"

        # Save the specific row to the new choice file
        specific_row['Status'] = 'Pending'
        print('qqqqqqqqqqqqqqq')
        print(specific_row)
        specific_row.to_csv(new_choice_file, index=False)
        process_booking_realloc(new_choice_file)

        df = df.drop(index=specific_row.index)

        

        # Save the DataFrame back to the CSV file
        # df.to_csv(new_choice_file, index=False)
        # process_booking_realloc(new_choice_file)

        relevant_columns = ['Name', 'Event_Time', 'Event_Date', 'Venue_Selection']
        df_relevant = df[relevant_columns]

        input_row_relevant = input_row[relevant_columns]

        row_index = df_relevant[df_relevant.eq(input_row_relevant).all(axis=1)].index[0]



        # Update the 'Status' column of the found row to 'Approved'
        df.at[row_index, 'Status'] = 'Approved'

        file = str(df['Venue_Selection'].item()) + '_booking.csv'
        
        print('------------------------')
        print(input_row)
        send_email(input_row['College_Email'], input_row['Venue_Selection'], input_row['Event_Date'], input_row['Event_Time'],"student","")
        df.to_csv(file,index=False)

        


@app.route('/display_request_form')
def requestform():
    return render_template('user_venue_request_form.html')

@app.route('/process_venue_booking_request')
def process_venue_booking_request():
    index = request.args.get('index')
    print(index)
    admin_name = session.get('name','Unknown')
    admin_incharge = session.get('incharge','Unknown')

    file_name = admin_incharge + "_booking.csv"
    print('((((((((((((((((()))))))))))))))))')
    print(type(index))
    print(file_name)

    df = pd.read_csv(file_name)

    # Filter the DataFrame based on the specified criteria
    # filtered_df = df[(df['Name'] == name) & (df['Event_Time'] == time) & (df['Event_Date'] == date)]
    filtered_df = df.iloc[int(index)]

    # print(encodeURIComponent(index))
    print("yessssssssss i ammmmmmmmmmm hereeeeeeeeeeeeee")

    handleCollision(file_name, filtered_df)
    return redirect(url_for('display_venue_request_admin'))
    # return render_template('venue_request_admin.html')


@app.route('/display_user_venue_cancel')
def display_user_venue_cancel():
    # file_name = str(session.get('incharge','Unknown')) + "_booking.csv"
    file_name = str(session.get('username','unknown')) + ".csv"
    print(file_name)

    # Initialize lists to store data from the CSV file
    name_arr=[]
    email_arr=[]
    contact_arr=[]
    event_name_arr=[]
    event_date_arr=[]
    capacity_arr=[]
    event_time_arr=[]
    event_duration_arr=[]
    venue_selection_arr=[]
    purpose_arr=[]
    status_arr=[]
    second_choice_arr=[]

    # Name,College_Email,Contact_Number,Event_Name,Event_Date,Capacity,Event_Time,Event_Duration,Venue_Selection,Purpose,Status,2nd Choice

    # Read data from the CSV file
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name_arr.append(row['Name'])
            email_arr.append(row['College_Email'])
            contact_arr.append(row['Contact_Number'])
            event_name_arr.append(row['Event_Name'])
            event_date_arr.append(row['Event_Date'])
            capacity_arr.append(row['Capacity'])
            event_time_arr.append(row['Event_Time'])
            event_duration_arr.append(row['Event_Duration'])
            venue_selection_arr.append(row['Venue_Selection'])
            purpose_arr.append(row['Purpose'])
            status_arr.append(row['Status'])
            second_choice_arr.append(row['2nd_Choice'])
        print("Name Array:", name_arr)
        print("Email Array:", email_arr)
        print("Contact Array:", contact_arr)
        print("Event Name Array:", event_name_arr)
        print("Event Date Array:", event_date_arr)
        print("Capacity Array:", capacity_arr)
        print("Event Time Array:", event_time_arr)
        print("Event Duration Array:", event_duration_arr)
        print("Venue Selection Array:", venue_selection_arr)
        print("Purpose Array:", purpose_arr)
        print("Status Array:", status_arr)
        print("Second Choice Array:", second_choice_arr)

    return render_template('user_venue_cancel.html', names=name_arr,
                           emails=email_arr,
                           contacts=contact_arr,
                           event_names=event_name_arr,
                           event_dates=event_date_arr,
                           capacities=capacity_arr,
                           event_times=event_time_arr,
                           event_durations=event_duration_arr,
                           venue_selections=venue_selection_arr,
                           purposes=purpose_arr,
                           statuses=status_arr,
                           second_choices=second_choice_arr)
    # return render_template('user_venue_cancel.html')

@app.route('/cancel_venue_booking_request')
def cancel_venue_booking_request():
    index = request.args.get('index')
    print(index)
    admin_name = session.get('name','Unknown')
    admin_incharge = session.get('incharge','Unknown')

    file_name = admin_incharge + "_booking.csv"
    print('((((((((((((((((()))))))))))))))))')
    print(type(index))
    print(file_name)

    df = pd.read_csv(file_name)

    # Filter the DataFrame based on the specified criteria
    # filtered_df = df[(df['Name'] == name) & (df['Event_Time'] == time) & (df['Event_Date'] == date)]
    filtered_df = df.iloc[int(index)]

    # print(encodeURIComponent(index))
    print("yessssssssss i ammmmmmmmmmm hereeeeeeeeeeeeee")

    handleCollision(file_name, filtered_df)
    return redirect(url_for('display_user_venue_cancel'))

from datetime import datetime
import pandas as pd
import os

#arrays to store form data:
name_arr = []
email_arr = []
contact_arr = []
event_name_arr = []
event_date_arr = []
capacity_arr = []
event_time_arr = []
event_duration_arr = []
venue_selection_arr = []
purpose_arr = []
status_arr = []
second_choice_arr = []

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # fullname = request.form['fullname']
    # email=request.form['email']
    contact=request.form['mobile_num']
    venue = request.form['venue']
    second_venue = request.form['venue_second']
    event_name=request.form['event_name']
    purpose = request.form['purpose']
    capacity=request.form['capacity']
    datep = request.form['date']
    time = request.form['time']

    print(time)
    print(type(time))

    # Original datetime string
    original_datetime = datep

    # Convert the string to a datetime object
    dt_object = datetime.strptime(original_datetime, "%Y-%m-%dT%H:%M")

    # Extract date and time components
    date_component = dt_object.strftime("%d/%m/%Y")
    time_component = dt_object.strftime("%H:%M:%S")

    print("Date:", date_component)
    print("Time:", time_component)

    data = {
        # 'fullname': [fullname],
        'Name' : session.get('username', 'Unknown'),
        # 'email': [email],
        'College_Email' : session.get('email', 'Unknown'),
        'Contact_Number': contact,
        'Event_Name': event_name,
        'Event_Date': date_component,
        'Capacity': capacity,
        'Event_Time' : time_component,
        'Event_Duration': time,
        'Venue_Selection': venue,
        'Purpose': purpose,
        'Status' : 'Pending',
        '2nd Choice': second_venue
    }
    # data = {
    #     'Name': [session.get('username', 'Unknown')],
    #     'College_Email': [session.get('email', 'Unknown')],
    #     'Contact_Number': [contact],
    #     'Event_Name': [event_name],
    #     'Event_Date': [date_component],
    #     'Capacity': [capacity],
    #     'Event_Time': [time_component],
    #     'Event_Duration': [time],
    #     'Venue_Selection': [venue],
    #     'Purpose': [purpose],
    #     'Status': ['Pending'],
    #     '2nd Choice': [second_venue]
    # }

    # Create a DataFrame using the dictionary
    df = pd.DataFrame(data,index=[0])
    print('--------------------------')
    print(df)

    # Construct file path for booking based on venue selection
    file_path_booking =str(venue) + "_booking.csv"


    if os.path.exists(file_path_booking) and os.path.getsize(file_path_booking) > 0:
        # Read existing booking DataFrame
        booking_df = pd.read_csv(file_path_booking)
        if ((booking_df['Event_Name'] == session.get('username', 'Unknown')) & (booking_df['Event_Date'] == date_component)).any():
            print("Booking with the same Name and Date already exists. Skipping...")
            return
    else:
        # Create an empty booking DataFrame if the file doesn't exist or is empty
        booking_df = pd.DataFrame()

    
    
    # booking_df
    # new_row_data = response_last_row
    import mysql.connector
    conn = mysql.connector.connect(
    host="localhost",
    user="arnav-rppoop1",
    password="Guitar@123",
    database="db_2"
    )   

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Define the username for which you want to retrieve the role
    desired_username = session.get('username', 'Unknown')

    # Define your SQL query
    sql_query = "SELECT role FROM accounts WHERE username = %s"

    # Execute the SQL query
    cursor.execute(sql_query, (desired_username,))

    # Fetch the result
    role = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    conn.close()

    print('--------------------------------------------------')
    match_found = False
    if (role == 'User'):
        for index, row in booking_df.iterrows():
            # Check if event dates match
            if row['Event_Date'] == date_component:
                # Convert event times to datetime objects for comparison
                event_time = pd.to_datetime(row['Event_Time'])
                new_event_time = pd.to_datetime(time_component)

                # Calculate end time of existing event
                end_time = event_time + pd.Timedelta(hours=row['Event_Duration'])

                # Check if the new event time falls within the existing event slot
                if new_event_time >= event_time and new_event_time < end_time:
                    print('Cannot add the slot, as it overlaps with an existing booking.')
                    match_found = True
                    break
        
    if (match_found == False):

        # Append the new row to the booking DataFrame
        booking_df = booking_df._append(data, ignore_index=True)

        name_file = data['Name'] + ".csv"
        print(name_file)
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        dp = pd.DataFrame(data,index=[0])
        print(dp)
        dp.to_csv(name_file, index=False)

        # Drop duplicate rows if any
        booking_df = booking_df.drop_duplicates()
        print(booking_df)

        # Save the booking DataFrame to CSV file
        booking_df.to_csv(file_path_booking, index=False)

        import mysql.connector

        # Connect to your MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="arnav-rppoop1",
            password="Guitar@123",
            database="db_2"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Define your SQL query with a WHERE condition
        incharge_name = data['Venue_Selection']  # Specify the incharge name here
        query = "SELECT email FROM accounts WHERE incharge = %s"

        # Execute the query with the parameter value
        cursor.execute(query, (incharge_name,))

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Extract the email addresses from the rows
        emails = [row[0] for row in rows]

        # Print the email addresses
        for email in emails:
            print(email)

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        print('eeeeeeeeeeeeeeeeeeee')
        print(email)

        send_email(email, data['Venue_Selection'], data['Event_Date'], data['Event_Time'],"admin","")
        print("Booking processed and saved successfully.")


    name_arr.append(session.get('username', 'Unknown'))
    email_arr.append(session.get('email', 'Unknown'))
    contact_arr.append(contact)
    event_name_arr.append(event_name)
    event_date_arr.append(date_component)
    capacity_arr.append(capacity)
    event_time_arr.append(time_component)
    event_duration_arr.append(time)
    venue_selection_arr.append(venue)
    purpose_arr.append(purpose)
    status_arr.append('Pending')
    second_choice_arr.append(second_venue)
    # Now you have the form data in variables
    # You can process or store them as required
    # For demonstration, I'll just print them
    print(f"Fullname: {session.get('username', 'Unknown')}, email-id: {session.get('email', 'Unknown')}, Contact: {contact}, Venue: {venue},  second venue: {second_venue}, Event name: {event_name},  Purpose: {purpose}, Capacity: {capacity}, Date and start time: {datep}, Time: {time}")
    return render_template('user_venue_request_form.html')

print("Name Array:", name_arr)
print("Email Array:", email_arr)
print("Contact Array:", contact_arr)
print("Event Name Array:", event_name_arr)
print("Event Date Array:", event_date_arr)
print("Capacity Array:", capacity_arr)
print("Event Time Array:", event_time_arr)
print("Event Duration Array:", event_duration_arr)
print("Venue Selection Array:", venue_selection_arr)
print("Purpose Array:", purpose_arr)
print("Status Array:", status_arr)
print("Second Choice Array:", second_choice_arr)

@app.route('/display_admin_dashboard')
def display_admin_dashboard():
    return render_template('admin_dashboard.html')


import csv
@app.route('/display_venue_request_admin')
def display_venue_request_admin():
    #   'Name' : session.get('username', 'Unknown'),
    file_name = str(session.get('incharge','Unknown')) + "_booking.csv"
    print(file_name)

    # Initialize lists to store data from the CSV file
    name_arr=[]
    email_arr=[]
    contact_arr=[]
    event_name_arr=[]
    event_date_arr=[]
    capacity_arr=[]
    event_time_arr=[]
    event_duration_arr=[]
    venue_selection_arr=[]
    purpose_arr=[]
    status_arr=[]
    second_choice_arr=[]

    # Name,College_Email,Contact_Number,Event_Name,Event_Date,Capacity,Event_Time,Event_Duration,Venue_Selection,Purpose,Status,2nd Choice

    # Read data from the CSV file
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name_arr.append(row['Name'])
            email_arr.append(row['College_Email'])
            contact_arr.append(row['Contact_Number'])
            event_name_arr.append(row['Event_Name'])
            event_date_arr.append(row['Event_Date'])
            capacity_arr.append(row['Capacity'])
            event_time_arr.append(row['Event_Time'])
            event_duration_arr.append(row['Event_Duration'])
            venue_selection_arr.append(row['Venue_Selection'])
            purpose_arr.append(row['Purpose'])
            status_arr.append(row['Status'])
            second_choice_arr.append(row['2nd_Choice'])
        print("Name Array:", name_arr)
        print("Email Array:", email_arr)
        print("Contact Array:", contact_arr)
        print("Event Name Array:", event_name_arr)
        print("Event Date Array:", event_date_arr)
        print("Capacity Array:", capacity_arr)
        print("Event Time Array:", event_time_arr)
        print("Event Duration Array:", event_duration_arr)
        print("Venue Selection Array:", venue_selection_arr)
        print("Purpose Array:", purpose_arr)
        print("Status Array:", status_arr)
        print("Second Choice Array:", second_choice_arr)

    return render_template('venue_request_admin.html', names=name_arr,
                           emails=email_arr,
                           contacts=contact_arr,
                           event_names=event_name_arr,
                           event_dates=event_date_arr,
                           capacities=capacity_arr,
                           event_times=event_time_arr,
                           event_durations=event_duration_arr,
                           venue_selections=venue_selection_arr,
                           purposes=purpose_arr,
                           statuses=status_arr,
                           second_choices=second_choice_arr)

@app.route('/display_timetable_input_form')
def display_timetable_input_form():
    return render_template('timetable_input_form.html')

from tt import *

def tt_input_sy(num_subjects,num_labs,subjects ,lab_subjects ):
    
    # year is there assuming year = year
    # consider 2 div
    sy_div1=SY_DIV1()    
    sy_div2=SY_DIV2() 

    l_subject=[]
    l_lab=[]
    for a in subjects:
        new=Subject(a[0],a[2],a[1],2)
        l_subject.append(new)
    for a in lab_subjects:
        new=Subject(a[0],a[2],a[1],2)
        l_lab.append(new)

    
    sy_div1.RandomiseTT(sy_subjectList,0)
    sy_div1.RandomiseTT(sy_labList, 1)
    sy_div2.RandomiseTT(sy_subjectList,0)
    sy_div2.RandomiseTT(sy_labList,1)

    SY_COMP(sy_div1,sy_div2)

    sy_data1=sy_div1.generate_data()
    sy_data2=sy_div2.generate_data()

    write_to_csv('sy_division1_timetable.csv', sy_data1)
    write_to_csv('sy_division2_timetable.csv', sy_data2) 

def tt_input_ty(num_subjects,num_labs,subjects ,lab_subjects ):
    
    # year is there assuming year = year
    # consider 2 div
    ty_div1=TY_DIV1()    
    ty_div2=TY_DIV2() 

    l_subject=[]
    l_lab=[]
    for a in subjects:
        new=Subject(a[0],a[2],a[1],2)
        l_subject.append(new)
    for a in lab_subjects:
        new=Subject(a[0],a[2],a[1],2)
        l_lab.append(new)

    
    ty_div1.RandomiseTT(sy_subjectList,0)
    ty_div1.RandomiseTT(sy_labList, 1)
    ty_div2.RandomiseTT(sy_subjectList,0)
    ty_div2.RandomiseTT(sy_labList,1)

    TY_COMP(sy_div1,sy_div2)

    ty_data1=ty_div1.generate_data()
    ty_data2=ty_div2.generate_data()

    write_to_csv('sy_division1_timetable.csv', ty_data1)
    write_to_csv('sy_division2_timetable.csv', ty_data2)


@app.route('/process_timetable_input_form', methods=['POST'])
def process_timetable_input_form():
    if request.method == 'POST':
        num_subjects = int(request.form['num_subjects'])
        num_labs = int(request.form['num_labs'])

        subjects = []
        lab_subjects = []

        for i in range(1, num_subjects + 1):
            subject_name = request.form[f'Subject{i}']
            faculties = [request.form[f'faculty{i}.{j}'] for j in range(1, 4)]  # Adjusted to handle 3 faculties per subject
            credits = int(request.form[f'credits{i}'])

            subjects.append((subject_name, faculties, credits))

        for i in range(1, num_labs + 1):
            lab_name = request.form[f'lab{i}']
            faculties = [request.form[f'lab_faculty{i}.{j}'] for j in range(1, 4)]  # Adjusted to handle 3 faculties per lab
            credits = int(request.form[f'lab_credits{i}'])
            venue = request.form[f'lab_venue{i}']

            lab_subjects.append((lab_name, faculties, credits, venue))
        
        # Print all arrays for debugging
        print("Subjects:")
        for subject in subjects:
            print(subject)

        print("Lab Subjects:")
        for lab_subject in lab_subjects:
            print(lab_subject)

        
        # Generate timetable logic

        return render_template('timetable_input_form.html')

if __name__ == '__main__':
    app.run(debug=True)


print('done!!')