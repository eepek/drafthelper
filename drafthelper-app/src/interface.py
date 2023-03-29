from roster import Roster
from consensusranking import ConsensusRanking

class App:
    def __init__(self):
        self.cr = ConsensusRanking()
        self.roster = Roster()
        #Kysytään liigan asetukset
        self.settings()

    def settings(self):
        #Määritetään liigan koko
        leagueSize = int()
        while leagueSize < 6 or leagueSize > 14:
            leagueSize = int(input('Liigan koko (6-14 joukkuetta): '))
        #Määritetään draft positio
        draftPosition = int()
        while True:
            draftPosition = int(input('Millä numerolla pääset varaamaan: '))
            if draftPosition > 0 and draftPosition <= leagueSize:
                break
            else:
                print()
                print(f'Anna numero välillä 1 - {leagueSize}')

        print()

        print(f'Liigan koko {leagueSize} joukkuetta')
        print(f'Varausnumerosi on {draftPosition}')

        return
    
    def draft(self, leagueSize, draftPosition):
        rounds = self.roster.getRosterSize()




    

app = App()