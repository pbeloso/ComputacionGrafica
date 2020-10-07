objFile = open('box.obj', 'r').readlines()


vertexList = []
facesList = []

normalList = []
normalFaces = []

textList = []
texturesFaces = []

for line in objFile:
	split = line.split()
	if not len(split) or split[0] == "o" or split[0] == "#":	# Si es un espacio en blanco, #, o;  continuo
		continue

	if split[0] == "v":			 	# Si empieza con v, lo agrego a la lista de vertices				
		vertex = [ float(split[1]), float(split[2]), float(split[3]) ]
		vertexList.append(vertex)

	if split[0] == "vn":			# Si empieza con vn, lo agrego a la lista de normales	
		normal = [ float(split[1]), float(split[2]), float(split[3]) ]
		normalList.append(normal)
	
	if split[0] == "vt":			# Si empieza con vt, lo agrego a la lista de texturas	
		texture = [ float(split[1]), float(split[2]) ]
		textList.append(texture)

	elif split[0] == "f":			# Si empieza con f, lo agrego a la lista de faces
		
		vert = []
		norm = []
		text = []

		for i in range(1,4):
			splitFace = split[i].split("/")
			vert.append(splitFace[0])
			norm.append(splitFace[1])
			text.append(splitFace[2])
		
		vertexface = [ vertexList[int(vert[0])-1], vertexList[int(vert[1])-1], vertexList[int(vert[2])-1] ]
		facesList.append(vertexface)

		normalFace = [ normalList[int(norm[0])-1], normalList[int(norm[1])-1], normalList[int(norm[2])-1] ]
		normalFaces.append(normalFace)

		textFace = [ textList[int(text[0])-1], textList[int(text[1])-1], textList[int(text[2])-1] ]
		texturesFaces.append(textFace)
			
print(texturesFaces)