import art

print(art.logo)

def find_highest_bidder(bidding):
    highest_bid =0
    winner = ""
    for key in bidding:
        if bidding[key] > highest_bid:
            highest_bid = bidding[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")        

bids={}
bid_continue=True
while bid_continue:
    name = input("Please write your name: ")
    bid = int(input("Please write your bid: $"))
    bids[name]=bid
    auction = input("Anyone else would like to bid?Type yes or no?").lower()
    if auction == "no":
        bid_continue = False
        find_highest_bidder(bids)
    elif auction=="yes":
        print("\n" * 20)    