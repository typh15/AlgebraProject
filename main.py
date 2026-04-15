from permutation import Permutation
from group import PermutationGroup
from utils import natural_numbers, symmetric_generators, cyclic_generator


def display_section(title):
    print("=" * 60)
    print(title)
    print("=" * 60)


def display_group_info(name, group, show_elements=True, max_elements=None):
    print(f"{name}:")
    print(f"  Group size: {len(group)}")
    print(f"  Abelian: {group.is_abelian()}")
    print(f"  Fully generated: {group.is_generated()}")

    if show_elements:
        elements = sorted(group.elements, key=lambda g: g.image_tuple)
        print("  Elements:")

        if max_elements is None:
            for g in elements:
                print(f"    {g.image_tuple}")
        else:
            for g in elements[:max_elements]:
                print(f"    {g.image_tuple}")
            if len(elements) > max_elements:
                print("    ...")

    print()


if __name__ == "__main__":
    display_section("Symmetric Group Examples")

    domain2 = natural_numbers(2)
    generators2 = [Permutation(f, domain2) for f in symmetric_generators(2)]
    S2 = PermutationGroup(generators2, domain2)
    S2.generate()
    display_group_info("Symmetric Group on 2 elements (S2)", S2)

    domain3 = natural_numbers(3)
    generators3 = [Permutation(f, domain3) for f in symmetric_generators(3)]
    S3 = PermutationGroup(generators3, domain3)
    S3.generate()
    display_group_info("Symmetric Group on 3 elements (S3)", S3)

    domain6 = natural_numbers(6)
    generators6 = [Permutation(f, domain6) for f in symmetric_generators(6)]
    S6 = PermutationGroup(generators6, domain6)

    print("Before generation:")
    display_group_info("Symmetric Group on 6 elements (S6)", S6, show_elements=True, max_elements=10)

    S6.generate()

    print("After generation:")
    display_group_info("Symmetric Group on 6 elements (S6)", S6, show_elements=True, max_elements=10)

    display_section("Cyclic Group Example")

    domain5 = natural_numbers(5)
    C5 = PermutationGroup([Permutation(cyclic_generator(5), domain5)], domain5)

    print("Before generation:")
    display_group_info("Cyclic Group of order 5 (C5)", C5)

    C5.generate()

    print("After generation:")
    display_group_info("Cyclic Group of order 5 (C5)", C5)

    display_section("Working with Individual Group Elements")

    g = S3.get_element((0, 2, 1))
    h = S3.get_element((1, 2, 0))

    print(f"g = {g.image_tuple}")
    print(f"h = {h.image_tuple}")
    print(f"g * h = {(g * h).image_tuple}")
    print(f"h * g = {(h * g).image_tuple}")
    print(f"g^(-1) = {g.inverse().image_tuple}")
    print(f"h^(-1) = {h.inverse().image_tuple}")
    print(f"Do g and h commute? {(g * h) == (h * g)}")
    print()

    display_section("Conjugation Example")

    g = S3.get_element((0, 2, 1))
    h = S3.get_element((1, 2, 0))

    print("Original elements:")
    print(f"  g = {g.image_tuple}")
    print(f"  h = {h.image_tuple}")
    print()

    conj = g.conjugate_by(h)

    print("Conjugation:")
    print(f"  h^(-1) * g * h = {conj.image_tuple}")
    print()
    print("Compare structure:")
    print(f"  g == conjugate? {g == conj}")
    print()

    display_section("Group Conjugation")

    G_conj = S3.conjugate_by(h)

    print("Original group size:", len(S3))
    print("Conjugated group size:", len(G_conj))
    print("Groups equal?", S3.elements == G_conj.elements)
    print()

    display_section("Cycle Decomposition")

    print(f"g = {g.image_tuple}")
    print(f"  cycles: {g.cycle_decomposition()}")
    print(f"  cycle type: {g.cycle_type()}")
    print()

    print(f"h = {h.image_tuple}")
    print(f"  cycles: {h.cycle_decomposition()}")
    print(f"  cycle type: {h.cycle_type()}")
    print()

    gh = g * h
    print(f"g * h = {gh.image_tuple}")
    print(f"  cycles: {gh.cycle_decomposition()}")
    print(f"  cycle type: {gh.cycle_type()}")
    print()