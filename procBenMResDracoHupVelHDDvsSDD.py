# BibWash 2018
import re
import glob
#from pylab import *
#from pylab import figure, axes, plot, title, show, savefig, close
#pattern = re.compile(r"[^-\d]*([\-]{0,1}\d+\.\d+)[^-\d]*")
#woHeSpaDDA='/u/gvargas/work/hierPolyMelt/bunchOfHUpVeLwHeSpaDDA/hupvelWhole_skin_P_vSkinHalf/log'
oldP='/u/gvargas/work/hierPolyMelt/bunchOfHUpVeL/hupvelWhole_skin_P_vMaxD/log/*'
#newP='/ptmp/gvargas/work/MResDDPaper/mresEnF/jobs/*'
#wHeSpaDDA='/u/gvargas/work/hierPolyMelt/bunchOfHUpVeLwHeSpaDDA/hupvelWhole_skin_P_vSkinHalf/log'
newPF='/u/gvargas/work/hierPolyMelt/bunchOfHUpVeLwHeSpaDDA/hupvelWhole_skin_P_vSkinHalf/log/*'
#ujP='/ptmp/gvargas/work/MResDDPaper/ujE/jobs/*'

#
#       Posible searchs
#    1.\bCPU time = \b
#    2.\bRun    time\b
#    3.\bPair   time\b
#    4.\bFENE   time\b\bFENE   time\b   
#    5.\bAngle  time\b  
#    6.\bComm1  time\b
#    7.\bComm2  time\b
#    8.\bInt1   time\b
#    9.\bInt2   time\b
#    10.\bResort time\b
#    11.\bOther  time\b
#    12.\bNeighbor list builds\b

auxT=r'\bRun    time\b'   # E++
#auxT=r'\bPerformance\b'  # Gromacs
#auxT=r'\bNeighbor list builds\b'

newFCpuTime=[]
newFIndexBM=[]
for filenamePF in glob.glob(newPF):
    try:
        with open (filenamePF, 'rt') as in_file:
          for line in in_file:
                aux=re.findall(str(auxT),line)
                if aux!=[]:
                        print "found IT pf "
                        print line
                        #pattern = re.compile(r"[^-\d]*(-?\d+\.\d+)[^-\d]*") 
                        pattern = re.compile(r"[^-\d]*([\-]{0,2}\d+\.\d+)[^-\d]*")
                        results = []
                        line2=line[5:]
                        match = pattern.match(line2)
                        if match:
                                results.append(match.groups()[0])
                        newFCpuTime.append(float(results[0]))
                        newFIndexBM.append(filenamePF)
    except:
        pass
'''
newCpuTime=[]
newIndexBM=[]
for filenameF in glob.glob(newP):               
    try:
        with open (filenameF, 'rt') as in_file:
          for line in in_file:
                aux=re.findall(str(auxT),line)
                if aux!=[]:
                        print "found IT newI"
                        print line
                        pattern = re.compile(r"[^-\d]*([\-]{0,2}\d+\.\d+)[^-\d]*")
                        results = []
                        line2=line[5:]
                        match = pattern.match(line2)                    
                        if match:
                                results.append(match.groups()[0])
                        newCpuTime.append(float(results[0]))
                        newIndexBM.append(filenameF)
    except:
        pass    
'''
oldCpuTime=[]
oldIndexBM=[]
for filenameO in glob.glob(oldP):
    try:
        with open (filenameO, 'rt') as in_file:
          for line in in_file:
                aux=re.findall(str(auxT),line)
                if aux!=[]:
                        print "found IT old"
                        print line
                        pattern = re.compile(r"[^-\d]*([\-]{0,2}\d+\.\d+)[^-\d]*")
                        results = []
                        line2=line[5:]
                        match = pattern.match(line2)
                        if match:
                                results.append(match.groups()[0])
                        oldCpuTime.append(float(results[0]))
                        oldIndexBM.append(filenameO)
    except:
        pass
'''
ujCpuTime=[]
ujIndexBM=[]
for filenameU in glob.glob(ujP):                
    try:
        with open (filenameU, 'rt') as in_file:
          for line in in_file:
                aux=re.findall(str(auxT),line)
                if aux!=[]:
                        print "found IT uj "
                        print line
                        pattern = re.compile(r"[^-\d]*([\-]{0,2}\d+\.\d+)[^-\d]*")
                        results = []
                        line2=line[5:]
                        match = pattern.match(line2)                    
                        if match:
                                results.append(match.groups()[0])
                        ujCpuTime.append(float(results[0]))
                        ujIndexBM.append(filenameU)
    except:
        pass    

'''
def subit(msg):
    # Use the below if the string is multiline
    # subbed = re.compile("(<.*?>)" re.DOTALL).sub("(<hh  >t", msg)
    subbed = re.sub("/u/gvargas/work/hierPolyMelt", " ", msg)
    return subbed

aka=[]
for msg in newFIndexBM:
    aka.append(subit(msg))

print 'new F_Cpu',newFCpuTime
print 'new F_Ind',aka#newFIndexBM

#print 'new_Cpu ',newCpuTime
#print 'new_Ind ',newIndexBM 

aka2=[]
for msg in oldIndexBM:
    aka2.append(subit(msg))

print 'old_Cpu ',oldCpuTime
print 'old_Ind ',aka2#oldIndexBM

#print 'uj_Cpu ',ujCpuTime
#print 'uj_Ind ',ujIndexBM 

# Plotting
'''
figure('hola', figsize=(9, 6))
plot(oldIndexBM,oldCpuTime,'ro--')
plot(newIndexBM,newCpuTime,'go--')
plot(newFIndexBM,newFCpuTime,'co--')
plot(ujIndexBM,ujCpuTime,'mo--')
savefig('compIG'+str(1)+'.png')
close('hola')
'''




#       figure(str(j+1), figsize=(9, 6)) 
#        plot(oldIndexBM,oldCpuTime,'ro')
#       plot(newIndexBM,newCpuTime,'go')
#       savefig('compUBI'+str(j+1)+'.png')
#       close(str(j+1))

