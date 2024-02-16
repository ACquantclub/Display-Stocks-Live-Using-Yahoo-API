# First, we install necessary packages using pip.
# yahoo_fin for accessing stock information, pygame for the graphical display, and other system utilities.
!pip install yahoo_fin
!pip install pygame

# Importing required libraries
from yahoo_fin import stock_info as si  # For stock information
import pygame, sys, os  # For graphical interface and system operations
from pygame.locals import *  # Importing constants from pygame

# Gathering user inputs for the stock ticker, purchase price, and quantity of stocks bought.
stock = input("Enter the ticker symbol: ")
bought = float(input("Enter the purchase price: "))
quantity = int(input("Enter the quantity of stocks purchased: "))

# Setting the resolution of the display window.
X, Y = 1920, 1080

# Initializing pygame and setting up the display window.
pygame.init()
DISPLAYSURF = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Stock Tracker')
os.environ['SDL_VIDEO_CENTERED'] = "True"  # Centers the display window on the screen.
pygame.font.init()  # Initializes the font module.

# Creating font objects for displaying text.
font = pygame.font.Font('freesansbold.ttf', 512)  # Large font for the stock ticker.
smallerFont = pygame.font.Font('freesansbold.ttf', 100)  # Smaller font for other texts.

# Fetching the most recent closing price of the stock.
openPrice = si.get_data(stock).close[-1]

# Preparing the stock ticker text for display.
stockSTR = font.render(stock.upper(), True, [0, 0, 0])
stockRect = stockSTR.get_rect()
stockRect.center = (X // 2, Y // 2 - 200)

# Main loop for updating and displaying stock information.
while True:
    # Fetching the current live price of the stock.
    current = round(si.get_live_price(stock), 2)

    # Calculating the difference per stock and total difference.
    diffPerStock = round(current - openPrice, 2)
    totalDiff = round((current - bought) * quantity, 2)

    # Setting the color based on whether the stock price has gone up or down.
    colourSub = [0, 255, 0] if diffPerStock > 0 else [255, 0, 0]
    colourSub2 = [0, 255, 0] if totalDiff > 0 else [255, 0, 0]

    # Preparing and positioning the texts for current price, difference per stock, and total difference.
    currentP = smallerFont.render("$ " + str(current), True, [0, 0, 0])
    currentPRect = currentP.get_rect()
    currentPRect.center = (X // 2, Y // 2 + 100)

    diffPerSTR = smallerFont.render("$ " + str(diffPerStock), True, colourSub)
    diffPerRect = diffPerSTR.get_rect()
    diffPerRect.center = (X // 2 - 400, Y // 2 + 300)

    totalDiffSTR = smallerFont.render("$ " + str(totalDiff), True, colourSub2)
    totalDiffRect = totalDiffSTR.get_rect()
    totalDiffRect.center = (X // 2 + 400, Y // 2 + 300)

    # Clearing the screen and blitting (drawing) the text objects onto the display surface.
    DISPLAYSURF.fill([255, 255, 255])
    DISPLAYSURF.blit(stockSTR, stockRect)
    DISPLAYSURF.blit(diffPerSTR, diffPerRect)
    DISPLAYSURF.blit(totalDiffSTR, totalDiffRect)
    DISPLAYSURF.blit(currentP, currentPRect)

    # Event loop to check for the QUIT event to exit the program.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Updating the display with the new information.
    pygame.display.update()
