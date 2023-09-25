fichier1 =open("//Users//omar//Downloads//SCRIPTHTML//ficher.html","r")
fichier2 =open("//Users//omar//Downloads//SCRIPTHTML//URL.txt","r")
fichier3 =open("//Users//omar//Downloads//SCRIPTHTML//UNSUB.txt","r")
read1=fichier1.readlines()
read2=fichier2.readlines()
read3=fichier3.readlines()
print(read2)
for i in range(len(read3)):
 filehtml="file"+str(i)
 if(i==len(read3)-1):
  read1[7]='<a target="_blank" style="text-decoration:none;" href="'+str(read2[i])+'">\n'
  read1[46]='Du kan avbryta prenumerationen nar som helst. <a href="'+str(read3[i])+'">Avanmala</a>\n'
 else:
  read1[7]='<a target="_blank" style="text-decoration:none;" href="'+str(read2[i])[0:len(read2[i])-1]+'">\n'
  read1[46]='Du kan avbryta prenumerationen nar som helst. <a href="'+str(read3[i])[0:len(read3[i])-1]+'">Avanmala</a>\n'
 finalfolder=open("//Users//omar//Downloads//SCRIPTHTML//"+filehtml+".html","w")
 finalfolder.writelines(read1)
 finalfolder.close()


fichier1.close()
fichier2.close()
fichier3.close()
fichier1 =open("//Users//omar//Downloads//SCRIPTHTML//ficher.html","w")
fichier2 =open("//Users//omar//Downloads//SCRIPTHTML//URL.txt","w")
fichier3 =open("//Users//omar//Downloads//SCRIPTHTML//UNSUB.txt","w")

fichier1.writelines(read1)
fichier2.writelines(read2)
fichier3.writelines(read3)

fichier1.close()
fichier2.close()
fichier3.close()

