#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import ex0.base as hint
import ex1 as fact

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Capacitor ==="
    header_0 = "Testing Creature with healing capability"
    header_1 = "Testing Creature with transform capability"
    base = "base:"
    evol = "evolved:"
    fact_type = "Factory types:\t\t"
    fact_outp = "Factory output:\t\t"

    passed = "[O.K.]"
    valid = "[valid]"


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++

# ---------------------------- test ----------------------------


def test_healfactory(
    factory: type[fact.HealingCreatureFactory]
) -> None:

    """
    Takes a factory as an argument,
    validates the factory and its outputs
    as well as the method output of the creatures
    """

    test_base: hint.Creature
    test_evol: hint.Creature

    print(FileVariables.header_0)

    print(FileVariables.fact_type, end='')
    assert (isinstance(factory, type(fact.HealingCreatureFactory)) is True)
    print(type(factory), '\t\t\t', FileVariables.valid)

    print(FileVariables.fact_outp, end='')
    assert (
        isinstance(
            test_base := factory.create_base(),
            hint.Creature
        )
    )
    print(str(test_base), FileVariables.passed)

    print(FileVariables.fact_outp, end='')
    assert (
        isinstance(
            test_evol := factory.create_evolved(),
            hint.Creature
        )
    )
    print(str(test_base), FileVariables.passed)

    print('')
    print(FileVariables.base)
    print(test_base.describe())
    print(test_base.attack())
    print(test_base.heal())

    print('')
    print(FileVariables.evol)
    print(test_evol.describe())
    print(test_evol.attack())
    print(test_evol.heal())


def test_transformfactory(
    factory: type[fact.TransformCreatureFactory]
) -> None:

    """
    Takes a factory as an argument,
    validates the factory and its outputs
    as well as the method output of the creatures
    """

    test_base: hint.Creature
    test_evol: hint.Creature

    print(FileVariables.header_1)

    print(FileVariables.fact_type, end='')
    assert (isinstance(factory, type(fact.TransformCreatureFactory)) is True)
    print(type(factory), '\t\t\t', FileVariables.valid)

    print(FileVariables.fact_outp, end='')
    assert (
        isinstance(
            test_base := factory.create_base(),
            hint.Creature
        )
    )
    print(str(test_base), FileVariables.passed)

    print(FileVariables.fact_outp, end='')
    assert (
        isinstance(
            test_evol := factory.create_evolved(),
            hint.Creature
        )
    )
    print(str(test_base), FileVariables.passed)

    print('')
    print(FileVariables.base)
    print(test_base.describe())
    print(test_base.attack())
    print(test_base.transform())
    print(test_base.attack())
    print(test_base.revert())

    print('')
    print(FileVariables.evol)
    print(test_evol.describe())
    print(test_evol.attack())
    print(test_evol.transform())
    print(test_evol.attack())
    print(test_evol.revert())


# ---------------------------- run ----------------------------


def main() -> None:

    print(FileVariables.name)

    print('')
    test_healfactory(fact.HealingCreatureFactory)
    print('')
    test_transformfactory(fact.TransformCreatureFactory)

# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':

    main()
