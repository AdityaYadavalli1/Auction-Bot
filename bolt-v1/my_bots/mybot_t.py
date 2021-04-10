from .client import Client
import asyncio
import math
import numpy as np

class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.name = "Amla Thopu Dammu Unte Aapu"
        self.s = 1e-5
        self.e = {}
        self.auctionActive = {}

    async def start(self, auction_id):
        await super().start(auction_id)
        self.auctionActive[auction_id] = True
        curr_bid = self.s
        await super().submit_bid(auction_id, curr_bid)

        while auction_id in self.auctionActive:
            if auction_id not in self.e and curr_bid * 1.125 <= 1:
                next_bid = curr_bid * 1.125
                if self.utility(next_bid) > self.utility(curr_bid):
                    curr_bid = next_bid
                    await super().submit_bid(auction_id, curr_bid)
            elif auction_id not in self.e:
                pass
            elif curr_bid * 1.125 > self.e[auction_id] and curr_bid * 1.125 <= 1:
                next_bid = curr_bid * 1.125
                if self.utility(next_bid) > self.utility(curr_bid):
                    curr_bid = next_bid
                    await super().submit_bid(auction_id, curr_bid)
            elif self.e[auction_id] >= curr_bid * 1.125 and self.e[auction_id] <= 1:
                next_bid = self.e[auction_id] + 1e-5
                if self.utility(next_bid) > self.utility(curr_bid):
                    curr_bid = next_bid
                    await super().submit_bid(auction_id, curr_bid)

            await asyncio.sleep(0.1)  # Do we need this

        if auction_id in self.e:
            self.e.pop(auction_id)

    @staticmethod
    def utility(bid):
        util_value = 1 - bid
        for i in range(1, 5):
            util_value += (np.arctan(bid/i)*(2/np.pi))
        util_value /= 4
        # print("bid:{0}, utility:{1}".format(bid, util_value))
        return util_value

    async def receive_bid(self, auction_id, bid_value):
        await super().receive_bid(auction_id, bid_value)
        if auction_id not in self.e or bid_value > self.e[auction_id]:
            self.e[auction_id] = bid_value

    async def end_auction(self, auction_id):
        await super().end_auction(auction_id)
        if auction_id in self.auctionActive:
            self.auctionActive.pop(auction_id)
