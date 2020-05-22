%*<html><head></head><body><div id="main">enable javascript support</div><script id="scr">
*%
def show(q,e='main'):
 document.getElementById(e).innerHTML=q
def req(q):
 xhr = new XMLHttpRequest()
 xhr.open('GET', q)
 xhr.send()
 return xhr.responseText
#######################
show('''название теста:
<form name="tni" onsubmit="name_h();return false">
<input type="text" name="tn">
<button type="submit">открыть</button>
</form>
<form name="reg_form" onsubmit="reg_h();return false">
<input type="text" name="token">
<button type="submit">start</button>
</form>
<div id="ct"></div>
''')
def name_h():
 q=document.forms.tni.elements.tn.value
 a=req('./'+q)
 show(a,'ct')
################################
%*</script></body></html>
*%
