# importing libraries
from durable.lang import *

# simple print messages as welcome note
def printmsg():
    print("\n\n\n==================================================================")
    print("\n\nKUSHAGRA'S CAREER AVISORY SYSTEM")
    print("-------------------------------------------------------------------------")
    nameoftheuser = input("Hi, Please enter your name: ")
    print("\nHi {0}, I'll help you with choosing career options after graduating from IIIT Delhi ".format(nameoftheuser))
    print("\n\nPlease answer few questions about your academics\n")
    print("\n----------------------------------------------------------------------")
    print("\nAre you purusing any of the below mentioned specialisations?")
    print('\tNon Specialisation ( Type ns)')
    print('\tArtificial Intelligence ( Type ai)')
    print('\tData Engineering (Type de) ')
    print('\tInformation Security ( Type is)')
    special = input("\nPlease enter your answer: ")
    print("\nHave you taken the following elective courses ?")
    print("\nPlease enter course initials or no")
    ansml=input("MACHINE LEARNING CSE 543 (ml):")
    ansdmg=input("DATA MINING CSE 506 (dm) :")
    ansoopd=input("OBJECT ORIENTED PROGRAMMING AND DESIGN CSE 600 (oopd)")
    ansga=input("GRADUATE ALGORITHMS CSE 525 (ga)")
    ansnlp=input("NATURAL LANGUAGE PROCESSING CSE 556 (nlp)")
    ansdw=input("DATA WAREHOUSING CSE 606 (dw)")
    print("\nOne last information!")
    gpa = input("Enter your GRADE POINT AVERAGE (gpa): ")
    return special, ansml, ansdmg, ansoopd, ansga, ansnlp, ansdw, gpa


with ruleset('checkcourses'):

    @when_all((m.area == 'ns') & (m.subjectcode == 'ml') & (m.grading >= 6))
    def func(c):
        c.assert_fact({'subject': 'MACHINE LEARNING ENGINEER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'dmg') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'oopd') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE DEVELOPMENT ENGINEER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'ga') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE ENGINEER or RESEARCHER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'nlp') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'AI ENGINEER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'dw') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})
    
    @when_all((m.area == 'ai') & (m.subjectcode == 'ml') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'MACHINE LEARNING & ARTIFICIAL INTELLIGENCE ENGINEER'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'dmg') & (m.grading >=5))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'oopd') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE DEVELOPMENT ENGINEER'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'ga') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE ENGINEER or RESEARCHER IN AI'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'nlp') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'NATURAL LANGUAGE PROCESSING ENGINEER'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'dw') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER OR BIG DATA ANALYTICS ENGINEER'})
    
    @when_all((m.area == 'de') & (m.subjectcode == 'ml') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'MACHINE LEARNING ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'dmg') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'oopd') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE DEVELOPMENT ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'ga') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'nlp') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'AI & NATURAL LANGUAGE PROCESSING ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'dw') & (m.grading >=9))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER OR BIG DATA ANALYTICS ENGINEER'})
    
    @when_all((m.area == 'is') & (m.subjectcode == 'ml') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'MACHINE LEARNING & SECURITY ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'dmg') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'oopd') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE DEVELOPMENT ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'ga') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE ENGINEER or WEB SECURITY ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'nlp') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'NATURAL LANGUAGE PROCESSING ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'dw') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'DATA SECURITY ENGINEER'})

    # output for must take courses
    @when_all(+m.subject)
    def output(c):
        print()
        print("{0}".format(c.m.subject))


def printmsg2():
    print("\nENROLLING IN IIIT DELHI WILL OBVIOUSLY MAKE YOU AN ENGINEER.\n")
    print("LET'S SEE WHAT OTHER CAREER OPTIONS DO YOU HAVE.\n\n ")
    print("IF YOU HAVE INTEREST IN PUBLIC ADMINISTRATION, TYPE = publicadmin") 
    print("IF YOU HAVE INTEREST IN PAINTING AND SKETCHING, TYPE = art")
    print("IF YOU HAVE INTEREST IN MUSIC, TYPE = music")
    print("IF YOU HAVE NO OTHER INTEREST AND WANT TO COMPLETE YOUR ENGINEERING COURSE, TYPE = tech")
    ch = input("Enter here: ")
    return ch

