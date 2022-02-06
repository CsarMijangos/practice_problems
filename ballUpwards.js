function maxBall(v0) {
    // your code
  let v = v0 * (5/18)  // Convertimos la velocidad a m/s
  const g = 9.81  // Declaramos el valor de la gravedad
  let t = v/g
  return Math.round(10*t)
}

console.log(maxBall(37))
console.log(maxBall(45))