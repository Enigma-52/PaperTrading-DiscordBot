import discord
from discord.ext import commands
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from prettytable import PrettyTable
import threading
import time


class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.nextorderId = None
        self.portfolio_data = []

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextorderId = orderId
        print("The next valid order id is: ", self.nextorderId)

    def orderStatus(
        self,
        orderId,
        status,
        filled,
        remaining,
        avgFullPrice,
        permId,
        parentId,
        lastFillPrice,
        clientId,
        whyHeld,
        mktCapPrice,
    ):
        print(
            "orderStatus - orderid:",
            orderId,
            "status:",
            status,
            "filled",
            filled,
            "remaining",
            remaining,
            "lastFillPrice",
            lastFillPrice,
        )

    def openOrder(self, orderId, contract, order, orderState):
        print(
            "openOrder id:",
            orderId,
            contract.symbol,
            contract.secType,
            "@",
            contract.exchange,
            ":",
            order.action,
            order.orderType,
            order.totalQuantity,
            orderState.status,
        )

    def execDetails(self, reqId, contract, execution):
        print(
            "Order Executed: ",
            reqId,
            contract.symbol,
            contract.secType,
            contract.currency,
            execution.execId,
            execution.orderId,
            execution.shares,
            execution.lastLiquidity,
        )
        # Move to the next order ID after executing an order
        self.nextorderId += 1
        print("Moving to the next order ID:", self.nextorderId)

    def updatePortfolio(
        self,
        contract,
        position,
        marketPrice,
        marketValue,
        averageCost,
        unrealizedPNL,
        realizedPNL,
        accountName,
    ):
        position_data = {
            "Symbol": contract.symbol,
            "Position": position,
            "Market Price": marketPrice,
            "Market Value": marketValue,
            "Average Cost": averageCost,
            "Unrealized P&L": unrealizedPNL,
            "Realized P&L": realizedPNL,
            "Account": accountName,
        }
        self.portfolio_data.append(position_data)

    def display_portfolio_table(self):
        table = PrettyTable()
        table.field_names = [
            "Symbol",
            "Position",
            "Market Price",
            "Market Value",
            "Average Cost",
            "Unrealized P&L",
            "Realized P&L",
            "Account",
        ]

        for position_data in self.portfolio_data:
            table.add_row([position_data[field] for field in table.field_names])

        return str(table)


def run_loop():
    app.run()


def stock_market_order(symbol, action, quantity):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"

    order = Order()
    order.action = action
    order.totalQuantity = quantity
    order.orderType = "MKT"
    order.transmit = True
    order.eTradeOnly = ""
    order.firmQuoteOnly = ""

    return contract, order


app = IBapi()
app.connect("127.0.0.1", 7497, 123)

api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

while True:
    if isinstance(app.nextorderId, int):
        print("connected")
        break
    else:
        print("waiting for connection")
        time.sleep(1)

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("------")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msg = message.content.upper()

    if msg[0] == "!":
        if "!BUY" in msg or "!SELL" in msg:
            command, stock_ticker = msg.split(maxsplit=1)
            command = command[1:].upper()
            stock_ticker = stock_ticker.upper()

            quantity = 1
            app.nextorderId += 1

            contract, order = stock_market_order(stock_ticker, command, quantity)
            app.placeOrder(app.nextorderId, contract, order)

            await message.channel.send(
                f"ORDER SUCCESSFUL : Order Type : {command} , Stock Ticker : {stock_ticker}"
            )
        elif "!HELP" in msg:
            command_list = [
                "!BUY <stock_ticker> - Buy 1 stock of <stock_ticker>",
                "!SELL <stock_ticker> - Sell 1 stock of <stock_ticker>",
                "!HELP - Display list of available commands",
                "!PORTFOLIO - Display the current Stock Portfolio"
                # Add more commands as needed
            ]
            await message.channel.send("\n".join(command_list))
        elif "!PORTFOLIO" in msg:
            portfolio_table = app.display_portfolio_table()
            await message.channel.send("```" + portfolio_table + "```")
        else:
            await message.channel.send("Incorrect Format! Use !help for Commands")


bot.run("BOT-TOKEN")
