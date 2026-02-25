def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'])


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0}
    M = max(mages, key=lambda x: x["power"])["power"]
    m = min(mages, key=lambda x: x["power"])["power"]
    s = sum(mage["power"] for mage in mages)
    return {"max_power": M, "min_power": m, "avg_power": s/len(mages)}


if __name__ == "__main__":
    artifacts = [
                    {'name': 'Fire Staff', 'power': 105, 'type': 'relic'},
                    {'name': 'Water Chalice', 'power': 81, 'type': 'armor'},
                    {'name': 'Earth Shield', 'power': 78, 'type': 'relic'},
                    {'name': 'Light Prism', 'power': 65, 'type': 'accessory'}
                ]
    mages = [
                {'name': 'Casey', 'power': 56, 'element': 'ice'},
                {'name': 'Rowan', 'power': 78, 'element': 'light'},
                {'name': 'Storm', 'power': 64, 'element': 'shadow'},
                {'name': 'Riley', 'power': 59, 'element': 'ice'},
                {'name': 'Jordan', 'power': 95, 'element': 'fire'}
            ]
    spells = ['darkness', 'tornado', 'freeze', 'meteor']

    try:
        print("artifact sorter:", artifact_sorter(artifacts))
        print("power_filter:", power_filter(mages, 66))
        print("spell_transformer:", spell_transformer(spells))
        print("mage_stats:", mage_stats(mages))
    except Exception as e:
        print(e)
