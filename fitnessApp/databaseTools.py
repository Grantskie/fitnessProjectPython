import mysql.connector

def connect():
    cnx = mysql.connector.connect(user='scalaFitnessApp', password='ScalaFitness1!',
                                  host='127.0.0.1',
                                  database='fitnessapp')
    cursor = cnx.cursor()
    return cursor