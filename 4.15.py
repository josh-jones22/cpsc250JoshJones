highway_number = int(input())

if 0 < highway_number < 100 and (highway_number % 2) == 0:
    print(f"I-{highway_number} is primary, going east/west.")
elif 0 < highway_number < 100 and (highway_number % 2) != 0:
    print(f"I-{highway_number} is primary, going north/south.")
elif 99 < highway_number < 1000 and (highway_number % 100) != 0 and (highway_number % 2) == 0:
    service = highway_number % 100
    print(f"I-{highway_number} is auxiliary, serving I-{service}, going east/west.")
elif 99 < highway_number < 1000 and (highway_number % 100) != 0 and (highway_number % 2) != 0:
    service = highway_number % 100
    print(f"I-{highway_number} is auxiliary, serving I-{service}, going north/south.")
elif 99 < highway_number < 1000 and (highway_number % 100) == 0:
    print(f"{highway_number} is not a valid interstate highway number.")
elif highway_number < 99 or highway_number > 999:
    print(f"{highway_number} is not a valid interstate highway number.")