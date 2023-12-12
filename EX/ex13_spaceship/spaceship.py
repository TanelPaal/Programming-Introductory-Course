"""Spaceship."""


class Crewmate:
    """ Crewmate class. """
    crewmate_roles = ["Sheriff", "Guardian Angel", "Altruist"]

    def __init__(self, color: str, role: str, tasks: int = 10):
        """ Crewmate constructor."""
        self.color = color.title()
        self.role = role.title() if role.title() in self.crewmate_roles else "Crewmate"
        self.tasks = tasks
        self.protected = False

    def __repr__(self):
        """ Crewmate representation. """
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        """ Complete task. """
        if self.tasks > 0:
            self.tasks -= 1
        else:
            print("No more tasks left.")


class Impostor:
    """ Impostor class. """
    def __init__(self, color: str, role: str = "Impostor"):
        """ Impostor constructor. """
        self.color = color.title()
        self.role = role.title()
        self.kills = 0

    def __repr__(self):
        """ Impostor representation. """
        return f"Impostor {self.color}, kills: {self.kills}."


class Spaceship:
    """ Spaceship class. """
    max_impostors = 3

    def __init__(self):
        """ Spaceship constructor. """
        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []

    def get_crewmate_list(self):
        """ Get crewmate list. """
        return self.crewmate_list

    def get_impostor_list(self):
        """ Get impostor list. """
        return self.impostor_list

    def get_dead_players(self):
        """ Get dead players. """
        return self.dead_players

    def add_crewmate(self, crewmate):
        """ Add crewmate. """
        if isinstance(crewmate, Crewmate):
            if crewmate.color not in [crew.color for crew in self.crewmate_list + self.impostor_list]:
                self.crewmate_list.append(crewmate)
            else:
                print(f"{crewmate.color} player already exists in Spaceship.")
        else:
            print(f"{crewmate.color} cannot be a Crewmate.")

    def add_impostor(self, impostor: Impostor):
        """ Add impostor."""
        if isinstance(impostor, Impostor):
            if len(self.impostor_list) < self.max_impostors:
                if impostor.color not in [imp.color for imp in self.impostor_list + self.crewmate_list]:
                    self.impostor_list.append(impostor)
                else:
                    print(f"{impostor.color} player already exists in Spaceship.")
            else:
                print("No more than three impostors can be on Spaceship.")
        else:
            print(f"{impostor.color} cannot be an Impostor.")

    def kill_crewmate(self, impostor: Impostor, crewmate_color: str):
        """ Kill crewmate. """
        for crewmate in self.crewmate_list:
            if crewmate.color.lower() == crewmate_color.lower():
                if not crewmate.protected:
                    self.dead_players.append(crewmate)
                    self.crewmate_list.remove(crewmate)
                    impostor.kills += 1
                else:
                    crewmate.protected = False  # Remove protection after an attempted kill
                return

    def kill_impostor(self, sheriff: Crewmate, impostor_color: str):
        """ Kill impostor. """
        if sheriff.role == "Sheriff" and sheriff in self.crewmate_list:
            for impostor in self.impostor_list:
                if impostor.color.lower() == impostor_color.lower():
                    self.dead_players.append(impostor)
                    self.impostor_list.remove(impostor)
                    return
            self.crewmate_list.remove(sheriff)
            self.dead_players.append(sheriff)

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        """ Revive crewmate. """
        if altruist.role == "Altruist" and altruist in self.crewmate_list and dead_crewmate in self.dead_players:
            self.dead_players.append(altruist)
            self.crewmate_list.remove(altruist)
            self.crewmate_list.append(dead_crewmate)
            self.dead_players.remove(dead_crewmate)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_protect: Crewmate):
        """ Protect crewmate. """
        is_protected = False
        for crewmate in self.crewmate_list:
            if crewmate.protected:
                is_protected = True
        if guardian_angel.role == "Guardian Angel" and guardian_angel in self.dead_players and crewmate_protect in self.crewmate_list and not is_protected:
            crewmate_protect.protected = True

    def sort_crewmates_by_tasks(self):
        """ Sort crewmate by tasks. """
        return sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)

    def sort_impostors_by_kills(self):
        """ Sort impostors by kills. """
        return sorted(self.impostor_list, key=lambda impostor: impostor.kills, reverse=True)

    def get_regular_crewmates(self):
        """ Get regular crewmate. """
        return [crewmate for crewmate in self.crewmate_list if crewmate.role == "Crewmate"]

    def get_role_of_player(self, color: str):
        """ Get role of player. """
        for crewmate in self.crewmate_list:
            if crewmate.color.lower() == color.lower():
                return crewmate.role
        for impostor in self.impostor_list:
            if impostor.color.lower() == color.lower():
                return impostor.role

    def get_crewmate_with_most_tasks_done(self):
        """ Crewmate with most tasks done. """
        return self.sort_crewmates_by_tasks()[-1]

    def get_impostor_with_most_kills(self):
        """ Get impostor with most kills. """
        return self.sort_impostors_by_kills()[0]


