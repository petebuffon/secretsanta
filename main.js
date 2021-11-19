// file:///home/pete/secretsanta/index.html?name=pete&msg=EtH_-BerP65VNDPqBqciTRa6noxy_0CV11674nHnhmc=&doc=

function Base64DecodeUrl(str){
    str = (str + '===').slice(0, str.length + (str.length % 4));
    return atob(str.replace(/-/g, '+').replace(/_/g, '/'));
}

// get query string parameters
let params = new URLSearchParams(window.location.search);
let name = params.get("name").trim().replace(/^\w/, (c) => c.toUpperCase());
let msg = Base64DecodeUrl(params.get("msg"));

// decode msg
let ct = msg.slice(0, 16);
let otp = msg.slice(16,32);
let pt = "";
for (let i = 0; i < 16; i++) {
    pt += String.fromCharCode(otp[i].charCodeAt(0) ^ ct[i].charCodeAt(0));
}
let name_len = pt[0].charCodeAt();
let assignment = pt.slice(1, name_len + 1);

// set name and assignment in html
document.getElementById("name").innerHTML = name;
document.getElementById("assignment").innerHTML = assignment;
