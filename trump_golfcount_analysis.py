import csv
import datetime
import calendar 
import matplotlib.pyplot as plt

SECONDS_IN_DAY = 24 * 60 * 60
TRUMP_TOTAL_CLUB_VISITS = 263

def main():
    trump_confirmed_golf_count = 0
    trump_confirmed_nonweekend_golf_count = 0
    trump_confirmed_time_at_golf_resort = 0.0
    trump_confirmed_time_at_golf_resort_during_work_week = 0.0
    with open("trumpgolfcountoutings_071820.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = [row for row in reader]
        for i in range(len(data)):
            for j in range(len(data[i])):
                if str(data[i][j]) == "Yes":            # "Yes" is only used to denote if President Trump was sighted/confirmed playing golf.
                    trump_confirmed_golf_count += 1
                    date_played = datetime.datetime(int(data[i][0][:4]), int(data[i][0][5:7]), int(data[i][0][8:10]))
                    if calendar.day_name[date_played.weekday()] == "Monday" or calendar.day_name[date_played.weekday()] == "Tuesday" or calendar.day_name[date_played.weekday()] == "Wednesday" or calendar.day_name[date_played.weekday()] == "Thursday" or (calendar.day_name[date_played.weekday()] == "Friday" and int(data[j][1][11:12]) <= 17):
                        trump_confirmed_nonweekend_golf_count += 1
                        trump_arrival_time = datetime.datetime(int(data[i][1][:4]), int(data[i][1][5:7]), int(data[i][1][8:10]), int(data[i][1][11:13]), int(data[i][1][14:16]))
                        trump_departure_time = datetime.datetime(int(data[i][3][:4]), int(data[i][3][5:7]), int(data[i][3][8:10]), int(data[i][3][11:13]), int(data[i][3][14:16]))
                        trump_confirmed_time_at_golf_resort_during_work_week += float((trump_departure_time - trump_arrival_time).total_seconds()/3600)
                    trump_arrival_time = datetime.datetime(int(data[i][1][:4]), int(data[i][1][5:7]), int(data[i][1][8:10]), int(data[i][1][11:13]), int(data[i][1][14:16]))
                    trump_departure_time = datetime.datetime(int(data[i][3][:4]), int(data[i][3][5:7]), int(data[i][3][8:10]), int(data[i][3][11:13]), int(data[i][3][14:16]))
                    trump_confirmed_time_at_golf_resort += float((trump_departure_time - trump_arrival_time).total_seconds()/3600)
                    
    labels_trump_golf_week_claim = "Trump Time At Golf Resort During Weekend (Hours)", "Trump Time At Golf Resort During Workweek (Hours)"
    sizes_trump_golf_week_claim = (((trump_confirmed_time_at_golf_resort - trump_confirmed_time_at_golf_resort_during_work_week)/trump_confirmed_time_at_golf_resort * 100), ((trump_confirmed_time_at_golf_resort_during_work_week)/trump_confirmed_time_at_golf_resort * 100))
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes_trump_golf_week_claim,  labels=labels_trump_golf_week_claim, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    
    
    labels_trump_golf_number_claim = "Trump Golf Plays During Weekend", "Trump Golf Plays During Workweek"
    sizes_trump_golf_number_claim = (((trump_confirmed_golf_count-trump_confirmed_nonweekend_golf_count)/trump_confirmed_golf_count * 100), ((trump_confirmed_nonweekend_golf_count)/trump_confirmed_golf_count * 100))
    fig2, ax1 = plt.subplots()
    ax1.pie(sizes_trump_golf_number_claim,  labels=labels_trump_golf_number_claim, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()
    
    print(trump_confirmed_golf_count, trump_confirmed_nonweekend_golf_count, trump_confirmed_time_at_golf_resort, trump_confirmed_time_at_golf_resort_during_work_week, trump_confirmed_time_at_golf_resort/TRUMP_TOTAL_CLUB_VISITS)
    

    
    
        
                    
        
    
    
    
    
if __name__ == "__main__":
    main()