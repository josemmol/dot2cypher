import pydot
filecypher="fileipkernelcypher.cy"
graphs = pydot.graph_from_dot_file('ipykernel-dependecies.dot')
graph = graphs[0]

f= open(filecypher,"w+")
f.write('CREATE \r\n')
for n in graph.get_nodes():
    print(n.get_name(),n.get_label())
    f.write('(n'+n.get_name().strip('"').replace('-','')+': python_package {name:\''+n.get_name()+'\'}),\r\n')
for e in graph.get_edge_list():
    print("origen: ",e.get_source())
    print("desti: ",e.get_destination())
    f.write('(n'+e.get_source().strip('"').replace('-','')+')-[:dependency {label:\''+e.get_label()+'\'}]->(n'+e.get_destination().strip('"').replace('-','')+'),\r\n')
f.write('\r\n')
f.write('\r\n')
f.close()
