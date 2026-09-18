#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import ex0.base as hint
import ex0 as creature

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Battle ==="
    test_0 = "--- Testing factory ---"
    test_0_1 = "Factory types:\t\t"
    test_0_2 = "Factory output:\t\t"
    test_0_3 = "Creture abillitites:\t"
    test_0_3_1 = "describe:\t"
    test_0_3_2 = "attack:\t\t"
    test_1 = "--- Testing battle ---"
    test_1_1 = "and now, Fight:"
    test_1_2 = "%s\n\n\t\tvs\n\n%s\n\n\t\tfight!"

    passed = "[O.K.]"
    valid = "[valid]"
    passed_all = "--> All tests passed :)"


class ControlValues:

    factory = {
        creature.FlameFactory: {
            "base descri": "Flameling is a Fire type Creature",
            "base attack": "Flameling uses Ember!",
            "evol descri": "Pyrodon is a Fire/Flying type Creature",
            "evol attack": "Pyrodon uses Flamethrower!"
        },
        creature.AquaFactory: {
            "base descri": "Aquabub is a Water type Creature",
            "base attack": "Aquabub uses Water Gun!",
            "evol descri": "Torragon is a Water type Creature",
            "evol attack": "Torragon uses Hydro Pump!"
        }
    }

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++

# ---------------------------- test ----------------------------


def test_factory(factory: type[hint.Factory]) -> None:

    """
    Takes a factory as an argument,
    validates the factory and its outputs
    as well as the method output of the creatures
    """

    test_base: hint.Creature
    test_evol: hint.Creature

    print(FileVariables.test_0)

    print(FileVariables.test_0_1, end='')
    assert (isinstance(factory, type(hint.Factory)) is True)
    print(type(factory), '\t\t', FileVariables.valid)

    print(FileVariables.test_0_2, end='')
    assert (
        isinstance(test_base := factory.create_base(), hint.Creature) is True
    )
    print(type(test_base), '\t', FileVariables.passed)
    print(FileVariables.test_0_2, end='')
    assert (
        isinstance(
            test_evol := factory.create_evolved(), hint.Creature
        ) is True
    )
    print(type(test_evol), '\t', FileVariables.passed)

    print('')
    print(FileVariables.test_0_3)
    print(FileVariables.test_0_3_1, end='')
    assert (
        test_base.describe() == ControlValues.factory[factory]["base descri"]
    )
    print(test_base.describe(), '\t', FileVariables.passed)

    print(FileVariables.test_0_3_2, end='')
    assert (
        test_base.attack() == ControlValues.factory[factory]["base attack"]
    )
    print(test_base.attack(), '\t\t', FileVariables.passed)

    print(FileVariables.test_0_3_1, end='')
    assert (
        test_evol.describe() == ControlValues.factory[factory]["evol descri"]
    )
    print(test_evol.describe(), '\t', FileVariables.passed)

    print(FileVariables.test_0_3_2, end='')
    assert (
        test_evol.attack() == ControlValues.factory[factory]["evol attack"]
    )
    print(test_evol.attack(), '\t\t', FileVariables.passed)

    print('\n', FileVariables.passed_all)


def test_battle(
    factory_a: type[hint.Factory], factory_b: type[hint.Factory]
) -> None:

    """
    Takes two (both) factories as arguments,
    validates them an the output of .create_base()
    then simulates a fight
    """

    base_a: hint.Creature
    base_b: hint.Creature

    print(FileVariables.test_1)

    print(FileVariables.test_0_1, end='')
    assert (isinstance(factory_a, type(hint.Factory)) is True)
    print(type(factory_a), '\t\t', FileVariables.valid)
    print(FileVariables.test_0_1, end='')
    assert (isinstance(factory_a, type(hint.Factory)) is True)
    print(type(factory_b), '\t\t', FileVariables.valid)

    print(FileVariables.test_0_2, end='')
    assert (
        isinstance(base_a := factory_a.create_base(), hint.Creature) is True
    )
    print(type(base_a), '\t', FileVariables.passed)
    print(FileVariables.test_0_2, end='')
    assert (
        isinstance(base_b := factory_b.create_base(), hint.Creature) is True
    )
    print(type(base_b), '\t', FileVariables.passed)

    print('\n', FileVariables.passed_all)
    print('')
    print(FileVariables.test_1_1, '\n')
    print(FileVariables.test_1_2 % (base_a.describe(), base_b.describe()))
    print('')
    print(base_a.attack())
    print(base_b.attack())


def test_battle_additional(
    factory_a: type[hint.Factory], factory_b: type[hint.Factory]
) -> None:

    pass

# ---------------------------- run ----------------------------


def main() -> None:

    print(FileVariables.name)

    print('')
    test_factory(creature.FlameFactory)
    print('')
    test_factory(creature.AquaFactory)
    print('')
    test_battle(
        factory_a=creature.FlameFactory,
        factory_b=creature.AquaFactory
    )
    print('')
    test_battle_additional(
        factory_a=creature.FlameFactory,
        factory_b=creature.AquaFactory
    )


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':

    main()
