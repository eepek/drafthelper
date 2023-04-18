from random import choices
from services.roster import Roster
from services.consensusranking import ConsensusRanking
from services.settings import Settings


class Draft:

    def __init__(self, settings: Settings, roster: Roster, consensusranking: ConsensusRanking):
        self.roster = roster
        self.consensusranking = consensusranking

        self.settings = settings

        self.league_size = self.settings.get_league_size()
        self.draft_position = self.settings.get_draft_position()
        self.consensusranking.generate_consensusranking()

        self.draft_start()

    def draft_start(self):
        rounds = self.roster.get_roster_size()

        current_round = 1
        rolling_draft_position = 1

        while current_round <= rounds:
            self.consensusranking.reset_indexes()

            if rolling_draft_position == self.draft_position:
                self.users_turn()

                print(self.roster.get_user_roster())

            else:
                team = 'User' + str(rolling_draft_position)
                self.bot_turn(team)

            if rolling_draft_position < self.league_size:
                rolling_draft_position += 1
            else:
                rolling_draft_position = 1
                current_round += 1

        self.roster.return_all_the_rosters()

    def users_turn(self):
        recommend_players_df = self.user_turn_info()
        while True:
            print()
            print('Valitse pelaajan numero tai -1, jos haluat varata muun pelaajan')
            try:
                choice = int(input('Valintasi: '))
            except ValueError:
                print('Virheellinen valinta!')
                continue

            if choice in [-1, 0, 1, 2, 3, 4]:
                if choice == -1:
                    chosen_player = self.choice_by_name()
                else:
                    player_name = recommend_players_df.at[choice, 'PLAYER NAME']
                    chosen_player = self.choice_by_id(player_name)
                self.roster.add_to_roster(
                    self.roster.user_team, chosen_player[0], chosen_player[1])

                if chosen_player is False or chosen_player[1] is False:
                    print('Jotain meni vikaan, valitse pelaaja uudelleen')
                    continue

                return chosen_player

    def user_turn_info(self):
        print()
        print('Sinun varausvuorosi!')
        print()
        print('Joukkueesi kokoonpano:')
        print(self.roster.get_user_roster())
        print()
        print(self.roster.check_full_positions(self.roster.user_team))
        full_positions = self.roster.check_full_positions(
            self.roster.user_team)
        recommend_players_df = self.consensusranking.get_players(5, full_positions)
        if recommend_players_df is False:
            print("Suositeltuja pelaajia ei tarjolla, ole hyvä ja valitse -1")
            return recommend_players_df
        print(recommend_players_df)
        return recommend_players_df

    def choice_by_name(self):
        while True:
            chosen_player = input('Anna pelaajan nimi: ')
            if self.consensusranking.is_a_real_player(chosen_player):
                pos = self.consensusranking.take_a_player_by_name(chosen_player)
                print(f'{chosen_player} valittu')
                chosen_player = (chosen_player, pos)
                return chosen_player

            print(f'Pelaajaa {chosen_player} ei löytynyt')

    def choice_by_id(self, name):
        if self.consensusranking.is_a_real_player(name):
            print(f'{name} valittu')
            return (name, self.consensusranking.take_a_player_by_name(name))

        return False

    def bot_turn(self, team_name: str):
        # Valitse random top 5 valinta ihan vaan toiminnalisuuden testauksen vuoksi
        filled_roster_spots = self.roster.check_full_positions(team_name)
        players_dataframe = self.consensusranking.get_players(
            5, filled_roster_spots)

        # Arvotaan valinta
        possibilities = [0, 1, 2, 3, 4]
        probabilities = [0.4, 0.2, 0.2, 0.1, 0.1]
        choice_id = choices(possibilities, probabilities)[0]

        # Haetaan pelajaa ja lisätään rosteriin
        chosen_player_name = players_dataframe.at[choice_id, 'PLAYER NAME']
        chosen_player_position = self.consensusranking.take_a_player_by_name(
            chosen_player_name)
        self.roster.add_to_roster(
            team_name, chosen_player_name, chosen_player_position)
        print(f'{team_name} valitsi pelaajan: {chosen_player_name}')

        return (chosen_player_name, chosen_player_position)
