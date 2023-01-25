class Students:
                
    school="ccs"

nikhil = Students()
nikhil.name ="nikhil"
nikhil.roll ="58"
nikhil.classs ="10th"


vivek = Students()
vivek.name = "vivek"
vivek.roll="66"
vivek.classs="10th"




print(nikhil.__dict__)


nikhil.school="DPS"
print(nikhil.__dict__)# it will not change main variable but it will create instance variable#first of all compilar check for compilafr variable than for instance variable