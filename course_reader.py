__author__ == "ttn6ew"

import csv
import psycopg2

PG_USER = "postgres"
PG_USER_PASS = "cs3240"
PG_HOST_INFO = ""


def load_course_database(db_name, csv_filename):
    conn = psycopg2.connect("dbname=" + db_name + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    print("** Connected to database.")
    cur = conn.cursor()

    with open(csv_filename, 'rU') as data:
        reader = csv.reader(data)
        for row in reader:
                cur.execute("INSERT INTO coursedata (deptID, courseNum, semester, meetingType, seatsTaken, "
                            "seatsOffered, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2],
                                                                                              row[3], row[4], row[5],
                                                                                              row[6]))
        print("** Executed SQL INSERT into database.")

if __name__ == "__main__":
    load_course_database("coursedata", "seas-courses-5years.csv")
