#Python Class And Object

class person:
    name = 'Dhrubojyoti'
    occupation = 'Software Engineer'
    city = 'Lalbagh'

    def info(self):
        print(f"{self.name} is a {self.occupation} ")


a = person()
b = person()
c = person()
a.occupation = "AIML"

b.name = 'Sayan'
b.occupation = 'Forntend Developer'

c.name = 'Ankur'
c.occupation = 'Forntend Developer'


a.info()
b.info()
c.info()
