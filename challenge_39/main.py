#Epidemic Outbreak Terminal App
'''
You will be responsible for writing a program that simulates the spread of an infectious disease
throughout a population. Using classes, you will model an individual person’s and an entire
population’s attributes and behaviors. Your program will allow users to set various initial
conditions in regards to the infection such as population size, infection rate, mortality rate, and
infection duration. The program will then simulate the interaction of people within a population
and spread the disease. Each iteration of spreading the disease will result in a summary
displaying statistics of the population.
'''
import random

class Simulation():
    def __init__(self):
        self.day_number = 1
        self.population_size = int(input('Enter the population of the town. '))
        self.infection_percent = int(input('Enter the initially infected population. '))/100
        self.infection_probability = int(input('Enter the probablity of a person getting infected. '))
        self.infection_duration = int(input('Enter the amount of time the infection will last. '))
        self.mortality_rate = int(input('Enter the mortality rate of those who are infected. '))
        self.sim_days = int(input('Enter the number of days that simulation will last. '))

class Person():
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self,simulation) :
        chances = random.randint(0,100)
        if chances < simulation.infection_probability :
            self.is_infected = True
    def heal(self):
        self.is_infected = False
        self.days_infected = 0
    def die(self):
        self.is_dead = True
    def update(self, simulation) :
        if self.is_dead == False:
            if self.is_infected:
                self.days_infected += 1
                dying_chance = random.randint(0,100)
                if dying_chance < simulation.mortality_rate :
                    self.die()
                elif self.days_infected == simulation.infection_duration :
                    self.heal()
                       
class Population():    
        def __init__(self, simulation):
             self.population = []
             for i in range(simulation.population_size):
                 person = Person()
                 self.population.append(person)

        def initial_infection(self, simulation):
            infected_count = int(round(simulation.infection_percent * simulation.population_size,0))
            for i in range(infected_count):
                #Infect the ith person in the population attribute
                self.population[i].is_infected = True
                self.population[i].days_infected = 1
                #Shuffle the population list so we spread the infection out randomly
            random.shuffle(self.population)
        def spread_infection(self,simulation):
            for i in range(len(self.population)):
                if self.population[i].is_dead == False:
                    if i == 0:
                        if self.population[i+1].is_infected:
                            self.population[i].infect(simulation)
                        elif i < len(self.population)-1:
                            if self.population[i-1].is_infected or self.population[i+1].is_infected:
                                self.population[i].infect(simulation)
                        #i is the last person in the list, can only check to the left[i-1].
                        elif i == len(self.population)-1:
                            if self.population[i-1].is_infected:
                                self.population[i].infect(simulation)

        def update(self,simulation) :
            simulation.day_number += 1
            for person in self.population :
                person.update(simulation)

        def display_statistics(self, simulation ) :
            #Initialize values
            total_infected_count = 0
            total_death_count = 0
            for person in self.population:
                #Person is infected
                if person.is_infected:
                    total_infected_count += 1
                #Person is dead
                if person.is_dead:
                    total_death_count += 1
            infected_percent = round(100*(total_infected_count/simulation.population_size), 4)
            death_percent = round(100*(total_death_count/simulation.population_size), 4)
            #Statistics summary
            print("\n-----Day # " + str(simulation.day_number) + "-----")
            print("Percentage of Population Infected: " + str(infected_percent) +"%")
            print("Percentage of Population Dead: " + str(death_percent) + "%")
            print("Total People Infected: " + str(total_infected_count) + " / " + str(simulation.population_size))
            print("Total Deaths: " + str(total_death_count) + " / " + str(simulation.population_size))

        def graphics(self):
            #'X' for dead, 'I' for Infected 'O' for Healhty
            status = []    
            for person in self.population :
                if person.is_dead :
                    char = 'X'
                else :
                    if person.is_infected :
                        char = 'I'
                    else :
                        char = 'O'
                status.append(char)
            for letter in status :
                print(letter, end='-')

if __name__ == "__main__":
    sim = Simulation()
    pop = Population(sim)

    pop.initial_infection(sim)
    pop.display_statistics(sim)
    pop.graphics()
    input('\n Press Enter begin to simulation.')
    for i in range(1, sim.sim_days):
        #For a single day, spread the infection, update the population, display statistics and graphics
        pop.spread_infection(sim)
        pop.update(sim)
        pop.display_statistics(sim)
        pop.graphics()
        #If it is not the last day of the simulation, pause the program
        if i != sim.sim_days - 1:
            input("\nPress enter to advance to the next day.")
