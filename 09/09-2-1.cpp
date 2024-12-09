#include <iostream>
#include <string>
using namespace std;

int main() {
  string s; cin >> s;
  if (s.size() % 2 == 1) s += "0";

  const int n = s.size() / 2;
  int len[n], ind[n];
  int empty[n], ind_empty[n];
  int c = 0;

  for (int i = 0; i < n; i++) {
    len[i] = s[i * 2] - '0';
    empty[i] = s[i * 2 + 1] - '0';
    ind[i] = c;
    ind_empty[i] = c += len[i];
    c += empty[i];
  }

  long long result = 0;
  int first[10];
  for (int i = 0; i < 10; i++) first[i] = 0;

  for (int i = n - 1; i >= 0; i--) {
    int k; for (k = first[len[i]]; k < i; k++) if (empty[k] >= len[i]) break;

    long long t = ind[i];
    if (empty[k] >= len[i]) {
      for (int j = len[i]; j < 10; j++) {
        first[j] = max(first[j], k);
      }
      t = ind_empty[k];
      empty[k] -= len[i];
      ind_empty[k] += len[i];
    }
    result += ((long long)len[i] * t + len[i] * (len[i] - 1) / 2) * i;
  }
  cout << result << endl;
}
