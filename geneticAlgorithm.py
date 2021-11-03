import random
import string


alphabet = string.ascii_letters + " !'."

#encoding
def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    chromosome = ""
    for i in range(size):
        chromosome += get_letter()
    return chromosome

#
#fitting function
def get_score(chrom):
    key = "jfneifgDGEjfnei jfhefi"
    correct = 0
    for i in range(len(chrom)):
        if (chrom[i]==key[i]):
            correct+=1
    return correct/len(chrom)


#selection function
def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)

    chromosome_keep = []
    dictionary = {}

    for i in chromosomes_list:
        dictionary[i] = get_score(i)


    dict(sorted(dictionary.items(), key=lambda item: item[1]))

    sorted_chromosones = list(dictionary.keys())


    chromosome_keep = sorted_chromosones [0:int(GRADED_RETAIN_PERCENT*len(chromosomes_list))]
    del sorted_chromosones [0:int(GRADED_RETAIN_PERCENT*len(chromosomes_list))]

    for i in range(int(NONGRADED_RETAIN_PERCENT*len(sorted_chromosones ))):
        index = random.randint(0,len(sorted_chromosones )-1)
        chromosome_keep.append(sorted_chromosones .pop(index))
   
    return chromosome_keep


#reproduciton 
def crossover(parent1, parent2):
    child = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
    return child


#random mutation 
def mutation(chrom):
    chrom = list(chrom)
    i = random.randint(0,len(chrom))
    chrom[i] = get_letter()
    return ''.join(chrom)

