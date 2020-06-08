"""
===============================
A simple text based python game
===============================

Notes:

As of now, prompt user to send message to the ailens or not to do that and simply go to them.
Find a way to organize this.
Add comments and doc strings.
Figure out the plot a bit more.

Bugs:
So far if you choose to repeat the game it doesn't work right.
This is mainly because in the repeat method in the UserInputs class
in the if statement to determine if the user wants to repeat the game
it just replays the start method and stops after all that code has been
executed.

So future me, set up a method to repeat the game and dynamically adjust to
whatever the choice the user has made.

"""


class UserInputs():

    def enter(self):
        press_key = None
        while press_key != '':
            press_key = input('\n**Press enter to continue** ')
            if press_key == '':
                continue

            else:
                press_key = input('\n**Press enter to continue** ')

    def repeat(self):
        print('\nThank you for playing.')
        repeat = ''
        while True:
            # * Asks to repeat the script.
            repeat = input(
                '\nWould you like to repeat the game? (Y/N): ').lower()
            if repeat[0] == 'y':
                g.start()
                continue
            if repeat[0] == 'n':
                break


ui = UserInputs()


class Game():

    def start(self):
        print('\nYou are an avid astronomer who has found alien life on a distant world. A mere 20 light years away. The year is 2035. ')
        print('\nYou must decide whether to tell the world about it and see how they react or keep it a secret and make sure no one finds out.')
        ui.enter()

        keep = input(
            "Keep it to yourself and a select few? Or share it? (y/n) ").lower()
        if keep[0] == 'y':
            print('\nVery well.')

        elif keep[0] == 'n':
            print('\nVery well.')

            tell_world = input('\nTell the world? (Y/N): ').lower()
            if tell_world[0] == 'y':
                print(
                    '\nYou have now made your decision, you must face the consequences.')
                tell_world = True

            elif tell_world[0] == 'n':
                print(
                    '\nYou have now made you decision, you must face the consequences.')
                tell_world = False

    def middle(self):
        print('\nYou have now decided to tell the world.')
        print('\nThe world is shocked.')

        print('\nBut it has also ignited to a spark to contact these beings and technology is now rapidly advancing.')
        print('\nIt is now the year 2050. With the spark of interest in these beings, it has now evolved into a wildfire of new technology and innovation.')
        print('\nIn 6 months, the humanities first interstellar ship with a range of 45 light years, will be ready for launch. It is called the Epsilon.')
        ui.enter()

        abort = input(
            'A rumor spread around the world has ensued with some panic and people are beginning to question the launch of Epsilon. Will you still proceed? (y/n): ')
        if abort[0] == 'y':
            print('Very well, you must face consequences. ')
            print('\nThe world is now in mass paninc as they believe talking about these beings will kill them and if they go near the star system, the universe will end.')
            print('This is the end. People only remember you now for your discovery of alien life that led to the partial demise of the world.')
            ui.enter()
            ui.repeat()

        if abort[0] == 'n':
            def world_panic():
                """
                Case if the user decided not to tell the world and it eventually
                got out in a terrible way. Which way? I'm not really sure yet.
                """
                contact = input(
                    '\nScientists and civilians are wanting to try and communicate with these ailens. Will you send the message? (Y/N) ')
                if contact[0] == 'y':
                    print(
                        '\nThe alien species has interpreted the message sent to them as an act of aggression.')
                    print(
                        '\nThey are now heading in the direction of Earth with the intention to obliterate humankind.')
                    retaliate = input(
                        'Do you wish to retaliate against the aliens?? (y/n): ')

                    if retaliate[0] == 'y':
                        pass
                        # * Note to future self: You choose to retaliate so now the Epsilon is converted into a battle ready warship and 75 others are in the planning with multiple supporting vessels.
                        # * Multiple probes are placed around the solar system as a constant radar with some being sent on an interstellar journey. All probes have a radar range of over 10 lightyears.
                    if retaliate[0] == 'n':
                        print(
                            '\nMass panic slowly enveloped the world. Everything collapsed.')
                        print(
                            '\nWhen the ailens finally got to Earth, 45 years after they were discovered, humankind was already gone.')
                        ui.enter()
                        ui.repeat()

                if contact[0] == 'n':
                    pass
                    print('\nVery well, you must deal with the consequences.')

                    print('\nThe Epsilon is now ready for launch and will be making first contact in the year 2075.')
                    ui.enter()

                    print('\nIt is now the year 2062. The crew is now halfway through their journey among the stars.')
                    # * continue the rest of the game, not really sure what happens after this.

            world_panic()


if __name__ == "__main__":
    g = Game()
    g.start()
    g.middle()
