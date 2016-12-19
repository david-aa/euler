<?php

function generateCollatz($num) {
  $ret = array($num);
  $next = end($ret);
  while (true) {
    $next = $next % 2 == 0 ? $next / 2 : 3*$next + 1;
    $ret []= $next;
    if ($next == 1) break;
  }
  return $ret;
}


$longest = 1;
$maxCount = 0;
for ($x = 1; $x < 1000000; $x++) {
  $collatz = generateCollatz($x);
  $nCollatz = count($collatz);
  if ($nCollatz > $maxCount) {
    $longest = $x;
    $maxCount = $nCollatz;
    echo "El número $x tiene $nCollatz términos\n";
  }

}
