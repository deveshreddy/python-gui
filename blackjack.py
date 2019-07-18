import tkinter
import random


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['king', 'queen', 'jack']
    extention = 'png'
    for suit in suits:
        for card in range(1, 11):
            name = 'cards/cards/{}_{}.{}'.format(str(card), suit, extention)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image, ))

        for card in face_cards:
            name = 'cards/cards/{}_{}.{}'.format(str(card), suit, extention)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image, ))


def _deal_cards(frame):
    # pop next card
    next_card = deck.pop(0)
    deck.append(next_card)
    # add image to a label and display
    # do not mix grid and pack in  the same frame
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # return card value
    return next_card


def score_hand(hand):
    # calculate ototal score of cards in list
    # ac =11 , 1 if hand is bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]

        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        if score > 21 and ace:
            score -= 10
            ace = False

    return score


def deal_player():
    if game_status =='on':
        player_score = score_hand(player_hand)


        if player_score < 21:
            player_hand.append(_deal_cards(player_card_frame))
            player_score = score_hand(player_hand)

        if player_score == 21:
            result_text.set('Player player wins')

        elif player_score > 21:
            result_text.set('Delaer Delaer wins')

        player_score_label.set(player_score)
    # if player_score > 21:
        #     result_text.set('dealer won')
        # global player_score
        # global player_ace
        #
        # card_value = deal_cards(player_card_frame)[0]
        #
        # if card_value == 1 and not player_ace:
        #     player_ace = True
        #     card_value = 11
        #
        # player_score = player_score + card_value
        #
        # if player_score > 21 and player_ace:
        #     player_score -= 10
        #     player_ace = False
        #
        # if player_score > 21:
        #     result_text.set("Dealer Wins")
        #
        # player_score_label.set(player_score)


def deal_dealer():

    dealer_score = score_hand(dealer_hand)
    # player score shouldnt exceed 21
    # deal until score is more than player but less than 21
    # deal until just more than player score
    player_score = score_hand(player_hand)

    if player_score <= 21:

        while dealer_score < player_score:
            dealer_hand.append(_deal_cards(dealer_card_frame))
            dealer_score = score_hand(dealer_hand)
            dealer_score_label.set(dealer_score)

        check_result(player_score, dealer_score)

    else:
        result_text.set('bad request')
        game_status ='off'


def check_result(ps, ds):
    global game_status
    if ps > 21:
        result_text.set("dealer won")
        game_status='off'


    elif ps == 21:
        result_text.set("playerio wins")
        game_status='off'

    elif ds > 21 or ds < ps:
        result_text.set("player wins")
        game_status='off'

    elif ds > ps:
        result_text.set("dealere wins")
        game_status ='off'
    else:
        result_text.set('draws')
        game_status='off'

def initial_deal():

    deal_player()
    dealer_hand.append(_deal_cards(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    global game_status
    game_status='on'


def newgame():

    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    global game_status
    # destroy all frames
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    dealer_hand = []
    player_hand = []
    game_status ='on'
    result_text.set('Game on')
    initial_deal()


def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    mainwindow.mainloop()

__name__ = '__main__'
mainwindow = tkinter.Tk()
# print(__name__)
mainwindow.title(" black jack game")
mainwindow.geometry("640x480")
mainwindow.configure(background='green')
#frame for result
result_text = tkinter.StringVar()
result_text_label = tkinter.Label(mainwindow, background='red', textvariable=result_text)
result_text_label.grid(row=0, column=0, columnspan=3)

#main card frame box
card_frame = tkinter.Frame(mainwindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew, ', rowspan=2, columnspan=3)

# initialize dealers score
dealer_score_label = tkinter.IntVar()
dealer_score = 0
dealer_ace = False

# label dealer
tkinter.Label(card_frame, text="Dealer", background='blue', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

# embeded frames
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

# initialize player variables
player_score_label = tkinter.IntVar()
player_score = 0
player_ace = False

# labelling player
tkinter.Label(card_frame, text="Player", background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

# frame for holding card images
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text='Hit dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text='Hit player', command=deal_player)
player_button.grid(row=0, column=1)

newgame_button = tkinter.Button(button_frame, text='restart game', command=newgame)
newgame_button.grid(row=0, column=3)

shufflebutton = tkinter.Button(button_frame, text='shuffle', command=shuffle)
shufflebutton.grid(row=0, column=4)
# Loading Card Images
cards = []
load_images(cards)
# print(cards)
rbValue = tkinter.IntVar()
# set default value
rbValue.set(1)
# buttons begin here
radioframe = tkinter.LabelFrame(mainwindow, text='select no of decks')
radioframe.grid(row=4, column=0)

radio1 = tkinter.Radiobutton(radioframe, text='1', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(radioframe, text='2', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(radioframe, text='3', value=3, variable=rbValue)

radio1.grid(row=0, column=0, sticky='ew')
radio2.grid(row=0, column=1, sticky='ew')
radio3.grid(row=0, column=2, sticky='ew')
deck = []

for i in range(0, rbValue.get()):
    deck = deck + list(cards)

random.shuffle(deck)

dealer_hand = []
player_hand = []
game_status ='on'
# play()
if __name__ == '__main__':
    play()
# deal_player()
# #deal_dealer()
# dealer_hand.append(deal_cards(dealer_card_frame))
# dealer_score_label.set(score_hand(dealer_hand))
# deal_player()