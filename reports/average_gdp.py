from collections import defaultdict

from reports.base import BaseReport


class AverageGDPReport(BaseReport):
    def generate(self):
        country_gdp = defaultdict(list)

        for row in self.data:
            country = row["country"]
            gdp = float(row["gdp"])
            country_gdp[country].append(gdp)

        result = []

        for country, values in country_gdp.items():
            avg = sum(values) / len(values)
            result.append({
                "country": country,
                "average_gdp": round(avg, 2),
            })

        result.sort(key=lambda x: x["average_gdp"], reverse=True)

        return result
