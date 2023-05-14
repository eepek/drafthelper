from services.draft import Draft
from entities.consensusranking import ConsensusRanking
from entities.roster import Roster


class TextUI:
    def __init__(self, draft: Draft, roster: Roster, consensusranking: ConsensusRanking):
        self.draft = draft
        self.roster = roster
        self.consensusranking = consensusranking


    def draft_start(self):
        """Method that runs the text-based interface draft event.
        Runs until draft is completed. With each pick a new player is chosen
        to current team picking. On each pick calls appropriate methods
        depending if it is users or bots turn to choose.
        """
        rounds = self.roster.get_roster_size()

        current_round = 1
        rolling_draft_position = 1

        while current_round <= rounds:
            self.consensusranking.reset_indexes()

            if rolling_draft_position == self.draft.draft_position:
                self.users_turn()

                print(self.roster.get_user_roster())

            else:
                team = self.roster.team_names[rolling_draft_position]
                chosen = self.draft.bot_turn(team)
                print(f'{team} valitsi pelaajan: {chosen[0]}')

            if rolling_draft_position < self.draft.league_size:
                rolling_draft_position += 1
            else:
                rolling_draft_position = 1
                current_round += 1

        self.roster.return_all_the_rosters()

    def users_turn(self):
        """Handles the users turn during text-based draft event. Gets recommended players,
        takes users choice and returns it. Only used in text based UI.
        Returns:
            Player chosen by user as tuple with player name and position
        """
        recommend_players_df = self.user_turn_info()
        while True:
            print()
            print('Valitse pelaajan numero tai -1, jos haluat varata muun pelaajan')
            try:
                choice = int(input('Valintasi: '))
            except ValueError:
                print('Virheellinen valinta!')
                continue

            if choice in [-1, 0, 1, 2]:
                if choice == -1:
                    chosen_player = self.get_player_from_user()
                else:
                    player_name = recommend_players_df.at[choice, 'PLAYER NAME']
                    chosen_player = self.draft.choose_player(player_name)
                self.roster.add_to_roster(
                    self.roster.user_team, chosen_player[0], chosen_player[1])

                if chosen_player is False or chosen_player[1] is False:
                    print('Jotain meni vikaan, valitse pelaaja uudelleen')
                    continue

                return chosen_player

    def user_turn_info(self):
        """Shows the information shown on users every turn. Shows users current roster.
        Gets recommended players form Consensusranking object and prints the player
        information for user. Only used in text-based UI.

        Returns:
            Pandas dataframe containing recommended players"""
        print()
        print('Sinun varausvuorosi!')
        print()
        print('Joukkueesi kokoonpano:')
        print(self.roster.get_user_roster())
        print()
        print(self.roster.check_full_positions(self.roster.user_team))
        full_positions = self.roster.check_full_positions(
            self.roster.user_team)
        recommend_players_df = self.consensusranking.get_players(3, full_positions)
        if recommend_players_df is False:
            print("Suositeltuja pelaajia ei tarjolla, ole hyvä ja valitse -1")
            return recommend_players_df
        print(recommend_players_df)
        return recommend_players_df

    def get_player_from_user(self):
        """Used in text interface to get name of the player chosen from the user

        Returns:
            tuple: (players name, playing position)
        """
        while True:
            player = input('Anna pelaajan nimi: ')
            chosen_player = self.draft.choose_player(player)
            if chosen_player is None:
                print(f'Pelaajaa {player} ei löytynyt')
                continue
            print(f'{chosen_player} valittu')
            return chosen_player