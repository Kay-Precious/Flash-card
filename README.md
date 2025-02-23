# Flash-card

A simple flashcard application built with Tkinter that helps users learn new words in French. The application displays a French word on the front of the card and the English translation on the back.

Requirements

- Python 3.x
- Tkinter library
- pandas library

Installation

1. Clone the repository using git clone
2. Install required libraries using pip install tkinter pandas
3. Run the application using python flash_card.py

Gameplay

1. The application displays a French word on the front of the card.
2. After 3 seconds, the card flips to display the English translation.
3. The user can click the "Right" button if they knew the word or the "Wrong" button if they didn't.
4. If the user clicks the "Right" button, the word is removed from the deck.

Code Structure

The code is structured into the following functions:

- next_card(): Displays the next card in the deck
- flip_card(): Flips the current card to display the English translation
- is_known(): Removes the current word from the deck if the user knew it
