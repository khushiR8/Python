min_sleep=9999

sleep_duration=float(input("Enter sleep duration for {date}:"))

if sleep_duration<min_sleep:
    min_sleep=sleep_duration


print("min sleep is:",min_sleep)

