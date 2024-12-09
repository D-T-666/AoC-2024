#include <iostream>
#include <string>
using namespace std;

struct E {
  int name;
  char size;
  int space_after;
  E* next;
  E* prev;

  E() {}
  E(int _name, char _size, int _space_after) {
    name = _name;
    size = _size;
    space_after = _space_after;
    next = nullptr;
  }
};

long long cost(E* elt) {
  long long c = 0;

  long long result = 0;

  while (elt != nullptr) {
    for (int j = 0; j < elt->size; j++) {
      result += c * elt->name;
      c += 1;
    }
    c += elt->space_after;
    elt = elt->next;
  }

  return result;
}

int main() {
  string s; cin >> s;
  if (s.size() % 2 == 1) {
    s += "0";
  }
  const int n = s.size() / 2;
  E elts[s.size() / 2];
  elts[0] = E(
    0,
    s[0] - '0',
    s[1] - '0'
  );
  for (int i = 1; i < n; i++) {
    elts[i] = E(
      i,
      s[i * 2] - '0',
      s[i * 2 + 1] - '0'
    );
    elts[i - 1].next = &elts[i];
    elts[i].prev = &elts[i - 1];
  }

  E* root = &elts[0];

  for (int i = n - 1; i > 0; i--) {
    E* elt = root;

    while (elt != nullptr && elt->name != elts[i].name) {
      if (elt->space_after < elts[i].size) {
        elt = elt->next;
        continue;
      }

      elts[i].prev->space_after += elts[i].size + elts[i].space_after;
      elts[i].space_after = elt->space_after - elts[i].size;
      elt->space_after = 0;

      elts[i].prev->next = elts[i].next;
      if (elts[i].next != nullptr)
        elts[i].next->prev = elts[i].prev;

      elts[i].next = elt->next;
      elts[i].prev = elt;
      elts[i].next->prev = &elts[i];
      elts[i].prev->next = &elts[i];

      break;
    }
  }

  cout << cost(root) << endl;
}
