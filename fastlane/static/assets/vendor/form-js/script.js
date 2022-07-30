function SendMail(){
  var params ={
    name : document.getElementById("name").value,
    email : document.getElementById("name").value,
    subject : document.getElementById("name").value,
    message : document.getElementById("name").value,
  }
  emailjs.send("service_ay8wv6l","template_yncdgr8",params).then(function(res){
    alert("Your Message has been sent!!"+ res.status);
  })
}