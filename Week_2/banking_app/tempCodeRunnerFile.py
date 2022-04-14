class Director:
    guild = "Guild of Directors"    
    def __init__(self,first_name,last_name,birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        
    def start_scene(self):
        print("ACTION!")
        return self
            
    def end_scene(self):
        print("CUT")
        return self
    
class Movie:
    def __init__(self,title,genre,release_date,box_office):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.box_office = box_office
    
spielberg = Director("steven","Spielberg","1946-12-18")
et = Movie("ET","Sci-fi","1982",250000000)

print(spielberg.birthday)

spielberg.start_scene().end_scene()

print(Director.guild)