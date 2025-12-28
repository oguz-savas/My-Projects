print("Welcome To The Secret Auction!")

bid_dict ={

}
while True:
    x = input("Enter your name: ")
    y = input("Enter your bid: ")
    y = int("".join(filter(str.isdigit, y)))
    bid_dict[x] = y
    z = input("Do we have any other bids?: ").lower()
    if z != "yes":
        break
def winner():
    key, values = max(bid_dict.items(), key=lambda x: x[1])
    print(f"{key} wins! Winner Bid Is = {values}")

winner()