class Horse:
    def __init__(self, speed, age, name, place_in_race=None):
        self.speed = speed
        self.age = age
        self.name = name
        self.place_in_race = place_in_race

class Race:
    def __init__(self):
        self.members = []

    def add_member(self, horse):
        if horse not in self.members and 3 <= horse.age <= 7:
            self.members.append(horse)

    def del_member(self, horse):
        if horse in self.members:
            self.members.remove(horse)
    
    def top_three_horses(self):
        avg_age = sum(horse.age for horse in self.members) / len(self.members)

        sorted_horses = sorted(self.members, key=lambda h: h.speed + abs(h.age - avg_age), reverse=True)
        print("Top Three Horses:")
        for i in range(min(3, len(sorted_horses))):
            horse = sorted_horses[i]
            print(f'Rank {i+1}: Name: {horse.name}, Speed: {horse.speed}, Age: {horse.age}')

    def sort_by_speed(self):
        self.members.sort(key=lambda horse: horse.speed)

my_horse_1 = Horse(25, 4, 'Baron')
my_horse_2 = Horse(30, 7, 'Hector')
my_horse_3 = Horse(10, 1, 'Jack')
my_horse_4 = Horse(20, 6, 'Max')
my_horse_5 = Horse(35, 5, 'Rex')

my_race = Race()

my_race.add_member(my_horse_1)
my_race.add_member(my_horse_2)
my_race.add_member(my_horse_3)
my_race.add_member(my_horse_4)
my_race.add_member(my_horse_5)

my_race.del_member(my_horse_1)

my_race.top_three_horses()
