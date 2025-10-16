#dictionary example
myDict=[
    {"id":'1',"name":'ravi',"age":'35'},
    {"id":'2',"name":'Kiki',"age":'12'},
    {"id":'3',"name":'hadi',"age":'25'},
    {"id":'4',"name":'Maria',"age":'15'}
]
for k in myDict:    #(->)this symbol pakai apa pun boleh just nak show arrow je
    print(k['id']+'->'+k['name']) # +'->'+k['age']) if wanna list the age as well