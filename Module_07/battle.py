#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import ex0.base as hint
import ex0 as creature

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class FileVariables:

    name = "=== Battle ==="
    test_0 = "Testing factory"
    test_1 = "Testing battle"


class ControlValues:

    factory = {
        creature.FlameFactory: {
            "base describe": "Flameling is a Fire type Creature",
            "base attack": "Flameling uses Ember!",
            "evol describe": "Pyrodon is a Fire/Flying type Creature",
            "evol attack": "Pyrodon uses Flamethrower!"
        },
        creature.AquaFactory: {
            "base describe": "Aquabub is a Water type Creature",
            "base attack": "Aquabub uses Water Gun!",
            "evol describe": "Torragon is a Water type Creature",
            "evol attack": "Torragon uses Hydropump!"
        }
    }

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++

# ---------------------------- run ----------------------------


def test_factory(factory: type[hint.Factory]) -> None:

    test_base: hint.Creature
    test_evol: hint.Creature

    print(FileVariables.test_0)

    assert (isinstance(factory, type(hint.Factory)) is True)
    assert (
        isinstance(test_base := factory.create_base(), hint.Creature) is True
    )
    assert (
        isinstance(
            test_evol := factory.create_evolved(), hint.Creature
        ) is True
    )
    print(test_base.describe())
    print(test_base.attack())
    print(test_evol.describe())
    print(test_evol.attack())


# ---------------------------- run ----------------------------


def main() -> None:

    test_0: hint.Creature
    test_1: hint.Creature
    test_2: hint.Creature
    test_3: hint.Creature

    print(FileVariables.name)

    test_0 = creature.FlameFactory.create_base()
    test_1 = creature.AquaFactory.create_base()
    test_2 = creature.FlameFactory.create_evolved()
    test_3 = creature.AquaFactory.create_evolved()

    print('')
    print(test_0.describe())
    print(test_0.attack())
    print(test_0.attack("wodden pole"))

    print('')
    print(test_1.describe())
    print(test_1.attack())
    print(test_1.attack(test_0))

    print('')
    print(test_2.describe())
    print(test_2.attack())
    print(test_2.attack(test_1))

    print('')
    print(test_3.describe())
    print(test_3.attack())
    print(test_3.attack(test_2))


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()

    print('')
    test_factory(creature.FlameFactory)
