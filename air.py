# Come Fly With Me Project

# Seat layout:
# Seats 1–4      = First Class ($50 fee each)
# Seats 5–8      = Emergency Exit (requires confirmation)
# Seats 9–20     = Regular (free)

SEAT_COUNT = 20
FIRST_CLASS = range(1, 5)
EMERGENCY_SEATS = range(5, 9)

# Store taken seats
taken_seats = []


def show_seats():
    print("\n--- SEAT MAP ---")
    for seat in range(1, SEAT_COUNT + 1):
        status = "X" if seat in taken_seats else "Available"
        print(f"Seat {seat}: {status}")
    print("----------------\n")


def purchase_seat():
    while True:
        try:
            seat = int(input("Enter seat number to purchase (1-20): "))
            if seat < 1 or seat > 20:
                print("Invalid seat number. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a number.")

    # Check if taken
    if seat in taken_seats:
        print("❌ Sorry, that seat is already taken.")
        return

    # First class seats
    if seat in FIRST_CLASS:
        print("This is a FIRST-CLASS seat. Fee: $50")
        pay = input("Do you want to continue? (yes/no): ").lower()
        if pay != "yes":
            print("Purchase cancelled.")
            return

    # Emergency exit seats
    if seat in EMERGENCY_SEATS:
        print("⚠ EMERGENCY EXIT SEAT SELECTED")
        confirm = input("Do you accept responsibility to assist in an emergency? (yes/no): ").lower()
        if confirm != "yes":
            print("You must accept responsibility to sit here. Purchase cancelled.")
            return

    # Mark seat as taken
    taken_seats.append(seat)
    print(f"✅ Seat {seat} successfully purchased!")


def main():
    print("✈ COME FLY WITH ME — Seat Purchasing System")

    while True:
        show_seats()
        purchase_seat()

        again = input("Do you want to purchase another seat? (yes/no): ").lower()
        if again != "yes":
            break

    print("\nFinal seats taken:", taken_seats)
    print("Thank you for booking with us! ✈")


main()
