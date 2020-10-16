#The data used is manually loaded into IBM Db2 database for querying.
#An alternative is to first load the dataset into a Pandas dataframe and then pushing it into the database. However, this is not optimal for querying SQL because pushing data using
Python will map it to default datatypes that are not ideal.
#There are three datasets: crime, socieconomic and school datasets/tables
#This implements sql-magic (SQL embedded into Python Jupyter Notebook)

#load the SQl extension to Jupyter and establish a connection with the database
%load_ext sql

# The connection string for Db2 is of the format:
# %sql ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name
# Enter the connection string for your Db2 on Cloud database instance below
# Removed for security reasons

#total number of crimes recorded from crime table
%sql SELECT COUNT(*) AS TOTAL_CRIMES FROM CRIME

#retrieve first 10 rows from crime table
%sql SELECT * FROM CRIME FETCH FIRST 10 ROWS ONLY

#number of crimes that involve an arrest
%sql SELECT COUNT(*) AS CRIME_WITH_ARREST FROM CRIME WHERE ARREST = 'TRUE'

#unique crimes recorded at GAS stations
%sql SELECT DISTINCT(PRIMARY_TYPE), LOCATION_DESCRIPTION FROM CRIME WHERE LOCATION_DESCRIPTION = 'GAS STATION'

#Community areas whose names start with 'B' from socioeconomic table
%sql SELECT COMMUNITY_AREA_NAME FROM SOCIOECONOMIC WHERE COMMUNITY_AREA_NAME LIKE 'B%'

#schools in community areas 10 to 15 are health certified
%sql SELECT NAME_OF_SCHOOL, COMMUNITY_AREA_NUMBER, HEALTHY_SCHOOL_CERTIFIED FROM SCHOOLS \
    WHERE HEALTHY_SCHOOL_CERTIFIED = 'Yes' AND COMMUNITY_AREA_NUMBER BETWEEN 10 AND 15 

#average school safety score
%sql SELECT AVG(SAFETY_SCORE) AS AVG_SAFETY_SCORE FROM SCHOOLS

#top 5 Community Areas by average College Enrollment
%sql SELECT COMMUNITY_AREA_NAME, COLLEGE_ENROLLMENT FROM SCHOOLS ORDER BY COLLEGE_ENROLLMENT DESC FETCH FIRST 5 ROWS ONLY
%sql SELECT MAX(COLLEGE_ENROLLMENT) FROM SCHOOLS LIMIT 5

#community area with lowest safety school score
%sql SELECT COMMUNITY_AREA_NAME FROM SCHOOLS WHERE SAFETY_SCORE = (SELECT MIN(SAFETY_SCORE) FROM SCHOOLS)

#Per Capita Income of the Community Area which has a school Safety Score of 1.
%sql SELECT  PER_CAPITA_INCOME, COMMUNITY_AREA_NUMBER, COMMUNITY_AREA_NAME FROM SOCIOECONOMIC SE, SCHOOLS SS\
    WHERE SE.COMMUNITY_AREA_NUMBER = SS.COMMUNITY_AREA_NUMBER AND SAFETY_SCORE = '1'
%sql SELECT * FROM SOCIOECONOMIC LIMIT 3
