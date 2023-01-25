import sqlite3
from datetime import datetime
from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__) 
root = '/api/v1'

# connect to database
conn = sqlite3.connect('reminder.db', check_same_thread=False)  
cursor = conn.cursor()
if not os.path.exists('reminder.db') or os.stat('reminder.db').st_size == 0:
    cursor.execute('''
        CREATE TABLE reminder (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            date DATE NOT NULL,
            time TIME
        );
    ''')    
    print('Reminder table created successfully')
    cursor.execute('''
        CREATE TABLE history (
            task_id INTEGER NOT NULL,
            status VARCHAR(255) NOT NULL,
            date DATE not NULL,
            time DATE NOT NULL
        );
    ''')  
    print('History table created successfully')
    cursor.execute('INSERT INTO reminder (task, date, time) VALUES ("iLab2 - YE.1", "2023-01-31", "23:59:59")')   
    cursor.execute('INSERT INTO history (task_id, status, date, time) VALUES (1, "TEST", "2023-01-01", "00:00:00")')
    conn.commit()

# get all reminders
@app.route(root + '/reminders')
def get_all_reminders():
    cursor.execute('SELECT * FROM reminder')
    reminders = cursor.fetchall()
    output = []
    for reminder in reminders:
        reminder_dict = { 'id': reminder[0], 'task': reminder[1], 'date': reminder[2], 'time': reminder[3] }
        output.append(reminder_dict)
    return jsonify(output)

# get a reminder by id
@app.route(root + '/reminders/<id>')
def get_reminder(id):
    cursor.execute('SELECT * FROM reminder WHERE id = ?', (id,))
    reminder = cursor.fetchone()
    if reminder:
        return  jsonify({ 'id': reminder[0], 'task': reminder[1], 'date': reminder[2], 'time': reminder[3]})
    else:
        return 'Reminder not found', 404

# add a reminder
@app.route(root + '/reminders', methods=['POST'])
def add_reminder():
    reminder = request.get_json()
    cursor.execute('INSERT INTO reminder (task, date, time) VALUES (?, ?, ?)', (reminder['task'], reminder['date'], reminder['time']))
    cursor.execute('INSERT INTO history (task_id, status, date, time) VALUES (?, ?, ?, ?)', (cursor.lastrowid, 'CREATED', datetime.today().strftime('%Y-%m-%d'), datetime.now().strftime('%H:%M:%S')))
    conn.commit()
    return 'Reminder added successfully', 201

# update a reminder
@app.route(root + '/reminders/<id>', methods=['PUT'])
def update_reminder(id):
    reminder = request.get_json()
    cursor.execute('UPDATE reminder SET task = ?, date = ?, time = ? WHERE id = ?', (reminder['task'], reminder['date'], reminder['time'], id))
    cursor.execute('INSERT INTO history (task_id, status, date, time) VALUES (?, ?, ?, ?)', (id, 'UPDATED', datetime.today().strftime('%Y-%m-%d'), datetime.now().strftime('%H:%M:%S')))
    conn.commit()
    return 'Reminder updated successfully', 200

@app.route(root + '/reminders/<id>', methods=['DELETE'])
def delete_reminder(id):
    cursor.execute('DELETE FROM reminder WHERE id = ?', (id,))
    cursor.execute('INSERT INTO history (task_id, status, date, time) VALUES (?, ?, ?, ?)', (id, 'DELETED', datetime.today().strftime('%Y-%m-%d'), datetime.now().strftime('%H:%M:%S')))
    conn.commit()
    return 'Reminder deleted successfully', 200

@app.route(root + '/histories')
def get_histories():
    cursor.execute('SELECT * FROM history')
    histories = cursor.fetchall()
    output = []
    for history in histories:
        history_dict = { 'task_id': history[0], 'status': history[1], 'date': history[2], 'time': history[3] }
        output.append(history_dict)
    return output

if __name__ == '__main__':
    app.run(port=8080)
