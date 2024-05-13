from payament_times.nine_months import nine_months
from payament_times.in_time import *
from config import *
from payament_times.six_months import six_months
from payament_times.three_months import three_months
from payament_times.twelve_months import twelve_months

def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return (in_time(desired_car))
    elif(time_option == 2):
        return (three_months(desired_car))
    elif(time_option == 3):
        return (six_months(desired_car))
    elif(time_option == 4):
        return (nine_months(desired_car))
    elif(time_option == 5):
        return (twelve_months(desired_car))
