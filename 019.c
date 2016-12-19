#include <stdio.h>
#include <stdlib.h>
#define SUNDAY 0


int is_leap_year(int year) {
	return (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0));
}

int days_in_month(int month, int year) {
	switch (month) {
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			return 31;
		case 2:
			return is_leap_year(year) ? 29 : 28;
		default:
			return 30;
	}
}

int days_to_init(int day, int month, int year) {
	int days = 0;
	int month0 = 1;
	int year0 = 1900;
	days += day;
	while (month > month0) {
		days += days_in_month(month - 1, year);
		month--;
	}
	while (year > year0) {
		days += is_leap_year(year - 1) ? 366 : 365;
		year--;
	}

	return days;
}

/* 1 => Monday .... 7 => Sunday */
int day_of_week(int day) {
	return day % 7;
}

int main(int argc, char *argv[]) {
	int n_sundays = 0;
	int days;
	for (int year_start = 1901; year_start <= 2000; year_start++) {
		for (int month_start = 1; month_start <= 12; month_start++) {
			days = days_to_init(1, month_start, year_start);
			if (day_of_week(days) == SUNDAY) {
				printf("%d/%d/%d es domingo\n", 1, month_start, year_start);
				n_sundays++;
			}
		}
	}
	printf("%d domingos caen en primero de mes.\n", n_sundays);
	return 0;
}