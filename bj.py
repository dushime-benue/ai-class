
std_names={'ben':97,'bike':86,'denis':78,'leon':56,'joel':45,'lucy':35,'neema':83,'aline':87,'lian':23,'tiwonge':63}
average= sum(std_names.values()) /len(std_names)
print(average)

# hieghest

hieghest_score= max(std_names.values())
for student,score in std_names.items():
    if score == hieghest_score:
        print(f'hieghest score:{student} with {score}')

std_names['lucy']=97
print(std_names)

for student,score in std_names.items():
    if score > 80:
        print(f'{student}: {score}')




class quiz:
    def ___init___(self,questions,answer):
        self.questions = questions
        self.answer = answer



















    