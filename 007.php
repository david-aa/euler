<?php
// https://projecteuler.net/problem=7

function isPrime($num) {
  if ($num == 2) return true;
  if ($num < 2 || $num % 2 == 0) return false;
  $max = (int) sqrt($num);
  for ($i = 3; $i <= $max; $i +=2) {
      if ($num % $i == 0) {
          return false;
      }
  }
  return true;
}

$counter = 0;
$num = 2;
$stop = false;
while (true) {
  if (isPrime($num)) {
    $counter++;
    if ($counter == 10001) {
      echo "$num\n";
      break;
    }
  }
  $num++;
}