def tech():
    
    print("WE SEE THAT YOU HAVE INTEREST ONLY IN TECH FIELD\n")
    print("ITS PRETTY GOOD!")
    print("\nPLEASE BEAR WITH A FEW MORE QUESTIONS")
    print("What is your GPA:")
    gpa=input(":")
    gpa=int(gpa)
    if gpa == 10 :
          cht='machinel'
    elif gpa > 7 and gpa < 10:
          cht='software'
    elif gpa == 7 and gpa < 7:
          cht='testing'
    return cht

def nontech():
    print("\nWE SEE THAT YOU HAVE OTHER INTERESTS THAN ENGINEERING\n")
    print("\nDON'T WORRY IT'S ABSOLUTELY FINE TO DROP OFF THE UNIVERSITY AND FOLLOW YOUR HEART\n")
    print("IF YOU HAVE INTEREST IN BIRD WATCHING, TYPE = bird")
    print("IF YOU WANT TO TRAVEL THE WORLD, TYPE = travel")
    print("IF YOU WANT TO DO VLOGGING, TYPE = vlog")
    cht = input("Enter here: ")
    return cht

with ruleset('career_option'):
    @when_all((m.domain == 'publicadmin') & (m.domtype == 'travel'))
    def club(e):
        e.assert_fact({'subject': 'YOU MIGHT WANT TO CONSIDER INDIAN ADMINISTRATION SERVICES AS A CAREER OPTION'})

    @when_all((m.domain == 'publicadmin') & (m.domtype == 'bird'))
    def club(e):
        e.assert_fact({'subject': 'YOU CAN CONSIDER UPSC SERVICES OR BE A BIRD WATCHER'})

    @when_all((m.domain == 'publicadmin') & (m.domtype == 'vlog'))
    def club(e):
        e.assert_fact({'subject': 'YOU CAN CONSIDER UPSC SERVICES OR ALSO BE A YOUTUBER'})

    @when_all((m.domain == 'art') & (m.domtype == 'travel'))
    def club(e):
        e.assert_fact({'subject': 'YOU CAN TRAVEL PLACES AND PAINT LANDSCAPES'})

    @when_all((m.domain == 'art') & (m.domtype == 'bird'))
    def club(e):
        e.assert_fact({'subject': 'INSTEAD OF CAPTURING BIRDS WITH YOUR CAMERA, PAINT THEN INSTEAD'})

    @when_all((m.domain == 'art') & (m.domtype == 'vlog'))
    def club(e):
        e.assert_fact({'subject': 'BE AN ART VLOGGER'})
    @when_all((m.domain == 'music') & (m.domtype == 'bird'))
    def club(e):
        e.assert_fact({'subject': 'BE A VOCALIST & BIRD WATCHER'})

    @when_all((m.domain == 'music') & (m.domtype == 'travel'))
    def club(e):
        e.assert_fact({'subject': 'BE A MUSIC COMPOSER BRINGING DIFFERENT CULTURES TOGETHER THROUGH YOUR COMPOSITIONS'})

    @when_all((m.domain == 'music') & (m.domtype == 'vlog'))
    def club(e):
        e.assert_fact({'subject': 'BE AN MUSIC VLOGGER'})

    @when_all((m.domain == 'tech') & (m.domtype == 'machinel'))
    def club(e):
        e.assert_fact({'subject': 'PURSUE CAREER AS A MACHINE LEARNING ENGINEER OR A DATA SCIENCE ENGINEER'})

    @when_all((m.domain == 'tech') & (m.domtype == 'software'))
    def club(e):
        e.assert_fact({'subject': 'PURSUE CAREER AS A SOFTWARE DEVELOPMENT ENGINEER'})


    @when_all((m.domain == 'tech') & (m.domtype == 'testing'))
    def club(e):
        e.assert_fact({'subject': 'PURSUE CAREER AS A DEV/TESTING ENGINEER'})


    @when_all(+m.subject)
    def output(e):
        print()
        print("\n-------------------------------HERE ARE SOME ADDITIONAL ADVICES FOR YOU-------------------------------\n\n")
        print('HERE ARE SOME OTHER CAREER OPTIONS FOR YOU: {0}'.format(e.m.subject))

