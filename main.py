chaseCardCreditIINs = [403116, 403213, 403690, 407166, 408161, 411816, 414720, 414740, 424631, 425331, 426245, 426650, 426681, 426684, 426685, 426690, 430587, 436614, 436616, 438852, 438854, 438857, 441711, 441712, 441716, 446568, 455953, 464018, 479851, 486521, 512257, 514874, 518337, 518445, 536990, 540168, 541711, 546604, 546626, 546657, 547363, 549092, 549104, 552475, 558250, 558967, 558987]
chaseCardDebitIINs = [406032, 406042, 406045, 406068, 412451, 412453, 420767, 428208, 430326, 431231, 434769, 441103, 441105, 442732, 442742, 442755, 450952, 456323, 456331, 461046, 473622, 475055, 475056, 478200, 483312, 483316, 483323, 483324, 486742, 486796, 490070, 490071, 511375, 511392, 511395, 511398, 511425, 515563, 528715, 537167, 537170, 557558, 559033]
bankOfAmericaCreditIINs = [374322, 374632, 374720, 400390, 402400, 403647, 407871, 407892, 414707, 414734, 414737, 414773, 417008, 426428, 426451, 426452, 426465, 431303, 431307, 431308, 431351, 431352, 433993, 444395, 447619, 448585, 448813, 461691, 471529, 480011, 481588, 488889, 488890, 488893, 488894, 517572, 520001, 532901, 532903, 532905, 532906, 532912, 534875, 546632, 547415, 547497, 549033, 549035, 549050, 549191, 552426]
bankOfAmericaDebitIINs = [411770, 411773, 411777, 413571, 413572, 413574, 413577, 425627, 425637, 430594, 432624, 432626, 432628, 432630, 433718, 435272, 435603, 435619, 435643, 435680, 435685, 435687, 435688, 436802, 442743, 442777, 453253, 455689, 463288, 463550, 463552, 463572, 463575, 463580, 463581, 463584, 463588, 463589, 464875, 464880, 470132, 470134, 471724, 471727, 474472, 474476, 474477, 474484, 481581, 484575, 484588, 484594, 494340, 511560, 527513, 527515, 527517, 527518, 527519, 527520, 527523, 531250, 531255, 531257, 531262, 531265, 531266, 534869, 541660, 549170, 553822, 557268]
wellsFargoCreditIINs = [407110, 407221, 414718, 414730, 431243, 448461]
wellsFargoDebitIINs = [425908, 425909, 434256, 434257, 434260, 435549, 473702, 473703, 474165, 474166, 482851, 482853, 482854, 482857, 482860, 482862, 482864, 486827, 486830, 486831, 511559, 515551]

def cardCompare():
    while True:
        creditNumber = input("Please enter a valid credit or debit card number: ")

        if len(creditNumber) > 16 or creditNumber.isdigit() == False:
            print("That is not a valid credit card, please try again")
            continue
        else:
            
            inputCardIIN = int(creditNumber[:6])
            
            if inputCardIIN in chaseCardDebitIINs:
                cardType = "Debit"
                cardIssuer = "Chase"    
            elif inputCardIIN in chaseCardCreditIINs:
                cardType = "Credit"
                cardIssuer = "Chase" 
            elif inputCardIIN in bankOfAmericaDebitIINs:
                cardType = "Debit"
                cardIssuer = "Bank of America"   
            elif inputCardIIN in bankOfAmericaCreditIINs:
                cardType = "Credit"
                cardIssuer = "Bank of America"
            elif inputCardIIN in wellsFargoDebitIINs:
                cardType = "Debit"
                cardIssuer = "Wells Fargo"
            elif inputCardIIN in wellsFargoCreditIINs:
                cardType = "Credit"
                cardIssuer = "Wells Fargo"
            else:
                print('This card is not recognized')

            print(f"Thanks for your input, the card you entered {creditNumber} is a {cardType} card issued by {cardIssuer}")

cardCompare()







