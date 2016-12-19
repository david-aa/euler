#!/usr/bin/perl

sub get_factors {
    my $num = shift;
    my @factors;
    for ($i = 1; $i <= $num; $i++) {
        if ($num % $i == 0) {
            push @factors, $i;
        }
    }
    return @factors;
}

my $i = 1;
my $num = 1;
while (true) {
    my @factors = get_factors($num);
    my $nfactors = @factors;
    if ($num % 1000 == 0) {
        print "Calculando para número $num..., tiene $nfactors factores.\n";
    }
    if ($nfactors > 500) {
        print "$num tiene $nfactors factores: " . join(", ", @factors) . "\n";
        last;
    }
    $i++;
    $num += $i;
}
