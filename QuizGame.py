import random
from random import randint
Questions = ['Which photo-based meme involves taking pictures of oneself in front of mirrors?', 'What popular internet meme involves a dog and broken English phrases?', 'Which meme features a character from the movie “300” shouting a phrase in defiance?', 'What famous meme is based on the excited reaction of a young boy opening a Nintendo 64 on Christmas morning?', 'Which meme involves an astronaut in space realizing a shocking truth?', 'What Internet meme features a frog riding a unicycle?']
CorrectAnswers = ['Selfie', 'Doge', 'This is Sparta!', 'N64 Kid','Wait, it’s all…? Always has been.','Dat Boi']
Options = [['Camera','Hashtag','Filter','Selfie',],['Cryptocurrency','Meme','Shiba','Doge',],['Leonidas','300','Persians','This is Sparta!',],['Nintendo','Excitement','Christmas','N64 Kid',],['Astronaut',"Earth",'Meme','Wait, it’s all…? Always has been.',],['Frog','Gajju','Unicycle','Dat Boi',]]

ans=dict(zip(Questions, CorrectAnswers))
q = random.randint(0, len(Questions)-1)
ques = Questions[q]
print(ques)

Ops = dict(zip(Questions, Options))
o = random.randint(0, len(Options)-1)
op = Options[o]
print(op)

Guess = input('Guess the Answer :')
if Guess == ans[ques]:
    print('Viola! You guessed it right')
else:
    print('Oh no! Guess you have to learn more')