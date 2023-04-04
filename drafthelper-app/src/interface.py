from roster import Roster
from consensusranking import ConsensusRanking
from random import randint

class App:
    def __init__(self):
        self.cr = ConsensusRanking()
        self.cr.get_cr()
        #Kysytään liigan asetukset        
        
        if True:
            self.settings()
        else:
            self.roster = Roster(10, 2)
            self.draft()

    def settings(self):
        #Määritetään liigan koko
        self.league_size = int()
        while self.league_size < 6 or self.league_size > 14:
            self.league_size = int(input('Liigan koko (6-14 joukkuetta): '))
        #Määritetään draft positio
        self.draft_position = int()
        while True:
            self.draft_position = int(input('Millä numerolla pääset varaamaan: '))
            if self.draft_position > 0 and self.draft_position <= self.league_size:
                break
            else:
                print()
                print(f'Anna numero välillä 1 - {self.league_size}')
        self.roster = Roster(self.league_size, self.draft_position)

        print()

        print(f'Liigan koko {self.league_size} joukkuetta')
        print(f'Varausnumerosi on {self.draft_position}')

        self.draft()
    
    def draft(self):
        rounds = self.roster.get_roster_size()

        i = 1
        rolling_draftPos = 1
        while i <= rounds:
            self.cr.reset_indexes()
            if rolling_draftPos == self.draft_position:
                chosen = self.users_turn()
                self.roster.add_to_user_roster(chosen[0],chosen[1])
            else:
                chosen = self.bot_turn()
                team = 'User' + str(rolling_draftPos)
                print(f'{team} valitsi pelaajan: {chosen[0]}')
                self.roster.add_to_bot_roster(team, chosen[0],chosen[1])
            if rolling_draftPos < self.league_size:
                rolling_draftPos += 1
            else:
                rolling_draftPos = 1
                i += 1
    

        
        
    def users_turn(self):
        print()
        print('Sinun varausvuorosi!')
        print()
        print('Joukkueesi kokoonpano:')
        print(self.roster.get_user_roster())
        print()
        print(self.cr.get_3())
        while True:
            print()
            print('Valitse pelaajan numero tai -1, jos haluat varata muun pelaajan')
            try:
                choice = int(input('Valintasi: '))
                if choice in [-1,0,1,2]:
                    if choice == -1:
                        chosen_player = self.choice_by_name()
                    else:
                        chosen_player = self.choice_by_id(choice)

                    return chosen_player
            except ValueError:
                continue

    def choice_by_name(self):
        while True:
            chosen_player = input('Anna pelaajan nimi: ')
            if self.cr.is_a_real_player(chosen_player):
                pos = self.cr.take_a_player_by_name(chosen_player)
                print(f'{chosen_player} valittu')
                chosen_player = (chosen_player, pos)
                return chosen_player
            else:
                print(f'Pelaajaa {chosen_player} ei löytynyt')


    def choice_by_id(self, id):
        chosen_player = self.cr.take_a_player_by_id(id)
        print(f'{chosen_player[0]} valittu')    
        return chosen_player                 

    def bot_turn(self):
        #Valitse random top 5 valinta ihan vaan toiminnalisuuden testauksen vuoksi
        choice = randint(0,6)
        return self.cr.take_a_player_by_id(choice)


    

app = App()