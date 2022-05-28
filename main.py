class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(miyyah, name, age, tracks, score):
        miyyah.name = str(name)        
        miyyah.age = int(age)
        miyyah.tracks = str(tracks)
        miyyah.score = float(score)
        
    def change_name(miyyah, change_name):
            miyyah.change_name = change_name
            print("Thy name is", change_name)
        
    def change_age(miyyah, change_age):
            miyyah.change_age = change_age
            print(miyyah.change_name + " is ", change_age , " years old.")

    def add_track(miyyah, add_track):
            miyyah.add_track = add_track
            print("Track of", miyyah.change_name ," is ", add_track)
        
    def get_score(miyyah):
            print(miyyah.change_name, " score is ", miyyah.score)
        
    pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
