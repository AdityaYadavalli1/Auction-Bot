from .client import Client
import asyncio

class Bid1(Client):
    def __init__(self):
        super().__init__()
        self.name = "Boring"
        self.auctionActive = {}
        self.e = {}

    async def start(self, auction_id):
        await super().start(auction_id)
        self.auctionActive[auction_id] = True
        curr_bid = 1
        await super().submit_bid(auction_id, curr_bid)

        while auction_id in self.auctionActive:
            await asyncio.sleep(0.5)

        if auction_id in self.e:
            self.e.pop(auction_id)

    async def receive_bid(self, auction_id, bid_value):
        await super().receive_bid(auction_id, bid_value)
        if auction_id not in self.e or bid_value > self.e[auction_id]:
            self.e[auction_id] = bid_value

    async def end_auction(self, auction_id):
        await super().end_auction(auction_id)
        if auction_id in self.auctionActive:
            self.auctionActive.pop(auction_id)
