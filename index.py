%*<html><head></head><body><div id="main">enable javascript support</div><script id="scr">
    // ref: http://stackoverflow.com/a/1293163/2343
    // This will parse a delimited string into an array of
    // arrays. The default delimiter is the comma, but this
    // can be overriden in the second argument.
    function CSVToArray( strData, strDelimiter ){
        // Check to see if the delimiter is defined. If not,
        // then default to comma.
        strDelimiter = (strDelimiter || ",");

        // Create a regular expression to parse the CSV values.
        var objPattern = new RegExp(
            (
                // Delimiters.
                "(\\" + strDelimiter + "|\\r?\\n|\\r|^)" +

                // Quoted fields.
                "(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +

                // Standard fields.
                "([^\"\\" + strDelimiter + "\\r\\n]*))"
            ),
            "gi"
            );


        // Create an array to hold our data. Give the array
        // a default empty first row.
        var arrData = [[]];

        // Create an array to hold our individual pattern
        // matching groups.
        var arrMatches = null;


        // Keep looping over the regular expression matches
        // until we can no longer find a match.
        while (arrMatches = objPattern.exec( strData )){

            // Get the delimiter that was found.
            var strMatchedDelimiter = arrMatches[ 1 ];

            // Check to see if the given delimiter has a length
            // (is not the start of string) and if it matches
            // field delimiter. If id does not, then we know
            // that this delimiter is a row delimiter.
            if (
                strMatchedDelimiter.length &&
                strMatchedDelimiter !== strDelimiter
                ){

                // Since we have reached a new row of data,
                // add an empty row to our data array.
                arrData.push( [] );

            }

            var strMatchedValue;

            // Now that we have our delimiter out of the way,
            // let's check to see which kind of value we
            // captured (quoted or unquoted).
            if (arrMatches[ 2 ]){

                // We found a quoted value. When we capture
                // this value, unescape any double quotes.
                strMatchedValue = arrMatches[ 2 ].replace(
                    new RegExp( "\"\"", "g" ),
                    "\""
                    );

            } else {

                // We found a non-quoted value.
                strMatchedValue = arrMatches[ 3 ];

            }


            // Now that we have our value string, let's add
            // it to the data array.
            arrData[ arrData.length - 1 ].push( strMatchedValue );
        }

        // Return the parsed data.
        return( arrData );
    }

*%
def show(q,e='main'):
 document.getElementById(e).innerHTML=q
cont=''
ranc=7
def fet(q):
 e=''
 fetch(q).then(function(r){
 if r.ok:
  r.text().then(function(t){
  cont=t
  show('<button onclick="tlis();return false">начать</button>')
  })
 else:
  alert(r.status+' '+r.statusText)
  cont=''
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
 a=fet('./'+q)
 show('подожди')
def tlis():
 a=cont
 a=a.replace('\r','\n')
 a=a.split('\n')
 a=a.filter(function(val,ind,arr){
 if val.indexOf(';')!=-1:
  return val.split(';').length>2
 return val.split(',').length>2
 })
 v=Math.floor(Math.random()*a.length)
 a=a[v]
 a=a.split('')
 for w<a.length:
  c=a[w].charCodeAt(0)>127
  if c>127 and c<256:
   c+=848
  a[w]=String.fromCharCode(c)
 a=a.join('')
 if a.indexOf(';')!=-1:
  a=a.split(';')
 else:
  a=a.split(',')
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
