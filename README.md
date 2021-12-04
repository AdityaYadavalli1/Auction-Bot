# Auction-Bot

## Contributors: Aditya Yadavalli, Teja Dhondu
## Bot Name: Flash

## Description 

The is a winner takes all auction. The item's value is 1 while the bots can bid however high they want to. However, the catch is even the loser bot has to pay for the item.  

There are many more intracies like the auction duration being a probabilistic function and the delay between the communication between the bots being a non-deterministic delta. We were advised to not share the details as its part of someone's research. 

## To Run the Simulator

```bash
python3 bolt.py
python3 player_client_1.py [port_number_1]
python3 player_client_2.py [port_number_2]
python3 run_tournament.py [number_of_auctions]
```
- Run all the 4 commands in 4 different terminals. Logs can be seen in port 8080.   


## Performance 

Even though we are 5th in the standings, we practically tied with the 3rd bot.    

Due to the auction being highly non-deterministic, the whole leaderboard could be highly non-deterministic as well. We didn't want to gamble our position away to this. Therefore, to be consistently placed well on the leaderboard, we employ a *hybrid* strategy where we also have a fixed bidding strategy component in addition to a reactive bidding strategy component that most teams have used. In the fixed bidding strategy, we bid slightly higher than the previous bid after a fixed duration (without looking at the opponents bid). Hence, the bot name **Flash** 

More about our strategy [here](https://github.com/AdityaYadavalli1/Auction-Bot/blob/master/bolt-v1/Strategy%20Documentation%20for%20the%20Bolt%20Auction%20Challenge.pdf)

## Final Leaderboard

| Bot Name | Score | 
| --- | --- |
| Electro_Sapien | 432.8993159 | 
| Lupin2.0 | 362.4395948 |
| New Genesis | 270.4999039 |
| Surreal | 268.7178726 |
| *Flash* | *267.550594* | 
| Sniper | 216.0746209 | 
| Zoe | 212.5030995 |
| Saitama | 182.0978188 |
| risk_hai_toh_ishq_hai | 173.3033357 |
| AGAPES | 163.9463596 | 
| Infinity | 159.8081097 | 
| BTBot | 158.3568178 | 
| Georgekutty | 145.6592417 | 
| 17 | 135.3406466 | 
| Kalasala | 118.1818238 | 
| Jadeja | 105.7512086 |
| Sagittarius | 23.11316904 |