if __name__ == '__main__':
    speciala, ansmla, ansdmga, ansoopda, ansgaa, ansnlpa, ansdwa, gpaa = printmsg()
    print("\n-------------------------------HERE ARE YOUR RESULTS-------------------------------")
    print("FOLLOWING ARE THE CAREERS RECOMMENDED FOR YOU:\n\n")
    if(speciala == 'ns'):
        if(ansmla == 'ml'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansmla, 'grading':gpaa})
        if(ansdmga == 'dmg'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdmga, 'grading':gpaa})
        if(ansoopda == 'oopd'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansoopda, 'grading':gpaa})
        if(ansgaa == 'ga'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansgaa, 'grading':gpaa})
        if(ansnlpa == 'nlp'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansnlpa, 'grading':gpaa})
        if(ansdwa == 'dw'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdwa, 'grading':gpaa})
    elif(speciala == 'ai'):
        if(ansmla == 'ml'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansmla, 'grading':gpaa})
        if(ansdmga == 'dmg'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdmga, 'grading':gpaa})
        if(ansoopda == 'oopd'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansoopda, 'grading':gpaa})
        if(ansgaa == 'ga'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansgaa, 'grading':gpaa})
        if(ansnlpa == 'nlp'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansnlpa, 'grading':gpaa})
        if(ansdwa == 'dw'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdwa, 'grading':gpaa})
    elif(speciala == 'de'):
        if(ansmla == 'ml'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansmla, 'grading':gpaa})
        if(ansdmga == 'dmg'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdmga, 'grading':gpaa})
        if(ansoopda == 'oopd'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansoopda, 'grading':gpaa})
        if(ansgaa == 'ga'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansgaa, 'grading':gpaa})
        if(ansnlpa == 'nlp'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansnlpa, 'grading':gpaa})
        if(ansdwa == 'dw'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdwa, 'grading':gpaa})
    elif(speciala == 'is'):
        if(ansmla == 'ml'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansmla, 'grading':gpaa})
        if(ansdmga == 'dmg'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdmga, 'grading':gpaa})
        if(ansoopda == 'oopd'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansoopda, 'grading':gpaa})
        if(ansgaa == 'ga'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansgaa, 'grading':gpaa})
        if(ansnlpa == 'nlp'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansnlpa, 'grading':gpaa})
        if(ansdwa == 'dw'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdwa, 'grading':gpaa})
  
    print("\n-----------------------------------------------------------------------------------")
    ch = printmsg2()
    print("\n-----------------------------------------------------------------------------------")
    if ch == 'tech':
        cht = tech()
    else:
        cht = nontech()
    assert_fact('career_option',{'domain':ch,'domtype':cht})
    print("\n-----------------------------------------------------------------------------------")
    print("\n\tI HOPE THAT I COULD HELP YOU WITH CAREER ADVICE. HAVE A GREAT DAY!")
    print("\n-----------------------------------------------------------------------------------")
# importing libraries
from durable.lang import *

