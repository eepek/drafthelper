from roster import Roster
from consensusranking import ConsensusRanking
from random import randint

class App:
    def __init__(self):
        self.cr = ConsensusRanking()
        self.cr.get_cr()
        #Kysytään liigan asetukset        
        
        if False:
            self.settings()
        else:
            self.leagueSize = 10
            self.draftPosition = 4

        self.roster = Roster(self.leagueSize, self.draftPosition)

        self.draft()

    def settings(self):
        #Määritetään liigan koko
        self.leagueSize = int()
        while self.leagueSize < 6 or self.leagueSize > 14:
            self.leagueSize = int(input('Liigan koko (6-14 joukkuetta): '))
        #Määritetään draft positio
        self.draftPosition = int()
        while True:
            self.draftPosition = int(input('Millä numerolla pääset varaamaan: '))
            if self.draftPosition > 0 and self.draftPosition <= self.leagueSize:
                break
            else:
                print()
                print(f'Anna numero välillä 1 - {self.leagueSize}')

        print()

        print(f'Liigan koko {self.leagueSize} joukkuetta')
        print(f'Varausnumerosi on {self.draftPosition}')

        self.draft()
    
    def draft(self):
        rounds = self.roster.getRosterSize()

        i = 0
        rollingDraftPos = 1
        while i < rounds:
            self.cr.reset_indexes()
            if rollingDraftPos == self.draftPosition:
                chosen = self.users_turn()
                self.roster.addToUserRoster(chosen[0],chosen[1])
            else:
                chosen = self.bot_turn()
                team = 'User' + str(rollingDraftPos)
                print(team)
                self.roster.addToBotRoster(team, chosen[0],chosen[1])
            if rollingDraftPos < self.leagueSize:
                rollingDraftPos += 1
            else:
                rollingDraftPos = 1
                i += 1
                print(i)

        
        
    def users_turn(self):
        print()
        print('Sinun varausvuorosi!')
        print('Valitse pelaaja tai -1, jos haluat varata muun pelaajan')
        print(self.cr.get_3())

        choice = int(input('Valintasi: '))
        if choice == -1:
            while True:
                chosen_player = input('Anna pelaajan nimi: ')
                if self.cr.is_a_real_player(chosen_player):
                    pos = self.cr.take_a_player_by_name(chosen_player)
                    print(f'{chosen_player} valittu')
                    chosen_player = (chosen_player, pos)
                    break
                else:
                    print(f'Pelaajaa {chosen_player} ei löytynyt')
        else:
            chosen_player = self.cr.take_a_player_by_id(choice)
            print(chosen_player[0])

        return chosen_player

    def bot_turn(self):
        #Valitse random top 5 valinta ihan vaan toiminnalisuuden testauksen vuoksi
        choice = randint(0,6)
        return self.cr.take_a_player_by_id(choice)


    

app = App()