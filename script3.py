fichier1 =open("//Users//omar//Downloads//SCRIPTHTML//BTCTELIA.html","r")
fichier2 =open("//Users//omar//Downloads//SCRIPTHTML//URL.txt","r")
fichier3 =open("//Users//omar//Downloads//SCRIPTHTML//IMG.txt","r")
read1=fichier1.readlines()
read2=fichier2.readlines()
read3=fichier3.readlines()
print(read1[19])
for i in range(len(read3)):
 filehtml="file"+str(i)
 if(i==len(read3)-1):
  read1[10]='<a href="'+str(read2[i])+'">\n'
  read1[19]='<p  class="center"'+' style="background-image: url'+"('"+str(read3[i])+"'"+'); width:1000px; height: 993px;">'
  finalfolder = open("//Users//omar//Downloads//SCRIPTHTML//" + filehtml + ".html", "w")
  finalfolder.writelines(read1)
  finalfolder.close()



 else:
  read1[10]='<a href="'+str(read2[i])[0:len(read2[i])-1]+'">\n'
  read1[19]='<p  class="center"'+' style="background-image: url'+"('"+str(read3[i])[0:len(read3[i])-1]+"'"+'); width:1000px; height: 993px;">'
  finalfolder = open("//Users//omar//Downloads//SCRIPTHTML//" + filehtml + ".html", "w")
  finalfolder.writelines(read1)
  finalfolder.close()


fichier1.close()
fichier2.close()
fichier3.close()