# simple print messages as welcome note
def printmsg():
    print("\n\n\n==================================================================")
    print("\n\nKUSHAGRA'S CAREER AVISORY SYSTEM")
    print("-------------------------------------------------------------------------")
    nameoftheuser = input("Hi, Please enter your name: ")
    print("\nHi {0}, I'll help you with choosing career options after graduating from IIIT Delhi ".format(nameoftheuser))
    print("\n\nPlease answer few questions about your academics\n")
    print("\n----------------------------------------------------------------------")
    print("\nAre you purusing any of the below mentioned specialisations?")
    print('\tNon Specialisation ( Type ns)')
    print('\tArtificial Intelligence ( Type ai)')
    print('\tData Engineering (Type de) ')
    print('\tInformation Security ( Type is)')
    special = input("\nPlease enter your answer: ")
    print("\nHave you taken the following elective courses ?")
    print("\nPlease enter course initials or no")
    ansml=input("MACHINE LEARNING CSE 543 (ml):")
    ansdmg=input("DATA MINING CSE 506 (dm) :")
    ansoopd=input("OBJECT ORIENTED PROGRAMMING AND DESIGN CSE 600 (oopd)")
    ansga=input("GRADUATE ALGORITHMS CSE 525 (ga)")
    ansnlp=input("NATURAL LANGUAGE PROCESSING CSE 556 (nlp)")
    ansdw=input("DATA WAREHOUSING CSE 606 (dw)")
    print("\nOne last information!")
    gpa = input("Enter your GRADE POINT AVERAGE (gpa): ")
    return special, ansml, ansdmg, ansoopd, ansga, ansnlp, ansdw, gpa


