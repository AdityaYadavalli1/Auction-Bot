from .client import Client
import asyncio
import math
import numpy as np
import time

class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.name = "Amla Thopu Dammu Unte Aapu"  # Your Bot's Name
        # Your Initialization Code Here
        self.s = 0.00001
        self.e = 0
        self.t = time.time()
        self.last_bid = {}
        pass

    async def start(self, auction_id):
        # self.e = 0
        await super().start(auction_id)
        self.last_bid[auction_id] = self.s
        print("Start Bid")
        await super().submit_bid(auction_id, self.s)
        while True:
            await asyncio.sleep(2.5)
            curr_bid = self.last_bid[auction_id]
            next_bid = max(1.125*curr_bid, self.e)
            if (self.utility(next_bid) > self.utility(curr_bid)):
                self.last_bid[auction_id] = next_bid+0.00001
                await super().submit_bid(auction_id, next_bid+0.00001)
            if self.stale_utility(curr_bid, next_bid, self.t) < self.stale_utility(curr_bid, next_bid, self.t+1):
                last_bid = self.last_bid[auction_id]
                await super().submit_bid(auction_id, last_bid*1.125)
            else:
                await super().end_auction(auction_id)  
        # Your code for starting an auction

    @staticmethod
    def utility(bid):
        util_value = 1-bid
        for i in range(1, 5):
            util_value +=  (np.arctan(bid/i)*(2/np.pi))
        util_value /= 4
        print("bid:{0}, utility:{1}".format(bid, util_value))
        return util_value

    def stale_utility(self, curr_bid, next_bid, time):
        return (self.utility(curr_bid)*(1-math.exp(-time)) + self.utility(next_bid)*(math.exp(-time)))

    async def receive_bid(self, auction_id, bid_value):
        # code for receiving bid
        await super().receive_bid(auction_id, bid_value)
        if bid_value > self.e:
            self.e = bid_value
            self.t = time.time()

    async def end_auction(self, auction_id):
        await super().end_auction(auction_id)
        # Your code for ending auction