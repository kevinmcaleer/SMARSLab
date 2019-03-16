var s = '{"version" : "0.0.8", "productname" : "SMARS Lab"}';

var obj = JSON.parse(s);

document.getElementById("product").innerHTML = "Name:" + obj.version + " " obj.productname;
