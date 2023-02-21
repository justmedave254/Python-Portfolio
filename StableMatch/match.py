#Women that the Men preffer
preferred_rankings_men = {
    'ryan'   : ['lizzie', 'sarah', 'zoey', 'daniella'],
    'josh'   : ['sarah', 'lizzie', 'daniella', 'zoey'],
    'blake'  : ['sarah', 'daniella', 'zoey', 'lizzy'],
    'connor' : ['lizzie', 'sarah', 'zoey', 'daniella']
}

#Men that the Women preffer
preferred_rankings_women = {
    'lizzie'   : ['ryan', 'blake', 'josh', 'connor'],
    'sarah'    : ['ryan', 'blake', 'connor', 'josh'],
    'zoey'     : ['connor', 'josh', 'ryan', 'blake'],
    'daniella' : ['ryan', 'josh', 'connor', 'blake']
}

#list to contain all people tentatively engaged
tentative_engagements = []

#men that have't proposed yet
free_men =[]

def init_free_men():
    for man in preferred_rankings_men:
        free_men.append(man)

def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            begin_matching(man)

def begin_matching(man):
    print("\n-------------------------------------------------")
    print(f"Currently dealing with {man}")
    print("-------------------------------------------------\n")

    for woman in preferred_rankings_men[man]:

        taken_match = [couple for couple in tentative_engagements if woman in couple]

        if len(taken_match) == 0:
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print(f"Hurray!!! {man} is no longer a free man and is now tentatively engaged to {woman}.")
            break
        elif len(taken_match) > 0:
            print(f"Oooppss!!! {woman} is already taken\n")
            print("Cheking to see if she prefers to stay with current partner .../ ")

            current_guy = preferred_rankings_women[woman].index(taken_match[0][0])
            potential_guy = preferred_rankings_women[woman].index(man)

            if current_guy < potential_guy:
                print(f"Check complete.\n\nOouff!! Sorry my guy, She is satisfied with her current partner being {taken_match[0][0]}")
            else:
                print(f"Check complete.\n It's you're lucky day. She prefers to be with you '{man}' as compared to her current guy '{taken_match[0][0]}'")
                print(f"System is making {taken_match[0][0]} free again and tenttively engaging {woman} to her new guy {man}.")

                #New guy is engaged...remove from free men
                free_men.remove(man)

                #Old guy is single so adding to free men
                free_men.append(taken_match[0][0])

                taken_match[0][0] = man
                break

def main():
    init_free_men()
    stable_matching()

    print("Program Complete...")
    print("Here is the list of who is with who...")
    print(tentative_engagements)

if __name__ == "__main__":
    main()

