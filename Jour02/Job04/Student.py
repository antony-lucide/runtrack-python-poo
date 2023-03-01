class Student:

    def __init__(self,nom,prenom,numero):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credit = 0
        self.__level = self.__StudentEval()
    
    def add_credits(self,credit):
        if credit > 0:
            self.__credit += credit
        print(self.__credit)
        self.__level = self.__StudentEval()

    def __StudentEval(self):
        if self.__credit >= 90:
          return("Excellent")
        elif self.__credit >= 80:
            return("Très Bien")
        elif self.__credit >= 70:
            return("Bien")
        elif self.__credit >= 60:
            return("Passable")
        else:
            return("insuffisant")

    def StudentInfo(self):
        print(self.__nom,self.__prenom,self.__numero,self.__credit,self.__level)

            
instance = Student("George","Washington",60)

instance.add_credits(76)

instance.StudentInfo()
