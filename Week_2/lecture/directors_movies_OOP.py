class Director:
    guild = "Guild of Directors"     
    all_directors = [] #class variable for all 
    def __init__(self,first_name,last_name,birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        Director.all_directors.append(self)
        
    def start_scene(self):
        print("ACTION!")
        return self
            
    def end_scene(self):
        print("CUT")
        return self
    
    @classmethod
    def rename_guild(cls,new_guild_name):
        cls.guild = new_guild_name
    
class Movie:
    rater = "MPAA"
    def __init__(self,title,genre,release_date,box_office):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.box_office = box_office
        
    @staticmethod
    def made_enough_money(box_office,cost):
        if(box_office > cost):
            print("This movie is a Bomb")
        elif(box_office < cost):
            print("At Least we broke even or made money")
    
spielberg = Director("steven","Spielberg","1946-12-18")
et = Movie("ET","Sci-fi","1982",250000000)

print(spielberg.birthday)

spielberg.start_scene().end_scene()

print(Director.guild) #RECOMMENDED

print(spielberg.guild) # NOT RECOMMENDED

for this_director in Director.all_directors:
    print(f"Director:{this_director.first_name} {this_director.last_name}")
    
Director.rename_guild("Kilo Maka")
print(f"After:{Director.guild}")

