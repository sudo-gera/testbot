%*<html><head></head><body><div id="main">enable javascript support</div><script id="scr">
*%
def show(q,e='main'):
 document.getElementById(e).innerHTML=q
cont=''
ranc=7
dd=''
reqq=''
reqr=0
def fet(q,r=0):
 if r==0:
  reqq=q
 reqr=r
 e=''
 fetch(q).then(function(r){
 if r.ok:
  r.text().then(function(t){
  cont=t
  show('<button onclick="tlis();return false">начать</button>')
  })
 else:
  if reqr==1:
   if r.status==404:
    show('файл '+reqq+'не найден')
   else:
    show(r.status.toString())
  else:
   fet(reqq+'.csv',1)
 })
def fran():
 if ranc:
  ranc-=1
  return Math.random()
 else:
  ranc=7
  return 0
#######################
show('''название теста:
<form name="tni" onsubmit="name_h();return false">
<input type="text" name="tn">
<button type="submit">открыть</button>
</form>
<div id="ct"></div>
''')
def name_h():
 q=document.forms.tni.elements.tn.value
 fet('./'+q)
 show('подожди')
def tlis():
 a=cont.split('')
 a=a.join('')
 if a.indexOf(';')==-1:
  dd=','
 else:
  dd=';'
 a=a.replace('\r','\n')
 a=a.split('\n')
 a=a.filter(function(val,ind,arr){
 r=val.split(dd)
 if r!=undefined and r.length>2:
  return 1==1
 return 1==2
 })
 v=Math.floor(Math.random()*a.length)
 a=a[v]
 a=a.split(dd)
 d=[]
 while d.length==0:
  for 2=w<a.length:
   if fran()<%*0.7*%:
    v='<br/><button onclick="return false">'+a[Math.floor(Math.random()*(a.length-2))+2]+'</button>'
    d.push(v)
 d.unshift('<br/><button onclick="tlis();return false">'+a[1]+'</button>')
 d.sort(function(o,p){return Math.random()-%*0.5*%})
 show(a[0]+d.join(''))
################################
%*</script></body></html>
*%
