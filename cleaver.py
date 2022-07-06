"""
    Capra-Cleaver, an easy way to losslessly cut videos.
    Copyright (C) 2022 MURA

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see https://www.gnu.org/licenses/gpl-3.0.html.
"""
import subprocess
import os
from dotenv import load_dotenv
import sys
from datetime import datetime
def fuu(inp,poi=0,va=0,nts=0):
  if poi:
    if isinstance(inp,list):
      return inp
    else:
      return [va.strip() for va in inp.strip('][').split(",")]
  if nts:
    if inp.lower() in ['make_zero','auto','make_non_negative','disabled']:
      return inp
    else:
      return "make_zero"
  if inp.lower() in ['true','1']:
    return True
  elif va and inp.lower() in ['auto']:
    return 'auto'
  else:
    return False   

if os.name is 'posix':
    slsh = "/"
else:
    slsh="\\"

if getattr(sys, 'frozen', False):
    adieu = os.path.dirname(sys.executable)

elif __file__:
    adieu = os.path.dirname(__file__)

with open(f"{adieu}{slsh}.env", "+a") as fle:
   fle.seek(0)
   tm = fle.readlines()
if tm:
  load_dotenv(f"{adieu}{slsh}.env")
  ygg = fuu(os.getenv('cleave_way', 'true'), 0, 1)
  sform = fuu(os.getenv('vfor', ['.mkv', '.mp4']), 1)
  hakglo = fuu(os.getenv('skip_choice', "true"))
  logp = fuu(os.getenv('cm_logs', 'false'))
  fflog = fuu(os.getenv('fflogs', 'false'))
  avoid_nts = fuu(os.getenv('avoid_negative_ts','make_zero'),0,0,1)
  pathlog = adieu+slsh+"cleave_logs"+slsh
  exop=""
else:
  with open(f"{adieu}{slsh}.env", "+a") as fle:
    fle.write("# false: split a video into segments, true: remove parts from a video, auto: pass value as argument in command line\n\ncleave_way=false\n\n# supported video formats, add a format not here\n\nvfor=[mkv,mp4,mov,wmv,avi]\n\n# true: skip specific timestamps on execution\n\nskip_choice=false\n\n# true: output as logs\n\ncm_logs=false\n\n# true: ffmpeg output as logs\n\nfflogs=false\n\n# value: make_zero , auto , make_non_negative , disable\n\navoid_negative_ts=make_zero")
    print("Restart")
    sys.exit()

def ice(s_io):
    if len(s_io)==1:
        s_io=['00',s_io[0]]
    return s_io

def curbra(sth,bpth):
  dech=1
  bou=sth.split(" ",1)
  sn=bou[0].split('|')
  if len(sn)!=3:
    return sth
  if sn[1].isnumeric():
    dech=int(sn[1])
  flist=[]
  if not slsh in bpth:
    bpth+=slsh
  drlis=os.listdir(bpth)
  drlis.sort()
  tm=0
  for fi in drlis:
    if not os.path.isdir(os.path.join(bpth,fi)):
     if fi.rsplit('.',1)[1] in sform:
      tm+=1
      if tm==dech:
        bou[0]=fi
        return " ".join(bou)
  return sth

