alert("this is external js file")
function myfun1()
{
    alert("submitted")
}
/*let fullname = "khushi";
let age = "18";
const price = "1500";
var a = 5;
var b = 6;
document.write("Name is:" + fullname+"<br>");
document.write("age is:" + age+"<br>");
document.write("price:" + price); 
document.write("a+b = "+ (a +b) + "<br>");
document.write("a-b = "- (a -b) + "<br>");
document.write("a*b = "+ (a *b) + "<br>");
document.write("a/b = "+ (a /b) + "<br>");
document.write("b/a = "+ (b/a) + "<br>");
document.write("a+=3"+"<br>")
document.write("b=!3"+"<br>")
document.write("a<=3"+"<br>")

marks = 75
if(marks >= 90){
    document.write("Grade A")

}
 else if(75<= marks<= 89){
    document.write("Grade B" +"<br>")
}
else if(65<= marks<=74){
    document.write("Grade C")
}
else{
    document.write("Fail")
}*/
let day =3;
switch (day){
    case 1 :
        document.write("Monday");
        break;
    case 2:
        document.write("Tuesday");
        break;
    case 3:
        document.write("Wednesday"+"<br>");
        break;
        default:
            document.write("Invalid Day")

}
for (let k = 1; k<=5; k++){
    document.write("Iteration: "+k +"<br>");
}
/*NESTED loop*/
for(let i =1; i<= 3; i++){
    for (let j = 1; j<=2; j++){
        document.write("i=" + i+", j=" +j+"<br>");
    }
}
/*WHILE LOOP*/
let i = 1;
while(i<=5){
    document.write("Count: "+i);
    i++;
}
/*DO WHILE*/
let j = 1;
do{
    document.write("Number: " +j);
    j++;
}while(j<=5);