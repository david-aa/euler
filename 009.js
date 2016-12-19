var SUM = 1000
for (var a = 1; a < SUM; a++) {
  for (var b = a + 1; b < SUM; b++) {
    c2 = a*a + b*b;
    c = Math.sqrt(c2)
    if (Math.round(c) == c) { // Pythagorean triplet
      if (a + b +c == SUM) {
        console.log("Triplet: ", a, b, c, "Product: ", a*b*c);
        process.exit(0);
      }
    }
  }
}
