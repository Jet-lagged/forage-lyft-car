from car import Car
from datetime import date
from engine.models import *
from battery.models import *

class CarFactory():

    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int)-> Car: 
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpinderBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = spindler_battery.SpinderBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpinderBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)
    
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)