# AlgebraProject

This is a small Python project for working with permutations and permutation groups.
It started as a way to experiment with group theory in code and gradually turned into a more structured framework.

The core idea is to take a set of generators, build the group they generate, and then explore properties of that group.

---

## What it does

- Builds permutation groups from a set of generators
- Generates the full group by closure (composition + inverses)
- Checks whether a group is abelian
- Lets you inspect and manipulate individual elements
- Includes a few example groups (symmetric groups and a cyclic group)

---

## How it’s organized

- `permutation.py` — defines a permutation and basic operations (composition, inverse)
- `group.py` — handles group generation and property checks
- `utils.py` — helper functions (domains, generators)
- `main.py` — example usage

---

## Running the demo

From the project folder:

```bash
python main.py