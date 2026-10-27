#==================== Shopping Savvy ===================
print("==================== Shopping Savvy ===================")
"""Hi! I'm Fatespeaker and I'm going to bill you all to help our precius blind Starflight here!
 So i'm just the assistant but I'm still great( hope i make friends????)- Fatespeaker\n"""

Valid= False

while not Valid:
    try:
        Bill= float(input("How much is your bill: "))
        Dis= int(input("How much is the discount percentage: "))
        Ppl= int(input("How many people are there for this product: "))
        nothing= 100/Ppl
        total=  (Bill * Ppl) * (1 - Dis / 100)
        print("the total price is.. ")
    except ValueError as Moonwatcher:
        print("Oh no! you put in a text or decimal! You were supposed to put in a NUMBER! Also ho makes istakes like that , except Ochre, after all all he cares about id FOOD- Fatespeaker, FATESEPEAKER!  No we dont be mean like that we take care of all dragons no matter how silly they arew! - Starflight" )
    except ZeroDivisionError as WOFisbest:
        print("oh no! You cannot put 0 as a number of people!!! It must be a positive number!!!")
    else:
        print("PROCESSING BILL.....")
    finally:
        print("PROCESSING BILL..........")
        print("your bill is ready! Here you go!(finallly, time to go find some cool work to do)- Fatespeaker WHAT! OH MY MOONS! you YOU  dont like math and books???!!!- Starflight ")
        print("================== BILL =======================")
        print("Your Bill originally was... ", Bill)
        print(" You added a number of people which was ", Ppl)
        print("The total price now is ", Bill*Ppl)
        print("The discount you entered is ", Dis)
        print("The final price is ", total)
        print("You hve payed ", total, "Thank You for Billing!")
        print("================================================")
        Valid=True

print("BILLING SUCCESSFUL.  BYE!!! - Fatespeaker who is trying to sound like a robot! never mingd those dont exit in the WOF WORLD so like a umm cool dragon")