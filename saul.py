import random
import time
import sys

# Color formatting codes
GOLD = "\033[33m\033[1m"
RED = "\033[31m\033[1m"
GREEN = "\033[32m\033[1m"
CYAN = "\033[36m\033[1m"
MAGENTA = "\033[35m\033[1m"
RESET = "\033[0m"

CASES = [
    {
        "client": "Badger & Skinny Pete",
        "crime": "Caught trying to sell sci-fi script ideas on a public bench at 3 AM.",
        "options": [
            {"desc": "Claim it was street performance art protected by First Amendment.", "payout": 2500, "heat": 10, "success": 0.8},
            {"desc": "Blame it on a secret government conspiracy and demand a trial.", "payout": 5000, "heat": 30, "success": 0.4},
            {"desc": "Bribe the arresting officer with a box of cinnamon rolls.", "payout": 1200, "heat": 5, "success": 0.9}
        ]
    },
    {
        "client": "Anxious ATM Guy",
        "crime": "Stuck inside a stolen convenience store ATM machine.",
        "options": [
            {"desc": "Argue he was just trapped inside and searching for his lost keys.", "payout": 3500, "heat": 15, "success": 0.75},
            {"desc": "Sue the store owner for poor machine ergonomics and emotional damage.", "payout": 7000, "heat": 35, "success": 0.35},
            {"desc": "Call Huell Babineaux to 'casually' lean on the court room door.", "payout": 4000, "heat": 20, "success": 0.85}
        ]
    },
    {
        "client": "Local Pet Store Owner",
        "crime": "His parrot testified against him as a primary prosecution witness.",
        "options": [
            {"desc": "Cross-examine the parrot until it gets confused and squawks nonsense.", "payout": 3000, "heat": 10, "success": 0.8},
            {"desc": "Object on grounds of hearsay since parrots aren't human citizens.", "payout": 4500, "heat": 20, "success": 0.65},
            {"desc": "Pay Mike Ehrmantraut to replace the parrot with a stunt double.", "payout": 6000, "heat": 25, "success": 0.9}
        ]
    },
    {
        "client": "A Chemist in a Porkpie Hat",
        "crime": "Suspicious activity involving RV motorhomes and giant barrels of methylamine.",
        "options": [
            {"desc": "Fabricate a complex fake identity and move the case to another district.", "payout": 15000, "heat": 40, "success": 0.6},
            {"desc": "Demand a speedy trial and overwhelm the prosecution with motion papers.", "payout": 10000, "heat": 25, "success": 0.75},
            {"desc": "Tell Hank Schrader it's just a mobile pest control startup.", "payout": 20000, "heat": 50, "success": 0.3}
        ]
    }
]

class SaulGame:
    def __init__(self):
        self.cash = 5000
        self.heat = 10
        self.day = 1
        self.office = "Nail Salon Backroom (Cucumber water is for paying customers only!)"

    def check_office_upgrade(self):
        if self.cash >= 100000:
            print(f"\n{GOLD}==================================================")
            print("  CONGRATULATIONS! YOU HIT $100,000!")
            print("  You bought the iconic Strip-Mall Office with")
            print("  the inflatable Statue of Liberty on top!")
            print(f"=================================================={RESET}\n")
            sys.exit(0)
        elif self.cash >= 30000 and "Strip-Mall" not in self.office:
            self.office = "Strip-Mall Office (Inflatable Statue of Liberty outside)"
            print(f"\n{GOLD}>>> OFFICE UPGRADE! You moved to: {self.office}{RESET}\n")

    def slippin_jimmy(self):
        print(f"\n{MAGENTA}=== SLIPPIN' JIMMY EMERGENCY SCAM ==={RESET}")
        print("You head over to the local ice rink to execute a classic fake slip-and-fall...")
        time.sleep(1)
        if random.random() < 0.5:
            gain = random.randint(3000, 7000)
            self.cash += gain
            self.heat += 15
            print(f"{GREEN}SUCCESS! The settlement paid out ${gain}! (Heat +15){RESET}")
        else:
            loss = random.randint(2000, 4000)
            self.cash = max(0, self.cash - loss)
            self.heat += 25
            print(f"{RED}BUSTED! Howard Hamlin caught you on camera. Lost ${loss} and Heat +25!{RESET}")

    def play_turn(self):
        print(f"\n{CYAN}--------------------------------------------------")
        print(f" DAY {self.day} | Cash: ${self.cash:,} | Heat: {self.heat}%")
        print(f" Current Location: {self.office}")
        print(f"--------------------------------------------------{RESET}")

        if self.heat >= 100:
            print(f"\n{RED}💀 GAME OVER! Hank Schrader & the DEA raided your office!")
            print(f"Your legal license has been revoked.{RESET}\n")
            sys.exit(0)

        case = random.choice(CASES)
        print(f"\n{GOLD}NEW CLIENT:{RESET} {case['client']}")
        print(f"{GOLD}SITUATION:{RESET} {case['crime']}\n")

        for idx, opt in enumerate(case["options"], 1):
            print(f"  [{idx}] {opt['desc']} (Reward: ${opt['payout']:,} | Heat: +{opt['heat']}%)")
        print(f"  [S] Run a 'Slippin' Jimmy' Scam")
        print(f"  [Q] Quit Game")

        choice = input("\nChoose your action (1-3, S, Q): ").strip().upper()

        if choice == "Q":
            print(f"\n{CYAN}Saul Goodman out! Final Cash: ${self.cash:,}{RESET}\n")
            sys.exit(0)
        elif choice == "S":
            self.slippin_jimmy()
        elif choice in ["1", "2", "3"]:
            opt = case["options"][int(choice) - 1]
            print("\nPresenting defense to the court...")
            time.sleep(1)
            if random.random() <= opt["success"]:
                self.cash += opt["payout"]
                self.heat = max(0, self.heat + opt["heat"])
                print(f"{GREEN}WIN! Case dismissed! Earned ${opt['payout']:,}. Heat is now {self.heat}%.{RESET}")
            else:
                self.heat += opt["heat"] + 10
                print(f"{RED}LOSS! Judge was not amused. Earned $0. Heat spiked to {self.heat}%.{RESET}")
        else:
            print("\nInvalid choice! You wasted the court's time.")

        self.day += 1
        self.check_office_upgrade()

def main():
    print(f"{GOLD}")
    print("      ___ _____ _____ _____ _____     ")
    print("     | __|  _  |  |  | __  | __  |    ")
    print("     |__ |     |  |  | __ -|    -|    ")
    print("     |___|__|__|_____|_____|__|__|    ")
    print("     BETTER CALL SAUL: LEGAL DEFENSE  ")
    print(f"{RESET}")
    game = SaulGame()
    while True:
        game.play_turn()

if __name__ == "__main__":
    main()
