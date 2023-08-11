class Human():
    def __init__(self, name, continent='Asia'):
        self.continent = continent
        self.name=name
    
    def change_continent(self, new_name):
        self.continent=new_name
        return "Successfully Changed Continent"


x = Human("Hamza")
y = Human("Ahmad", continent='Africa')

x.continent = 'North America'

status = x.change_continent('Europe')
print(status)

print(f"{x.name} belongs to {x.continent}")
print(f"{y.name} belongs to {y.continent}")