with ruleset('checkcourses'):

    @when_all((m.area == 'ns') & (m.subjectcode == 'ml') & (m.grading >= 6))
    def func(c):
        c.assert_fact({'subject': 'MACHINE LEARNING ENGINEER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'dmg') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'oopd') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE DEVELOPMENT ENGINEER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'ga') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE ENGINEER or RESEARCHER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'nlp') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'AI ENGINEER'})

    @when_all((m.area == 'ns') & (m.subjectcode == 'dw') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})
    
    @when_all((m.area == 'ai') & (m.subjectcode == 'ml') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'MACHINE LEARNING & ARTIFICIAL INTELLIGENCE ENGINEER'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'dmg') & (m.grading >=5))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'oopd') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE DEVELOPMENT ENGINEER'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'ga') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE ENGINEER or RESEARCHER IN AI'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'nlp') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'NATURAL LANGUAGE PROCESSING ENGINEER'})

    @when_all((m.area == 'ai') & (m.subjectcode == 'dw') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER OR BIG DATA ANALYTICS ENGINEER'})
    
    @when_all((m.area == 'de') & (m.subjectcode == 'ml') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'MACHINE LEARNING ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'dmg') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'oopd') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE DEVELOPMENT ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'ga') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'nlp') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'AI & NATURAL LANGUAGE PROCESSING ENGINEER'})

    @when_all((m.area == 'de') & (m.subjectcode == 'dw') & (m.grading >=9))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER OR BIG DATA ANALYTICS ENGINEER'})
    
    @when_all((m.area == 'is') & (m.subjectcode == 'ml') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'MACHINE LEARNING & SECURITY ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'dmg') & (m.grading >=8))
    def func(c):
        c.assert_fact({'subject': 'DATA ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'oopd') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE DEVELOPMENT ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'ga') & (m.grading >=7))
    def func(c):
        c.assert_fact({'subject': 'SOFTWARE ENGINEER or WEB SECURITY ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'nlp') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'NATURAL LANGUAGE PROCESSING ENGINEER'})

    @when_all((m.area == 'is') & (m.subjectcode == 'dw') & (m.grading >=6))
    def func(c):
        c.assert_fact({'subject': 'DATA SECURITY ENGINEER'})

    # output for must take courses
    @when_all(+m.subject)
    def output(c):
        print()
        print("{0}".format(c.m.subject))


def printmsg2():
    print("\nENROLLING IN IIIT DELHI WILL OBVIOUSLY MAKE YOU AN ENGINEER.\n")
    print("LET'S SEE WHAT OTHER CAREER OPTIONS DO YOU HAVE.\n\n ")
    print("IF YOU HAVE INTEREST IN PUBLIC ADMINISTRATION, TYPE = publicadmin") 
    print("IF YOU HAVE INTEREST IN PAINTING AND SKETCHING, TYPE = art")
    print("IF YOU HAVE INTEREST IN MUSIC, TYPE = music")
    print("IF YOU HAVE NO OTHER INTEREST AND WANT TO COMPLETE YOUR ENGINEERING COURSE, TYPE = tech")
    ch = input("Enter here: ")
    return ch

def tech():
    
    print("WE SEE THAT YOU HAVE INTEREST ONLY IN TECH FIELD\n")
    print("ITS PRETTY GOOD!")
    print("\nPLEASE BEAR WITH A FEW MORE QUESTIONS")
    print("What is your GPA:")
    gpa=input(":")
    gpa=int(gpa)
    if gpa == 10 :
          cht='machinel'
    elif gpa > 7 and gpa < 10:
          cht='software'
    elif gpa == 7 and gpa < 7:
          cht='testing'
    return cht

def nontech():
    print("\nWE SEE THAT YOU HAVE OTHER INTERESTS THAN ENGINEERING\n")
    print("\nDON'T WORRY IT'S ABSOLUTELY FINE TO DROP OFF THE UNIVERSITY AND FOLLOW YOUR HEART\n")
    print("IF YOU HAVE INTEREST IN BIRD WATCHING, TYPE = bird")
    print("IF YOU WANT TO TRAVEL THE WORLD, TYPE = travel")
    print("IF YOU WANT TO DO VLOGGING, TYPE = vlog")
    cht = input("Enter here: ")
    return cht

with ruleset('career_option'):
    @when_all((m.domain == 'publicadmin') & (m.domtype == 'travel'))
    def club(e):
        e.assert_fact({'subject': 'YOU MIGHT WANT TO CONSIDER INDIAN ADMINISTRATION SERVICES AS A CAREER OPTION'})

    @when_all((m.domain == 'publicadmin') & (m.domtype == 'bird'))
    def club(e):
        e.assert_fact({'subject': 'YOU CAN CONSIDER UPSC SERVICES OR BE A BIRD WATCHER'})

    @when_all((m.domain == 'publicadmin') & (m.domtype == 'vlog'))
    def club(e):
        e.assert_fact({'subject': 'YOU CAN CONSIDER UPSC SERVICES OR ALSO BE A YOUTUBER'})

    @when_all((m.domain == 'art') & (m.domtype == 'travel'))
    def club(e):
        e.assert_fact({'subject': 'YOU CAN TRAVEL PLACES AND PAINT LANDSCAPES'})

    @when_all((m.domain == 'art') & (m.domtype == 'bird'))
    def club(e):
        e.assert_fact({'subject': 'INSTEAD OF CAPTURING BIRDS WITH YOUR CAMERA, PAINT THEN INSTEAD'})

    @when_all((m.domain == 'art') & (m.domtype == 'vlog'))
    def club(e):
        e.assert_fact({'subject': 'BE AN ART VLOGGER'})
    @when_all((m.domain == 'music') & (m.domtype == 'bird'))
    def club(e):
        e.assert_fact({'subject': 'BE A VOCALIST & BIRD WATCHER'})

    @when_all((m.domain == 'music') & (m.domtype == 'travel'))
    def club(e):
        e.assert_fact({'subject': 'BE A MUSIC COMPOSER BRINGING DIFFERENT CULTURES TOGETHER THROUGH YOUR COMPOSITIONS'})

    @when_all((m.domain == 'music') & (m.domtype == 'vlog'))
    def club(e):
        e.assert_fact({'subject': 'BE AN MUSIC VLOGGER'})

    @when_all((m.domain == 'tech') & (m.domtype == 'machinel'))
    def club(e):
        e.assert_fact({'subject': 'PURSUE CAREER AS A MACHINE LEARNING ENGINEER OR A DATA SCIENCE ENGINEER'})

    @when_all((m.domain == 'tech') & (m.domtype == 'software'))
    def club(e):
        e.assert_fact({'subject': 'PURSUE CAREER AS A SOFTWARE DEVELOPMENT ENGINEER'})


    @when_all((m.domain == 'tech') & (m.domtype == 'testing'))
    def club(e):
        e.assert_fact({'subject': 'PURSUE CAREER AS A DEV/TESTING ENGINEER'})


    @when_all(+m.subject)
    def output(e):
        print()
        print("\n-------------------------------HERE ARE SOME ADDITIONAL ADVICES FOR YOU-------------------------------\n\n")
        print('HERE ARE SOME OTHER CAREER OPTIONS FOR YOU: {0}'.format(e.m.subject))

if __name__ == '__main__':
    speciala, ansmla, ansdmga, ansoopda, ansgaa, ansnlpa, ansdwa, gpaa = printmsg()
    print("\n-------------------------------HERE ARE YOUR RESULTS-------------------------------")
    print("FOLLOWING ARE THE CAREERS RECOMMENDED FOR YOU:\n\n")
    if(speciala == 'ns'):
        if(ansmla == 'ml'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansmla, 'grading':gpaa})
        if(ansdmga == 'dmg'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdmga, 'grading':gpaa})
        if(ansoopda == 'oopd'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansoopda, 'grading':gpaa})
        if(ansgaa == 'ga'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansgaa, 'grading':gpaa})
        if(ansnlpa == 'nlp'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansnlpa, 'grading':gpaa})
        if(ansdwa == 'dw'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdwa, 'grading':gpaa})
    elif(speciala == 'ai'):
        if(ansmla == 'ml'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansmla, 'grading':gpaa})
        if(ansdmga == 'dmg'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdmga, 'grading':gpaa})
        if(ansoopda == 'oopd'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansoopda, 'grading':gpaa})
        if(ansgaa == 'ga'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansgaa, 'grading':gpaa})
        if(ansnlpa == 'nlp'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansnlpa, 'grading':gpaa})
        if(ansdwa == 'dw'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdwa, 'grading':gpaa})
    elif(speciala == 'de'):
        if(ansmla == 'ml'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansmla, 'grading':gpaa})
        if(ansdmga == 'dmg'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdmga, 'grading':gpaa})
        if(ansoopda == 'oopd'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansoopda, 'grading':gpaa})
        if(ansgaa == 'ga'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansgaa, 'grading':gpaa})
        if(ansnlpa == 'nlp'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansnlpa, 'grading':gpaa})
        if(ansdwa == 'dw'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdwa, 'grading':gpaa})
    elif(speciala == 'is'):
        if(ansmla == 'ml'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansmla, 'grading':gpaa})
        if(ansdmga == 'dmg'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdmga, 'grading':gpaa})
        if(ansoopda == 'oopd'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansoopda, 'grading':gpaa})
        if(ansgaa == 'ga'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansgaa, 'grading':gpaa})
        if(ansnlpa == 'nlp'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansnlpa, 'grading':gpaa})
        if(ansdwa == 'dw'):
            assert_fact('checkcourses',{'area':speciala, 'subjectcode':ansdwa, 'grading':gpaa})
  
    print("\n-----------------------------------------------------------------------------------")
    ch = printmsg2()
    print("\n-----------------------------------------------------------------------------------")
    if ch == 'tech':
        cht = tech()
    else:
        cht = nontech()
    assert_fact('career_option',{'domain':ch,'domtype':cht})
    print("\n-----------------------------------------------------------------------------------")
    print("\n\tI HOPE THAT I COULD HELP YOU WITH CAREER ADVICE. HAVE A GREAT DAY!")
    print("\n-----------------------------------------------------------------------------------")
