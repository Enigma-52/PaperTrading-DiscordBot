# Paper Trading Discord Bot

## Introduction
This Discord bot is designed for paper trading and utilizes the Interactive Brokers (IBKR) API for executing stock market orders. It allows users to simulate buying and selling stocks in a Discord server environment without using real money.


![00F15675-5C55-4A8A-BE0B-7A3F539B4E4B](https://github.com/Enigma-52/PaperTrading-DiscordBot/assets/95529619/e303b0ef-3ec3-4799-870a-4cb7e7012467)

## Prerequisites
- Python 3.7 or higher
- Discord.py library
- IBKR API library
- PrettyTable library

## Installation
1. Install the required Python libraries:
    ```bash
    pip install discord.py ibapi prettytable
    ```

2. Ensure you have the necessary API keys or credentials for the Interactive Brokers account.

## Setting Up Interactive Brokers TWS (Trader Workstation)
1. [Download](https://www.interactivebrokers.com/en/index.php?f=16040) and install Interactive Brokers TWS (Trader Workstation) on your machine.
2. Open TWS and log in with your Interactive Brokers account.
3. Configure the API settings:
    - Navigate to `File` > `Global Configuration` > `API` > `Settings`.
    - Check the box for `Enable ActiveX and Socket Clients`.
    - Set the Socket port (default is 7496 for the main connection and 7497 for the secondary connection).
    - Note your Client ID for API connections.

![9103CA5A-6B07-482A-90D6-779E9D1AFBB1](https://github.com/Enigma-52/PaperTrading-DiscordBot/assets/95529619/2a1dcecf-9781-46e9-840d-f826a288e312)

## Features
- **Buy and Sell Commands:** Simulate buying and selling stocks using the `!BUY` and `!SELL` commands.
- **Help Command:** Display a list of available commands using `!HELP`.
- **Portfolio Display:** View the current stock portfolio using the `!PORTFOLIO` command.

## How to Use
1. Clone or download the bot code from the repository.
2. Replace `"BOT-TOKEN"` with your Discord bot token in the last line of the code.
3. Run the bot using the following command:
    ```bash
    python app.py
    ```

## Commands
- `!BUY <stock_ticker>`: Buy 1 stock of the specified `<stock_ticker>`.
- `!SELL <stock_ticker>`: Sell 1 stock of the specified `<stock_ticker>`.
- `!HELP`: Display a list of available commands.
- `!PORTFOLIO`: Display the current stock portfolio.

## Example Usage
- To buy a stock: `!BUY AAPL`
- To sell a stock: `!SELL MSFT`
- To display available commands: `!HELP`
- To view the current portfolio: `!PORTFOLIO`

## Note
This bot is for educational purposes only and uses a paper trading environment. It does not involve real money transactions.

Feel free to contribute or report issues on [GitHub](https://github.com/yourusername/your-repository).

