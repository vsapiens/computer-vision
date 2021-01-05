import numpy as np
smash = ['Mario', 'DK', 'Link', 'Samus', 'Yoshi', 'Kirby', 'Fox', 'Pikachu']
print('1',smash)
smash.append('Luigi')
smash.append('Ness')
smash.append('C. Falcon')
smash.append('Jigglypuff')
print('2',smash)
smash.append(['Metal Mario', 'Polygon Team', 'Master Hand'])
print('3',smash)
smash = ['Original Roster'] + smash[8:]
print('4',smash)
def null_matrix(M,N):
  return [[0]*N]*M
print('5', null_matrix(3,4))
bigMatrix = [[['?']*2]*3]*4
print('6', bigMatrix)
mensualidad = {'Disney+': 7, 'Netflix': 8.99, 'Prime': 12.99}
print('7', mensualidad)
mensualidad.pop('Disney+')
mensualidad['Blim'] = 109
mensualidad['Netflix'] = 139
mensualidad['Prime'] = 99
print('8', mensualidad)
mensualidad['Tec'] = 20400
print('9', mensualidad)
raw = np.arange(1,17,1)
raw = raw.reshape(4,4)
print('10', raw)
raw11 = raw[:2,1:3]
print('11', raw11)
raw12 = raw[1:4,2:4]
print('12', raw12)
features,labels = raw[:4,:3],raw[:,3:]
labels = labels.flatten()
print('13')
print('Features:\n',features)
print('Label:\n',labels)
zipped = list(zip(features,labels))
print('14',zipped)
train,test = zipped[:3],zipped[3:]
print('15')
print('Test:\n',test)
print('Train:\n',train)
print('16','P(A|B)= 0.5')
print('17')
print('18','answer = -2x^4sin(x^2)+3x^2cos(x^2)')
print('19','answer = x^2cos(x)+2xsin(x)+4x^3')
print('20','f\'(x)=3x^2 +2xz + z^2 f\'(y)=3z^2 +2xz + x^2')