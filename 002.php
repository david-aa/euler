<?php

function fib($max) {
  $ret = array(1, 2);
  $x = 3;
  while (true) {
    $new = $ret[$x-2] + $ret[$x-3];
    if ($new <= $max) {
      $ret []= $new;
      $x++;
    } else {
      break;
    }
  }
  return $ret;
}


$sum = 0;
foreach (fib(4000000) as $n) {
  if ($n % 2 == 0) {
    $sum += $n;
  }
}

echo "$sum\n";
