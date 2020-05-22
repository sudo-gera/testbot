%*<html><head></head><body><div id="main">enable javascript support</div><script id="scr">
*%
def show(q,e='main'):
 document.getElementById(e).innerHTML=q
def req(q):
 xhr = new XMLHttpRequest()
 xhr.open('GET', q)
 xhr.responseType='text'
 alert(q)
 xhr.send()
 if xhr.status!=200:
  alert('error '+xhr.status+': '+xhr.statusText)
 return xhr.responseText
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
 a=req('./'+q)
 alert('text'+a)
################################
%*</script></body></html>
*%
