#!/usr/bin/env ruby

$divisors_precalculated = []

def divisors_sum number
  if $divisors_precalculated[number] != nil
    return $divisors_precalculated[number] 
  end
  sum = 0
  i = 1
  max = number / 2
  while i <= max
    if number % i == 0
      sum += i
    end
    i += 1
  end
  $divisors_precalculated[number] = sum
  return sum
end

def is_abundant number
  return divisors_sum(number) > number
end

total = 0

for current_number in 1..28123
  is_sum_of_two_abundant_numbers = false
  fist_half = current_number - 1
  second_half = 1
  while second_half <= fist_half
    if is_abundant(fist_half) and is_abundant(second_half)
      is_sum_of_two_abundant_numbers = true
      break
    end
    fist_half -= 1
    second_half += 1
  end
  if !is_sum_of_two_abundant_numbers
    #puts current_number.to_s + ' cannot be written as the sum of two abundant numbers'
    total += current_number
  end
end

puts "Result: " + total.to_s