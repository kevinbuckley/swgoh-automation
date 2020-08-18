
def get_players():
    player_scores = []
    player_scores.append(Player(["Apex"]))
    player_scores.append(Player(["AznGrimReaper"]))
    player_scores.append(Player(["Bader"]))
    player_scores.append(Player(["Balerion"]))
    player_scores.append(Player(["BaneDoom", "aneDoom"]))
    player_scores.append(Player(["BigUnit"]))
    player_scores.append(Player(["Bloodpapa"]))
    player_scores.append(Player(["BombRob12"]))
    player_scores.append(Player(["Cloudkicker"]))
    player_scores.append(Player(["DarthKelleyus"]))
    player_scores.append(Player(["Decks"]))
    player_scores.append(Player(["Dr Sleep"]))
    player_scores.append(Player(["Emilia Starcrusher"]))
    player_scores.append(Player(["Generaljew"]))
    player_scores.append(Player(["GreyRevan GuardianDragon"]))
    player_scores.append(Player(["Gutterz"]))
    player_scores.append(Player(["Icyjediknight"]))
    player_scores.append(Player(["ImABombadPirateMF"]))
    player_scores.append(Player(["Jalexor"]))
    player_scores.append(Player(["Jlexor"]))
    player_scores.append(Player(["Kaytee Glopio"]))
    player_scores.append(Player(["Kbux"]))
    player_scores.append(Player(["Lazarus"]))
    player_scores.append(Player(["LBBNSKI"]))
    player_scores.append(Player(["Lenders Quizan"]))
    player_scores.append(Player(["Macery"]))
    player_scores.append(Player(["Messor"]))
    player_scores.append(Player(["Nater"]))
    player_scores.append(Player(["Patria", "patrra", "Patrria"]))
    player_scores.append(Player(["plank"]))
    player_scores.append(Player(["Raekwon Reef"]))
    player_scores.append(Player(["Ramm Rod"]))
    player_scores.append(Player(["Revan5"]))
    player_scores.append(Player(["Rokhan Raiders"]))
    player_scores.append(Player(["Schotime"]))
    player_scores.append(Player(["Shadowfox"]))
    player_scores.append(Player(["Shadraq"]))
    player_scores.append(Player(["Spectre"]))
    player_scores.append(Player(["Spencetheboss"]))
    player_scores.append(Player(["Stretchman"]))    
    player_scores.append(Player(["Sweaty Sweiit Concorkill"]))
    player_scores.append(Player(["SwoleDarthHero"]))
    player_scores.append(Player(["Thunder Bunny"]))
    player_scores.append(Player(["Timmers"]))
    player_scores.append(Player(["Tomcat"]))
    player_scores.append(Player(["Torbjorn87"]))
    player_scores.append(Player(["Xeptor"]))
    player_scores.append(Player(["ZanyeZest"]))
    
    return player_scores

class Player:

    def __init__(self, names):
        self.name = names[0]
        self.names = names    # creates a new empty list for each dog
        self.score = 0
    