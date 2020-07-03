"""
===============================
A simple text based python game
===============================

Notes:



Bugs:

No bugs I'm currently aware of
as of the latest commit.

"""


class UserInputs():
    """
    Inputs the user has to provide that effect the game.
    """

    def enter(self):
        press_key = None
        while press_key != '':
            press_key = input('\n**Press enter to continue** ')
            if press_key == '':
                continue

            else:
                press_key = input('\n**Press enter to continue** ')

    def repeat(self):
        print('----------------------')
        print('Thank you for playing.')
        print('----------------------')
        repeat = ''
        while True:
            # * Asks to repeat the script.
            repeat = input(
                '\nWould you like to repeat the game? (Y/N): ').lower()
            if repeat[0] == 'y':
                main()
                continue
            if repeat[0] == 'n':
                break


ui = UserInputs()


def main():
    """
    The game.
    """
    print('\nYou are an avid astronomer who has found alien life on a distant world. A mere 20 light years away. The year is 2035. ')
    print('\nYou must decide whether to tell the world about it and see how they react or keep it a secret and make sure no one finds out.')
    ui.enter()

    keep = input(
        "Keep it to yourself and a select few? Or share it? (y/n) ").lower()
    if keep[0] == 'y':
        print('\nVery well.')
        ui.repeat()

    elif keep[0] == 'n':
        print('\nVery well.')

        tell_world = None

        tell_world = input('\nTell the world? (Y/N): ').lower()
        if tell_world[0] == 'y':
            print(
                '\nYou have now made your decision, you must face the consequences.')
            tell_world = 'yes'

        if tell_world[0] == 'n':
            print(
                '\nYou have now made you decision, you must face the consequences.')
            tell_world = 'no'

        if tell_world == 'yes':
            print('\nYou have now decided to tell the world.')
            print('\nThe world is shocked.')

            print(
                '\nBut it has also ignited to a spark to contact these beings and technology is now rapidly advancing.')
            print('\nIt is now the year 2050. With the spark of interest in these beings, it has now evolved into a wildfire of new technology and innovation.')
            print('\nIn 6 months, the humanities first interstellar ship with a range of 45 light years, will be ready for launch. It is called the Epsilon.')
            ui.enter()

            abort = input(
                'A rumor spread around the world has ensued with some panic and people are beginning to question the launch of Epsilon. Will you still proceed? (Y/N): ').lower()
            if abort[0] == 'n':
                print('Very well, you must face consequences. ')
                print('\nThe world is now in mass paninc as they believe talking about these beings will kill them and if they go near the star system, the universe will end.')
                print(
                    'This is the end. People only remember you now for your discovery of alien life that led to the partial demise of the world.')
                ui.enter()
                ui.repeat()

            if abort[0] == 'y':
                def world_panic():
                    """
                    Case if the user decided not to tell the world and it eventually
                    got out in a terrible way. Which way? I'm not really sure yet.
                    """
                    contact = input(
                        '\nScientists and civilians are wanting to try and communicate with these ailens. Will you send the message? (Y/N) ').lower()
                    if contact[0] == 'y':
                        print(
                            '\nThe alien species has interpreted the message sent to them as an act of aggression.')
                        print(
                            '\nThey are now heading in the direction of Earth with the intention to obliterate humankind.')
                        retaliate = input(
                            'Do you wish to retaliate against the aliens?? (Y/N): ')

                        if retaliate[0] == 'y':
                            pass
                            print(
                                '\nThe Epsilon is now converted into a warship and 75 smaller ships are now under construction.')
                            print(
                                'Hundreds of probes are launched and placed around the solar system as long range radar. They have a range of over 15 light years.')
                            print(
                                '\nOrbital shipyards are placed around Mars, Jupiter, Saturn, and Pluto.')

                            evac = input(
                                'Do you want to Evacuate Earth and colonies throughout the solar system to a nearby star system, Alpha Centauri? (Y/N): ').lower()
                            if evac[0] == 'y':
                                print(
                                    'Evacuations have begun, in 10 years 80% of Humanity will be approaching Alpha Centauri.')
                                ui.enter()

                                print(
                                    '\nThe remaining 20% of Humanity will stay behind to build the ships and protect the Solar System.')
                                # * Continue the story after this, maybe have something happen like discovering more ailens or an early attack.
                                ui.enter()
                                print(
                                    '\nThe ailens sent some sort of probe in the direction of Earth that has immense gravity, that of a large gas giant.')
                                print(
                                    '\nThis probe has caused large amounts of comets in the oort cloud to head towards the inner solar system.')
                                ui.enter()

                                destroy_comets = input(
                                    'Do you want to destroy the comets? Or hope it misses Earth? (D/M): ').lower()
                                if destroy_comets[0] == 'd':
                                    spend_money = input(
                                        'The plan to destory the comets is around 17 billion dollars. Will you still proceed? (Y/N): ').lower()
                                    if spend_money[0] == 'y':
                                        pass
                                        # * Start running out of money here

                                    if spend_money[0] == 'n':
                                        print(
                                            'The Earth is hit by a few medium sized comets ranging in size from 5 to 12 meters.')
                                        print(
                                            '\nThe 12 meter comet impacted a critical manufacturing site for the rockets responsible for orbital construction.')

                                if destroy_comets[0] == 'm':
                                    silence_people = input(
                                        'Online, multiple people are spreading rumors that the comets heading towards the Earth are 100m wide and will destory everything. Will you silence them? (Y/N): ').lower()
                                    if silence_people[0] == 'n':
                                        print(
                                            '\nEven though these people online are spreading rumors, they quickly lose popularity as the newest observations show that the comets are between 5m-12m.')
                                    if silence_people[0] == 'y':
                                        print(
                                            '\nYou realize that the majority of these people live in the US. You cant take away their right to free speech.')
                                        ui.enter()
                                        print(
                                            '\nPeople view this as a reinforcement of their false beliefs.')
                                        print(
                                            'More panic spreads among people everywhere.')
                                        # * just do more stuff after this.
                                        ui.enter()

                        if retaliate[0] == 'n':
                            print(
                                '\nMass panic slowly enveloped the world. Everything collapsed.')
                            print(
                                '\nWhen the ailens finally got to Earth, 45 years after they were discovered, humankind was already gone.')
                            ui.enter()
                            ui.repeat()

                    if contact[0] == 'n':
                        pass
                        print(
                            '\nVery well, you must deal with the consequences.')

                        print(
                            '\nThe Epsilon is now ready for launch and will be making first contact in the year 2075.')
                        ui.enter()

                        print('The Epsilon has now launched.')
                        ui.enter()

                        print(
                            '\nIt is now the year 2062. The crew is now halfway through their journey among the stars.')
                        ui.repeat()
                        # * continue the rest of the game, not really sure what happens after this.

                world_panic()
        elif tell_world == 'no':
            print(
                'Word quickly spreads among the highest people of world authority.')
            ui.enter()
            print('\nMassive ships are now being constructed.')


if __name__ == "__main__":
    main()
