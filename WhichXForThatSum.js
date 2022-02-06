function solve(m) {
  // your code       
let x1 = (1+2*m+Math.sqrt(4*m+1))/(2*m)
let x2 = (1+2*m-Math.sqrt(4*m+1))/(2*m)
if (x1*x2>0){
  return Math.min(x1,x2)
}
else{ 
  return Math.max(x1,x2)
}
}

console.log(solve(2));