def degure(inf,des):
    shib=inf.copy()
    pont = len(shib)
    emt,felt=[],[]
    tar=0
    while tar<pont:
     suly=tar
     io, vy = shib[suly][0], shib[suly][1]
     mi, mx = int(io[1]), int(vy[1])
     nls=[]
     while pont>suly:
        nt=range(mi,mx)
        aoi, hat = shib[suly][0], shib[suly][1]
        ao, ha = int(aoi[1]), int(hat[1])
        ntr=range(ao,ha)
        if (ao in nt or ha in nt) and nls:
          if ao<mi:
            io=aoi
            pass
          if ha>mx:
            vy=hat
          nls[0]=[io,vy]
          felt.append(shib[suly])
          if suly:
              suly+=1
          else:
           suly=tar+1
          continue
        elif (mi in ntr or mx in ntr) and nls:
          if ao < mi:
            io=aoi
            pass
          if ha > mx:
            vy=hat
          nls[0]=[io,vy]
          felt.append(shib[suly])
          if suly:
              suly += 1
          else:
           suly = tar+1
          continue
        else:
          nls.append([aoi,hat])
        suly+=1
     if shib[tar] not in felt and nls[0] not in emt and nls[0] not in felt:
       emt.append(nls[0])
     tar+=1
    emt.sort(key=lambda em: int(em[0][1]))
    rem=[[['00:00','0']]]
    ugra=len(emt)
    petr=0
    while ugra>petr:
      if petr==0:
       rem[0].append(emt[petr][0])
       if emt[petr][0][1]=='0':
         rem.pop(0)
       if petr==ugra-1:
         rem.append([emt[petr][1],des])
      elif petr==ugra-1:
        rem.append([emt[petr-1][1],emt[petr][0]])
        if emt[petr][1][1]!=des[1]:
          rem.append([emt[petr][1],des])
      else:
        rem.append([emt[petr-1][1],emt[petr][0]])
      petr+=1
    emt=rem 
    return emt
  
def consec(lis):
    se=0
    r=len(lis)-1
    for nu in lis: 
        se+=int(nu)*(60**(r))
        r-=1
    return str(se)


def chaff(sec):
    sec = sec % (24 * 3600)
    hr = sec// 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    if hr==0:
      return "%02d:%02d" % (min, sec)
    elif hr < 10:
     return "0%0d:%02d:%02d" % (hr, min, sec)
    else:
     return "%d:%02d:%02d" % (hr, min, sec)
   
def fede(filename):
    res = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    return str(int(float(res.stdout)))
  
def reg(a,lo):
    if not os.path.exists(pathlog):
      os.mkdir(pathlog)
    if a==1:
        with open(f"{pathlog}Cleaver.log","+a") as ff:
            ff.write(f'{lo}\n')
    elif a==2:
      with open(f"{pathlog}FF.log","+a") as ff:
        ff.write(f'{lo.decode()}\n\n{"-"*50}\n\n\n')
    else:
        with open(f"{pathlog}Err.log","+a") as f:
            f.write(f"{datetime.now()} | {lo}\n")
            
