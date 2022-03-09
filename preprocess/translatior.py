import json
filename1 = './example/example30.txt'
f = open(filename1, "r", encoding="utf-8")
lines = f.read()

datas = lines.split('\n')


result = []
for i in range(len(datas)):
    if i % 2 !=0:
        blocks = datas[i].split(' ')[1:]
        result.append(blocks)

init = []
goal = []
block_names = []
for i in range(len(result)):
    tmp3 = []
    tmp4 = []
    j = 0
    for r1 in result[i]:
        j +=1
        tmp3.append(int(r1))
        tmp4.append('block' + str(j))
    if i % 2 == 0:
        init.append(tmp3)
        block_names.append(tmp4)
    if i % 2 != 0:
        goal.append(tmp3)

num_blocks = len(init[0])


#print('blocks:',block_names)

#init
#print('init:', init)
on = []
clear = []

for i in range(len(init)):
    tmp1 = []
    tmp2 = []
    for j in range(num_blocks):
        tmp1.append('ontable')
        tmp2.append('clear')
    on.append(tmp1)
    clear.append(tmp2)


for i in range(len(init)):
    for j in range(len(init[i])):
        if init[i][j] != 0:
            on[i][j] = 'block' + str(init[i][j])
            clear[i][init[i][j]-1] = 'noclear'

#print('on:', on)
#print('clear:',clear, '\n')


#goal
#print('goal:', goal)
on_goal = []
clear_goal = []

for i in range(len(goal)):
    tmp1 = []
    tmp2 = []
    for j in range(num_blocks):
        tmp1.append('ontable')
        tmp2.append('clear')
    on_goal.append(tmp1)
    clear_goal.append(tmp2)



for i in range(len(goal)):
    for j in range(len(goal[i])):
        if goal[i][j] != 0:
            on_goal[i][j] = 'block' + str(goal[i][j])
            clear_goal[i][goal[i][j]-1] = 'noclear'

#print('on:', on_goal)
#print('clear:',clear_goal)



#write to PPDL


sample = '''(define (problem pb2)
   (:domain blocks)
   (:objects a b)
   (:init (ontable a) (ontable b)  (clear a)  (clear b) (handempty))
   (:goal (and (on a b))))
   '''

text1 = '''(define (problem pb2)
    (:domain blocks)'''


for i in range(len(clear)):
    text = ''
    tmp_block = block_names[i]
    text_block = ' '.join(tmp_block)
    text2 = '''
    (:objects ''' + text_block + ')'

    on_relation = on[i]
    tmp_clear = clear[i]
    tmp_block = block_names[i]

    tmp_text3 = '''
    (:init'''
    for j in range(len(on_relation)):
        if on_relation[j] == 'ontable':
            tmp_text3 = tmp_text3 + ' (ontable ' +  tmp_block[j] + ')'
        if on_relation[j] != 'ontable':
            tmp_text3 = tmp_text3 + ' (on ' +  tmp_block[j] + ' ' + on_relation[j] + ')'

    for k in range(len(tmp_clear)):
        if tmp_clear[k] == 'clear':
            tmp_text3 = tmp_text3 + ' (clear' + ' ' + tmp_block[k] + ')'

    tmp_text3 = tmp_text3 + ' (handempty))'
    text3 = tmp_text3


    tmp_text4 = '''
    (:goal (and'''

    on_relation_goal = on_goal[i]
    tmp_clear_goal = clear_goal[i]
    tmp_block = block_names[i]

    for j in range(len(on_relation_goal)):
        if on_relation_goal[j] == 'ontable':
            tmp_text4 = tmp_text4 + ' (ontable ' +  tmp_block[j] + ')'
        if on_relation_goal[j] != 'ontable':
            tmp_text4 = tmp_text4 + ' (on ' +  tmp_block[j] + ' ' + on_relation_goal[j] + ')'

    for k in range(len(tmp_clear_goal)):
        if tmp_clear_goal[k] == 'clear':
            tmp_text4 = tmp_text4 + ' (clear' + ' ' + tmp_block[k] + ')'

    tmp_text4 = tmp_text4 + ' )))'
    text4 = tmp_text4

    #print(text4)
    text = text1 + text2 + text3 + text4

    #print(text, '\n')

    outfile = './problem30-' + str(i) + '.pddl'
    with open(outfile, 'w') as f:
        f.write(text)




