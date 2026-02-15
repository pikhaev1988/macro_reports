from reports.average_gdp import AverageGDPReport


def test_average_gdp():
    data = [
        {"country": "A", "gdp": "10"},
        {"country": "A", "gdp": "20"},
        {"country": "B", "gdp": "30"},
    ]

    report = AverageGDPReport(data)
    result = report.generate()

    assert result == [
        {"country": "B", "average_gdp": 30.0},
        {"country": "A", "average_gdp": 15.0},
    ]
