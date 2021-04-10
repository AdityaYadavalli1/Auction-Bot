from .client import Client
import asyncio


class FixedBot(Client):
    def __init__(self):
        super().__init__()
        self.name = "Superman"  # Your Bot's Name
        self.last_bid = {}
        # Your Initialization Code Here
        pass

    async def start(self, auction_id):
        await super().start(auction_id)
        await super().submit_bid(auction_id, 0.4)
        self.last_bid[auction_id] = 0.4
        last = self.last_bid[auction_id]
        while last < 1:
            last = self.last_bid[auction_id]
            await asyncio.sleep(0.5)
            print("Time to submit a bid")
            last = self.last_bid[auction_id]
            self.last_bid[auction_id] = last*1.125
            if last*1.125 > 1:
                break
            await super().submit_bid(auction_id,last*1.125)


    async def receive_bid(self, auction_id, bid_value):
        await super().receive_bid(auction_id, bid_value)
        # Your code for receiving bids
        pass

    async def end_auction(self, auction_id):
        await super().end_auction(auction_id)
        # Your code for ending auction
