
var sum = 0;
var squares = 0;
for (var i = 0; i <= 100; i++) {
  sum += i;
  squares += i*i;
}
console.log(sum * sum - squares);
