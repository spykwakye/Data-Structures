#Papa Yaw Appiah-Kwakye
#6929121
#Github Username -  spykwakye
#Github Repsitory Link - https://github.com/spykwakye/Data-Structures

# Script for online car store AI
print('Welcome valued Customer!')
cars = {'Bugatti Veyron':30000.00 , 'Bugatti Chiron':29000.00 , 'Bugatti Divo':28000.00 , 'Bugatti Royale':27000.00 ,
'Mercedes_benz S-Class':16000 , 'Mercedes_benz A-Class':17000 , 'Mercedes_benz C-Class':18000 , 'Mercedes_benz G-Class':21000 , 
'Suzuki Swift':11000 , 'Suzuki Vitara':12000 , 'Suzuki Jimny':14000 , 'Suzuki Ignis':13000 ,
'Chervolet Corvette':32000 , 'Chervolet Cruze':33000 , 'Chervolet Equinox':34000 ,
'Tesla Model Y':20000 , 'Tesla Model S':25000 , 'Tesla Model 3':15000 , 'Tesla Roadster':10000 ,
'Ferrari F40':31000 , 'Ferrari Enzo':19000 , 'Ferrari F50':35000 ,
'Audi A4':36000 , 'Audi R8':30500 , 'Audi TT':29500 , 'Audi Quattro':28500 , 'Audi Q7':25500 ,
'Lexus IS':13500 , 'Lexus RX':20500 , 'Lexus LS':25500}
#bugatti,mercedes_benz,suzuki,chervolet,tesla,ferrari,audi,lexus = model
car_model = input('What are you looking to drive: ')
if car_model in cars:
    print('Very exquisite selection.')
    print('This beauty is worth USD '+ str(cars[car_model] + .0))
else: 
    print('Sorry,this model is currently not available.')
    