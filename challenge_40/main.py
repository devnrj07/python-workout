# Epidemic Outbreak GUI App
import math
import random
import tkinter  

class Simulation():
    def __init__(self):
        self.day_number = 1
        self.population_size = int(input('\n Enter the population size. '))
        root = math.sqrt(self.population_size)
        if int(root + .5)**2 != self.population_size:
            root = round(root, 0) # round(8.881, 0) = 9.0
            self.grid_size = int(root) #grid_size = 9
            self.population_size = self.grid_size**2
            print("Rounding population size to " + str(self.population_size) + "for visual purposes.")
        else:
            self.grid_size = int(math.sqrt(self.population_size))  
        print("\nWe must first start by infecting a portion of the population.")
        self.infection_percent = float(input("---Enter the percentage (0-100) of the population to initially infect: "))
        self.infection_percent /= 100      
        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = float(input("---Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("---Enter the duration (in days) of the infection: "))
        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = float(input("---Enter the mortality rate (0-100) of the infection: "))
        print("\nWe must know how long to run the simulation.")
        self.sim_days = int(input("---Enter the number of days to simulate: "))


class Person():
    def __init__(self):
        self.is_infected = False #Person starts healthy, not infected
        self.is_dead = False #Person starts ALIVE
        self.days_infected = 0
    def infect(self, simulation):
    #random number generated must be less than infection_probability to infect
        if random.randint(0, 100) < simulation.infection_probability:
            self.is_infected = True
    def heal(self):
        self.is_infected = False
        self.days_infected = 0
    def die(self):
        self.is_dead = True 
    def update(self, simulation):
        if not self.is_dead:
            #Check if the person is infected
            if self.is_infected:
                self.days_infected += 1
            #Check to see if the person will die
            if random.randint(0, 100) < simulation.mortality_rate:
                self.die()
            #Check if the infection is over, if it is, heal the person
            elif self.days_infected == simulation.infection_duration:
                self.heal()
class Population():
    def __init__(self, simulation):
        self.population = []
        for i in range(simulation.grid_size):
            row = []
        #Loop through the needed number of Person objects for each row
        for j in range(simulation.grid_size):
            person = Person()
            row.append(person)
        #The entire row is complete, append it to the population
        self.population.append(row)
    def initial_infection(self, simulation):
        infected_count = int(round(simulation.infection_percent*simulation.population_size, 0))
        infections = 0
        while infections < infected_count:
            x = random.randint(0, simulation.grid_size - 1)
            y = random.randint(0, simulation.grid_size - 1)
            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1
    def spread_infection(self, simulation):
        for i in range(simulation.grid_size):
            for j in range(simulation.grid_size):
                if self.population[i][j].is_dead == False:
                    if i == 0:
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                            else :
                                if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                    self.population[i][j].infect(simulation)
                        elif i == simulation.grid_size-1:
                            if j == 0:
                                if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)
                            elif j == simulation.grid_size-1:
                                if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)
                            else:
                                if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)       
                        else:
                            if j == 0:
                                if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)  
                            elif j == simulation.grid_size-1:
                                if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)

                            else:
                                if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(simulation)                  

    def update(self, simulation):
        """Update the whole population by updating each individual Person"""
        simulation.day_number += 1
        #Loop through the population to access each row
        for row in self.population:
        #Loop through the row to update each Person
            for person in row:
                person.update(simulation)      

    def display_statistics(self, simulation):
        """Display the statistics of the population"""
        #Initialize values
        total_infected_count = 0
        total_death_count = 0                          
        for row in self.population:
        #Loop through the row to access each person
            for person in row:
                #Person is infected
                if person.is_infected:
                    total_infected_count += 1
                #Person is dead
                if person.is_dead:
                    total_death_count += 1
        infected_percent = round(100*(total_infected_count/ simulation.population_size), 4)
        death_percent = round(100*(total_death_count/ simulation.population_size), 4)            

        print("\n-----Day # " + str(simulation.day_number) + "-----")
        print("Percentage of Population Infected: " + str(infected_percent) + "%")
        print("Percentage of Population Dead: " + str(death_percent) + "%")
        print("Total People Infected: " + str(total_infected_count) + " / " + str(simulation.population_size))
        print("Total Deaths: " + str(total_death_count) + " / " + str(simulation.population_size))
    
    def graphics(simulation, population, canvas):
        square_dimension = 600//simulation.grid_size
        for i in range(simulation.grid_size):
            #y is the starting index of where a given square should be drawn
            y = i*square_dimension
            #Loop through all persons in the row
            for j in range(simulation.grid_size):
            #x is the starting index of where a given square should be drawn.
                x = j*square_dimension
                #Check to see if the given person is dead
                if population.population[i][j].is_dead:
                    #Create a red square at the correct location
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='red')
                else:
                    if population.population[i][j].is_infected:
                        #Create a yellow square at the correct location
                        canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='yellow')
                    else:
                        canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='green')    


if __name__ == "__main__":
    #The main code
    #Create a simulation object
    sim = Simulation()
    #Set constant variables for window size
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    #Create the tkinter window and canvas
    sim_window = tkinter.Tk()
    sim_window.title("Epidemic Outbreak")
    sim_canvas = tkinter.Canvas(sim_window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='lightblue')
    sim_canvas.pack(side=tkinter.LEFT)

    #Create a population object
    pop = Population(sim)
    #Set the initial conditions of the population
    pop.initial_infection(sim)
    pop.display_statistics(sim)
    input("Press Enter to begin simulation.")
    for i in range(1, sim.sim_days):
        pop.spread_infection(sim)
        pop.update(sim)
        pop.display_statistics(sim)
        graphics(sim, pop, sim_canvas)
        sim_window.update()

        if i != sim.sim_days-1:
            sim_canvas.delete('all')
