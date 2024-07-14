var shape = prompt("Enter the shape of your choice (circle, rectangle, triangle)")

if(shape==="circle"){
   var radius = prompt("Enter the radius");
   var area = (3.1457 * (radius**2));
   alert("The area of the circle is "+area);

} else if(shape==="rectangle"){
    var length = prompt("Enter the length");
    var width = prompt("Enter the width");
    var area = (length*width);
    alert("The area of the rectangle is "+area);

} else if(shape==="triangle"){
    var base = prompt("Enter the length of base");
    var height = prompt("Enter the height");
    var area = 0.5*base*height;
    alert("The area of the triangle is "+area);
    
} else{
    alert("Enter a valid shape!!")
}