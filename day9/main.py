# Secret Auction Game/Program

bids ={}
bidding_finished =False
def find_highest_bidder(bidding_record):
    higest_bid = 0
    winner =""
    for bidder in bidding_record:
       bid_amount = bidding_record[bidder]
       if bid_amount>higest_bid:
         higest_bid=bid_amount
         winner =bidder
    print(f"The winer is {winner} with a bid of ${higest_bid}")

while not  bidding_finished:
    name =input("what is your name? ")
    price =int(input("what is yoir bid? $"))
    bids[name]=price
   
    should_continous= input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continous =='no':
        bidding_finished =True
        find_highest_bidder(bids)
   