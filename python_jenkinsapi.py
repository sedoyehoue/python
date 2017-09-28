#!/usr/bin/python

from jenkinsapi.jenkins import Jenkins

import sqlite3
import datetime


#Connect to databse
conn = sqlite3.connect('job_db.db')

#print "Opened database successfully";

#Create SQL table JOB in the database
conn.execute('''CREATE TABLE JOB
         (ID      INT PRIMARY KEY      NOT NULL AUTOINCREMENT,
         job_name            TEXT      NOT NULL,
         job_description     TEXT,
         job_status          BOOLEAN   NOT NULL,
         job_enable          BOOLEAN,
         Job_datetime        TIMESTAMP);''')
print "Table created successfully";


#function to create server Instance 
def getServerInstance():
    jenkins_url = 'http://localhost:8080'
    server = Jenkins(jenkins_url, username = 'sedoyehoue', password = 'Root1@')
    return server

""" Function  to Get job details of each job that is running on the Jenkins instance And Insert in the SQL DATABASE"""
def getJobDetails():   
    server = get_server_instance()
    for job_name, job_instance in server.get_jobs():
        jobName      = job_instance.name
        jobDesc      = job_instance.get_description()
        jobStatus    = job_instance.is_running()
        jobEnable    = job_instance.get_description()
        jobCheckDate = datetime.datetime.fromtimestamp(long(current['timestamp'])*0.001)
        conn.execute("INSERT INTO JOB (job_name, job_description,job_status,job_enable,Job_datetime) VALUES (jobName, jobDesc, jobStatus, jobEnable,jobCheckDate) "); 
        if conn
        return true
        else 
        return false
        break

#get Server Instance
get_server_instance()

#get job details and insert in table job
if getJobDetails():
   conn.commit()
   print "job saved successfully";
else
   conn.rollback()
   print "An error occured";

#close database connection
conn.close()




   