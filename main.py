class Student: 
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
        
    def change_name(self, change_name):
        self.change_name = change_name
        print ("Your name is" , change_name)
    
    def change_age(self, change_age):
        self.change_age = change_age
        print ("Your age is" , change_age)
    
    def add_tracks(self, add_track):
        self.add_track = add_track
        print ("Your track is", add_track)
    
    def get_score(self):
        return ("Your score is", self.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_tracks("Full stack")
Bob.get_score()
