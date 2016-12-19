#include <stdio.h>

unsigned long n_paths = 0;
void move_point(int x, int y, int xmax, int ymax) {
  if (x == xmax && y == ymax) {
    n_paths++;
  } else if (y < ymax) {
    move_point(x, y + 1, xmax, ymax);
    if (x < xmax) {
      move_point(x + 1, y, xmax, ymax);
    }
  } else if (x < xmax) {
    move_point(x + 1, y, xmax, ymax);
  }
}

int main() {
  move_point(0, 0, 20, 20);
  printf("n_paths: %lu\n", n_paths);
  return (0);
}
