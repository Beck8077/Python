import pandas as pd
import csv

df = pd.read_csv('lesson18/hw/tackoverflow_qa.csv')


# Find all questions that were created before 2014
questions_before_2014 = df['creationdate'] < '2014-01-01'
print(df[questions_before_2014])


# Find all questions with a score more than 50
score_more_than_50 = df['score'] > 50
print(df[score_more_than_50])

# Find all questions with a score between 50 and 100
score_between_50_100 = (df['score'] > 50) & (df['score'] < 100)
print(df[score_between_50_100])

# Find all questions answered by Scott Boston
answer_by = df['ans_name'] == 'Scott Boston'
print(df[answer_by])

# Find all questions answered by the following 5 users
most_answers = df['ans_name'].value_counts()
print(most_answers.sort_values(ascending=False).head(5))

# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
created_at = (df['creationdate'] > '2014-03-01') & (df['creationdate'] < '2014-10-31')
answered_by = df['ans_name'] == 'unutbu'
score_less_5 = df['score'] < 5
final = created_at & answered_by & score_less_5
print(df[final])

# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
score_btw_5_10 = (df['score'] > 4) & (df['score'] < 11)
view_count = df['viewcount'] > 10000
final_step = score_btw_5_10 | view_count
print(df[final_step])


# Find all questions that are not answered by Scott Boston
not_answered = df['ans_name'] != 'Scott Boston'
print(df[not_answered])


titanic_df = pd.read_csv("lesson18/hw/titanic.csv")
df = pd.DataFrame(titanic_df)


# Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
class1_passengers = titanic_df['Pclass'] == 1
pass_age = titanic_df['Age'].between(20, 30)
class1_30_20_pass = class1_passengers & pass_age
print(titanic_df[class1_30_20_pass])


# Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
fare_more_100 = titanic_df['Fare'] > 100
print(titanic_df[fare_more_100])


# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
survived_pass = titanic_df['Survived'] == 1
no_relatives = (titanic_df['SibSp'] == 0) & (titanic_df['Parch'] == 0)
survived_with_no_rels = survived_pass & no_relatives
print(titanic_df[survived_with_no_rels])


# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
embarked_c = titanic_df['Embarked'] == 'C'
fare_more_50 = titanic_df['Fare'] > 50
c_pass_and_50 = embarked_c & fare_more_50
print(titanic_df[c_pass_and_50])


# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
siblings_yes = titanic_df['SibSp'] > 0
parents_yes = titanic_df['Parch'] > 0
sibsp_parch_yes = siblings_yes & parents_yes
print(titanic_df[sibsp_parch_yes])


# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
aged_15_less = titanic_df['Age'] <= 15
survival = titanic_df['Survived'] == 0
age_15_not_survived = aged_15_less & survival
print(titanic_df[age_15_not_survived])


# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
cabin_yes = titanic_df['Cabin'].notna()
fare_200 = titanic_df['Fare'] > 200
cabin_fare_200 = cabin_yes & fare_200
print(titanic_df[cabin_fare_200])


# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
passid = titanic_df['PassengerId'] % 2 != 0
print(titanic_df[passid])


# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
unique_tickets = df['Ticket'].value_counts()
unique_ticket_numbers = unique_tickets[unique_tickets == 1].index
unique_ticket_df = df[df['Ticket'].isin(unique_ticket_numbers)]
print(unique_ticket_df)

# Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
name_miss = titanic_df['Name'].str.contains('Miss')
class1_passengers = titanic_df['Pclass'] == 1
miss_class_1 = name_miss & class1_passengers
print(titanic_df[miss_class_1])