if __name__ == "__main__":
    print("Spaceship.")

    spaceship = Spaceship()
    print(spaceship.get_dead_players())  # -> []
    print()

    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    white = Crewmate("White", "Impostor")
    yellow = Crewmate("Yellow", "Guardian Angel", tasks=5)
    green = Crewmate("green", "Altruist")
    blue = Crewmate("BLUE", "Sheriff", tasks=0)

    print(red)  # -> Red, role: Crewmate, tasks left: 10.
    print(white)  # -> White, role: Crewmate, tasks left: 10.
    print(yellow)  # -> Yellow, role: Guardian Angel, tasks left: 5.
    print(blue)  # -> Blue, role: Sheriff, tasks left: 0.
    print()

    print("Let's make Yellow complete a task.")
    yellow.complete_task()
    print(yellow)  # ->  Yellow, role: Guardian Angel, tasks left: 4.
    print()

    print("Adding crewmates to Spaceship:")
    spaceship.add_crewmate(red)
    spaceship.add_crewmate(white)
    spaceship.add_crewmate(yellow)
    spaceship.add_crewmate(green)
    print(spaceship.get_crewmate_list())  # -> Red, White, Yellow and Green

    spaceship.add_impostor(blue)  # Blue cannot be an Impostor.
    print(spaceship.get_impostor_list())  # -> []
    spaceship.add_crewmate(blue)
    print()

    print("Now let's add impostors.")
    orange = Impostor("orANge")
    black = Impostor("black")
    purple = Impostor("Purple")
    spaceship.add_impostor(orange)
    spaceship.add_impostor(black)

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    print(spaceship.get_impostor_list())  # -> Orange, Black and Purple
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    spaceship.kill_crewmate(black, "purple")  # You can't kill another Impostor, silly!
    print(spaceship.get_dead_players())  # -> Yellow
    print()

    print("Yellow is a Guardian angel, and can protect their allies when dead.")
    spaceship.protect_crewmate(yellow, green)
    print(green.protected)  # -> True
    spaceship.kill_crewmate(orange, "green")
    print(green in spaceship.dead_players)  # -> False
    print(green.protected)  # -> False
    print()

    print("Green revives their ally.")
    spaceship.kill_crewmate(purple, "RED")
    spaceship.revive_crewmate(green, red)
    print(red in spaceship.dead_players)  # -> False
    print()

    print("Let's check if the sorting and filtering works correctly.")

    red.complete_task()
    print(spaceship.get_role_of_player("Blue"))  # -> Sheriff
    spaceship.kill_crewmate(purple, "blue")
    print(spaceship.sort_crewmates_by_tasks())  # -> Red, White
    print(spaceship.sort_impostors_by_kills())  # -> Purple, Orange, Black
    print(spaceship.get_regular_crewmates())  # -> White, Red