def mergd(ram):
  rem=[]
  for nm in ram:
    with open(f"{adieu}{slsh}tmp.txt","+bw") as fp:
      fp.write(nm[0].encode('utf-8'))
    onm = os.path.splitext(nm[1])
    if logp:
      reg(1, f"Merging following files:\n{nm[0]}")
    else:
      print(f"Merging following files:\n{nm[0]}")
    if fflog:
     cm = subprocess.run(['ffmpeg', '-safe', '0', '-f', 'concat', '-y', '-i', f'{adieu}{slsh}tmp.txt', '-map','0','-c', 'copy', f"{onm[0]}_edit_{onm[1]}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else:
      cm = subprocess.run(['ffmpeg', '-safe', '0', '-f', 'concat', '-y', '-i', f'{adieu}{slsh}tmp.txt', '-map', '0', '-c', 'copy', f"{onm[0]}_edit_{onm[1]}"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if logp:
     reg(1,"Merged\n")
    else:
     print('Merged\n')
    if fflog:
      reg(2, cm.stdout)
    if cm.stderr:
      reg(0,f"CmdErr:{cm.stderr}")
    rem.append(nm[2])

  os.remove(f"{adieu}{slsh}tmp.txt")
  
  lia=""
  if logp:
    reg(1,"Deleting following files:")
  else:
    print("Deleting following files:")
  for nm in rem:
      for fnm in nm:
          os.remove(fnm)
          lia+=fnm+"\n"
  if logp:
    reg(1,f"{lia}\n\nDeleted\n\n{'-'*50}\n")
  else:
    print(f"{lia}\n\nDeleted")

def clv(li,tr):
 cmdstp=[]
 for il in li:
   if not li[il]:
     if logp:
      reg(1, f"No input found\n\n{'-'*50}\n\n")
     else:
      print("No input found\n")
     return
   if logp:
     reg(1, f"Directory: {il}\n")
   else:
    print(f"Directory: {il}\n")
   for inp in li[il]:
    if type(li[il][inp]) is dict:
        zeyg=il
        if exop!="":
          zeyg=exop
        inu=f"{il}{slsh}{inp}"
        filyun=os.path.splitext(inp)
        if logp:
         reg(1, f"Input: {inp}\n")
        else:
         print(f"Input: {inp}\n")
        if li[il][inp]['Err']:
            if logp:
             reg(1,f"Due to timestamp not existing, excluding the following:\n{li[il][inp]['Err']}\n")
            else:
             print(f"Due to timestamp not existing, excluding the following:\n{li[il][inp]['Err']}\n")
        cmds=[]
        cmdsnm=[]
        for timsp in li[il][inp]['Cmds']:
            if logp:
             reg(1, f"Cutting off {timsp[0][0]} - {timsp[1][0]}\n")
            else:
             print(f"Cutting off {timsp[0][0]} - {timsp[1][0]}")
            if hakglo and not logp:
             ch=input("")
             if ch.lower() in ["n","no"]:
                continue
            optfl = f"{zeyg}{slsh}{filyun[0]} {timsp[0][0].replace(':','_')}-{timsp[1][0].replace(':','_')}{filyun[1]}"
            cmds.append(f"file '{optfl}'\n")
            cmdsnm.append(optfl)
            stm=timsp[0][0]
            durat=str(int(timsp[1][1])-int(timsp[0][1]))
            if fflog:
             cmd = subprocess.run(["ffmpeg", "-hide_banner", "-ss", stm, "-noaccurate_seek", "-y", "-i", inu, "-t", durat, "-avoid_negative_ts", avoid_nts, "-c", "copy", "-map" ,"0", optfl], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            else:
             cmd = subprocess.run(["ffmpeg", "-hide_banner", "-ss", stm ,"-noaccurate_seek", "-y", "-i", inu, "-t", durat,"-avoid_negative_ts", avoid_nts,"-c", "copy", "-map" ,"0",optfl], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            if fflog:
              reg(2,cmd.stdout)
            if cmd.stderr:
              reg(0,f"CmdErr:{cmd.stderr}")
        cmdstp.append(["".join(cmds),inu,cmdsnm])
        
    else:
      if logp:
          reg(1, f"Input: {inp}\n{li[il][inp]}\n")
      else:
        print(f"Input: {inp}\n{li[il][inp]}\n")
 if tr and cmdstp:
     mergd(cmdstp)
 else:
  if logp:
   reg(1, f"{'-'*50}\n")
   
def sich(cont):
    yhor={}
    c=1
    ln=0
    for i in cont:
        ln += 1
        i=i.strip()
        if c:
         if "base=" in i and "/" not in i:
             c=0
             bsname=i.split("base=")[1]
             yhor[bsname]={}
        else:
            if not os.path.exists(bsname):
                if logp:
                  reg(1,f"{bsname} does not exist\n\n{'-'*50}\n\n")
                else:
                  print(f"Location {bsname} does not exist.")
                sys.exit()
            else:
                if "/" not in i and ""!=i:
                    shi=i
                    if "|" in shi:
                      shi=curbra(shi,bsname)
                    if '.' in shi:
                     ane = shi.rsplit(".", 1)[1].split(" ")[0]
                     if ane in sform:
                        yu=shi.rfind(ane)+len(ane)
                        ru,ki=shi[:yu],shi[yu+1:].split(" ")
                        if os.path.isfile(bsname+slsh+ru):
                            yhor[bsname][ru]={}
                            ts=fede(bsname+slsh+ru)
                            timesp=[]
                            for el in ki:
                              tmp=[io for io in el.split(":") if io.isnumeric()]
                              if tmp!=[]:
                                tmp=ice(tmp.copy())
                                timesp.append([":".join(tmp), consec(tmp)])
                            if timesp:                                                            
                             tls,fia=[],[]
                             hy=len(timesp)
                             io=0
                             crts=[]
                             while hy>0:
                                if hy!=1:
                                 tls=timesp[io:io+2]
                                 tls.sort(key=lambda ta: int(ta[1]))
                                 tem=[tls[0][1],tls[1][1]]
                                 io += 2
                                 hy-=2
                                else:
                                 tls=timesp[io:io+1]
                                 tem=[tls[0][1]]
                                 deu=len(tls[0][0])
                                 if deu%2:
                                  deu=(deu//2)-1
                                 else:
                                  deu=(deu//2)-2
                                  if deu<1: deu=1
                                 tls=[[f'{deu*"00:"}00','0']]+tls
                                 io += 1
                                 hy-=1
                                 if ygg:
                                     crts.append(tls)
                                     continue
                                if max([max(tem, key=int), ts], key=int) == ts:
                                  fia.append(tls)
                                else:
                                  crts.append(tls)
                             if ygg:
                              fia=degure(fia,[chaff(int(ts)),ts])                                          
                             erts=""
                             for pol in crts:
                               erts+=f"{pol[0][0]} - {pol[1][0]}\n" 
                             yhor[bsname][ru]['Cmds']=fia
                             yhor[bsname][ru]['Err'] = erts
                            else: 
                             yhor[bsname][ru]=f"Excluding {ru} due to incorrect format"
                                                    
                        else:
                           yhor[bsname][ru] = f"File {ru} doesn't exist in the directory"
    return yhor   
 
def advent(arg=sys.argv[1:]):
 try:
  if arg==[]:
    arch=0
  else:
    arch=1
  global ygg
  global exop
  if ygg in ['auto']:
    if '-c' in arg:
      if arg.index('-c')<(len(arg)-1):
       ygg=fuu(arg[arg.index('-c')+1])
       arch=0
    else:
      arch=0
      ygg=False

  if "-e" in arg:
    if arg.index("-e")<(len(arg)-1):
     if os.path.isdir(arg[arg.index("-e")+1]):
      exop=arg[arg.index("-e")+1]
     else:
      print(f"Using default output path\n")
     arch=0

  if '-f' in arg and arg.index("-f")<(len(arg)-1):
    if os.path.isfile(arg[arg.index('-f')+1]):
      ptde=arg[arg.index('-f')+1]
    else:
     if logp:
      reg(0, f"LocErr : File {arg[arg.index('-f')+1]} does not exist")
     else:
      print(f"Error : File {arg[arg.index('-f')+1]} does not exist")
     sys.exit()
  elif arg and arch:
    if logp:
     reg(0, f"ArgErr : Error splitting the argument list: Option not found")
    else:
     print(f"Error splitting the argument list: Option not found")
    sys.exit()
  else:
   ptde=f'{adieu}{slsh}cleave.txt'
   with open(ptde, "+a") as f:
    f.seek(0)
    em = f.readlines()
    if not em:
      f.write("/base directory where file is stored\nbase=\n\n/name startpoint endpoint")
      print("Cleave text file created")
      sys.exit()
  
  with open(ptde,"+r") as f:
    em=f.readlines()
  lia=sich(em)
  if lia:
    clv(lia,ygg)
  else:
   if logp:
    reg(1,f"Base path not found\n\n{'-'*50}\n\n")
   else:
    print("Base path not found")
 except Exception as e:
  if str(e) == "[WinError 2] The system cannot find the file specified":
    print("Unexpected Error: FFmpeg may not be properly installed")
  else:
   print(f"Unexpected Error: {e}")
  reg(0,f"UnknownErr : {e}")

if __name__=='__main__':
  advent()
