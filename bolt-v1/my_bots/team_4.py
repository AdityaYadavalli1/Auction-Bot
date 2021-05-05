from .client import Client
import asyncio
from time import time

class Team_4_Bot(Client):
    # Init Function
    def __init__(self):
        super().__init__()
        self.name = "Flash"
        self.e = {}             # Dictionary of last enemy bid for each auction_id
        self.tasks = {}         # Dictionary of asyncio tasks for each auction_id
        self.auctionEnded = {}  # Dictionary of auction_id that have ended
        self.multiplier = 1.126     # Enemy bid multipler. Set as 1 or 1.126
        self.start_bid = 0.2    # Starting Bid
        self.time_limit = 270   # Time limit on how long asyncio task should run for each auction

    # Start Auction function
    async def start(self, auction_id):
        await super().start(auction_id)
        # Check if auction has not ended
        if auction_id not in self.auctionEnded:
            # Creates an asyncio task for each auction
            loop = asyncio.get_event_loop()
            self.tasks[auction_id] = loop.create_task(self.run(auction_id))

    # Run auction task
    async def run(self, auction_id):
        # Submit an initial bid
        start = time()
        curr_bid = self.start_bid
        await super().submit_bid(auction_id, curr_bid)

        # Loop while auction is active or less than time limit seconds have passed
        while auction_id not in self.auctionEnded and time() - start < self.time_limit:
            make_bid = True
            # If enemy has not bid yet
            if auction_id not in self.e and curr_bid * 1.125 <= 1:
                curr_bid = curr_bid * 1.125
            elif auction_id not in self.e:
                make_bid = False
            # If Fixed bid is greater than reactive bid
            elif curr_bid * 1.125 > self.e[auction_id] * self.multiplier and curr_bid * 1.125 <= 1:
                curr_bid = curr_bid * 1.125
            # If Reactive bid is greater than fixed bid
            elif self.e[auction_id] * self.multiplier >= curr_bid * 1.125 and self.e[auction_id] * self.multiplier <= 1:
                curr_bid = self.e[auction_id] * self.multiplier + 1e-5
            else:
                make_bid = False
            # Submit bid and then sleep for 5 seconds
            if make_bid:
                await super().submit_bid(auction_id, curr_bid)
                await asyncio.sleep(5)
            else:
                await asyncio.sleep(0.1)

    # Receive enemy bid function
    async def receive_bid(self, auction_id, bid_value):
        # Update enemy bid if higher than previous bid
        if auction_id not in self.e or bid_value > self.e[auction_id]:
            self.e[auction_id] = bid_value

    # End auction function
    async def end_auction(self, auction_id):
        await super().end_auction(auction_id)
        # Update auction as ended
        self.auctionEnded[auction_id] = True
        # End asyncio task for auction
        if auction_id in self.tasks:
            await self.tasks[auction_id]
